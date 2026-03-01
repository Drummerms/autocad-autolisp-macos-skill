# expand (AutoLISP)

Allocates additional memory for AutoLISP

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(expand n-expand)
```

*n-expand*
:   *Type:* Integer

    An number indicating the amount of additional memory to be allocated. Memory is allocated as follows:

    * *n-alloc* free symbols
    * *n-alloc* free strings
    * *n-alloc* free usubrs
    * *n-alloc* free reals
    * *n-alloc* \*
      *n-expand* cons cells

    where
    *n-alloc* is the current segment size.

## Return Values

*Type:* Integer

A number indicating the number of free conses divided by
*n-alloc*.

## Examples

Set the segment size to 100:

```
(alloc 100)
1000
```

Allocate memory for two additional segments:

```
(expand 2)
82
```

This ensures that AutoLISP now has memory available for at least 200 additional symbols, strings, usubrs and reals each, and
8200 free conses.

#### Related References

* [alloc (AutoLISP)](alloc-AutoLISP.md)

#### Related Concepts

* [Memory Management Functions Reference (AutoLISP)](Memory-Management-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*