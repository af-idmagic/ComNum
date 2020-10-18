# ------------------------------------------------------------------------
# Module:      comnum
# Object:      Basic operations with complex numbers
#
# Author:      Alexey FEDOROV
# Created:     07.10.2020
# Copyright:   (c) Alexey FEDOROV (idmagic) 2020
# ------------------------------------------------------------------------

# To launch the doctests:  python -m doctest -v comnum.py

from __future__ import annotations

from math import sqrt as sqrt
from math import atan2 as atan2
from math import sin as sin
from math import cos as cos
from math import log as log


class ComNum:
    """ Define a complex number x + y*i where i*i = -1 """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """ Initialize a complex number x + y*i where i*i = -1.
            
            Parameters
            ----------
            x : float
                Real part of the complex number.
            y : float
                Imaginary part of the complex number.
                
            Returns
            -------
            None
                As per PEP-484.
        
            Examples
            --------
            >>> dum_tup = (1, 2)
            >>> isinstance(dum_tup, tuple)
            True
            >>> dum_CN = ComNum(1, 2)
            >>> isinstance(dum_CN, tuple)
            False
            >>> isinstance(dum_CN, ComNum)
            True
        """
        self.real = x
        self.img = y

# Getter method for the real part of a complex number.
    @property
    def real(self):
        return self.__real

# Setter method for the real part of a complex number.
# Impose conditions to set value limits.
    @real.setter
    def real(self, real):
        self.__real = real

# Getter method for the imaginary part of a complex number.
    @property
    def img(self):
        return self.__img

# Setter method for the imaginary part of a complex number.
# Impose conditions to set value limits.
    @img.setter
    def img(self, img):
        self.__img = img

    def __str__(self) -> str:
        """ Print a complex number as "[x] +/- [y*i]" for clarity.
            The elements in brackets are omitted when equal to zero.
            
            Parameters
            ----------
            No parameters.
                
            Returns
            -------
            str
                The printable representation of the complex number.
        
            Examples
            --------
            >>> print(ComNum(1, 2))
            1 + 2*i
            >>> print(ComNum(5, 0))
            5
            >>> print(ComNum(0, -3))
            -3*i
        """
        r = self.real
        i = self.img

        # Complex number is zero.
        if r == 0 and i == 0:
            prtstr = "0"

        # Complex number is purely imaginary.
        elif r == 0:
            prtstr = str(i) + "*i"

        # Complex number is purely real.
        elif i == 0:
            prtstr = str(r)

        # Complex number with both real and imaginary parts.
        else:
            if i < 0:
                sigstr = " - "
                sig = -1
            else:
                sigstr = " + "
                sig = 1
            prtstr = str(r) + sigstr + str(sig*i) + "*i"

        return prtstr

    def __round__(self, n: int = 0) -> ComNum:
        """ Round real and imaginary parts of a complex number
            (x and y in x + y*i) to n decimal places each.
            
            Parameters
            ----------
            n : int
                The number of decimal places for rounding.
                
            Returns
            -------
            ComNum
                The rounded complex number.
        
            Examples
            --------
            >>> from math import sqrt
            >>> from math import pi
            >>> print(round(ComNum(sqrt(2), pi), 5))
            1.41421 + 3.14159*i
        """
        r = self.real
        i = self.img
        r = round(r, n)
        i = round(i, n)
        return ComNum(r, i)

    def __eq__(self, other: ComNum) -> bool:
        """ Check if the 2 complex numbers are equal.
            The result is a boolean value.
        
            Parameters
            ----------
            other : ComNum
                The second complex number to check the equality with.
                
            Returns
            -------
            bool
                True if the 2 numbers are equal, False otherwise.
        
            Examples
            --------
            >>> ComNum(1, 2) == ComNum(3, 4)
            False
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return r1 == r2 and i1 == i2

    def __add__(self, other: ComNum) -> ComNum:
        """ Add 2 complex numbers x1 + y1*i and x2 + y2*i.
            The result is (x1 + x2) + (y1 + y2)*i.
        
            Parameters
            ----------
            other : ComNum
                The 2nd complex number to be added to the 1st one.
                
            Returns
            -------
            ComNum
                The result of the addition.
        
            Examples
            --------
            >>> print(ComNum(1, 2) + ComNum(3, 4))
            4 + 6*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1+r2, i1+i2)

    def __sub__(self, other: ComNum) -> ComNum:
        """ Subtract 2 complex numbers x1 + y1*i and x2 + y2*i.
            The result is (x1 - x2) + (y1 - y2)*i.
        
            Parameters
            ----------
            other : ComNum
                The 2nd complex number to be subtracted from the 1st one.
                
            Returns
            -------
            ComNum
                The result of the subtraction.
        
            Examples
            --------
            >>> print(ComNum(1, 2) - ComNum(3, 4))
            -2 - 2*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1-r2, i1-i2)

    def __mul__(self, other: ComNum) -> ComNum:
        """ Multiply 2 complex numbers x1 + y1*i and x2 + y2*i.
            The result is (x1*x2 - y1*y2) + (x1*y2 - y1*x2)*i.
        
            Parameters
            ----------
            other : ComNum
                The 2nd complex number to multiply the 1st one by.
                
            Returns
            -------
            ComNum
                The result of the multiplication.
        
            Examples
            --------
            >>> print(ComNum(1, 2)*ComNum(3, 4))
            -5 + 10*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1*r2 - i1*i2, r1*i2 + i1*r2)

    def __truediv__(self, other: ComNum) -> ComNum:
        """ Divide 2 complex numbers x1 + y1*i and x2 + y2*i.
            The result is z*(x1*x2 + y1*y2) + z*(y1*x2 - x1*y2)*i
            where z = 1/(x2*x2 + y2*y2).
        
            Parameters
            ----------
            other : ComNum
                The 2nd complex number to divide the 1st one by.
                
            Returns
            -------
            ComNum
                The result of the division.
        
            Examples
            --------
            >>> print(ComNum(1, 2)/ComNum(3, 4))
            0.44 + 0.08*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        fact = 1/(r2*r2 + i2*i2)
        return ComNum(fact*(r1*r2 + i1*i2), fact*(i1*r2 - r1*i2))

    def modul(self) -> float:
        """ Find the modulus of a complex number x + y*i.
            The result is sqrt(x^2 + y^2).
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            float
                The modulus.
        
            Examples
            --------
            >>> ComNum.modul(ComNum(1, 2))
            2.23606797749979
        """
        r = self.real
        i = self.img
        modul = sqrt(r*r + i*i)
        return modul

    def argt(self) -> float:
        """ Find the argument of a complex number x + y*i.
            The result is atan2(y, x).
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            float
                The argument.
        
            Examples
            --------
            >>> ComNum.argt(ComNum(1, 2))
            1.1071487177940904
        """
        r = self.real
        i = self.img
        return atan2(i, r)

    def conjug(self) -> ComNum:
        """ Conjugate a complex number x + y*i.
            The result is x - y*i.
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            ComNum
                The conjugate of the complex number.
        
            Examples
            --------
            >>> print(ComNum.conjug(ComNum(1, 2)))
            1 - 2*i
        """
        r = self.real
        i = self.img
        return ComNum(r, -1*i)

    def recipr(self) -> ComNum:
        """ Reciprocate a complex number x + y*i.
            The result is 1/(x + y*i) = z*x - z*y*i
            where z = 1(x^2 + y^2).
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            ComNum
                The reciprocated complex number.
        
            Examples
            --------
            >>> print(ComNum.recipr(ComNum(1, 2)))
            0.2 - 0.4*i
        """
        r = self.real
        i = self.img
        fact = 1/(r*r + i*i)
        return ComNum(fact*r, -1*fact*i)

    def pr_sqrt(self) -> ComNum:
        """ Find the principal square root of the complex number x + y*i.
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            ComNum
                The principal square root of the complex number.
        
            Examples
            --------
            >>> print(ComNum.pr_sqrt(ComNum(1, 2)))
            1.272019649514069 + 0.7861513777574233*i
        """
        r = self.real
        i = self.img
        if i < 0:
            sig = -1
        else:
            sig = 1
        modul = ComNum.modul(self)
        return ComNum(sqrt((modul+r)/2), sig*sqrt((modul-r)/2))

    def pr_com_ln(self) -> ComNum:
        """ Find the principal value of the natural logarithm
            of a complex number v = x + y*i.
            The result is ln(|x|) + arg(v)*i.
            
            Parameters
            ----------
            No parameters.
            
            Returns
            -------
            ComNum
                The principal value of the natural logarithm
                of the complex number.
        
            Examples
            --------
            >>> print(ComNum.pr_com_ln(ComNum(1, 2)))
            0.8047189562170503 + 1.1071487177940904*i
        """
        modul = ComNum.modul(self)
        argt = ComNum.argt(self)
        return ComNum(log(modul), argt)

    def com_exp(self, n: int = 1) -> ComNum:
        """ Raise a complex number to the power of n (n is an integer).
            Rounds the result to 10 decimals.
        
            Parameters
            ----------
            n : int
                The power to raise the complex number to.
                
            Returns
            -------
            ComNum
                The complex number raised to the power of n.
        
            Examples
            --------
            >>> print(ComNum.com_exp(ComNum(1, 2), 3))
            -11.0 - 2.0*i
        """
        if isinstance(n, float):
            raise ValueError("the power n must be an integer!")

        modul = ComNum.modul(self)
        argt = ComNum.argt(self)
        fact = modul**n
        r_exp = round(fact*cos(n*argt), 10)
        i_exp = round(fact*sin(n*argt), 10)
        return ComNum(r_exp, i_exp)

    def com_exp_alt(self, n: int = 1) -> ComNum:
        """ Raise a complex number to the power of n (n is an integer).
            (An alternative calculation solution).
            Rounds the result to 10 decimals.
        
            Parameters
            ----------
            n : int
                The power to raise the complex number to.
                
            Returns
            -------
            ComNum
                The complex number raised to the power of n.
        
            Examples
            --------
            >>> print(ComNum.com_exp_alt(ComNum(1, 2), -4))
            -0.0112 + 0.0384*i
        """
        if isinstance(n, float):
            raise ValueError("the power n must be an integer!")
        if n == 0:
            return ComNum(1, 0)
        elif n > 0:
            k = 1
            mult = self
            while k < n:
                self *= mult
                k += 1
            return ComNum.__round__(self, 10)
        else:
            n = -n
            k = 1
            mult = self
            while k < n:
                self *= mult
                k += 1
            return ComNum.__round__(ComNum.recipr(self), 10)
