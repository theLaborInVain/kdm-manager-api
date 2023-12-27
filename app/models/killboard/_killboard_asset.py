'''

    The Killboard "asset" is basically a record we synthesize from Settlement
    data.

'''

# KD:M API imports
from app import utils


class KillboardAsset:
    """ This is where we do work with killboard assets. """

    def __repr__(self):
        return '[%s] killboard object (%s)' % (self._id, self.created_on)

    def __init__(self, _id=None, params=None, monsters_collection_obj=None):
        """ Basic init routine. Use a valid ObjectID as '_id' if you've got an
        edit that you want to do; leave '_id' set to None to create a new
        entry in the killboard."""

        # built-in attribs
        self.logger = utils.get_logger()

        # baseline attribs
        self.type = None

        # initialize kwargs to be attribs
        self._id = _id
        self.params = params

        # sanity checks
        if self.params is None:
            self.params = {}

        if self._id is None and params == {}:
            err = str(
                "New killboard objects must be initialized with an '_id' value "
                "of None and a non-empty 'params' dict!"
            )
            raise TypeError(err)

        if self._id is None and params != {}:
            self.new()  # defines self._id when it's done inserting

        # now that we've got a self._id defined, add the document as an attrib
        self.document = utils.mdb.killboard.find_one({'_id': self._id})
        if self.document is None:
            err = "Cannot find a killboard entry with _id=%s" % self._id
            raise ValueError(err)

        # set all document keys to be attributes
        for key, value in self.document.items():
            setattr(self, key, value)

        self.monster_asset = monsters_collection_obj.get_asset_from_name(
            self.name
        )

        #finally, normalize:
        self._normalize()


    def save(self, verbose=True):
        """ Generic save method. """
        utils.mdb.killboard.save(self.document)
        if verbose:
            self.logger.info('Saved changes to Killboard object: %s', self)


    def _normalize(self):
        """ Forces Killboard objects to adhere to our data model. """

        perform_save = False

        # fix invalid types 
        if self.type in ['monsters', None]:
            orig_type = self.type
            warn = "%s Fixing killboard obj 'type' attr..." % self
            self.logger.warning(warn)
            self.type = self.monster_asset.get('sub_type', None)
            self.document['type'] = self.type
            perform_save = True
            self.logger.warning(
                "%s Changed type from '%s' to '%s'", self, orig_type, self.type
            )

        if perform_save:
            self.save()
