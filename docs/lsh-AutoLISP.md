# lsh (AutoLISP)

Returns the logical bitwise shift of an integer by a specified number of bits

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(lsh int numbits)
```

*int*
:   *Type:* Integer

    A numeric value.

*numbits*
:   *Type:* Integer

    Number of bits to shift
    *int*.

    If
    *numbits* is positive,
    *int* is shifted to the left; if
    *numbits* is negative,
    *int* is shifted to the right. In either case, zero bits are shifted in, and the bits shifted out are discarded.

    If
    *numbits* is not specified, no shift occurs.

## Return Values

*Type:* Integer

The value of
*int* after the bitwise shift. The returned value is positive if the significant bit (bit number 31) contains a 0 after the shift
operation; otherwise it is negative. If no arguments are supplied,
lsh returns 0.

The behavior is different from other languages (>> & << of C, C++, or Java) where more than 32 left shifts (of a 32 bit integer)
result in 0. In right shift, the integer appears again on every 32 shifts.

## Examples

```
(lsh 2 1)
4

(lsh 2 -1)
1

(lsh 40 2)
160
```

#### Related References

* [~ (bitwise NOT) (AutoLISP)](~-bitwise-NOT-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*