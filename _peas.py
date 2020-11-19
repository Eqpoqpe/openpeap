# Writtin by Ryan William (l_.ll@hotmail.com)

class pea:
    def __init__(self):
        self.func = []
        self.func.append(self._pea1)
        self.func.append(self._pea2)
        self.func.append(self._pea3)
        self.func = tuple(self.func)
        '''
        self.func_dict = {
            "_pea1" : self._pea1,
            "_pea2" : self._pea2,
            "_pea3" : self._pea3
        }
        '''

    def _pea1(self):
        print("pea1")

    def _pea2(self):
        print("pea2")

    def _pea3(self):
        print("pea3")
        return 1

def _patch1():
    print("patch1")

def _patch2():
    print("patch2")

def _patch3():
    return 0

func_nonclass = []
func_nonclass.append(_patch1)
func_nonclass.append(_patch2)
func_nonclass.append(_patch3)

func_nonclass_dict = {
        "_patch1" : _patch1,
        "_patch2" : _patch2,
        "_patch3" : _patch3
}
