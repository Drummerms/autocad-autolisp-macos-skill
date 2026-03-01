# INTELLIGENTUPDATE (System Variable)

Controls the graphics refresh rate.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 20 |

The default value is 20 frames per second. If you encounter problems related to graphics generation or timing, turn off the
variable by setting it to 0. INTELLIGENTUPDATE works by suppressing the graphics update until the timer expires. Subsequent
updates reset the timer.

The performance improvement significantly affects updates for scripts and AutoLISP graphics. Those using regular AutoCAD commands
will not see a noticeable difference in performance.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*