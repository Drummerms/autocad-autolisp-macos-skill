# About Integers (AutoLISP)

Integers are whole numbers; numbers that do not contain a decimal point.

AutoLISP integers are 32-bit signed numbers with values ranging from +2,147,483,647 to -2,147,483,648. Some functions through,
only accept 16-bit numbers ranging from +32767 to -32678. When you explicitly use an integer, that value is known as a constant.
Numbers such as 2, -56, and 1,200,196 are valid integers.

If you enter a number that is greater than the maximum integer allowed (resulting in integer overflow), AutoLISP converts
the integer to a real number. However, if you perform an arithmetic operation on two valid integers, and the result is greater
than the maximum allowable integer, the resulting number will be invalid.

The following examples demonstrate how AutoLISP handles integer overflow.

The largest positive integer value retains its specified value:

```
(setq int1 2147483647)
2147483647
```

If you enter an integer that is greater than the largest allowable value, AutoLISP returns the value as a real:

```
(setq int2 2147483648)
2.14748e+009
```

An arithmetic operation involving two valid integers, but resulting in integer overflow, produces an invalid result:

```
(setq int3 (+ 2147483646 3))
-2147483647
```

In the previous example the result is clearly invalid, as the addition of two positive numbers results in a negative number.
But note how the following operation produces a valid result:

```
(setq int4 (+ 2147483648 2))
2.14748e+009
```

In this instance, AutoLISP converts 2147483648 to a valid real before adding 2 to the number. The result is a valid real.
The largest negative integer value retains its specified value:

```
(setq int5 -2147483647)
-2147483647
```

If you enter a negative integer larger than the greatest allowable negative value, AutoLISP returns the value as a real:

```
(setq int6 -2147483648)
-2.14748e+009
```

The following operation concludes successfully, because AutoLISP first converts the overflow negative integer to a valid real:

```
(setq int7 (- -2147483648 1))
-2.14748e+009
```

#### Related Concepts

* [About Number Handling (AutoLISP)](About-Number-Handling-AutoLISP.md)
* [About Reals (AutoLISP)](About-Reals-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [About Angular Conversion (AutoLISP)](About-Angular-Conversion-AutoLISP.md)
* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*