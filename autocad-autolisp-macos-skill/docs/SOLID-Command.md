# SOLID (Command)

Creates solid-filled triangles and quadrilaterals.

## Summary

2D solids are filled only when the [FILLMODE](FILLMODE-System-Variable.md) system variable is on (1) and the viewing direction is orthogonal to the 2D solid.

## List of Prompts

The following prompts are displayed.

First point
:   Sets the first point in the 2D solid.

Second point
:   Sets the first edge of the 2D solid.

Third point
:   Sets the corner that is opposite the second point.

Fourth point or <exit>
:   The fourth point is diagonally opposite the first point. Pressing Enter at the Fourth Point prompt creates a filled triangle.
    Specifying a fifth point creates a quadrilateral area.

    ![](../images/GUID-0F5E3638-AF0A-42C4-ABE7-A629908B7D61-low.png)

    Specifying successive third and fourth points creates further connected triangles and four-sided polygons in a single solid
    object.

    ![](../images/GUID-BEC2177B-69FE-42DD-A86C-F2EBBE69FDEF-low.png)

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*