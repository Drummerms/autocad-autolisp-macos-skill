# COORDS (System Variable)

Controls the format and update frequency of coordinates on the status line.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| 0 | The absolute coordinates of your pointing device is updated only when you specify points |
| 1 | The absolute coordinates of your pointing device is updated continuously |
| 2 | The absolute coordinates of your pointing device is updated continuously except when a point, distance, or angle is requested. In that case, relative polar coordinates are displayed instead of *X* and *Y*. The *Z* values always display as absolute coordinates. |
| 3 | The absolute coordinates (WCS) of your pointing device is updated continuously with the latitude and longitude coordinate values of the geographic location. |

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*