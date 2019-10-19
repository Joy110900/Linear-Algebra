import math

class vector(object):
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


    def __str__(self):
        return 'vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def v_add(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return vector(new_coordinates)
    
    def v_sub(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return vector(new_coordinates)

    def v_scalar_mul(self, k):
        new_coordinates = [x*k for x in self.coordinates]
        return vector(new_coordinates)

    def v_mag(self):
        magnitude = 0
        for i in self.coordinates:
            magnitude += i**2
        return math.pow(magnitude,0.5)

    def v_normalised(self):
        try:
            mag = self.v_mag()
            return self.v_scalar_mul(1.0/mag)

        except ZeroDivisionError:
            print('Cannot normalise a zero vector')

    def v_dot(self,v):
        t = 0
        for x,y in zip(self.coordinates, v.coordinates):
            t += x*y
        return t
    
    def v_ang(self,v, in_degree=False):
        x = self.v_normalised()
        y = v.v_normalised()
        dr = math.acos(x.v_dot(y))
        
        if in_degree:
            radian_to_deg = 180.0/3.1415326
            return dr * radian_to_deg
        
        else:
            return dr

v1 = vector([3.183,-7.627])
v2 = vector([-2.668, 5.319])

print(v1.v_ang(v2))