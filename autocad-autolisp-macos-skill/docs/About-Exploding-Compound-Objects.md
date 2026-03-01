# About Exploding Compound Objects

You can convert a compound object, such as a polyline, dimension, hatch, or block reference, into individual elements.

You can explode a compound object, such as a polyline, dimension, hatch, or block reference, to convert it into individual
elements. For example, exploding a polyline breaks it down to simple lines and arcs. Exploding a block reference or an associative
dimension replaces it with copies of the objects that compose the block or dimension.

## Explode Dimensions and Hatches

When you explode a dimension or a hatch, all associativity is lost and the dimension or hatch object is replaced by individual
objects such as lines, text, points, and 2D solids. To explode dimensions automatically when you create them, set the DIMASSOC
system variable to 0.

## Explode Polylines

When you explode a polyline, any associated width information is discarded. The resulting lines and arcs follow the polyline's
centerline. If you explode a block that contains a polyline, you need to explode the polyline separately. If you explode a
donut, its width becomes 0.

## Explode Block References

If you explode a block with attributes, the attribute values are lost, leaving only the attribute definitions. The colors
and linetypes of objects in exploded block references can change.

NOTE:Blocks inserted with MINSERT (multiple insert) result in a *minsert block* object, and cannot be exploded directly. You can convert the minsert block object into a block object with the FLATTEN Express
Tool. (MINSERT is not available in AutoCAD LT.)

## Explode External References

An external reference (xref) is a drawing file linked (or attached) to another drawing. You cannot explode xrefs and their
dependent blocks.

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Concepts

* [About Modifying Helixes](About-Modifying-Helixes.md)
* [About Polylines](About-Polylines.md)

#### Related Information

* [About Modifying Splines](About-Modifying-Splines.md)
* [To Explode an Object](To-Explode-an-Object.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*