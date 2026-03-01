# NCOPY (Command)

Copies objects that are contained in an xref or block.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Copy Nested Objects.
![](../images/GUID-CBB3160E-A087-4CA2-8850-7928178BCDBF-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Copy Nested Objects.

Instead of exploding or binding an xref or block to be able to copy objects nested within them, you can copy the selected
objects directly into the current drawing.

The following prompts are displayed.

## Nested Objects to Copy

Specifies the component of an xref, block, or underlay that you want to copy.

Base point
:   Sets the point to be used as a base point for placing the copied objects.

Second point
:   In combination with the first point, specifies a vector that indicates how far, and in what direction, the selected objects
    are moved.

    If you press Enter to accept the Use first point as displacement default, the first point is interpreted as a relative
    *X,Y,Z* displacement. For example, if you specify
    *2,3* for the base point and press Enter at the next prompt, the objects move 2 units in the
    *X* direction and 3 units in the
    *Y* direction from their current position.

## Displacement

Specifies a relative distance and direction from the base point location.

## Multiple

Controls whether multiple copies are created automatically as you specify additional locations.

## Array

Arranges a specified number of copies in a linear array using the first and second copy as the spacing distance.

Number of items to array
:   Specifies the number of sets of the selected objects in the array, including the original selection set.

    * *Second point (Number of items).* Determines a distance and direction for the array relative to the base point. The distance you specify determines the distance
      between the base points of each object in the array.

Fit
:   Arranges a specified number of copies in a linear array using the first and last copy as the total spacing distance.

    * *Second point (Fit)*. Positions the last copy in the array at the specified displacement distance and direction. The other copies are evenly spaced
      in a linear array between the first copy and the last copy.

## Settings

Controls whether named objects that are associated with the selected objects are added to the drawing.

Insert
:   Duplicates the selected objects to the current layer without regard to named objects. This option is similar to the COPY command.

Bind
:   Includes named objects such as blocks, dimension styles, layers, linetypes, and text styles associated with the copied objects
    into the drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*