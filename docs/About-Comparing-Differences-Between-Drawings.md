# About Comparing Differences Between Drawings

Use the DWG Compare feature to compare a specified drawing with the current drawing. Color and revision clouds highlight the
differences in the current drawing as you work.

As your design progresses, it becomes more difficult to remember what was changed from one revision to the next, especially
when working in a remotely distributed team. The DWG Compare feature provides a way to perform a visual comparison between
two drawings.

During the comparison process, the DWG Compare feature identifies objects that have been modified, added, or removed from
the two drawings. For example, consider these two highly simplified drawings. Each drawing has differences that are not in
the other drawing.

![](../images/GUID-2DB68E32-86DC-4A97-8C41-7EF91D9F7C54-low.png)

Let's say that drawing 1 is the previous version of a drawing and drawing 2 is the current drawing.

When the COMPARE command is started, the DWG Compare visor displays at the top of the drawing area when you specify the
*comparison drawing*, drawing 1 in this example.

![](../images/GUID-26472838-69C1-47C8-891B-F002A4B3909B-low.png)

The result of the comparison is displayed in the current drawing as shown below.

NOTE:For better clarity, color-blind friendly colors were used in the illustrations that follow.

![](../images/GUID-9C0EFC6E-52ED-4E2E-8ADA-943078C2C2D2-low.png)

* Objects that are common between the drawings are displayed in gray by default.
* Objects that are in the
  *comparison drawing* but not in the current drawing are displayed in red by default.
* Objects that are in the current drawing but not in the
  *comparison drawing* are displayed in green by default.
* Differences are highlighted using revision clouds as
  *change sets*. The arrow buttons in the DWG Compare visor provide a way to zoom into each change set automatically.

You can specify different colors in the Settings palette of the DWG Compare visor. The Settings palette also provides additional
display controls.
![](../images/GUID-0D7CBE9D-323C-4535-9511-31C9029357E6-low.png)

## Notes

* When the comparison is active, changes to the current drawing are detected automatically.
* If the
  *comparison* drawing is also open, any changes you make in the comparison drawing do not display in a comparison until you save the changes.
* If you have a layer that is turned off or frozen in your current drawing, it will not become part of the comparison result.
* You can start the DWG Compare utility from the File menu even when you don't have any open drawings. In the DWG Compare dialog,
  specify the base and reference drawing, and click Compare. The comparison result is shown in the base drawing.

## Import Differences into the Current Drawing

From the DWG Compare visor, you can import differences from the compared drawing into the current drawing. Only those objects
that are different in the
*comparison* drawing can be imported into the current drawing.

![](../images/GUID-6F903996-C601-474A-8FF7-05E7F9DB4D8C-low.png)

Imported differences automatically turn gray because they are now present in both drawings.

## Export the Comparison Result

You can export the results of a comparison into a new
*snapshot drawing* for reference. The snapshot drawing maintains the visual appearance of the comparison and is named using a combination of
the drawing names.

![](../images/GUID-2E2C81D8-E831-4BE4-9F5C-B1CC8521E7DB-low.png)

NOTE:The snapshot drawing contains two blocks, one for each of the two compared drawings.

## General Limitations

The limitations for the DWG Compare feature include the following:

* Operates in model space only. If a drawing selected for comparison was saved in a layout, DWG Compare automatically switches
  to the Model tab.
* Supports DWG files only.
* Does not support all object types. Exceptions include OLE objects, cameras, geographic data, GIS objects from Map 3D, non-DWG
  underlays, images, coordination models, and point clouds.
* Does not support using a comparison result to compare against a third drawing.
* Cannot detect ByBlock or ByLayer property changes within nested blocks.
* Comparison graphics are displayed only in the 2D Wireframe visual style. (AutoCAD only)
* Revision clouds cannot enclose changes in a 3D isometric view.

#### Related Tasks

* [To Compare Drawings](To-Compare-Drawings.md)
* [To Compare Xrefs](To-Compare-Xrefs.md)

#### Related References

* [Commands for Working With DWG Compare](Commands-for-Working-With-DWG-Compare.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*