import os

from .cache import CacheObject

HyperGlobalVariable = CacheObject("hgv.json")
cache = HyperGlobalVariable

def u_get_src_path()->os.PathLike:
    return os.path.dirname(os.path.realpath(__file__))

def u_generate_id()->int:
    ...