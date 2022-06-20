c = 1


class Transform():
    def __init__(self, v) -> None:
        self.v = v
        self.gamma = 1 / (1 - (v/c)**2)**0.5

    def transform(self, x, t):
        return (self.gamma*(x - v*t),
                self.gamma*(t - v*x/c**2))
        
    def reverse_transform(self, x, t):
        return (self.gamma*(x + v*t),
                self.gamma*(t + v*x/c**2))


if __name__ == '__main__':
    print(f"Speed of light is {c}.")

    v = float(input("v: "))

    t = Transform(v)

    x1 = float(input("x1 (light second): "))
    t1 = float(input("t1 (second): "))

    x2, t2 = t.transform(x1, t1)

    print(f"{x2=}, {t2=}")
    
    print(t.reverse_transform(x2, t2))
