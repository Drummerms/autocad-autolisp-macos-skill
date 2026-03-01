# About Aligning Objects

You can move, rotate, or tilt an object so that it aligns with another object.

In the following example, two pairs of points are used to align the piping in 2D using the ALIGN command. Endpoint object
snaps align the pipes precisely.

![](../images/GUID-2CDEB3F6-45D6-4FE3-9742-7733BEA13D04-low.png)

## Aligning Objects in 3D

In 3D, use the 3DALIGN command to specify up to three points to define the source plane followed by up to three points to
define the destination plane.

* The first source point on an object, called the *base point*, is always moved to the first destination point.
* Specifying a second point for either the source or the destination results in the selected objects being rotated.
* A third point for either the source or the destination results in further rotation of the selected objects.

With 3D solid models, it is recommended that you turn on dynamic UCS to speed the selection of the destination plane.

NOTE:3D alignment is not available in AutoCAD LT.

#### Related Concepts

* [About Moving Objects](About-Moving-Objects.md)

#### Related Information

* [To Align Two Objects in 2D](To-Align-Two-Objects-in-2D.md)
* [To Align Two Objects in 3D](To-Align-Two-Objects-in-3D.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*