"""

    Following the October 2023 refactor of the API, Fighting Arts are broken out
    into three definitions files: one for regular farts, one for secret farts
    and one for strain farts.

    Rather than breaking them by expansion, we're going to do this (for now) in
    order to continue to leverage 'sub_type' assignments, etc.

"""

from .._collection import Collection

from .fighting_arts import *
from .secret_fighting_arts import *
from .strain_fighting_arts import *

class Assets(Collection):

    def __init__(self, *args, **kwargs):
        Collection.__init__(self,  *args, **kwargs)
