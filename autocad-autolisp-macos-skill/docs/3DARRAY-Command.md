# 3DARRAY (Command)

Maintains legacy behavior for creating nonassociative, 3D rectangular or polar arrays.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) 3D Array.
![](../images/GUID-A855E70A-B2D0-4B9C-9B5C-C6291F765211-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) 3D Array.

## Summary

3DARRAY functionality has been replaced with the enhanced
[ARRAY](ARRAY-Command.md) command, which allows you to create associative or nonassociative, 2D or 3D, rectangular, path, or polar arrays. 3DARRAY
maintains legacy behavior.

For 3D rectangular arrays, in addition to columns and rows, you also specify the number of levels in the Z direction. For
3D polar arrays, you specify the axis of rotation with any two points in space.

![](../images/GUID-1A0D4AC9-F79E-4717-B9B6-4C9F2F48946F-low.gif)

The entire selection set is treated as a single element in the array.

![](../images/GUID-74657F28-C229-407E-A926-4EA0D78BA07B-low.png)

## List of Prompts

The following prompts are displayed.

Enter type of array [[Rectangular](3DARRAY-Command.md)/[Polar](3DARRAY-Command.md)] <R>: *Enter an option or press Enter*

![](../images/GUID-1E9DC585-2DA0-4E87-8EFD-E9A811CB16FC-low.png)

Rectangular Array

Copies objects in a matrix of rows (*X* axis), columns (*Y* axis), and levels (*Z* axis). An array must have at least two rows or two columns or two levels.

Specifying one row requires that more than one column be specified, and vice versa. Specifying one level creates a two-dimensional
array.

Positive values generate the array along the positive
*X*,
*Y*, and
*Z* axes. Negative values generate the array along the negative
*X*,
*Y*, and
*Z* axes.

Polar Array

Copies objects about an axis of rotation.

The specified angle determines how far the objects are arrayed about the axis of rotation. A positive number produces a counterclockwise
array rotation. A negative number produces a clockwise array rotation.

Entering
*y* or pressing Enter rotates each array element.

![](../images/GUID-4CE2B5ED-9BB5-4996-B90D-E727B95EB57B-low.png)

#### Related Concepts

* [About Arrays](About-Arrays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*