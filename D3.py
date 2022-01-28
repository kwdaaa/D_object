class Square:
    def __init__(self, side):
        self.side = side

    # 正方形の面積を求める。（辺 × 辺）
    def area(self):
        result = self.side * self.side
        return result

    # 正方形の対角の長さを求める。（辺 × 1.41421356237）
    def diagonal(self):
        result = self.side * 1.41421356237
        return f"{result:.2f}"


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
