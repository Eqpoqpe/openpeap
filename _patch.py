def xpatch1():   print("_patch.patch1")

def xpatch2():  print("_patch.patch2")

def xpatch3():  print("_patch.patch3")

class patch:
    def __init__(self):
        self.patch = []
        self.patch.append(self._patch1)
        self.patch.append(self._patch2)
        self.patch.append(self._patch3)

    def _patch1(self):
        print("patch1")

    def _patch2(self):
        print("patch2")

    def _patch3(self):
        return 0
