class Graphics:
    def __init__(self, square_side=None, length=None, width=None, radius=None):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius
    
    def getSquareArea(self):
        if self.square_side is not None:
            square_area = self.square_side * self.square_side
            return square_area
        else:
            return None

    def getRectangleArea(self):
        if self.length is not None and self.width is not None:
            rectangle_area = self.length * self.width
            return rectangle_area
        else:
            return None

    def getCircleArea(self):
        if self.radius is not None:
            circle_area = self.radius * self.radius * 3.14
            return circle_area
        else:
            return None

def main():
    graphics_object = Graphics()
    print(graphics_object.getSquareArea())
    print(graphics_object.getRectangleArea())
    print(graphics_object.getCircleArea())

if __name__ =='__main__':
    main()


    