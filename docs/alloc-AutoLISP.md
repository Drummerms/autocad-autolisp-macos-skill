# alloc (AutoLISP)

Sets the size of the segment to be used by the
*expand* function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(alloc n-alloc)
```

*n-alloc*
:   *Type:* Integer

    A number indicating the amount of memory to be allocated. The integer represents the number of symbols, strings, usubrs, reals,
    and cons cells.

## Return Values

*Type:* Integer

The previous setting of
n-alloc.

## Examples

```
(alloc 100)
1000
```

#### Related References

* [expand (AutoLISP)](expand-AutoLISP.md)

#### Related Concepts

* [Memory Management Functions Reference (AutoLISP)](Memory-Management-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*