# HPMAXAREAS (System Variable)

Sets the maximum number of "enclosed areas" that a single hatch object can have and still automatically switch between solid
and pattern hatches during zoom operations.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 100 |

Valid values are from 0 to 10,000,000.

When set to a value of 0, hatches are displayed with their assigned pattern while performing zoom operations. This provides
for the best visual fidelity, but might impact the performance of zoom operations. Hatches plot and publish as expected.

NOTE:The display of hatches in associative arrays and blocks are not affected by this system variable.

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*