# About User-Defined Attributes (DCL)

When defining tiles, you can assign your own attributes.

The name of the attribute can be any valid name that does not conflict with the standard and predefined attributes. An attribute
name, like a keyword, can contain letters, numbers, or the underscore (\_), and must begin with a letter.

If a user-defined attribute name conflicts with a predefined attribute, the PDB feature does not recognize the attribute
as a new one, and attempts to use the value you assign it with the standard attribute. This can be very hard to debug.

The values you assign to the attribute, and their meanings, are defined by your application. Values for user-defined attributes
must conform to those used for standard attributes.

Defining attributes is comparable to defining application-specific client data. Both techniques enable the PDB feature to
manage data you supply. User-defined attributes are read-only, that is, they are static while the dialog box is active. If
you need to change the values dynamically, you must use client data at runtime. Also, end users can inspect the value of user-defined
attributes in the application's DCL file, but client data remains invisible.

The definition of the AutoCAD Drawing Aids dialog box defines its own attribute,
errmsg, which has a unique string value for each tile. A common error handler uses the value of
errmsg when it displays a warning. For example, the tile could assign the following value to
errmsg:

```
errmsg = "Grid Y Spacing";
```

If the user enters an unusable value, such as a negative number, AutoCAD displays the following error message:

Invalid Grid Y Spacing.

The word Invalid and the trailing period (.) are supplied by the error handler.

User-defined attributes can also be used for limits on the value of a tile and the name of a subdialog box that the tile
activates.

#### Related Concepts

* [About Restricted Attributes (DCL)](About-Restricted-Attributes-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*