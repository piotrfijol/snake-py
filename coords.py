from dataclasses import dataclass

@dataclass
class Vector2:
    x: int
    y: int

    def __iter__(self):
        return iter([self.x, self.y])
    
    def copy(self):
        return Vector2(self.x, self.y)