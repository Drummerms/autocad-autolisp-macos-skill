# ssgetfirst (AutoLISP)

Determines which objects are selected and gripped

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssgetfirst)
```

No arguments.

## Return Values

*Type:* List or nil

Returns a list of two selection sets similar to those passed to
sssetfirst. The first element in the list is always
nil because AutoCAD no longer supports grips on unselected objects. The second element is a selection set of entities that are
selected and gripped. Both elements of the list can be
nil.

## Remarks

NOTE:Only entities from the current drawing's model space and paper space, not nongraphical objects or entities in other block
definitions, can be analyzed by this function.

## Examples

N/A

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssdel (AutoLISP)](ssdel-AutoLISP.md)
* [sssetfirst (AutoLISP)](sssetfirst-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*