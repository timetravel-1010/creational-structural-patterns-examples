class Director:
    
    """ Controls the construction process.
    Director has a builder associated with him. Director then
    delegates building of the smaller parts to the builder and
    assembles them together.
    """

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car

# The whole product
class Car:
    
    """ The final product.
    A car is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """

    def __init__(self):
        self.__wheels  = list()
        self.__engine  = None
        self.__body    = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f"body: {self.__body.shape}")
        print(f"engine horsepower: {self.__engine.horsepower}")
        print(f"tire size: {self.__wheels[0].size}\'")


class Builder:

    """ Creates various parts of a vehicle.
    This class is responsible for constructing all
    the parts for a vehicle.
    """

    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


class LamborghiniBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Lamborghini's convertible.
    """

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 770
        return engine

    def getBody(self):
        body = Body()
        body.shape = "convertible"
        return body


class JeepBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

class NissanBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 85
        return engine

    def getBody(self):
        body = Body()
        body.shape = "sport"
        return body
     

class PichiriloBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 14
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 60
        return engine

    def getBody(self):
        body = Body()
        body.shape = "sport"
        return body


# Car parts
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

def main():
    lamborghiniBuilder = LamborghiniBuilder()
    nissanBuilder = NissanBuilder()
    pichiriloBuilder = PichiriloBuilder()

    director = Director()

    # Build Lamborghini
    print("Lamborghini")
    director.setBuilder(lamborghiniBuilder)
    lamborghini = director.getCar()
    lamborghini.specification()

    print("")

    # Build Nissan
    print ("Nissan")
    director.setBuilder(nissanBuilder)
    nissan = director.getCar()
    nissan.specification()

    print("")

    # Build Nissan
    print ("Pichirilo")
    director.setBuilder(pichiriloBuilder)
    pichirilo = director.getCar()
    pichirilo.specification()


if __name__ == "__main__":
    main()