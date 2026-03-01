# About Displaying the Original Components of Composite Solids

Composite objects, which are objects created with Boolean operations, retain a history of their original object components
that can be displayed and modified.

## Retain the History of the Composite Components

You can modify the shape of a composite object by modifying a highlighted wireframe image of its original components. If
the Show History property is 1 (On), wireframes of the original forms—including forms that have been removed—are displayed
in a dimmed state. (The SHOWHIST system variable also controls this setting.)

![](../images/GUID-8491B396-182D-4C9F-8730-AC351971D0FC-low.png)

To retain a history of the original parts of composite solids, the History property must be set to Record (On) in the Properties
palette when the Boolean operation occurs. You can also use the SOLIDHIST system variable to set this property.

## Display and Remove the History to Modify the Composite

When you modify the composite object, you can display the history. Then use the grips on the history subobject to modify
the object.

You can remove the history of a selected composite object by changing its History setting to None, or by entering the BREP
command. After a history has been removed, you can no longer select and modify the original, removed, components of the solid.
You can restart history retention for the solid by changing its History setting back to Record.

![](../images/GUID-0C3CE0FA-3EE7-4132-99AB-EA034F5AE224-low.png)

Removing a composite history is useful when you work with complex composite solids. With this process, you can create a complex
composite object, and then reset the history to serve as a new starting point for additional composite operations.

#### Related Tasks

* [To Work With Creating Composite Objects](To-Work-With-Creating-Composite-Objects.md)
* [To Work With Displaying Composite Object History](To-Work-With-Displaying-Composite-Object-History.md)
* [To Work With Selecting a Component of a Composite Solid](To-Work-With-Selecting-a-Component-of-a-Composite-Solid.md)
* [To Separate a Composite 3D Solid Into Individual Solids](To-Separate-a-Composite-3D-Solid-Into-Individual-Solids.md)

#### Related Concepts

* [About Creating Composite Objects](About-Creating-Composite-Objects.md)
* [About Modifying Composite Solids and Surfaces](About-Modifying-Composite-Solids-and-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*