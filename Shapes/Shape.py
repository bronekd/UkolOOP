from abc import ABC, abstractmethod
import pickle
class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        #Abstraktní metoda pro výpočet tvaru implementována do odvozených tříd
        pass

    def Show(self):
        print(self.__str__())

    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


