# ISAVEPERCENT (System Variable)

Controls the amount of space allocated in DWG files for incremental saves, which affects the number of quick save operations
that can be performed before a full save is required.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 50 |

When the file save estimate exceeds the specified percentage, the next save will be a full save. Valid values can range from
0 to 100 percent.

* A value of 0 means that all save operations are full saves. A full save optimizes the size of a DWG file, but is noticeably
  slower on large drawings.
* A value of 100 increases the space available to append changes to the maximum possible. This value results in the greatest
  number of incremental quick save operations between full saves at the expense of larger file sizes.

NOTE:To optimize speed, automatic saves are incremental, temporarily overriding the value of ISAVEPERCENT with a value of 90. A
full save occurs when the number of changes exceeds the ISAVEPERCENT setting. Saving to a different format always results
in a full save.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*