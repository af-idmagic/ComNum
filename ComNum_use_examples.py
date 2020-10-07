
from ComNum_test import ComNum as CN

from math import sqrt as sqrt
from math import pi as pi

print("== Script démonstratif pour des opérations avec des nombres complexes ==")
print("   Module utilisé : ComNum_test.py (c) Alexey FEDOROV\n")

a = CN(1, 2)
print("a = ", a)

b = CN(3, -4)
print("b = ", b)

print("a == b ?  ", a==b)

c = CN(0, 5)
print("c = ", c)

d = CN(7, 0)
print("d = ", d)

f = CN(sqrt(2), pi)
print("f = ", f)

f_round5 = round(f, 5)
print("round(f, 5) = ", f_round5)

print("a + b =", a + b)

print("b - a =", b - a)

print("a*b =", a*b)

print("a/b =", a/b)

a_modul = CN.modul(a)
print("|a| =", a_modul)

a_argt = CN.argt(a)
print("arg(a) =", a_argt)

a_conjug = CN.conjug(a)
print("a conjugué =", a_conjug)

a_recipr = CN.recipr(a)
print("1/a =", a_recipr)

a_sqroot = CN.pr_sqrt(a)
print("valeur principale de sqrt(a) =", a_sqroot)

a_ln = CN.pr_com_ln(a)
print("valeur principale de ln(a) =", a_ln)

a_pw4 = CN.com_exp(a, 4)
print("a^4 =", a_pw4, " [com_exp]")

a_pw4_alt = CN.com_exp_alt(a, 4)
print("a^4 =", a_pw4_alt, " [com_exp_alt]")

a_pwmin3 = CN.com_exp(a, -3)
print("a^(-3) =", a_pwmin3, " [com_exp]")

a_pwmin3_alt = CN.com_exp_alt(a, -3)
print("a^(-3) =", a_pwmin3_alt, " [com_exp_alt]")

try:
    a_pwfloat = CN.com_exp(a, 1.5465787)
    print("a^1.5465787 =", a_pwfloat, " [com_exp]")
except ValueError as VE:
    print("a^1.5465787 est introuvable :", str(VE), " [com_exp]")
