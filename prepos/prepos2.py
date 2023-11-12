# mc_cons_symmetry: ((p >> q) >> q) >> ((q >> p) >> p)
from dneg import thm as dneg
# other direction
from mc_commut import thm as mc_commut
# other direction
from mc_dist import thm as mc_dist
from mc_identity import thm as rep
from mc_reduct import thm as mc_reduct
from mc_vacons import thm as modt
# modp: p >> ((p >> q) >> q)
from syllo_aaa1 import thm as aaa1

# other direction
from mc_transpos thm as transpose
