class graphics:
    def __init__(self,square_side,length,weidth,redius) -> None:
        self.square_side,self.length,self.weidth,self.redius = square_side,length,weidth,redius
    
    def getSquareArea(self) :
        Square = self.square_side * self.square_side
        return square

    def getRectangleArea(self) :
        Rectangle = self.length *self.weidth
        return Rectangle

    def getCircleArea(self) :
        Circle = self.redius *self.redius *3.14
        return Circle

def main():
    Graphics = graphics
    