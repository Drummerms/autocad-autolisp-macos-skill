# About Controlling the Graphics and Text Windows (AutoLISP)

You can control the display of the graphics and text windows from an application.

Early releases of AutoCAD could be configured to use two different screens; one displayed the graphics screen while the other
displayed the contents of the text window. In those early releases, AutoCAD could be installed using a single-screen. With
single-screen AutoCAD installations, a call to
graphscr displayed the graphics window, and a call to
textscr displayed the text window. Using these functions was equivalent to toggling the Flip Screen function key. The function
textpage is equivalent to
textscr.

In later and the most recent release, the text window is a floating window that can be independently displayed and resized
instead of being a separate screen. A call to
graphscr hides the text window and ensures that the graphics window is displayed, while a call to
textscr displays the text window. If the text window is already displayed when
textscr is called, the window is moved to the foreground in front of the AutoCAD application window.

The
redraw function is similar to the AutoCAD REDRAW command, but provides more control over what is displayed. It not only redraws
the entire graphics area, but can also specify a single object to be redrawn or undrawn (that is, blanked out). If the object
is a complex object such as a "legacy" polyline or a block,
redraw can draw (or undraw) either the entire object or its header. The
redraw function can also highlight and unhighlight specified objects.

#### Related Concepts

* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [About Controlling Low-Level Graphics (AutoLISP)](About-Controlling-Low-Level-Graphics-AutoLISP.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*