# To Compare Xrefs

Review the differences between an attached xref and the referenced drawing file.

1. Click
   Window menu ![](../images/ac.menuaro.gif) Reference Manager.
2. In the Reference Manager palette, right-click the DWG reference you want to compare.
3. Click Compare and choose one of the following options.
   * *Recent Changes.* Compares the selected xref with the latest version of the referenced drawing file.
   * *Select File.* Opens a standard file selection dialog box, in which you can select a drawing file to compare with the specified xref.

The Xref Compare visor opens and the comparison results display in the current drawing. This visor provides several commands
and settings to review and control the comparison result.

![](../images/GUID-556E029F-41F3-4A84-B979-27435C621FA7-low.png)

Differences between the comparison drawing and the attached xref are grouped by proximity into
*change sets* that are surrounded by revision clouds. Differences are separated by color. By default, the colors are assigned as follows:

* Red - Objects that are only in the compared drawing
* Green - Objects that are only in the current drawing
* Gray - Objects that are common to both drawings
* Faded - Objects that are not part of the xref comparison

## Change the Display Settings for the Comparison

1. Click Settings on the Xref Compare visor.
   ![](../images/GUID-0D7CBE9D-323C-4535-9511-31C9029357E6-low.png)
2. In the Settings panel, click the controls that you want to change.

Change the Visibility of the Compared Objects
:   Click the light bulb icon for objects that you want to turn on or off in the comparison result.
    ![](../images/GUID-F0FA6860-A205-433B-8E59-526E0E9D52A2-low.png)

Change the Draw Order of the Compared Objects
:   ![](../images/GUID-51D58F34-F9F0-43E4-BE79-1F5C34E41DFE-low.png) Click to reverse the draw order between overlapping objects in the xref and the referenced drawing file in the comparison.
    By default, the objects in the host drawing are displayed above the objects in the referenced drawing file.

Change the Visibility, Color, and Shape of the Revision Clouds
:   Revision clouds are used to highlight the differences between an attached xref and the referenced drawing file.

    * To toggle the visibility of the revision clouds, click the light bulb icon.
    * To change the shape of the revision clouds, select Rectangular or Polygonal from the Shape drop-down list.
    * To change the offset distance between the change sets and the revision clouds, use the Margin slider.

      The size of the change sets is determined by the proximity of the changed objects compared to the size of the revision clouds.

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

## End the Comparison

* ![](../images/GUID-9002B3B8-BF54-447F-B816-6EA0CDF91EFC-low.png) Click to end the comparison and close the DWG Compare visor.

#### Related Tasks

* [To Compare Drawings](To-Compare-Drawings.md)

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)

#### Related Concepts

* [About Updating Referenced Drawing Attachments](About-Updating-Referenced-Drawing-Attachments.md)
* [About Comparing Differences Between Drawings](About-Comparing-Differences-Between-Drawings.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Work With Attaching and Detaching Referenced Drawings](To-Work-With-Attaching-and-Detaching-Referenced-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*