# sslength (AutoLISP)

Returns an integer containing the number of objects (entities) in a selection set

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(sslength ss)
```

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

## Return Values

*Type:* Integer

The number of objects in the selection set.

## Examples

Add the last object to a new selection set:

```
(setq sset (ssget "L"))
<Selection set: 8>
```

Use
sslength to determine the number of objects in the new selection set:

```
(sslength sset)
1
```

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssdel (AutoLISP)](ssdel-AutoLISP.md)
* [ssmemb (AutoLISP)](ssmemb-AutoLISP.md)
* [ssname (AutoLISP)](ssname-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*