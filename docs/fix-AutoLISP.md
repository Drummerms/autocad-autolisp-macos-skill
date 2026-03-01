# fix (AutoLISP)

Returns the conversion of a real number into the nearest smaller integer

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(fix number)
```

*number*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* Integer

The integer derived from
*number*.

If
*number* is larger than the largest possible integer (+2,147,483,647 or -2,147,483,648 on a 32-bit platform),
fix returns a truncated real (although integers transferred between AutoLISP and AutoCAD are restricted to 16-bit values).

## Remarks

The
fixfunction truncates
*number* to the nearest integer by discarding the fractional portion.

## Examples

```
(fix 3)
3

(fix 3.7)
3
```

#### Related References

* [float (AutoLISP)](float-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*