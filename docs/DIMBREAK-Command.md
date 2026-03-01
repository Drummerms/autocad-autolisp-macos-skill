# DIMBREAK (Command)

Breaks or restores dimension and extension lines where they cross other objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension, Dimbreak.
![](../images/GUID-5FB2D06D-8AC6-48EA-8B7A-A1CF1FEDD526-low.png)

*Menu*:
Dimension
![](../images/ac.menuaro.gif) Dimension Break.

## Summary

Dimension breaks can be added to linear, angular, and ordinate dimensions, among others.

## List of Prompts

The following prompts are displayed.

Select a dimension to add/remove break or [[Multiple](DIMBREAK-Command.md)]:
*Select a dimension, or enter**m* *and press*Enter

After you select a dimension, the following prompt is displayed:

Select object to break dimension or [[Auto](DIMBREAK-Command.md)/[Manual](DIMBREAK-Command.md)/[Remove](DIMBREAK-Command.md)] <Auto>:
*Select an object that intersects the dimension or extension lines of the selected dimension, enter an option, or press* Enter

After you select an object to break the dimension with, the following prompt is displayed:

Select object to break dimension:
*Select an object that passes through the dimension or press*Enter *to end the command*

NOTE:Dimension breaks can be added to dimensions for objects that do not intersect the dimension or extension lines using the by
Manual option.

Multiple
:   Specifies multiple dimensions to add breaks to or remove breaks from.

Auto
:   Places dimension breaks automatically at all the intersection points of the objects that intersect the selected dimension.
    Any dimension break created using this option is updated automatically when the dimension or an intersecting object is modified.

    When a new object is drawn over the top of a dimension that has any dimension breaks, no new dimension breaks are automatically
    applied at the intersecting points along the dimension object. To add the new dimension breaks, must be run the command again.

Remove
:   Removes all dimension breaks from the selected dimensions.

Manual
:   Places a dimension break manually. You specify two points on the dimension or extension lines for the location of the break.
    Any dimension break that is created using this option is not updated if the dimension or intersecting objects are modified.
    You can only place a single manual dimension break at a time with this option.

#### Related Concepts

* [About Creating Breaks in Dimensions](About-Creating-Breaks-in-Dimensions.md)
* [About Dimensioning](About-Dimensioning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*