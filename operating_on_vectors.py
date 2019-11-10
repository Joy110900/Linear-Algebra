import math

pi = math.pi
e = math.e

class vector(object):
    def __init__(self, coordinates):
        """This func is like constructor in c++. Here it initialises our vector with values from user."""
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
        """This func returns the sum of the vectors."""
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return vector(new_coordinates)
    
    def v_sub(self, v):
        """This func returns the difference of the vectors."""
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return vector(new_coordinates)

    def v_scalar_mul(self, k):
        """This func returns the scalar product of the vector"""
        new_coordinates = [x*k for x in self.coordinates]
        return vector(new_coordinates)

    def v_mag(self):
        """This func returns the magnitude of the vector. 
            It is calculated as mag = root(sum of squares of all coordinates)"""
        magnitude = 0
        for i in self.coordinates:
            magnitude += i**2
        return math.pow(magnitude,0.5)

    def v_normalised(self):
        """This func returns normalised or the unit vector of the vector. 
        normalised = v*(1/mag(v))"""
        try:
            mag = self.v_mag()
            return self.v_scalar_mul(1.0/mag)

        except ZeroDivisionError:
            print('Cannot normalise a zero vector')

    def v_dot(self,v):
        """This func returns the dot product between 2 vectors"""
        t = 0
        for x,y in zip(self.coordinates, v.coordinates):
            t += x*y
        return t
    
    def v_ang(self,v, in_degree=False):
        """This func returns angle between 2 vectors in radian. If we want angle in degree make in_degree = True"""
        x = self.v_normalised()
        y = v.v_normalised()
        dr = math.acos(x.v_dot(y))
        
        if dr > 2*pi:
            dr -= 2*pi

        if in_degree:
            radian_to_deg = 180.0/pi
            dd = dr * radian_to_deg
            return dd
        
        else:
            return dr

    def is_zero(self, tolerance=1e-10):
        """Func to check weather the given vector is zero vector or not"""
        return self.v_mag() < tolerance

    def is_parallel_to(self, v):
        """Func to check if 2 vectors are parallel to each other."""
        return (self.is_zero() or v.is_zero() or self.v_ang(v) == 0 or self.v_ang(v) == pi)

    def is_orthogonal_to(self, v, tolerance=1e-10):
       """Func to check if 2 vectors are perpendicular to each other."""
       return abs(self.v_dot(v)) < tolerance  

    def parallel_component_to(self, basis):
        v_norm = basis.v_normalised()
        v1 = self.v_dot(v_norm)
        return v_norm.v_scalar_mul(v1)

    def perpendicular_component_to(self, v):
        vp = self.parallel_component_to(v)
        return self.v_sub(v)

    def cross(self, v):
        if len(self.coordinates) == 2:
            self_embedded_in_r3 = vector(self.coordinates + (0,))
            v_embedded_in_r3 = vector(v.coordinates + (0,))
            return self_embedded_in_r3.cross(v_embedded_in_r3)
       
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates

        new_coordinates = [ y1*z2 - y2*z1, -(x1*z2 - x2*z1), x1*y2 - x2*y1]

        return vector(new_coordinates)

    def area_of_parallelogram_with(self, v):
        return (self.cross(v)).v_mag()

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / 2.0