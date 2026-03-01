# About Mirroring Objects

You can flip objects about a specified axis to create a symmetrical mirror image.

You flip objects about an axis called a mirror line to create a mirror image. To specify this temporary mirror line, you enter
two points. You can choose whether to erase or retain the original objects.

![](../images/GUID-E47CEA94-6089-4AD4-9C1E-406CD31D4F6D-low.png)

By default, when you mirror text, hatches, attributes, and attribute definitions, they are not reversed or turned upside down
in the mirror image. The text has the same alignment and justification as before the object was mirrored. If you do want text
to be reversed, set the MIRRTEXT system variable to 1.

![](../images/GUID-CD32F61A-C0EC-48A5-8607-9DAE139BADA5-low.png)

MIRRTEXT affects text that is created with the TEXT, ATTDEF, or MTEXT commands; attribute definitions; and variable attributes.
Text and constant attributes that are part of an inserted block are reversed when the block is mirrored regardless of the
value of MIRRTEXT.

MIRRHATCH affects hatch objects created with the GRADIENT or HATCH commands. Use the MIRRHATCH system variable control whether
hatch pattern direction is mirrored or retained.

## Mirror in 3D (Not available in AutoCAD LT)

With MIRROR3D, you can mirror objects across a specified mirroring plane. The mirroring plane can be one of the following:

* The plane of a planar object
* A plane parallel to the *XY*, *YZ*, or *XZ* plane of the current UCS that passes through a specified point
* A plane defined by three specified points (2, 3, and 4)

![](../images/GUID-9D82945E-4276-49A5-87A1-4538034AFF31-low.png)

#### Related Tasks

* [To Mirror Objects Using Grips](To-Mirror-Objects-Using-Grips.md)

#### Related References

* [Commands for Duplicating Objects](Commands-for-Duplicating-Objects.md)

#### Related Information

* [To Mirror Objects in 2D](To-Mirror-Objects-in-2D.md)
* [To Mirror Objects in 3D](To-Mirror-Objects-in-3D.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*