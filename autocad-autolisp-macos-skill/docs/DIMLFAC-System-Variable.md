# DIMLFAC (System Variable)

Sets a scale factor for linear dimension measurements.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 1.0000 |

All linear dimension distances, including radii, diameters, and coordinates, are multiplied by DIMLFAC before being converted
to dimension text. Positive values of DIMLFAC are applied to dimensions in both model space and paper space; negative values
are applied to paper space only.

DIMLFAC applies primarily to nonassociative dimensions (DIMASSOC set 0 or 1). For nonassociative dimensions in paper space,
DIMLFAC must be set individually for each layout viewport to accommodate viewport scaling.

DIMLFAC has no effect on angular dimensions, and is not applied to the values held in  [DIMRND](DIMRND-System-Variable.md),  [DIMTM](DIMTM-System-Variable.md), or  [DIMTP](DIMTP-System-Variable.md).

#### Related Concepts

* [About Setting the Scale for Dimensions](About-Setting-the-Scale-for-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*