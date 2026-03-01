# To Compare Drawings

Review the differences between the current drawing and a specified comparison drawing.

1. Open the first drawing you want to compare with another drawing.
2. Click DWG Compare on the toolbar.
   ![](../images/GUID-F4525FD8-467E-44D9-BD45-AEB73673ADFB-low.png)
3. In the selection dialog box, specify the drawing file that you want to compare with the current drawing and click Open.

The DWG Compare visor opens and the comparison results display in the current drawing. This visor provides several commands
and options to review and control the comparison result.

![](../images/GUID-12D0F0A8-BA83-4BC5-8FAB-E2A358CD2218-low.png)

Differences between the comparison drawing and the current drawing are grouped by proximity into
*change sets* that are surrounded by revision clouds. Differences are separated by color. By default, the colors are assigned as follows:

* Red - Objects that are only in the compared drawing
* Green - Objects that are only in the current drawing
* Gray - Objects that are common to both drawings

NOTE:

* If you have a layer that is turned off or frozen in your current drawing, it will not become part of the comparison result.
* Any changes you make in the comparison drawing do not display in a comparison until you save the changes in the comparison
  drawing.
* You can start the DWG Compare utility from the File menu even when you don't have any open drawings. In the DWG Compare dialog,
  specify the base and reference drawing, and click Compare. The comparison result is shown in the base drawing.

## Change the Display Settings for the Comparison

1. Click Settings on the DWG Compare visor.
   ![](../images/GUID-0D7CBE9D-323C-4535-9511-31C9029357E6-low.png)
2. In the Settings panel, click the controls that you want to change.

![](../images/GUID-CEA84EDD-B5D4-4A2D-8676-5D1C0062273F-low.png)

Change the Visibility of the Compared Objects
:   * Click the light bulb next to the Not in Current Drawing or Only in Current Drawing options to toggle the visibility of the
      differences between the compared or the current drawing files.
      ![](../images/GUID-F0FA6860-A205-433B-8E59-526E0E9D52A2-low.png)
    * Click the light bulb next to No Differences option to toggle the visibility of the objects that are the same in both of the
      drawing files.

Change the Draw Order of the Compared Objects
:   ![](../images/GUID-51D58F34-F9F0-43E4-BE79-1F5C34E41DFE-low.png) Click to reverse the draw order between overlapping objects in the current drawing and the compared drawing. By default,
    the objects in the current drawing are displayed on top of those in the compared drawing.

Change the Visibility, Color, and Shape of the Revision Clouds
:   Revision clouds are used on the comparison drawing to highlight the differences between the compared files.

    * To toggle the visibility of the revision clouds, click the light bulb icon.
    * To change the shape of the revision clouds, select Rectangular or Polygonal from the Shape drop-down list.
    * To change the offset distance between the change sets and the revision clouds, use the Margin slider.
    * The size of the change sets is determined by the proximity of the changed objects compared to the size of the revision clouds.

    NOTE:The size of the arcs in the revision clouds is determined automatically based on the extents of the current drawing. Larger
    drawings automatically use larger arcs in their revision clouds.

Exclude Hatch or Text From the Comparison
:   Filters provide a way to hide the comparison results for the following objects:

    * ![](../images/GUID-E6623040-7B2A-4D96-8139-754031532DDC-low.png) Click to hide hatch object comparisons in your comparison result
    * ![](../images/GUID-6AEDDB35-1B7A-4D11-B2B4-86A1C71AD3CD-low.png) Click to hide text object comparisons in your comparison result

Temporarily Turn Off the Comparison Results
:   * ![](../images/GUID-72DF67CE-5EBB-47F9-8D6E-0E6F7E98C7C8-low.png) Click to hide the comparison results temporarily as you work in the current drawing.

## Navigate Between Change Sets

* ![](../images/GUID-E08DF176-4250-4E77-AD7F-803C79CC4961-low.png) ![](../images/GUID-1022F615-E637-472E-A23E-FE09CAD7F4C0-low.png) Click the right and left arrows to zoom in to the next or previous change set.

## Copy Objects From the Compared Drawing to the Current Drawing

1. ![](../images/GUID-A25D47BB-899C-49B4-B969-D5E21B7071A1-low.png) Click Import Objects to import selected objects from the compared drawing into the current drawing.
2. Select the objects in the comparison that you want to copy into the current drawing and press Enter. Only those objects that
   are not in the current drawing can be imported.

The objects you selected from the comparison are copied into to your current drawing and no longer differ between the drawings.

## Export a Snapshot Drawing to Save the Differences

1. ![](../images/GUID-D32B0E1E-6551-4A10-8CBD-E8258B398BE8-low.png) Click Export Snapshot to combine the two comparison drawings into a new
   *snapshot drawing* file for further review.
2. In the Export a Comparison Snapshot dialog box, click Continue.
3. Save the drawing file. By default, the file name is Compare\_*Current Drawing* vs
   *Compared Drawing*.dwg

This operation creates a drawing file displaying the differences between the two files. In the snapshot drawing, the two drawings
in the comparison are stored as blocks.

## End the Comparison

* ![](../images/GUID-9002B3B8-BF54-447F-B816-6EA0CDF91EFC-low.png) Click to end the comparison and close the DWG Compare visor.

#### Related Tasks

* [To Compare Xrefs](To-Compare-Xrefs.md)

#### Related References

* [Commands for Working With DWG Compare](Commands-for-Working-With-DWG-Compare.md)

#### Related Concepts

* [About Comparing Differences Between Drawings](About-Comparing-Differences-Between-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*