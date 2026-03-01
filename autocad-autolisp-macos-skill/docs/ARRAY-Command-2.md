# -ARRAY (Command)

Maintains legacy command line behavior for creating nonassociative, 2D rectangular or polar arrays.

## List of Prompts

The following prompts are displayed.

Select objects: *Use an object selection method*

Enter the type of array [[Rectangular](ARRAY-Command-2.md)/[Polar](ARRAY-Command-2.md)] <*current*>: *Enter an option or press* Enter

Rectangular

Creates an array of rows and columns of copies of the selected objects.

![](../images/GUID-91635C32-6E9E-4336-AB19-32B562D72442-low.png)

Enter the number of rows (---) <1>: *Enter a nonzero integer or press* Enter

Enter the number of columns (|||) <1>: *Enter a nonzero integer or press* Enter

If you specify one row, you must specify more than one column and vice versa.

The selected object, or cornerstone element, is assumed to be in the lower-left corner, and generates the array up and to
the right.

The specified distance between the rows and columns includes the corresponding lengths of the object to be arrayed.

Enter the distance between rows or specify unit cell (---):

To add rows downward, specify a negative value for the distance between rows. ARRAY skips the next prompt if you specify two
points for the opposite corners of a rectangle.

Specify the distance between columns (|||):

To add columns to the left, specify a negative value for the distance between columns. Rectangular arrays are constructed
along a baseline defined by the current snap rotation. This angle is normally 0, so the rows and columns are orthogonal with
respect to the *X* and *Y* drawing axes. The Rotate option of the [SNAP](SNAP-Command.md) command changes the angle and creates a rotated array. The [SNAPANG](SNAPANG-System-Variable.md) system variable stores the snap rotation angle.

If you specify a large number of rows and columns for the array, it might take a while to create the copies. By default, the
maximum number of array elements that you can generate in one command is 100,000. How you change this limit depends on the
product:

* Most AutoCAD-based products: The limit is set by the MAXARRAY setting in the registry. To reset the limit to 200,000, for
  example, enter (setenv "MaxArray" "200000") at the Command prompt.
* AutoCAD LT: You can change the maximum number of array elements by setting the MaxArray system registry variable using the
  SETENV command.

Polar

Creates an array by copying the selected objects around a specified center point.

![](../images/GUID-E0E29461-68FE-4712-ADDD-4FE04E80C1EE-low.png)

Specify center point of array or [Base]: *Specify a point or enter* *b* *to specify a new base point*

Center Point
:   Creates an array defined by a center point.

Base
:   Specifies a new reference (base) point relative to the selected objects that will remain at a constant distance from the center
    point of the array as the objects are arrayed.

Enter the number of items in the array: *Enter a positive integer or press* Enter

If you enter a value for the number of items, you must specify either the angle to fill or the angle between items. If you
press Enter (and do not provide the number of items), you must specify both.

Specify the angle to fill (+=ccw, -=cw) <360>: *Enter a positive number for a counterclockwise rotation or a negative number for a clockwise rotation*

You can enter *0* for the angle to fill only if you specify the number of items.

If you specify an angle to fill without providing the number of items, or if you specify the number of items and enter *0* as the angle to fill or press Enter, the following prompt is displayed:

Angle between items: *Specify an angle*

If you specified the number of items and entered 0 as the angle to fill or pressed Enter, ARRAY prompts for a positive or
negative number to indicate the direction of the array:

Angle between items (+=ccw, -=cw): *Enter a positive number for a counterclockwise rotation or a negative number for a clockwise rotation*

ARRAY determines the distance from the array's center point to a reference point on the last object selected. Reference points
include locations such as the center point of a circle or arc, the insertion base point of a block, the start point of text,
or the endpoint of a line.

Rotate arrayed objects? <Y>: *Enter* *y* *or* *n**, or press* Enter

In a polar array, the reference point of the last object in the selection set is used for all objects. If you defined the
selection set by using window or crossing selection, the last object in the selection set is arbitrary. Removing an object
from the selection set and adding it back forces that object to be the last object selected. You can also make the selection
set into a block and replicate it.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*