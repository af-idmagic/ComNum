**Basic operations with complex numbers**
==================================================
_© Alexey FEDOROV (idmagic) 2020_

`comnum.py`
---
The class `ComNum` defines a [complex number](https://en.wikipedia.org/wiki/Complex_number):

    >>> print(ComNum(X, Y))
    X + Y*i

where `i` is the imaginary unit (`i*i = -1`),

`X` is the real part of the number

and `Y` is the imaginary part of the number


The package contains the basic methods for complex numbers:

  *  `print` :&nbsp;&nbsp;  printing a complex number in its classic form (`X + Y*i`)
  *  `round` :&nbsp;&nbsp;  rounding the real part and the imaginary part of a complex number to `n` decimal places
  *  `==` :&nbsp;&nbsp;  checking equality between 2 complex numbers
  *  `+ - * /` :&nbsp;&nbsp;  basic arithmetic operations
  *  `modul`, `argt` :&nbsp;&nbsp;  modulus and argument of a complex number
  *  `conjug` :&nbsp;&nbsp;  conjugate of a complex number (`X - Y*i`)
  *  `recipr` :&nbsp;&nbsp;  reciprocated complex number
  *  `pr_sqrt` :&nbsp;&nbsp;  principal square root of a complex number
  *  `pr_com_ln` :&nbsp;&nbsp;  principal value of the natural logarithm of a complex number
  *  `com_exp` :&nbsp;&nbsp;  complex number to the power of `n` (where `n` must be an integer)
  *  `com_exp_alt` :&nbsp;&nbsp;  idem, alternative calculation solution
  
Launch `help(ComNum)` to read the docstrings and doctest examples for these methods.


`comnum_use_examples.py`
---
Demonstrative script for operations with complex numbers
that used all the methods defined in comnum.py

Launch it for a concise et explicit demonstration.