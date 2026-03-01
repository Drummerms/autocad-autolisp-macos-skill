# COPY (Command)

Copies objects a specified distance in a specified direction.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Copy.
![](../images/GUID-3FFF159C-9CD3-4A0C-AC82-E712A515ED3A-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Copy.

![](../images/GUID-FEEBE4B9-0DE3-4555-9F12-C2C2FDDD322A-low.png)

With the COPYMODE system variable, you can control whether multiple copies are created automatically.

![](../images/GUID-7A9EC2F4-4552-491C-BED9-EA8C1CED533F-low.gif)

The following prompts are displayed.

Select objects:
*Use an object selection method and press**Enter* *when you finish*

Specify base point or [Displacement/mOde/Multiple] <Displacement>:
*Specify a base point or enter an option*

Specify second point or [Array] <use first point as displacement>:
*Specify a second point or enter an option*

## Displacement

Specifies a relative distance and direction using coordinates.

The two points you specify define a vector that indicates how far from the original the copied objects are to be placed and
in what direction.

If you press Enter at the Specify Second Point prompt, the first point is interpreted as a relative
*X,Y,Z* displacement. For example, if you specify
*2,3* for the base point and press Enter at the next prompt, the objects are copied 2 units in the
*X* direction and 3 units in the
*Y* direction from their current location.

## Mode

Controls whether the command repeats automatically (COPYMODE system variable).

Single
:   Creates a single copy of selected objects and ends the command.

Multiple
:   Overrides the Single mode setting. The COPY command is set to repeat automatically for the duration of the command.

## Array

Arranges a specified number of copies in a linear array.

Number of Items to Array
:   Specifies the number of items in the array, including the original selection set.

Second Point
:   Determines a distance and direction for the array relative to the base point. By default, the first copy in the array is positioned
    at the specified displacement. The remaining copies are positioned in a linear array beyond that point using the same incremental
    displacement.

Fit
:   Positions the final copy in the array at the specified displacement. The other copies are fit in a linear array between the
    original selection set and the final copy.

## Fit

Redefines the array to use the specified displacement as the location of the last copy rather than the first copy, fitting
the other copies between the original selection set and the final copy.

#### Related Concepts

* [About Editing with Grips](About-Editing-with-Grips.md)

#### Related Information

* [About Copying Objects](About-Copying-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*