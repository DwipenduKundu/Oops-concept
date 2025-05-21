class Triangle:
    def __init__(self):
        self.point = []

    def add_point(self, x, y):
        self.point.append((x, y))

    def distance(self, x1, y1, x2, y2):
        return ((abs(x2-x1)**2)+(abs(y2-y1)**2))**0.5

    def perimeter(self):
        a_x, a_y = self.point[0]
        b_x, b_y = self.point[1]
        c_x, c_y = self.point[2]
        a_side = self.distance(a_x, a_y, b_x, b_y)
        b_side = self.distance(b_x, b_y, c_x, c_y)
        c_side = self.distance(c_x, c_y, a_x, a_y)
        return a_side+b_side+c_side

    def __eq__(self, traingle):
        return self.point == traingle.point


if __name__ == "__main__":
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)

    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)

    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)

    print(t1.perimeter())
    print(t2.perimeter())
    print(t3.perimeter())

    print(t2.__eq__(t3))
    print(t1.__eq__(t3))
    print(t3.__eq__(t1))
