# mapcar (AutoLISP)

Returns a list that is the result of executing a function with a list (or lists) supplied as arguments to the function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(mapcar function list1... listn)
```

*function*
:   *Type:* Subroutine

    A function.

*list1... listn*
:   *Type:* List

    One or more lists. The number of lists must match the number of arguments required by
    *function*.

## Return Values

*Type:* List

A list.

## Examples

```
(setq a 10 b 20 c 30)
30

(mapcar '1+ (list a b c))
(11 21 31)
```

This is equivalent to the following series of expressions, except that
mapcar returns a list of the results:

```
(1+ a)
(1+ b)
(1+ c)
```

The
lambda function can specify an anonymous function to be performed by
mapcar. This is useful when some of the function arguments are constant or are supplied by some other means. The following example
demonstrates the use of
lambda with
mapcar:

```
(mapcar '(lambda (x)
          (+ x 3)
          )
         '(10 20 30)
)
(13 23 33)
```

#### Related References

* [lambda (AutoLISP)](lambda-AutoLISP.md)
* [function (AutoLISP/Visual LISP IDE)](function-AutoLISP-Visual-LISP-IDE.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*