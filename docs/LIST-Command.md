# LIST (Command)

Displays property data for selected objects.

## Access Methods

![](../images/ac.mouse.gif) Menu:   Tools
 ![](../images/ac.menuaro.gif)  Inquiry
 ![](../images/ac.menuaro.gif)  List Not available in menus in the current workspace

## Summary

You can use LIST to display and then copy the properties of selected objects to a text file.

The text window displays the object type, object layer, and the
*X*,*Y*,*Z* position relative to the current user coordinate system (UCS) and whether the object is in model space or paper space.

LIST also reports the following information:

* Color, linetype, lineweight, and transparency information, if these properties are not set to BYLAYER.
* The thickness of an object, if it is nonzero.
* Elevation (*Z* coordinate information).
* Extrusion direction (UCS coordinates), if the extrusion direction differs from the
  *Z* axis (0,0,1) of the current UCS.
* Additional information related to the specific object type. For example, for dimensional constraint objects, LIST displays
  the constraint type (annotation or dynamic), reference type (yes or no), name, expression, and value.

#### Related Concepts

* [Overview of Object Properties](Overview-of-Object-Properties.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*