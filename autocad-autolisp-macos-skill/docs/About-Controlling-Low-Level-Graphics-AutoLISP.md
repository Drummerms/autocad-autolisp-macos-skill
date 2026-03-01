# About Controlling Low-Level Graphics (AutoLISP)

Low-level graphics in the drawing area and application window can be controlled using AutoLISP functions.

The following functions can be used to draw temporary objects in the drawing area or display text in the status bar:

* grtext – Displays text directly in the status bar area, with or without highlighting.

  NOTE:This function is supported on Mac OS, but does not affect AutoCAD.
* grdraw – Draws a temporary vector in the current viewport with control over color and highlighting.
* grvecs – Draws multiple temporary vectors.
* redraw – Redraws the current viewport or a specified object (entity) in the current viewport.

NOTE:Because these functions depend on code in AutoCAD, their operation can be expected to change from release to release. There
is no guarantee that applications calling these functions will be upward compatible. Also, they depend on current hardware
configurations. In particular, applications that call grtext are not likely to work the same on all configurations unless the developer is very careful to use them as described and to
avoid hardware-specific features. Finally, because they are low-level functions, they do almost no error reporting and can
alter the graphics screen display unexpectedly (see the following example for a way to fix this).

The following sequence restores the default graphics window display caused by incorrect calls to grtext, grdraw, or grvecs:

```
(grtext) ; Restores standard text
(redraw)
```

#### Related Concepts

* [About Controlling the Graphics and Text Windows (AutoLISP)](About-Controlling-the-Graphics-and-Text-Windows-AutoLISP.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*