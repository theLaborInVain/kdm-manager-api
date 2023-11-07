'''

    The Killboard "asset" is basically a record we synthesize from Settlement
    data.

'''

# KD:M API imports
from app import utils
from app.assets import kingdom_death as KingdomDeath

# dirty-ass constants

MONSTERS = KingdomDeath.monsters.Assets()

class KillboardAsset:
    """ This is where we do work with killboard assets. """

    def __init__(self, _id=None, params=None):
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

        #finally, normalize:
        self.normalize()


    def save(self, verbose=True):
        """ Generic save method. """
        utils.mdb.killboard.save(self.document)
        if verbose:
            self.logger.info('Saved changes to Killboard object: %s', self._id)


    def normalize(self):
        """ Forces Killboard objects to adhere to our data model. """

        perform_save = False

        # fix the type, if necessary, to be the type in the monsters asset dict
        if self.type == 'monsters':
            self.logger.warning("Correcting Killboard entry 'type' attribute!")
            monster_asset = KingdomDeath.monsters.Monster(
                handle = self.handle,
                collection_obj = MONSTERS
            )
            self.type = monster_asset.asset.get('sub_type', None)
            self.document['type'] = self.type
            perform_save = True

        if perform_save:
            self.save()
