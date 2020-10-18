from math import sqrt as sqrt
from math import pi as pi

from comnum.comnum import ComNum


class TestComNum:
    """ pytests for the class ComNum defining a complex number x + y*i.
        To launch the pytests :  python -m pytest comnum_test.py
    """

    def test_round(self):
        num = ComNum(sqrt(2), pi)
        assert ComNum.__round__(num, 5) == ComNum(1.41421, 3.14159)

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
        assert ComNum.com_exp(num, -1) == ComNum.__round__(ComNum.recipr(num), 10)

    def test_com_exp_alt(self):
        num = ComNum(2, 3)
        assert ComNum.com_exp_alt(num, 4) == num*num*num*num
        assert ComNum.com_exp_alt(num, 4) == ComNum.com_exp(num, 4)
        assert ComNum.com_exp_alt(num, 0) == ComNum(1, 0)
        assert ComNum.com_exp_alt(num, -1) == ComNum.__round__(ComNum.recipr(num), 10)
