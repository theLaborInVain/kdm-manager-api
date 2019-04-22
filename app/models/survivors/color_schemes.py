"""

    This imports the app/assets/survivors/color_schemes.py as its root module.

"""

from app.assets.survivors import color_schemes
from app import models


class Assets(models.AssetCollection):


    def __init__(self, *args, **kwargs):
        self.root_module = color_schemes
        models.AssetCollection.__init__(self,  *args, **kwargs)

        self.post_process()


    def post_process(self):
        """ Creates the 'style_string' attribute based on the key/value pairs
        in the 'style' attrib. """

        for asset_dict in self.get_dicts():
            style_string = ""
            for k,v in asset_dict['style'].items():
                style_string += '%s: %s;' % (k, v)
            self.assets[asset_dict['handle']]['style_string'] = style_string
