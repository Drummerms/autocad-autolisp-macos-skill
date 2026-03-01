# Selection Set Manipulation Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP selection set manipulation functions.

| Selection set manipulation functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(ssadd [ename [ss]])](ssadd-AutoLISP.md) | Adds an object (entity) to a selection set, or creates a new selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssdel ename ss)](ssdel-AutoLISP.md) | Deletes an object (entity) from a selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssget [mode] [pt1 [pt2]] [pt-list] [filter-list])](ssget-AutoLISP.md) | Prompts the user to select objects (entities), and returns a selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssgetfirst)](ssgetfirst-AutoLISP.md) | Determines which objects are selected and gripped | ✓ | ✓ | ✓ | -- | ✓ |
| [(sslength ss)](sslength-AutoLISP.md) | Returns an integer containing the number of objects (entities) in a selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssmemb ename ss)](ssmemb-AutoLISP.md) | Tests whether an object (entity) is a member of a selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssname ss index)](ssname-AutoLISP.md) | Returns the object (entity) name of the indexed element of a selection set | ✓ | ✓ | ✓ | -- | ✓ |
| [(ssnamex ss index)](ssnamex-AutoLISP.md) | Retrieves information about how a selection set was created | ✓ | ✓ | ✓ | -- | ✓ |
| [(sssetfirst gripset [pickset])](sssetfirst-AutoLISP.md) | Sets which objects are selected and gripped | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*