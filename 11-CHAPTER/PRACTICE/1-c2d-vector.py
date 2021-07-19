class C2dvector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}i"

class A3dVector(C2dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}i + {self.kcap}k"


v2d = C2dvector(1,3)
v3d= A3dVector(1,9, 7)
print(v2d)
print(v3d)