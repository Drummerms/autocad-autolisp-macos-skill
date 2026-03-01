# About Suppressing Zeros in Dimensions

You can suppress leading and trailing zeros in the numeric portion of dimension text. You can also specify the sub unit for
the dimension distance.

If you suppress leading zeros in decimal dimensions, 0.500 becomes .500. If you suppress trailing zeros, 0.500 becomes 0.5.
You can suppress *both* leading and trailing zeros so that 0.5000 becomes .5 and 0.0000 becomes 0.

For dimension distances less than one unit, you can set the dimension distance to display in sub units. If the distance is
shown in *m*, you can set to display distances less than one *m* in *cm* or *mm*.

The table shows the effect of selecting each option and provides examples of the architectural units style. If feet are included
with a fractional inch, the number of inches is indicated as zero, no matter which option you select. Thus, the dimension
4'-3/4" becomes 4'-0 3/4".

| Zero suppression for feet and inches | | | | | |
| Option | Effect | Examples | | | |
| No options selected | Includes zero feet and zero inches | 0'-0 1/2" | 0'-6" | 1'-0" | 1'-0 3/4" |
| 0 Inches selected | Suppresses zero inches (includes zero feet) | 0'-0 1/2" | 0'-6" | 1' | 1'-0 3/4" |
| 0 Feet selected | Suppresses zero feet (includes zero inches) | 1/2" | 6" | 1'-0" | 1'-0 3/4" |
| 0 Feet and 0 Inches selected | Suppresses zero feet and zero inches | 1/2" | 6" | 1' | 1'-0 3/4" |

#### Related Tasks

* [To Suppress Zeros in Dimension Values](To-Suppress-Zeros-in-Dimension-Values.md)

#### Related Concepts

* [About Rounding Off Dimension Values](About-Rounding-Off-Dimension-Values.md)
* [About Controlling the Display of Dimension Units](About-Controlling-the-Display-of-Dimension-Units.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*