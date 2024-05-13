

class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def __str__(self):
        return f'{self.type} těstoviny s: {self.sauce} omáčkou, {self.topping} toppingem a  {self.dressing} dressingem'

class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self, pasta_type):
        self.pasta.type = pasta_type
        return self

    def set_sauce(self, sauce):
        self.pasta.sauce = sauce
        return self

    def set_topping(self, topping):
        self.pasta.topping = topping
        return self

    def set_dressing(self, dressing):
        self.pasta.dressing = dressing
        return self

    def build(self):
        return self.pasta





if __name__ == '__main__':
    #builder
    builder_spaghetti = PastaBuilder()
    builder_penne = PastaBuilder()

    #tvorba těstovin
    spaghetti = builder_spaghetti.set_type('Spaghetti').set_sauce('Tomato').set_topping('Cheese').build()
    penne = builder_penne.set_type('Penne').set_sauce('Cream').set_topping('Chicken').set_dressing('Pesto').build()

    print(spaghetti)
    print(penne)





