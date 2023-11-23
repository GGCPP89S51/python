class Graphics:
    def __init__(self, square_side=None, length=None, width=None, radius=None):
        self.square_side, self.length, self.width, self.radius = square_side, length, width, radius
    
    def getSquareArea(self):
        square_area = self.square_side * self.square_side
        return square_area

    def getRectangleArea(self):
        rectangle_area = self.length * self.width
        return rectangle_area

    def getCircleArea(self):
        circle_area = self.radius * self.radius * 3.14
        return circle_area

def main():
    graphics_object = Graphics(5, 10, 5, 6)
    print(graphics_object.getSquareArea())
    print(graphics_object.getRectangleArea())
    print(graphics_object.getCircleArea())

if __name__ =='__main__':
    main()

    