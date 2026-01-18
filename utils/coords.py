from dataclasses import dataclass

@dataclass
class Vector2:
    x: int
    y: int

    def __iter__(self):
        return iter([self.x, self.y])
    
    def copy(self):
        return Vector2(self.x, self.y)
    
    def __eq__(self, val):
        if type(val) != Vector2:
            raise TypeError("Vector2 can't be compared to other types")
        
        return self.x == val.x and self.y == val.y 
    
    def __add__(self, val):
        if type(val) != Vector2:
            raise TypeError("Second operand isn't of type Vector2")
        
        return Vector2(self.x + val.x, self.y + val.y)

    def __mul__(self, scalar):

        if type(scalar) != int:
            return NotImplemented
        
        return Vector2(self.x * scalar, self.y * scalar)