# acet-ent-geomextents (AutoLISP/Express Tools)

Returns the geometric extents of the given object.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-ent-geomextents ename)
```

*ename*
:   *Type:* Ename (entity name)

    The entity name of an object.

## Return Values

*Type:* List

A list containing two points, such as
((1.0 1.0 0.0) (2.0 2.0 0.0)) describing the geometric extents or
nil.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*