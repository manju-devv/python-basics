class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show2D(self):
        print(f"this is {self.i}i + {self.j}j 2D Vector")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show3D(self):
        print(f"this is {self.i}i + {self.j}j + {self.k}k 3D Vector")


two_d = TwoDVector(2,5)
two_d.show2D()
three_d = ThreeDVector(2,5,7)
three_d.show3D()
