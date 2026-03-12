from abc import ABC, abstractmethod

class Volador(ABC)
    @abstractmethod
    def volar(self): pass
    @abstractmethod
    def aterrizar(self): pass
    
class Nadador(ABC):
    @abstractmethod
    def nadar(self): pass
    
#Herencia multiple - Python lo soporta de forma nativa
class Pato(Volador, Nadador):
    def volar(self):    print("volar")
    def aterrizar(self):    print("Plof!")
    def nadar(self):    print("Nadar")