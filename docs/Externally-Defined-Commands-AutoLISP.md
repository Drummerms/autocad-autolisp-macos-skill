# Externally Defined Commands (AutoLISP)

AutoCAD
 ®  commands defined by ObjectARX ®  or AutoLISP ®  applications are called externally defined. AutoLISP applications may need to access externally defined commands differently
from the way they access built-in AutoLISP functions. Many externally defined commands have their own programming interfaces
that allow AutoLISP applications to take advantage of their functionality.

| Externally defined functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(c:3dsin mode [multimat create] file)](3dsin-AutoLISP-External-Function.md) | Imports a 3D Studio (.3ds) file | ✓ | -- | -- | -- | -- |
| [(align args ...)](align-AutoLISP-External-Function.md) | Translates and rotates objects, allowing them to be aligned with other objects | ✓ | ✓ | ✓ | -- | -- |
| [(c:cal expression)](cal-AutoLISP-External-Function.md) | Invokes the on-line geometry calculator and returns the value of the evaluated expression | ✓ | -- | ✓ | -- | -- |
| [(mirror3d args ...)](mirror3d-AutoLISP-External-Function.md) | Reflects selected objects about a user-specified plane | ✓ | -- | ✓ | -- | -- |
| [(rotate3d args ...)](rotate3d-AutoLISP-External-Function.md) | Rotates an object about an arbitrary 3D axis | ✓ | -- | ✓ | -- | -- |
| [(c:solprof args ...)](solprof-AutoLISP-External-Function.md) | Creates profile images of three-dimensional solids | ✓ | -- | ✓ | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*