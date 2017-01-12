from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        added_coordinates = [ x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(added_coordinates)

    def minus(self, v):
        minus_coordinates = [ x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(minus_coordinates)

    def scalarmultiplication(self, c):
        multiplied_coordinates = map(lambda x: x*c, self.coordinates)
        return Vector(multiplied_coordinates)

    def magnitude(self):
        vectorsquare = map(lambda x: x**2, self.coordinates)
        return sqrt(sum(vectorsquare))

    def normalise(self):
        try:
            magnitude = self.magnitude()
            return self.scalarmultiplication(1/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalise the zero vector')

    def dotproduct(self, v):
        dot_prod = sum([ x*y for x,y in zip(self.coordinates, v.coordinates)])
        return dot_prod

    def angle(self, v):
        self.dotproduct(v)/(self.magnitude() * v.magnitude())

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
