# DIMSCALE (System Variable)

Sets the overall scale factor applied to dimensioning variables that specify sizes, distances, or offsets.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 1.0000 |

Also affects the leader objects with the LEADER command.

Use [MLEADERSCALE](MLEADERSCALE-System-Variable.md) to scale multileader objects created with the [MLEADER](MLEADER-Command.md) command.

| 0.0 | A reasonable default value is computed based on the scaling between the current model space viewport and paper space. If you are in paper space or model space and not using the paper space feature, the scale factor is 1.0. |
| >0 | A scale factor is computed that leads text sizes, arrowhead sizes, and other scaled distances to plot at their face values. |

DIMSCALE does not affect measured lengths, coordinates, or angles.

Use DIMSCALE to control the overall scale of dimensions. However, if the current dimension style is annotative, DIMSCALE is
automatically set to zero and the dimension scale is controlled by the [CANNOSCALE](CANNOSCALE-System-Variable.md) system variable. DIMSCALE cannot be set to a non-zero value when using annotative dimensions.

#### Related Concepts

* [About Setting the Scale for Dimensions](About-Setting-the-Scale-for-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*