# About Custom Linetypes and Linetype Definitions

A standard library of linetypes is provided with your product that can be used as they are or modified to suit your needs.
You can also create your own custom linetypes.

The standard linetypes that come with the product are stored in two different library files, the names of those files is dependent
on which product or products have been installed:

* AutoCAD and AutoCAD-based products -
  *acad.lin* and
  *acadiso.lin*
* AutoCAD LT product -
  *acadlt.lin* and
  *acadltiso.lin*

## Linetype Definitions

Linetypes are defined in one or more linetype definition files that have a
*.lin* file extension.

The linetype name and definition determine the particular dash-dot sequence, the relative lengths of dashes and blank spaces,
and the characteristics of any included text or shapes. You can use the linetypes as they are, modify them, or create your
own custom linetypes.

The following is an example of a linetype definition. The numbers represent the lengths of dashes and spaces, and the 0 represents
a dot.

```
*BORDER,Border __ __ . __ __ . __ __ . __ __ . __ __ .
A,.5,-.25,.5,-.25,0,-.25
```

A LIN file can contain definitions of many simple and complex linetypes. You can add new linetype definitions to an existing
LIN file or you can create new definitions by editing a LIN file using a text editor.

After you create or modify a linetype, you must load the linetype into your current drawing before you can use it.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Text in Custom Linetypes](About-Text-in-Custom-Linetypes.md)
* [About Shapes in Custom Linetypes](About-Shapes-in-Custom-Linetypes.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*