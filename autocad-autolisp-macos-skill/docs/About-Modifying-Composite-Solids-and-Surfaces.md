# About Modifying Composite Solids and Surfaces

Modify the entire form of a composite 3D object or the original forms that make up the composite.

You can move, scale, or rotate a selected composite objects using grips or gizmos.

## Modify Original Components of Composites

When the History property is set to Record (On), press the Ctrl key to display any original forms that were removed during
a union, subtract, or intersect operation. If the original, removed form was a solid primitive, you can drag the displayed
grips to change its shape and size. As a result, the composite object is modified.

![](../images/GUID-2254F043-DBBF-4744-8C2E-534EDA7B7FC7-low.png)

If the selected individual form does not contain its history, you can move, rotate, scale, or delete the form.

## Modify Complex Composites

A composite object might be made up of other composite objects. You can select the history images of composite objects by
holding down the Ctrl key as you click the forms. (For best results, set the subobject selection filter to Solid History.)

![](../images/GUID-2BDA276B-CDFF-4886-BD1A-E87AF7DCFF7E-low.png)

You can also change the size and shape of composite objects by clicking and dragging grips on individual faces, edges, and
vertices.

## Separate Discrete Objects Combined With a Union

If you have combined discrete 3D solids or surfaces using a union operation, you can separate them into their original components.
(Use the Separate option of the SOLIDEDIT command.) Composite objects cannot overlap or share a common area or volume to be
separated.

After separation, the individual solids retain their original layers and colors. All nested 3D solid objects are restored
to their simplest forms.

#### Related Tasks

* [To Work With Creating Composite Objects](To-Work-With-Creating-Composite-Objects.md)
* [To Work With Displaying Composite Object History](To-Work-With-Displaying-Composite-Object-History.md)
* [To Work With Selecting a Component of a Composite Solid](To-Work-With-Selecting-a-Component-of-a-Composite-Solid.md)
* [To Separate a Composite 3D Solid Into Individual Solids](To-Separate-a-Composite-3D-Solid-Into-Individual-Solids.md)

#### Related Concepts

* [About Creating Composite Objects](About-Creating-Composite-Objects.md)
* [About Displaying the Original Components of Composite Solids](About-Displaying-the-Original-Components-of-Composite-Solids.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*