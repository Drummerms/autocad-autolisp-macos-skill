# HPCOLOR (System Variable)

Sets the default color for new hatches in the current drawing.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | use current |

Valid values include the following:

* "." to use the current color set in the CECOLOR system variable
* ByLayer or ByBlock
* AutoCAD Color Index (ACI): integer values from 1 to 255, or a color name from the first seven colors
* True Colors: RGB or HSL values from 000 to 255 in the form "RGB:130,200,240"
* Color Books: Text from standard color books, guides, or sets, for example "DIC COLOR GUIDE(R)$DIC 43"

Values other than the "." (use current) value override the current color (CECOLOR).

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*