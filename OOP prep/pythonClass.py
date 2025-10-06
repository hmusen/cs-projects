class Rectangle:
    def __init__(self, w, h ):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * (self.width)) + (2 * (self.height))
    
    def get_diagonal(self):
        return (((self.width)**2) + ((self.height)**2))**0.5

rect_1 = Rectangle(10, 223)

area = print("Area is ", rect_1.get_area())

perimeter = print("Perimeter is", rect_1.get_perimeter())

diagonal = print("The diagonal is", round(rect_1.get_diagonal(), 2), "to 2 decimal places")

