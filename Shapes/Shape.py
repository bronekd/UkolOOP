from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        #Abstraktní metoda pro výpočet tvaru implementována do odvozených tříd
        pass
    