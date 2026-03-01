# About Dynamic Blocks

Dynamic blocks are an advanced form of blocks that you can change as required, without needing to explode and modify the
component objects. Dynamic blocks contain rules, called *parameters*, for changing the appearance of the block reference when it is inserted in the drawing.

With dynamic blocks you can insert one block that can change shape, size, or configuration instead of inserting one of many
static block definitions. For example in a non-dynamic block, if you needed to scale the door block, it would scale the thickness
of the door along with its width and height. With dynamic blocks, you can prevent this from happening by scaling certain components
without affecting the entire block.

Dynamic block references contain grips (as shown in the graphic below) or custom properties that change the way the reference
is displayed in the drawing after it is inserted. For example, a dynamic block reference of a door can change size after you
insert the block reference into your drawing. Dynamic blocks allow you to insert one block that can change shape, size, or
configuration, instead of inserting one of many static block definitions.

You author dynamic blocks using parameters and assigning actions to them.

![](../images/GUID-476B99C7-1930-45FC-B85D-FAA3904870E2-low.png)

NOTE:The red grips indicate that the grips are activated for action or manipulation.

## About Actions and Parameters

In a block definition, actions and parameters provide rules for the behavior of a block once it is inserted into the drawing.

![](../images/GUID-D62B63E2-3457-45F6-9C77-50DAF8F4161B-low.png)

Depending on the specified block geometry or parameter, you can associate an action to that parameter. The parameter is represented
as a grip in the drawing. The grips are associated with a point, object, or region in the block definition. When you edit
the grip, the associated action determines what will change in the block reference. The display of the tooltip is controlled
by the GRIPTIPS system variable.

Action parameters can be changed using the Properties Inspector.

## About Saving Dynamic Blocks

When you save a block definition, the current values of the geometry and parameters in the block become the default values
for the block reference. The default visibility state for the block reference is the visibility state at the top of the list
in the Manage Visibility States dialog box.

NOTE:If you click File menu-->Save while you are in the Block Editor, you will save the drawing but not the block definition. You
must specifically save the block definition while you are in the Block Editor.

#### Related Concepts

* [About Grips on Dynamic Blocks](About-Grips-on-Dynamic-Blocks.md)
* [About Controlling the Visibility of Objects in Dynamic Blocks](About-Controlling-the-Visibility-of-Objects-in-Dynamic-Blocks.md)

#### Related Information

* [About Creating Dynamic Blocks](About-Creating-Dynamic-Blocks.md)
* [About Adding Parameters to Dynamic Blocks](About-Adding-Parameters-to-Dynamic-Blocks.md)
* [About Specifying Properties for Dynamic Blocks](About-Specifying-Properties-for-Dynamic-Blocks.md)
* [Work With Action Parameters in Blocks](Work-With-Action-Parameters-in-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*