# About Reducing Save Time

An incremental saving updates only those portions of an already-saved drawing file that you've changed.

When you use incremental saves, drawing files will contain a percentage of potentially wasted space. This percentage increases
after each incremental save until it reaches a specified maximum, at which time a full save is performed instead.

To reduce the size of drawing files, it is recommended that you perform a full save (with ISAVEPERCENT set to 0) before transmitting
or archiving a drawing.

When 50 is entered, the estimate of wasted space within the file does not exceed 50 percent of the total file size. Wasted
space is eliminated by periodic full saves. When the estimate exceeds 50 percent, the next save will be a full save. This
resets the wasted space estimate to 0. If ISAVEPERCENT is set to 0, every save is a full save.

#### Related Information

* [To Reduce Save Time](To-Reduce-Save-Time.md)
* [About Saving Drawings](About-Saving-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*