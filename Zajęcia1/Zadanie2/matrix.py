class Matrix:
    def __init__(self, a, b, c, d):
        self.a, self.b = a, b
        self.c, self.d = c, d

    def __add__(self, other):
        return Matrix(
            self.a + other.a, self.b + other.b,
            self.c + other.c, self.d + other.d
        )

    def __mul__(self, other):
        return Matrix(
            self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d
        )

    def __str__(self):
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"
