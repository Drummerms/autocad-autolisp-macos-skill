# ADDSELECTED (Command)

Creates a new object based on the object type and general properties of a selected object.

## Access Methods

*Toolbar*:
![](../images/GUID-2173CF22-55F6-42EF-AA05-CA38D90C9695-low.png)

*Shortcut Menu*: Select a single object, right-click, and choose Add Selected.

## Summary

Differs from COPY by duplicating only the
[general properties](General-Properties-of-Objects.md) of an object. For example, creating an object based on a selected circle adopts the general properties of the circle, such
as its color and layer, but prompts you for the new circle’s center point and radius.

With the ADDSELECTED command, you can create a new object with the same object type as a selected object. Certain objects
have special properties that are supported in addition to its general properties, as shown in the following table.

| Object type | Special properties supported by ADDSELECTED |
| Gradient | Gradient name, Color 1, Color 2, Gradient Angle, Centered |
| Text, MText, Attribute Definition | Text Style, Height |
| Dimensions (Linear, Aligned, Radial, Diametric, Angular, Arc Length, and Ordinate) | Dim Style, Dim Scale |
| Tolerance | Dim Style |
| Leader | Dim Style, Dim Scale |
| Multileader | Multileader Style, Overall Scale |
| Table | Table Style |
| Hatch | Pattern, Scale, Rotation |
| Block Reference, External Reference | Name |
| Underlays (Image) | Name |

## List of Prompts

The following prompt is displayed.

Select object:
*Use an object selection method*

The prompts vary by object type.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*