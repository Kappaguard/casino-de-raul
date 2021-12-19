from numbers import Number
import itertools


class MatrixDomainError(ValueError):
    pass

class MatrixTypeError(TypeError):
    pass


class Matrix:
    """Matrix itself"""
    
    def __init__(self, arg=0):
        """
        args — arguments
        """
        if isinstance(arg, Number):
            self.args = [arg]
        elif isinstance(arg, list):
            self.args = arg.copy()
        elif isinstance(arg, Matrix):
            self.args = arg.args.copy()
        else:
            raise MatrixTypeError("You are trying to create matrix from " + repr(arg))

    def __list__(self):
        """Array of 3x3 initialization"""
        array=[]
        for i in range(3):
            array.append([])
            array[i]=[0]*3
            
        return (list(self.args))
   
    def __eq__(self, other):
       
        if isinstance(other, Number):
            other = Matrix(other)
        
        if isinstance(other, Matrix):
            return self.args == other.args
        else:
            raise MatrixDomainError("Can't say if Matrix is equal to " + str(type(other)))

    def __add__(self, other):
        if isinstance(other, Number):
            other = Matrix(other)
        
        sargs = self.args.copy()
        oargs = other.args.copy()
        
        return Matrix([
            sarg + oarg for sarg, oarg in zip(sargs, oargs)
        ])
        
        
    def __radd__(self, other):
        return self.__add__(other)  # Коммутативность

    def __neg__(self):
        return Matrix([-c for c in self.args])

    def __sub__(self, other):
        if isinstance(other, Number):
            other = Matrix(other)

        return self.__add__(other.__neg__())

    
    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    
    def __mul__(self, other):
        if isinstance(other, Number):
            other = Matrix(other)
        
        c = [0] * (len(self.args) + len(other.args) - 1)
        for sc, sci in zip(self.args, itertools.count()):
            for oc, oci in zip(other.args, itertools.count()):
                c[sci + oci] += sc * oc
        
        return Matrix(c)
        
        
    #def __rmul__(self, other):
       # return self.__mul__(other)  # Коммутативность

    def __int__(self) -> int:
        if not len(self.args):
            return 0
        elif len(self.args) == 1:
            return int(self.args[0])
        else:
            raise MatrixDomainError("Can't consider higher degree matrix as an integer")

m1 = Matrix()
m2 = Matrix([1,2,3,4])
m3 = 3

print(m2+m3)
