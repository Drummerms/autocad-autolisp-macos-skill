# HPTRANSPARENCY (System Variable)

Sets the default transparency for new hatches and fills.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | use current |

Valid values include “use current” (or “.”), ByLayer, ByBlock, and integer values from 0 to 90. The higher the value, the
more transparent the hatch.

Values other than “use current” or “.” override the current transparency ([CETRANSPARENCY](CETRANSPARENCY-System-Variable.md)).

Changing this value does not affect existing hatch objects.

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*