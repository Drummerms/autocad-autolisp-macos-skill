# About Annotation Scale

Annotation scale is used to determine text height or the overall scale of an annotation object.

The approach used to calculate an annotation scale depends on whether the object is placed in model space or on a layout.

## In Model Space

When annotation objects are created in model space, the following must be considered:

* Drawing or plot scale if plotting from model space.
* Viewport scale of a layout viewport if plotting from a paper space layout.

The text height or scale of an annotation object in model space can be set to a fixed text height or be controlled by assigning
the object an annotation scale. Annotation objects assigned a fixed text height or object scale remain proportionate in size
to the current plot or viewport scale.

If the annotative property of an annotation object is enabled, the text height or scale of the annotation object adjusts based
on the current drawing annotation or layout viewport scale with the result that it will remain at the same size automatically.

## Directly on a Layout

Annotation objects created in paper space on a layout should be created at full size because layouts are commonly plotted
at a 1:1 scale. For example, text created with a height of 1/8” in paper space will be output at 1/8” unless a scale other
than 1:1 is used to plot the layout.

#### Related Tasks

* [To Calculate the Fixed Height for Text Objects in Model Space](To-Calculate-the-Fixed-Height-for-Text-Objects-in-Model-Space.md)

#### Related Concepts

* [About Annotation Objects](About-Annotation-Objects.md)
* [About Calculating the Scale of Annotation Objects in Model Space](About-Calculating-the-Scale-of-Annotation-Objects-in-Model-Space.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*