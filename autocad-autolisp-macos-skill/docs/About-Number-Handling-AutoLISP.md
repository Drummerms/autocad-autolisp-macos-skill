# About Number Handling (AutoLISP)

AutoLISP provides functions for working with integers and real numbers.

In addition to performing basic and complex mathematical computations, you can use the number-handling functions to help
you in your daily use of AutoCAD. If you are drawing a steel connection detail that uses a 2.5" bolt with a diameter of 0.5"
and has 13 threads per inch, you could calculate the total number of threads for the bolt by multiplying 2.5 by 13. In AutoLISP,
this is done with the multiplication ( *\** ) function. Remember, the name of a function comes before the arguments you are passing to a function.

```
(* 2.5 13)
32.5
```

The arithmetic functions that have a *number* argument (as opposed to *num* or *angle*, for example) return different values if you provide integers or reals as arguments. If all arguments are integers, the value
returned is an integer. However, if one or all the arguments are reals, the value returned is a real.

```
(/ 12 5)
2

(/ 12.0 5)
2.4
```

#### Related Concepts

* [About Integers (AutoLISP)](About-Integers-AutoLISP.md)
* [About Reals (AutoLISP)](About-Reals-AutoLISP.md)
* [About Point Lists (AutoLISP)](About-Point-Lists-AutoLISP.md)
* [About Angular Conversion (AutoLISP)](About-Angular-Conversion-AutoLISP.md)
* [About Geometric Utilities (AutoLISP)](About-Geometric-Utilities-AutoLISP.md)
* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*