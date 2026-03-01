# Count

Quickly and accurately count the instances of blocks or other selected objects in a drawing. You can insert a table with the
block count data into the current drawing.

![](../images/GUID-F9E317F2-D1FD-4B45-8C52-F43B79F8177E-low.png)

The Count feature offers visual count results and more control over the count criteria.

![](../images/GUID-40BA8FD5-7C95-4A7F-9A41-9866B065F4C3-low.png)

When you're in an active count, the Count visor displays at the top of the drawing area. The Count visor includes the number
of objects and issues, along with other controls to manage the counted objects.

![](../images/GUID-3951D146-B66F-4393-B135-8CEDEB6C08F1-low.png)

The count details icon changes depending on whether the current count contains errors. Click
![](../images/GUID-FBAC9A26-4A4D-4E99-BF12-68A302626888-low.png) or
![](../images/GUID-4ADA7BAA-4104-4C0C-B3AB-8EAE788DCAAC-low.png) to open the Count palette and view more details.

| ![](../images/GUID-BF2DBC8C-3390-4661-BFD8-AF1CE0A36153-low.png) | Displays the count criteria including the general properties of the counted objects and any user-defined block attributes and parameters. |
| ![](../images/GUID-525D7C63-B386-4CE0-8067-475C63D0D592-low.png) | Displays the count criteria including the general properties, user-defined block attributes and parameters, and the issue report of the counted objects. Issues can include overlapping, exploded, or renamed objects. |

NOTE:The count list includes blocks that are nested within other blocks.

Count all blocks

1. Select Count from the toolbar.
   ![](../images/GUID-1FBDE4F0-CE0E-42FA-AEB8-F17779ECC144-low.png)
2. Enter E for the entire model space, then press Enter to list all blocks.

   The Count palette displays the number of instances of each block on the drawing.
3. Click a block name on the palette to highlight all instances of that block in the drawing.
4. Right-click a block name to filter based on certain properties.

Count objects within an area

1. Select Count from the toolbar.
   ![](../images/GUID-1FBDE4F0-CE0E-42FA-AEB8-F17779ECC144-low.png)
2. Specify the two corners for the area on the drawing.
3. Select specific objects or blocks or press Enter to count all blocks within the area.

   All instances that match the selected objects are highlighted in the drawing.

   NOTE:The specified area becomes the current area for the next count.
4. Click Details to open the palette for further filtering options.
   ![](../images/GUID-BF2DBC8C-3390-4661-BFD8-AF1CE0A36153-low.png)
5. Click Select to select the highlighted objects.
   ![](../images/GUID-8CD7650C-9809-4C89-886A-A81B64959DE7-low.png)

Count a specific object type

1. Select an object, such as a line or a block.
2. Right-click and select Count.
3. Click Details to open the palette for further filtering options.
   ![](../images/GUID-BF2DBC8C-3390-4661-BFD8-AF1CE0A36153-low.png)
4. Click Select to select the highlighted objects.
   ![](../images/GUID-8CD7650C-9809-4C89-886A-A81B64959DE7-low.png)

## *New Commands*

[COUNT](COUNT-Command.md) - Counts and highlights the instances of the selected object in the drawing.

[COUNTAREA](COUNTAREA-Command.md) - Defines the area to count the instances of an object or block.

[COUNTAREACLOSE](COUNTAREACLOSE-Command.md) - Cancels the count selection area.

[COUNTCLOSE](COUNTCLOSE-Command.md) - Closes the Count toolbar and exits the count.

[COUNTFIELD](COUNTFIELD-Command.md) - Creates a field that's set to the value of the current count.

[COUNTLIST](COUNTLIST-Command.md) - Opens the Count palette to view and manage the counted blocks.

[COUNTLISTCLOSE](COUNTLISTCLOSE-Command.md) - Closes the Count palette.

[COUNTNAVNEXT](COUNTNAVNEXT-Command.md) - Zooms to the next object in the count result.

[COUNTNAVPREV](COUNTNAVPREV-Command.md) - Zooms to the previous object in the count result.

[COUNTTABLE](COUNTTABLE-Command.md) - Inserts a table containing the block names and the corresponding count of each block in the drawing.

[SELECTCOUNT](SELECTCOUNT-Command.md) - Finds all objects within the current count that match the properties of the selected objects, and then adds them to the
selection set.

## *Changed Commands*

[FIELD](FIELD-Command.md) - Creates a multiline text object with a field that can be updated automatically as the field value changes. Count was added
to the Objects category.

## *New System Variables*

[COUNTCHECK](COUNTCHECK-System-Variable.md) - Controls the types of errors to check in the count.

[COUNTCOLOR](COUNTCOLOR-System-Variable.md) - Sets the highlighting color on objects in a count.

[COUNTERRORCOLOR](COUNTERRORCOLOR-System-Variable.md) - Sets the highlighting color on objects that can cause potential errors in a count.

[COUNTERRORNUM](COUNTERRORNUM-System-Variable.md) - Displays the number errors in the current count.

[COUNTNUMBER](COUNTNUMBER-System-Variable.md) - Displays the number of the current count.

[COUNTPALETTESTATE](COUNTPALETTESTATE-System-Variable.md) - Reports whether the Count palette is open or closed.

[COUNTSERVICE](COUNTSERVICE-System-Variable.md) - Controls the background indexing of the count.

#### Related Tasks

* [To Work with Counting Objects](To-Work-with-Counting-Objects.md)

#### Related Concepts

* [About Counting Objects](About-Counting-Objects.md)
* [What's New in AutoCAD for Mac 2023](What's-New-in-AutoCAD-for-Mac-2023.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*