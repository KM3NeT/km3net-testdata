import os
from pkg_resources import get_distribution, DistributionNotFound

version = get_distribution(__name__).version


def testdata(*path_elements):
    return os.path.join(*path_elements)
