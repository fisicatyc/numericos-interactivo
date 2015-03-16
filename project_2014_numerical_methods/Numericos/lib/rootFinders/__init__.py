# rootFinder - initializing file
# Generic root finder module
__all__ = ['bisection','fixedpoint','muller','polyroot','regulafalsi','secant'];
from .bisection import bisection
from .fixedpoint import fixedpoint
from .muller import muller
from .polyroot import polyroot
from .regulafalsi import regulafalsi
from .secant import secant