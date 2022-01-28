class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 長方形の面積を求める。（高さ×幅）※小数点第二位以下を四捨五入
    def area(self):
        result = self.height * self.width
        return f"{result:.2f}"

    # 長方形の対角線の長さを求める。（(高さの2乗 + 幅の2乗)×0.5×0.5）※小数点第二位以下を四捨五入
    def diagonal(self):
        result = ((self.height * self.height) + (self.width * self.width)) ** 0.5
        return f"{result:.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
