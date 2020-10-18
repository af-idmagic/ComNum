from comnum.comnum import ComNum

from math import sqrt as sqrt
from math import pi as pi

print("== Demonstration script for operations with complex numbers ==")
print("   Used Python module: comnum.py (c) Alexey FEDOROV\n")

a = ComNum(1, 2)
print("a = ", a)

b = ComNum(3, -4)
print("b = ", b)

print("a == b ?  ", a == b)

c = ComNum(0, 5)
print("c = ", c)

d = ComNum(7, 0)
print("d = ", d)

f = ComNum(sqrt(2), pi)
print("f = ", f)

f_round5 = round(f, 5)
print("round(f, 5) = ", f_round5)

print("a + b =", a + b)

print("b - a =", b - a)

print("a*b =", a*b)

print("a/b =", a/b)

a_modul = ComNum.modul(a)
print("|a| =", a_modul)

a_argt = ComNum.argt(a)
print("arg(a) =", a_argt)

a_conjug = ComNum.conjug(a)
print("Conjugate of a =", a_conjug)

a_recipr = ComNum.recipr(a)
print("1/a =", a_recipr)

a_sqroot = ComNum.pr_sqrt(a)
print("Principal value of sqrt(a) =", a_sqroot)

a_ln = ComNum.pr_com_ln(a)
print("Principal value of ln(a) =", a_ln)

a_pw4 = ComNum.com_exp(a, 4)
print("a^4 =", a_pw4, " [com_exp]")

a_pw4_alt = ComNum.com_exp_alt(a, 4)
print("a^4 =", a_pw4_alt, " [com_exp_alt]")

a_pwmin3 = ComNum.com_exp(a, -3)
print("a^(-3) =", a_pwmin3, " [com_exp]")

a_pwmin3_alt = ComNum.com_exp_alt(a, -3)
print("a^(-3) =", a_pwmin3_alt, " [com_exp_alt]")

try:
    a_pwfloat = ComNum.com_exp(a, 1.5465787)
    print("a^1.5465787 =", a_pwfloat, " [com_exp]")
except ValueError as VE:
    print("a^1.5465787 cannot be found:", str(VE), " [com_exp]")
