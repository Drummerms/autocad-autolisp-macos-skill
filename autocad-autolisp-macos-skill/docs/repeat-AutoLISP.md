# repeat (AutoLISP)

Evaluates each expression a specified number of times, and returns the value of the last expression

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(repeat int [expr ...])
```

*int*
:   *Type:* Integer

    A numeric value. Must be a positive number.

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    One or more atoms or expressions.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The value of the last expression or atom evaluated. If
*expr* is not supplied,
repeat returns
nil.

## Examples

```
(setq a 10 b 100)
100

(repeat 4 (setq a (+ a 10)) (setq b (+ b 100)))
500
```

After evaluation,
a is 50,
b is 500, and
repeat returns 500.

If strings are supplied as arguments,
repeat returns the last string:

```
(repeat 100 "Me" "You")
"You"
```

#### Related References

* [while (AutoLISP)](while-AutoLISP.md)
* [foreach (AutoLISP)](foreach-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*