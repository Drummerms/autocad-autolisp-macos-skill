# About Grips on Dynamic Blocks

Custom grips can be used to manipulate the geometry of a dynamic block reference.

When you add a parameter to a dynamic block definition, custom grips associated with key points of the parameter are automatically
added to the block.

You can specify the number of grips on all parameters except the alignment parameter, which always displays one grip. When
you select a parameter in the Block Editor, the Number of Grips property on the Properties palette allows you to select the
number of grips you want to display. Parameters that are not associated with an action do not display grips.

Even if you specify that a parameter has 0 grips, you can still edit the dynamic block reference in the Properties palette
if the block is defined to accept this input.

If a dynamic block definition contains visibility states or a lookup table, you can define the block so that only the lookup
grip is displayed. Clicking this grip on the block reference displays a drop-down list. When you select an item from the list,
the display of the block reference may change.

![](../images/GUID-6D7B6BFD-9465-47E6-A2E1-1E8C204623EE-low.png)

Grips are automatically added at key points on the parameter. You can reposition a grip anywhere in the block space relative
to its associated key point on the parameter. When you reposition a grip, it is still tied to the key point with which it
is associated. Key points that are not associated with an action do not display grips.

The type of parameter you add to the dynamic block definition determines the type of grips that are added to the block.

## Specify Tooltips on Grips

All dynamic block parameters except basepoint and alignment has one or more description fields.

| Parameter | Description |
| Point | Position description |
| Linear | Distance description |
| Polar | Distance description, angle description |
| XY | Horizontal distance description, vertical distance description |
| Rotation | Angle description |
| Flip | Flip description |
| Visibility | Visibility description |
| Lookup | Lookup description |
| Alignment | Set to “Aligns block to object” |
| Basepoint | No special tooltip is required |

## Specify Insertion Cycling for Grips in Dynamic Blocks

Grips in dynamic blocks have a property called
*Cycling* that allows you to set a grip as a potential insertion point for the block. When you insert the dynamic block reference in
a drawing, you can tap the Ctrl key to cycle through the available grips to specify which grip will be used as the insertion
point.

#### Related Tasks

* [To Set the Number of Custom Grips to Display for a Dynamic Block Parameter](To-Set-the-Number-of-Custom-Grips-to-Display-for-a-Dynamic-Block-Parameter.md)
* [To Reposition a Grip in a Dynamic Block Definition](To-Reposition-a-Grip-in-a-Dynamic-Block-Definition.md)
* [To Restore the Default Location for Grips in a Dynamic Block Definition](To-Restore-the-Default-Location-for-Grips-in-a-Dynamic-Block-Definition.md)

#### Related References

* [Dynamic Block Grip Reference](Dynamic-Block-Grip-Reference.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*