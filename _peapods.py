# Writtin by Ryan William (l_.ll@hotmail.com)

from _peas import pea
from _peas import func_nonclass
from _patch import *

def _sipea(cpy_func_size) -> int:
    return cpy_func_size

def _sepods(cpy_func, set_ize) -> list or tuple:
    '''
    if (type(cpy_func) != tuple or dict):
        error()
    '''
    peapod = []
    set_ize += 1
    for lo_val in range(set_ize):
        if (lo_val == 0):
            peapod.append(cpy_func)
        else:   peapod.append([])
    return peapod

def _sepatch(peapod) -> dict or tuple:
    _isize = len(peapod) - 1 # pods index
    _csize = len(peapod[0]) # cpy_func index
    patch_pod = []
    for lo_val in range(_csize):
        if (lo_val > len(peapod[_isize]) - 1 or peapod[_isize][lo_val] == None):
            in_lo = _isize
            while (in_lo >= 0):
                if (lo_val > len(peapod[in_lo]) - 1 or peapod[in_lo][lo_val] == None):
                    in_lo -= 1
                else:
                    patch_pod.append(peapod[in_lo][lo_val])
                    in_lo = -1 # stop while loop
        else:   patch_pod.append(peapod[_isize][lo_val])
    return patch_pod

openpeap_func = {
        "set patch sort" : _sepatch,
        "made null peapod" : _sepods,
        "set null pod index" : _sipea
}

# rename functions
# smart programmer won't do that, it's stupid
_set_patch = openpeap_func["set patch sort"]
_set_pods  = openPeap_func["made null peapod"]

if __name__ == "__main__":
    cpy_func = pea().func
    cpy_func_nonclass = func_nonclass
    cpy_patch_nonclass = []
    cpy_patch_nonclass.append(xpatch1)
    cpy_patch_nonclass.append(xpatch2)
    cpy_patch_nonclass.append(xpatch3)
    cpy_patch = patch().patch
    # peapod = _sepods(cpy_func, 2)
    peapod = [cpy_func, cpy_patch_nonclass, cpy_patch]
    # ex
    upeapod = [
            cpy_func,
            [
                xpatch1,
                xpatch2,
            ],
            [
                cpy_patch[0]
            ]
    ]
    rpeapod = _sepatch(upeapod)
    # call functions use loop
    for lo_func in rpeapod:
        lo_func()
