from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        multiplied_coordinates = map(lambda x: x*Decimal(c), self.coordinates)
        return Vector(multiplied_coordinates)

    def magnitude(self):
        vectorsquare = map(lambda x: x**2, self.coordinates)
        return sqrt(sum(vectorsquare))

    def normalise(self):
        try:
            magnitude = self.magnitude()
            return self.scalarmultiplication(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalise the zero vector')

    def dotproduct(self, v):
        dot_prod = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        return dot_prod

    # v.w = |v||w|cosx, x = arccos(v.w/|v||w|)
    def angle(self, v, deg=False):
        try:
            v1 = self.normalise()
            v2 = v.normalise()
            angle_rad = acos(v1.dotproduct(v2))

            if deg:
                angle_deg = angle_rad * (180. / pi)
                return angle_deg
            else:
                return angle_rad

        except Exception as e:
            raise e

    def angle(self, v):
        self.dotproduct(v)/(self.magnitude() * v.magnitude())

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])

print v.dotproduct(w)

print v.angle(w)
