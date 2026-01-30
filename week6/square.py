from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)



if __name__ == "__main__":
    sq = Square("MNOP", 4)
    print(sq)