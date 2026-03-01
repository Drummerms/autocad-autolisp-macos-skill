# cond (AutoLISP)

Serves as the primary conditional function for AutoLISP

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(cond [((test) (result ...)) ...])
```

*test*
:   *Type:* List

    Test condition to be evaluated.

*result*
:   *Type:* List

    Arguments that are executed if the test condition is successful.

## Return Values

*Type:* T or nil

The value of the last expression in the sublist. If there is only one expression in the sublist (that is, if
*result* is missing), the value of the
*test* expression is returned. If no arguments are supplied,
cond returns
nil.

## Remarks

The
cond function accepts any number of lists as arguments. It evaluates the first item in each list (in the order supplied) until
one of these items returns a value other than
nil. It then evaluates those expressions that follow the test that succeeded.

## Examples

The following example uses
cond to perform an absolute value calculation:

```
(cond
   ((minusp a) (- a))
   (t a)
)
```

If the variable
a is set to the value-10, this returns 10.

As shown,
cond can be used as a
*case* type function. It is common to use
T as the last (default)
*test* expression. Here's another simple example. Given a user response string in the variable
s, this function tests the response and returns 1 if it is
Y or
y, 0 if it is
N or
n; otherwise
nil.

```
(cond
   ((= s "Y") 1)
   ((= s "y") 1)
   ((= s "N") 0)
   ((= s "n") 0)
   (t nil)
)
```

#### Related References

* [if (AutoLISP)](if-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*