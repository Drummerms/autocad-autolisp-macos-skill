# To Modify Multilines

Multiline objects are composed of 1 to 16 parallel lines, called
*elements*.

## Delete a Vertex From a Multiline

1. Click
   Modify menu ![](../images/ac.menuaro.gif)Object![](../images/ac.menuaro.gif)Multiline.At the Command prompt, enter MLEDIT.
2. Enter DV.
3. In the drawing, specify the vertex to delete. Press Enter.

![](../images/GUID-0C48BD67-19A9-4741-A18A-DA870D23065C-low.png)

## Create a Closed Cross Intersection

Multilines can intersect in a cross or a
*T* shape, and the crosses or
*T* shapes can be closed, open, or merged.

1. Click
   Modify menu ![](../images/ac.menuaro.gif)Object![](../images/ac.menuaro.gif)Multiline.At the Command prompt, enter MLEDIT.
2. Enter CC.
3. Select the multiline for the foreground.
4. Select the multiline for the background.

   The intersection is modified. You can continue selecting intersecting multilines to modify, or press Enter to end the command.

![](../images/GUID-B1146DA3-91CA-4EF2-BCF4-0264C0308756-low.png)

## Use Common Editing Commands on Multilines

You can use most of the common editing commands on multilines
*except*

* BREAK
* CHAMFER
* FILLET
* LENGTHEN
* OFFSET

To perform these operations, first use EXPLODE to replace the multiline object with separate line objects.

NOTE:If you trim or extend a multiline object, only the first boundary object encountered determines the shape of the end of the
multiline. A multiline cannot have a complex boundary at its endpoint.

#### Related Tasks

* [To Draw a Multiline](To-Draw-a-Multiline.md)

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Concepts

* [About Multilines](About-Multilines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*