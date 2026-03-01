# MLEADERSCALE (System Variable)

Sets the overall scale factor applied to multileader objects.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 1.0000 |

Use DIMSCALE to scale leader objects created with the LEADER command.

| Value | Description |
| 0.0 | A reasonable default value is computed based on the scaling between the current model space viewport and paper space. If you are in paper space or model space and not using the paper space feature, the scale factor is 1.0. |
| >0 | A scale factor is computed that leads text sizes, arrowhead sizes, and other scaled distances to plot at their face values. |

MLEADERSCALE does not affect measured lengths, coordinates, or angles.

When MLEADERSCALE is set to 0, and the current multileader style is not annotative, the overall multileader scale of multileader
objects created in paper space viewports is determined by the viewport scale. When the current multileader style is annotative,
the MLEADERSCALE value is set to 0. Changes to the MLEADERSCALE value are ignored and the value is reset to 0.

#### Related Concepts

* [About Creating Leaders](About-Creating-Leaders.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*