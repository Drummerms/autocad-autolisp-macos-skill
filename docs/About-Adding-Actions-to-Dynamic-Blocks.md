# About Adding Actions to Dynamic Blocks

Actions define how the geometry of a dynamic block reference will move or change when its grips are manipulated.

In general, you associate an action with a parameter and the following:

* **Key point** . The point on a parameter that drives the action.
* **Selection set** . The geometry that will be affected by the action.

![](../images/GUID-0F3820BD-FF1B-4A0A-9EF3-8EA5073647A5-low.png)

When you move the grip in the example above, only the geometry in the selection set is stretched.

![](../images/GUID-BD18B0E9-1C78-453F-BEA5-7FDAE23E6043-low.png)

## Specify Distance and Angle Override Values

Distance multiplier and angle offset override properties allow you to specify a factor by which a parameter value is increased
or decreased.

Action overrides are properties of actions that have no effect on the block reference until it is manipulated in a drawing.
Use distance multiplier overrides with the following actions:

* Move action
* Stretch action
* Polar Stretch action

You can specify these action override properties on the command line when you add an action to a dynamic block definition.
You can also specify these properties in the Properties palette when you select an action in the Block Editor.

#### Related Information

* [About Dynamic Blocks](About-Dynamic-Blocks.md)
* [About Creating Dynamic Blocks](About-Creating-Dynamic-Blocks.md)
* [About Specifying Properties for Dynamic Blocks](About-Specifying-Properties-for-Dynamic-Blocks.md)
* [About Adding Parameters to Dynamic Blocks](About-Adding-Parameters-to-Dynamic-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*