from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color: str):
        self.color = color       # estado compartido

    @abstractmethod
    def area(self) -> float: pass

    @abstractmethod
    def perimetro(self) -> float: pass

    def describir(self):        # concreto — reutilizable
        return f"[{self.color}] A={self.area():.2f} P={self.perimetro():.2f}"

class Circulo(Figura):
    def __init__(self, r, color):
        super().__init__(color)
        self.r = r
    def area(self):      return math.pi * self.r ** 2
    def perimetro(self): return 2 * math.pi * self.r