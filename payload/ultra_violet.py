from collections import namedtuple

# Authorship -----------------------------------------------------------------------------#
__author__      = ["Geoffrey Hyde Garrett", "Vladimir"]
__copyright__   = None
__credits__     = None
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = ["Geoffrey Hyde Garrett", "Vladimir"]
__email__       = ["g.h.garrett13@gmail.com", "vladifm97@gmail.com"]
__status__      = "Development"

uv_mapping = namedtuple('ir_mapping', 'mission_name ifov mass p_av p_peak')

JUNO_UVS = uv_mapping(mission_name="juno",
                      ifov=0.267,
                      mass=21.6,
                      p_av=9.8,
                      p_peak=13.85)
