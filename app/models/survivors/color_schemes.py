"""

    This imports the app/assets/survivors/color_schemes.py as its root module.

"""

from app import models
from app.assets.survivors import color_schemes

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        ''' Basic init followed by a quick loop to set the HTML 'style_string'
        attribute, which is used in the webapp. '''

        self.root_module = color_schemes    # has to be set; unusual path

        models.AssetCollection.__init__(self,  *args, **kwargs)

        for asset_dict in self.get_dicts():
            style_string = ""
            for k,v in asset_dict['style'].items():
                style_string += '%s: %s;' % (k, v)
            self.assets[asset_dict['handle']]['style_string'] = style_string
