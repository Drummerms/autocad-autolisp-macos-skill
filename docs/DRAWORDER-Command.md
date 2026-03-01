# DRAWORDER (Command)

Changes the draw order of images and other objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Draw Order drop-down.
![](../images/GUID-1E34B062-BE8B-47C5-9337-C456A694413B-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Draw Order.

Several options are available that control the order in which overlapping objects are displayed. In addition to the DRAWORDER
command, the TEXTTOFRONT command brings all text, dimensions, or leaders in a drawing in front of other objects, and the HATCHTOBACK
command sends all hatch objects behind other objects.

By default, when you create new objects from several existing ones (for example, FILLET or PEDIT), the resulting objects assume
the draw order of the object that you selected first.

Use the DRAWORDERCTL system variable to control the default display behavior of overlapping objects.

The following prompts are displayed.

Select Objects
:   Specifies the objects for which you want to change the draw order. For the Above and Under options, an additional prompt displays
    in which you select the reference objects that the originally selected objects should be above or under.

Above Objects ![](../images/GUID-6BBDB8A1-768B-4D0B-B2B3-4CD1B6187AFA-low.png)
:   Moves the selected object above the specified reference objects.

Under Objects ![](../images/GUID-40F3C9F4-B49C-4FAB-8F6E-C7FC4FCA67AA-low.png)
:   Moves the selected objects below the specified reference objects.

Front ![](../images/GUID-1E34B062-BE8B-47C5-9337-C456A694413B-low.png)
:   Moves the selected objects to the top of the order of objects in the drawing.

Back ![](../images/GUID-11F63F64-EAE2-4568-B699-4A4A97D36FB9-low.png)
:   Moves the selected objects to the bottom of the order of objects in the drawing.

#### Related Tasks

* [To Control the Draw Order of Overlapping Objects](To-Control-the-Draw-Order-of-Overlapping-Objects.md)

#### Related References

* [HATCHTOBACK (Command)](HATCHTOBACK-Command.md)
* [TEXTTOFRONT (Command)](TEXTTOFRONT-Command.md)

#### Related Concepts

* [About the Draw Order of Overlapping Objects](About-the-Draw-Order-of-Overlapping-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*