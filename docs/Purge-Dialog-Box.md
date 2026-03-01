# Purge Dialog Box

Removes unused items, such as block definitions and layers, from the drawing. Displays items that can be purged.

PURGE (Command)

*Toolbar:* Purge
![](../images/GUID-089301D9-6EA7-4E69-B931-839242981CFB-low.png)

![](../images/GUID-462253DC-B0FE-432E-B451-D3FB7E85EF2F-low.png)

By default, all named items are selected for purge. Click Show Details to select categories or individual items to purge.

![](../images/GUID-141EC20A-44EC-4FA3-8B40-7FC051EFAB9B-low.png)

## Purge Dialog Views

Two views are available in Purge dialog box:

* Purgeable Items
* Non-Purgeable Items

![](../images/GUID-2FC61CA1-8637-4118-BBEC-6ABDEEB33C8F-low.png)

## Purgeable Items

Lists the items in your current drawing that you can purge in the tree view pane on the left side. Additional items can be
removed from the drawing under the Purge Unnamed Objects pane on the right side of the dialog box.

Named Items Not Used
:   Lists the named objects that are not used in the current drawing and that can be purged. Select a category to purge all items
    within that category. Click the arrow to display a list of the individual items in that category. Once you expand a category,
    select or clear individual items.

Preview
:   Highlight an individual item in Named Items Not Used to display a preview.

    ![](../images/GUID-F3667266-FBD3-4B9A-9D45-7C774BCF63F5-low.png)

    NOTE: Not all items can be previewed.

### Options

Nested Items
:   Removes all unused named objects from the drawing that are contained within or referenced by other unused named objects.

Zero-length Geometry
:   Deletes geometry of zero length (lines, arcs, polylines and so on) in non-block objects.

Empty Text Objects
:   Deletes mtext and text that contains only spaces (no text) in non-block objects.

    NOTE:The PURGE command will not remove zero-length geometry or empty text and mtext objects from blocks or locked layers.

Orphaned Data
:   Performs a drawing scan and removes obsolete DGN linestyle data when you open the Purge dialog box.

Unsupported Objects
:   Deletes custom objects or data not supported by AutoCAD for Mac but are used or referenced in current drawing. After selecting
    Purge, a dialog box displays listing the unsupported objects referenced in the current drawing.

    ![](../images/GUID-9AD8ECCC-F2CE-45D7-8B7A-BAE1D7684EF2-low.png)

    NOTE:Purging unsupported objects may result in a loss of data. Please review the list of unsupported objects carefully.

File Size About
:   Initially, the maximum amount the drawing size can be reduced is shown.

    ![](../images/GUID-07DFD419-2BCA-4C04-A255-135DF5E988E9-low.png)

    After selecting items for purging and clicking Purge, the amount my drawing file size was reduced and the amount that can
    still be purged are shown.

    ![](../images/GUID-4B8F72EE-0C79-4D13-9F16-8D6EA8C1AFEB-low.png)

## Non-Purgeable Items

Preview objects that you can't purge and find those objects in your drawing.

![](../images/GUID-86118B0E-E5FB-4A4A-8B0B-D4134A9EDF1C-low.png)

Named Items In Use
:   Lists the named objects that are used in the current drawing and can't be purged.

    Most of these objects are currently used in the drawing or are default items that can't be removed. When you select individual
    named objects, information about why you can't purge the item is displayed.

Preview
:   Displays a preview of the item you selected in the tree view by clicking on its name.

Details
:   Displays information about the object's size, location, and the total number of those objects in your drawing.

    Select Objects
    :   Closes the purge dialog box, selects the non-purgeable objects, and zooms in to them.

        ![](../images/GUID-65FC91DC-797F-4DC9-B1FA-27112D35EC22-low.png)

Reasons
:   Displays information about why you can't purge the selected item.

## Expand\Collapse

![](../images/GUID-C2EC9BD0-B63D-44C1-B026-A9DD7C1CA9EE-low.png) - expands the tree list

![](../images/GUID-60359A4F-845C-48C3-A9E5-FC6E724A2064-low.png) - collapses the tree list

## Show\Hide Details

Switches between displaying the detailed version of the dialog box that contains the list of items that can be purged and
the preview, and the version that has a check box to purge all named items. The state of the dialog box persists across sessions
of AutoCAD.

## Purge

Purges the selected items.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*