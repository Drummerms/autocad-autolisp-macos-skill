# xdroom (AutoLISP)

Returns the amount of extended data (xdata) space that is available for an object (entity)

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(xdroom ename)
```

*ename*
:   *Type:* Ename (entity name)

    An entity name.

## Return Values

*Type:* Integer or nil

An integer reflecting the number of bytes of available space. If unsuccessful,
xdroom returns
nil.

## Remarks

Because there is a limit (currently, 16 kilobytes) on the amount of extended data that can be assigned to an entity definition,
and because multiple applications can append extended data to the same entity, this function is provided so an application
can verify there is room for the extended data that it will append. It can be called in conjunction with
xdsize, which returns the size of an extended data list.

## Examples

The following example looks up the available space for extended data of a viewport object:

```
(xdroom vpname)
16162
```

In this example, 16,162 bytes of the original 16,383 bytes of extended data space are available, meaning that 221 bytes are
used.

#### Related References

* [regapp (AutoLISP)](regapp-AutoLISP.md)
* [xdsize (AutoLISP)](xdsize-AutoLISP.md)

#### Related Concepts

* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*