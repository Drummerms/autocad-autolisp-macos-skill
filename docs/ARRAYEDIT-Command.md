# ARRAYEDIT (Command)

Edits associative array objects and their source objects.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Array Edit.
![](../images/GUID-E58CAAE3-4BED-4C34-BC4E-11689CADD252-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

Modify associative arrays by editing the array properties, editing source objects, or replacing items with other objects.

When you select a single associative array object, one of the following visors is displayed:

* Path Array visor
* Polar Array visor
* Rectangular Array visor

The following prompt is displayed.

## Select array

Selects an array for editing. The type of array you select (rectangular, path, or polar) determines the remaining prompts.

## Source

Activates an editing state in which you can update the associative array by editing one of its items.

Select item in array
:   Select one of the array items as a source object to modify. All changes (including the creation of new objects) are instantly
    applied to all items that reference the same source objects. While the editing state is active, a contextual ribbon is displayed.

## Replace

Replaces the source objects for selected items or for all items referencing the original source objects.

Replacement objects
:   Select the new source objects.

Base point
:   Specifies a base point for positioning each replacement object.

Key point
:   Specifies a constraint point to be used for positioning.

Item in the array to replace
:   Specifies an array item to replace, and continues to prompt for additional items.

Source objects
:   Replaces the original set of source objects in the array, which updates all items that have not been previously replaced.

## Base point

Redefines the base point of the array. Path arrays are repositioned relative to the new base point.

Base point
:   Specifies a base point for positioning the objects in the array.

Key point
:   For associative arrays, specifies a valid constraint (or
    *key point*) on the source objects to use as the base point. If you edit the source objects of the resulting array, the base point of
    the array remains coincident with the key point of the source objects.

## Rows

Specifies the number and spacing of rows, and the incrementing elevation between them.

Number of rows
:   Specifies the number of rows in the array.

Expression
:   Derives a value using a mathematical formula or equation.

Total
:   Specifies the total distance between the first and last rows.

Incrementing elevation
:   Specifies the amount of elevation change between each successive row.

## Columns (rectangular arrays)

Specifies the number and spacing of columns.

Number of columns
:   Specifies the number of columns in the array.

Distance between columns
:   Specifies the distance between columns.

Expression
:   Derives a value using a mathematical formula or equation.

Total
:   Specifies the total distance between the first and last columns.

## Levels

Specifies the number and spacing of levels (for 3D arrays).

Number of levels
:   Specifies the number of levels in the array.

Distance between levels
:   Specifies the distance between the levels.

Expression
:   Derives a value using a mathematical formula or equation.

Total
:   Specifies the total distance between the first and last levels.

## Method (path arrays)

Controls how to distribute items along the path.

* *Divide.* Redistributes items to divide evenly along the length of the path.
* *Measure.* Maintains current spacing when the path is edited, or when the number of items is edited through grips or the Properties
  palette. When the number of items is edited using ARRAYEDIT, you are prompted to redefine the distribution method.

## Items (path and polar arrays)

Number of items
:   Specifies the number of items in the array using a value or expression.

Fill entire path (path arrays)
:   Uses the distance between items value to determine how the path is filled. Use this option if you expect the size of the path
    to change and want to maintain a specific spacing between array items.

    For path arrays whose Method property is set to Measure, you are prompted to redefine the distribution method (Divide, Total,
    Expression).

## Align items (path arrays)

Specifies whether to align each item to be tangent to the path direction. Alignment is relative to the orientation of the
first item.

Yes
:   Sets the each arrayed item to follow the normal, or perpendicular orientation of the curve.

No
:   Sets all arrayed items to the same alignment as the source object in the array.

## Z direction (path arrays)

Specifies whether to maintain the original
*Z* direction or to naturally bank the items along a 3D path.

## Angle between (polar arrays)

Specifies the angle between items using a value or expression.

## Fill angle (polar arrays)

Specifies the angle between the first and last item in the array using a value or expression.

## Rotate items (polar arrays)

Controls whether items are rotated as they are arrayed.

## Reset

Restores erased items and removes any item overrides.

## Exit

Exits the command.

#### Related Concepts

* [About Arrays](About-Arrays.md)

#### Related Information

* [About Editing Associative Arrays](About-Editing-Associative-Arrays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*