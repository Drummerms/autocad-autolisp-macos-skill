# max (AutoLISP)

Returns the largest of the numbers given

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(max [number number ...])
```

*number*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Integer or Real

A number. If any of the arguments are real numbers, a real is returned; otherwise an integer is returned. If no argument is
supplied,
max returns 0.

## Examples

```
(max 4.07 -144)
4.07

(max -88 19 5 2)
19

(max 2.1 4 8)
8.0
```

#### Related References

* [min (AutoLISP)](min-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*