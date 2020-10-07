#-------------------------------------------------------------------------------
# Module:      ComNum_test
# Objet:       Opérations basiques avec des nombres complexes
#
# Auteur:      Alexey FEDOROV
# Créé le:     07.10.2020
# Copyright:   (c) Alexey FEDOROV (idmagic) 2020
#-------------------------------------------------------------------------------

# Pour lancer les doctests :  python -m doctest -v ComNum_test.py


from math import sqrt as sqrt
from math import atan2 as atan2
from math import sin as sin
from math import cos as cos
from math import pi as pi
from math import log as log


class ComNum:
    """ Un nombre complexe X + Y*i où i*i = -1 """

    def __init__(self, X=0, Y=0):
        """ Initialiser un nombre complexe X + i*Y où i*i = -1
            >>> dum_tup = (1, 2)
            >>> isinstance(dum_tup, tuple)
            True
            >>> dum_CN = ComNum(1, 2)
            >>> isinstance(dum_CN, tuple)
            False
            >>> isinstance(dum_CN, ComNum)
            True
        """
        self.real = X
        self.img = Y

    def __str__(self):
        """ Imprimer un nombre complexe sous format [X] +/- [Y*i]
            >>> print(ComNum(1, 2))
            1 + 2*i
            >>> print(ComNum(5, 0))
            5
            >>> print(ComNum(0, -3))
            -3*i
        """
        r = self.real
        i = self.img

        # nombre est zéro
        if r == 0 and i == 0:
            prtstr = "0"

        # nombre purement imaginaire
        elif r == 0:
            prtstr = str(i) + "*i"

        # nombre purement réel
        elif i == 0:
            prtstr = str(r)

        # nombre complexe
        else:
            if i < 0:
                sigstr = " - "
                sig = -1
            else:
                sigstr = " + "
                sig = 1
            prtstr = str(r) + sigstr + str(sig*i) + "*i"

        return prtstr

    def __round__(self, n=0):
        """ Arrondir X et Y d'un nombre complexe X + i*Y à n décimales chacun
            >>> print(round(ComNum(sqrt(2), pi), 5))
            1.41421 + 3.14159*i
        """
        r = self.real
        i = self.img
        r = round(r, n)
        i = round(i, n)
        return ComNum(r, i)

    def __eq__(self, other):
        """ Vérifier égalité entre 2 nombres complexes
            >>> ComNum(1, 2) == ComNum(3, 4)
            False
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return (r1==r2 and i1==i2)

    def __add__(self, other):
        """ Ajouter 2 nombres complexes
            >>> print(ComNum(1, 2) + ComNum(3, 4))
            4 + 6*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1+r2, i1+i2)

    def __sub__(self, other):
        """ Soustraire 2 nombres complexes
            >>> print(ComNum(1, 2) - ComNum(3, 4))
            -2 - 2*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1-r2, i1-i2)

    def __mul__(self, other):
        """ Multiplier 2 nombres complexes
            >>> print(ComNum(1, 2)*ComNum(3, 4))
            -5 + 10*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        return ComNum(r1*r2 - i1*i2, r1*i2 + i1*r2)

    def __truediv__(self, other):
        """ Diviser 2 nombres complexes
            >>> print(ComNum(1, 2)/ComNum(3, 4))
            0.44 + 0.08*i
        """
        r1 = self.real
        i1 = self.img
        r2 = other.real
        i2 = other.img
        fact = 1/(r2*r2 + i2*i2)
        return ComNum(fact*(r1*r2 + i1*i2), fact*(i1*r2 - r1*i2))

    def modul(self):
        """ Trouver le modulus d'un nombre complexe
            >>> ComNum.modul(ComNum(1, 2))
            2.23606797749979
        """
        r = self.real
        i = self.img
        modul = sqrt(r*r + i*i)
        return modul

    def argt(self):
        """ Trouver l'argument d'un nombre complexe
            >>> ComNum.argt(ComNum(1, 2))
            1.1071487177940904
        """
        r = self.real
        i = self.img
        return atan2(i,r)

    def conjug(self):
        """ Conjuguer un nombre complexe
            >>> print(ComNum.conjug(ComNum(1, 2)))
            1 - 2*i
        """
        r = self.real
        i = self.img
        return ComNum(r, -1*i)

    def recipr(self):
        """ Réciproquer un nombre complexe
            >>> print(ComNum.recipr(ComNum(1, 2)))
            0.2 - 0.4*i
        """
        r = self.real
        i = self.img
        fact = 1/(r*r + i*i)
        return ComNum(fact*r, -1*fact*i)

    def pr_sqrt(self):
        """ Trouver la racine carrée principale d'un nombre complexe
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

    def pr_com_ln(self):
        """ Trouver la valeur principale de log naturel d'un nombre complexe
            >>> print(ComNum.pr_com_ln(ComNum(1, 2)))
            0.8047189562170503 + 1.1071487177940904*i
        """
        r = self.real
        i = self.img
        modul = ComNum.modul(self)
        argt = ComNum.argt(self)
        return ComNum(log(modul), argt)

    def com_exp(self, n=1):
        """ Elever un nombre complexe en puissance n (n est un nombre entier)
            >>> print(ComNum.com_exp(ComNum(1, 2), 3))
            -11.0 - 2.0*i
        """
        if isinstance(n, float):
            raise ValueError("la puissance n doit être un nombre entier !")
        r = self.real
        i = self.img
        modul = ComNum.modul(self)
        argt = ComNum.argt(self)
        fact = modul**n
        r_exp = round(fact*cos(n*argt), 10)
        i_exp = round(fact*sin(n*argt), 10)
        return ComNum(r_exp, i_exp)

    def com_exp_alt(self, n=1):
        """ Elever un nombre complexe en puissance n (n est un nombre entier) —
            solution alternative
            >>> print(ComNum.com_exp_alt(ComNum(1, 2), -4))
            -0.0112 + 0.0384*i
        """
        if isinstance(n, float):
            raise ValueError("la puissance n doit être un nombre entier !")
        if n == 0:
            return ComNum(1, 0)
        elif n > 0:
            k = 1
            mult = self
            while k < n:
                self *= mult
                k += 1
            return round(self, 10)
        else:
            n = -n
            k = 1
            mult = self
            while k < n:
                self *= mult
                k += 1
            return round(ComNum.recipr(self), 10)


class TestComNum:
    """ pytests pour la classe ComNum dont un objet est un nombre complexe X + Y*i
        Pour lancer les pytests :  python -m pytest ComNum_test.py
    """

    def test_round(self):
        num = ComNum(sqrt(2), pi)
        assert round(num, 5) == ComNum(1.41421, 3.14159)

    def test_eq(self):
        assert ComNum(2, 3) == ComNum(2, 3)

    def test_add(self):
        assert ComNum(2, 3) + ComNum(4, -5) == ComNum(6, -2)

    def test_sub(self):
        assert ComNum(2, 3) - ComNum(4, -5) == ComNum(-2, 8)

    def test_mul(self):
        assert ComNum(2, 3)*ComNum(4, -5) == ComNum(23, 2)

    def test_div(self):
        assert ComNum(4, 6)/ComNum(2, 3) == ComNum(2, 0)

    def test_modul(self):
        assert ComNum.modul(ComNum(3, 4)) == 5

    def test_argt(self):
        assert ComNum.argt(ComNum(0, 1)) == pi/2

    def test_conjug(self):
        assert ComNum.conjug(ComNum(2, 3)) == ComNum(2, -3)

    def test_recipr(self):
        assert ComNum.recipr(ComNum(2, 3)) == ComNum(1, 0)/ComNum(2, 3)

    def test_sqrt(self):
        assert ComNum.pr_sqrt(ComNum(3, 4)) == ComNum(2, 1)

    def test_com_ln(self):
        assert ComNum.pr_com_ln(ComNum(0, 1)) == ComNum(0, pi/2)

    def test_com_exp(self):
        num = ComNum(2, 3)
        assert ComNum.com_exp(num, 4) == num*num*num*num
        assert ComNum.com_exp(num, 4) == ComNum.com_exp_alt(num, 4)
        assert ComNum.com_exp(num, 0) == ComNum(1, 0)
        assert ComNum.com_exp(num, -1) == round(ComNum.recipr(num), 10)

    def test_com_exp_alt(self):
        num = ComNum(2, 3)
        assert ComNum.com_exp_alt(num, 4) == num*num*num*num
        assert ComNum.com_exp_alt(num, 4) == ComNum.com_exp(num, 4)
        assert ComNum.com_exp_alt(num, 0) == ComNum(1, 0)
        assert ComNum.com_exp_alt(num, -1) == round(ComNum.recipr(num), 10)
