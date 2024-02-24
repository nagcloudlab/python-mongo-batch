

"""
    
    design issues
    -------------
    --> tight-coupling b/w Billing ( dependent ) & PriceMatrix ( Dependency) classes

    problems:
    --> can't extend or replace PriceMatrix class with some other implementation


    performance issues
    -------------------
    --> for every cart, new instance of PriceMatrix class is created

    problems:
    --> memory use will be increased, and effect on performance


    why these issues?

    --> creating dependency object in the dependent class

    solution:

    --> don't create dependency object in the dependent class, get it from factory

    limitation on factory:

    --> dependent must know how to get the dependency from factory

    best solution:

    --> don't create, don't lookup, get from factory, let someone else inject it
        ( Inversion of Control )

    how to implement IoC?

    --> Dependency Injection ( DI )


    ------------------------------------------------------------------------------

    SOLID Principles aka OO design Principles

    S - Single Responsibility Principle
    O - Open for extension, Closed for modification Principle
    L - Liskov Substitution Principle
    I - Interface Segregation Principle
    D - Dependency Inversion Principle

    ------------------------------------------------------------------------------


"""

class Billing:

    def __init__(self,priceMatrix):
        self.priceMatrix = priceMatrix

    def getTotalPrice(self,cart):
        total = 0
        for item in cart:
            total+=self.priceMatrix.get_price(item)
        return total