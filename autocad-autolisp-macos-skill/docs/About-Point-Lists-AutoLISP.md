# About Point Lists (AutoLISP)

AutoLISP utilizes the list data type to represent graphical coordinate values.

Points are expressed as *lists* with either two or three numerical values.

* 2D point - List with two integer or real numbers, (X and Y, respectively), as in (3.4 7.52).
* 3D point – List with three integer or real numbers, (X, Y, and Z, respectively), as in (3.4 7.52 1.0).

You can use the list function to form point lists, as shown in the following examples:

```
(list 3.875 1.23)
(3.875 1.23)

(list 88.0 14.77 3.14)
(88.0 14.77 3.14)
```

To assign particular coordinates to a point variable, you can use one of the following expressions:

```
(setq pt1 (list 3.875 1.23))
(3.875 1.23)

(setq pt2 (list 88.0 14.77 3.14))
(88.0 14.77 3.14)

(setq abc 3.45)
3.45

(setq pt3 (list abc 1.23))
(3.45 1.23)
```

The latter uses the value of variable abc as the *X* component of the point list. If all members of a list are constant values, you can use the quote function to explicitly define the list, rather than the list function. The quote function returns an expression without evaluation, as follows:

```
(setq pt1 (quote (4.5 7.5)))
(4.5 7.5)
```

The single quotation mark ( *'* ) can be used as shorthand for the quote function. The following code produces the same result as the preceding code.

```
(setq pt1 '(4.5 7.5))
(4.5 7.5)
```

The quote and (‘) functions cannot be used to create a list using values that are stored in a variable. The following code
does not return the excepted results:

```
(setq abc 3.45)
3.45

(setq pt4 (quote abc 1.23))
; error: syntax error
```

## Retrieve the X, Y, and Z components of a point list

You can retrieve the *X*, *Y*, and *Z* components of a point list using three additional built-in functions; car, cadr, and caddr. The following code examples show how to retrieve values from a 3D point list. The pt variable is set to the point 1.5,3.2,2:

```
(setq pt '(1.5 3.2 2.0))
(1.5 3.2 2.0)
```

The car function returns the first member of a list. In this example, it returns the *X* value of the point list to the x\_val variable.

```
(setq x_val (car pt))
1.5
```

The cadr function returns the second member of a list. In this example it returns the Y value of the point list to the y\_val variable.

```
(setq y_val (cadr pt))
3.2
```

The caddr function returns the third member of a list. In this example it returns the Z value of the point list to the z\_val variable.

```
(setq z_val (caddr pt))
2.0
```

You can use the following code to define the lower-left and upper-right (pt1 and pt2) corners of a rectangle, as follows:

```
(setq pt1 '(1.0 2.0) pt2 '(3.0 4.0))
(3.0 4.0)
```

You can use the car and cadr functions to set the pt3 variable to the upper-left corner of the rectangle, by extracting the *X* component of pt1 and the *Y* component of pt2, as follows:

```
(setq pt3 (list (car pt1) (cadr pt2)))
(1.0 4.0)
```

The preceding statement sets pt3 equal to point (1.0, 4.0).

AutoLISP supports combinations of the car and cdr functions up to four levels deep. Some examples of these functions are caaaar and cadr. Each a represents *a* call to car and each *d* represents a call to cdr. For example:

```
(caar x) is equivalent to  (car (car x))
(cdar x) is equivalent to  (cdr (car x))
(cadar x) is equivalent to  (car (cdr (car x)))
(cadr x) is equivalent to  (car (cdr x))
(cddr x) is equivalent to  (cdr (cdr x))
(caddr x) is equivalent to  (car (cdr (cdr x)))
```

#### Related Concepts

* [About Lists (AutoLISP)](About-Lists-AutoLISP.md)
* [About Dotted Pairs (AutoLISP)](About-Dotted-Pairs-AutoLISP.md)
* [About Selection Set Filter Lists (AutoLISP)](About-Selection-Set-Filter-Lists-AutoLISP.md)
* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*