"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}
    def __init__(self, name, flavor, price):

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[name] = self.cache.get(name,
                             self)
    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
        self.qty += int(amount)

    def sell(self, amount):
        if self.qty > amount:
            self.qty -= amount
        elif self.qty == amount:
            print("there are no more cupcakes after this purchase")
        elif self.qty == 0:
            print(f"Sorry, these cupcakes are sold out")
        elif self.qty < amount:
            self.qty = 0
            # print(f"i can sell you {self.qty} cupcakes")

    # static methods
    @staticmethod
    def scale_recipe(ingredients, amount):
        return [ (ingred, num * amount) for ingred, num in ingredients]
            
        
    # class methods
    @classmethod
    def get(cls, name):
        if name in cls.cache.keys():
            return cls.cache[name] 
        else:
            print("Sorry, that cupcake doesn't exist")


class Brownie (Cupcake):
    def __init__(self, name, price):
        super().__init__(name, "chocolate", price)


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Brownie name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
