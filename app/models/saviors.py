
from app.assets import saviors
from app import models

class Assets(models.AssetCollection):

    def __init__(self, *args, **kwargs):
        self.is_game_asset = False
        self.root_module = saviors
        models.AssetCollection.__init__(self,  *args, **kwargs)


    def get_asset_by_color(self, color=None):
        """ This method will return an asset dictionary whose 'color' attrib
        matches the value of the 'color' kwarg. """

        if color is None:
            msg = "get_asset_by_color() requires the 'color' kwarg!"
            self.logger.exception(msg)
            raise Exception(msg)

        output = None
        for d in self.get_dicts():
            if d["color"] == color and output is None:
                output = d
            elif d["color"] == color and output is not None:
                msg = "Multiple savior asset dicts have the color '%s'.\
                    Did you rememeber to filter?" % color
                self.logger.exception(msg)
                raise Exception(msg)

        if output is None:
            msg = "No asset dict found for color '%s'!" % color

        return output
