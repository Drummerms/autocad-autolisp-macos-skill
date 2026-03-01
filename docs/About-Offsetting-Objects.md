# About Offsetting Objects

Creates a geometric object that is parallel or concentric to the selected object at a specified distance.

For example, if you offset a circle or an arc, a larger or smaller circle or arc is created, depending on which side you
specify the offset. If you offset a polyline, the result is a polyline that parallels the original.

![](../images/GUID-15846644-6100-4DB2-80B7-2E7406E4C035-low.png)

An effective drawing technique is to offset objects and then trim or extend their ends.

![](../images/GUID-C1F36928-46F9-44BF-B511-8F922C611718-low.png)

Use OFFSET to offset most of the geometric objects. Splines and polyline are trimmed automatically when the offset distance
is larger than can otherwise be accommodated.

## Special Cases

Offsetting splines and polylines can produce complex results.

Splines and polylines are trimmed automatically when the offset distance is larger than can otherwise be accommodated.

![](../images/GUID-1522F953-3499-444B-867E-C78C11445846-low.png)

Polyline segments can be trimmed or deleted in some cases, and extended to fill gaps in others.

![](../images/GUID-AC173697-59A4-4A32-981D-EECD3C09C90D-low.png)

The
OFFSETGAPTYPE system variable controls whether the extended corners are sharp, filleted, or chamfered.

#### Related References

* [Commands for Duplicating Objects](Commands-for-Duplicating-Objects.md)

#### Related Concepts

* [About Copying Objects](About-Copying-Objects.md)

#### Related Information

* [To Offset an Object by Specifying a Distance](To-Offset-an-Object-by-Specifying-a-Distance.md)
* [To Offset an Object Through a Point](To-Offset-an-Object-Through-a-Point.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*