# min (AutoLISP)

Returns the smallest of the numbers given

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(min [number number ...])
```

*number*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Integer or Real

A numeric value. If any
*number* argument is a real, a real is returned; otherwise, an integer is returned. If no argument is supplied,
min returns 0.

## Examples

```
(min 683 -10.0)
-10.0

(min 73 2 48 5)
2

(min 73.0 2 48 5)
2.0

(min 2 4 6.7)
2.0
```

#### Related References

* [max (AutoLISP)](max-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*