class Graphics:
    def __init__(self, square_side, length, width, radius) -> None :
        self.square_side, self.length, self.width, self.radius = square_side, length, width, radius
    
    def getSquareArea(self):
        if self.square_side != None :
            square_area = self.square_side * self.square_side
            return square_area
        else:
            return None
    def getRectangleArea(self):
        if self.length != None and self.width != None:
            rectangle_area = self.length * self.width
            return rectangle_area
        else:
            return None

    def getCircleArea(self):
        if self.radius != None :
            circle_area = self.radius * self.radius * 3.14
            return circle_area
        else:
            return None
def main():
    graphics_object = Graphics(5, 10, 5, 6)
    print(graphics_object.getSquareArea())
    print(graphics_object.getRectangleArea())
    print(graphics_object.getCircleArea())

if __name__ =='__main__':
    main()

    