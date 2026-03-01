# Display Control Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP display control functions.

| Display control functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(graphscr)](graphscr-AutoLISP.md) | Displays the AutoCAD graphics screen | ✓ | ✓ | / - supported, but doesn't do anything | -- | / - supported, but doesn't do anything |
| [(grdraw from to color [highlight])](grdraw-AutoLISP.md) | Draws a vector between two points, in the current viewport | ✓ | ✓ | ✓ | -- | ✓ |
| [(grtext [box text [highlight]])](grtext-AutoLISP.md) | Writes text to the status line or to screen menu areas | ✓ | ✓ | ✓ | -- | ✓ |
| [(grvecs vlist [trans])](grvecs-AutoLISP.md) | Draws multiple vectors on the graphics screen | ✓ | ✓ | ✓ | -- | ✓ |
| [(menucmd string)](menucmd-AutoLISP.md) | Issues menu commands, or sets and retrieves menu item status | ✓ | ✓ | / - supported, but limited | -- | / - supported, but limited |
| [(menugroup groupname)](menugroup-AutoLISP.md) | Verifies that a menu group is loaded | ✓ | ✓ | / - supported, but always returns *groupname* | -- | / - supported, but always returns *groupname* |
| [(prin1 [expr [file-desc]])](prin1-AutoLISP.md) | Prints an expression to the command line or writes an expression to an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(princ [expr [file-desc]])](princ-AutoLISP.md) | Prints an expression to the command line, or writes an expression to an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(print [expr [file-desc]])](print-AutoLISP.md) | Prints an expression to the command line, or writes an expression to an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(prompt msg)](prompt-AutoLISP.md) | Displays a string on your screen's prompt area | ✓ | ✓ | ✓ | -- | ✓ |
| [(redraw [ename [mode]])](redraw-AutoLISP.md) | Redraws the current viewport or a specified object (entity) in the current viewport | ✓ | ✓ | ✓ | -- | ✓ |
| [(terpri)](terpri-AutoLISP.md) | Prints a newline to the Command line | ✓ | ✓ | ✓ | -- | ✓ |
| [(textpage)](textpage-AutoLISP.md) | Switches from the graphics screen to the text screen | ✓ | ✓ | / - supported, but doesn't do anything | -- | / - supported, but doesn't do anything |
| [(textscr)](textscr-AutoLISP.md) | Switches from the graphics screen to the text screen (like the AutoCAD Flip Screen function key) | ✓ | ✓ | / - supported, but doesn't do anything | -- | / - supported, but doesn't do anything |
| [(vports)](vports-AutoLISP.md) | Returns a list of viewport descriptors for the current viewport configuration | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*