# User Input Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP user input functions.

| User input functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(entsel [msg])](entsel-AutoLISP.md) | Prompts the user to select a single object (entity) by specifying a point | ✓ | ✓ | ✓ | -- | ✓ |
| [(getangle [pt] [msg])](getangle-AutoLISP.md) | Pauses for user input of an angle, and returns that angle in radians | ✓ | ✓ | ✓ | -- | ✓ |
| [(getcorner pt [msg])](getcorner-AutoLISP.md) | Pauses for user input of a rectangle's second corner | ✓ | ✓ | ✓ | -- | ✓ |
| [(getdist [pt] [msg])](getdist-AutoLISP.md) | Pauses for user input of a distance | ✓ | ✓ | ✓ | -- | ✓ |
| [(getfiled title default ext flags)](getfiled-AutoLISP.md) | Prompts the user for a file name with the standard AutoCAD file dialog box, and returns that file name | ✓ | ✓ | ✓ | -- | / - supported, but does not display the standard AutoCAD file dialog box and always returns a value of 1 |
| [(getint [msg])](getint-AutoLISP.md) | Pauses for user input of an integer, and returns that integer | ✓ | ✓ | ✓ | -- | ✓ |
| [(getkword [msg])](getkword-AutoLISP.md) | Pauses for user input of a keyword, and returns that keyword | ✓ | ✓ | ✓ | -- | ✓ |
| [(getorient [pt] [msg])](getorient-AutoLISP.md) | Pauses for user input of an angle, and returns that angle in radians | ✓ | ✓ | ✓ | -- | ✓ |
| [(getpoint [pt] [msg])](getpoint-AutoLISP.md) | Pauses for user input of a point, and returns that point | ✓ | ✓ | ✓ | -- | ✓ |
| [(getreal [msg])](getreal-AutoLISP.md) | Pauses for user input of a real number, and returns that real number | ✓ | ✓ | ✓ | -- | ✓ |
| [(getstring [cr] [msg])](getstring-AutoLISP.md) | Pauses for user input of a string, and returns that string | ✓ | ✓ | ✓ | -- | ✓ |
| [(initget [bits] [string])](initget-AutoLISP.md) | Establishes keywords for use by the next user input function call | ✓ | ✓ | ✓ | -- | ✓ |
| [(nentsel [msg])](nentsel-AutoLISP.md) | Prompts the user to select an object (entity) by specifying a point, and provides access to the definition data contained within a complex object | ✓ | ✓ | ✓ | -- | ✓ |
| [(nentselp [msg] [pt])](nentselp-AutoLISP.md) | Provides similar functionality to that of the nentsel function without the need for user input | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*