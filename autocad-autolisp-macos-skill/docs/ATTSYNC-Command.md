# ATTSYNC (Command)

Applies attribute changes in a block definition to all block references.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Synchronize Attributes.
![](../images/GUID-8D538B40-498B-441F-840B-D4D314A7F177-low.png)

Use this command to update instances of blocks containing attributes that were redefined using the BLOCK or BEDIT commands.
ATTSYNC does not change any values assigned to attributes in existing blocks.

NOTE: ATTSYNC removes any format or property changes made with the ATTEDIT or EATTEDIT commands. It also deletes any extended data
associated with the block, and might affect dynamic blocks and blocks created by third-party applications.

The following prompts are displayed.

?
:   Lists all block definitions in the drawing that contain attributes.

Name
:   Enter the name of the block whose attributes you want to update.

Select
:   Specify a block for update by selecting a block reference in the drawing area.

ATTSYNC <block\_name>?
:   Specify whether to continue (Yes) or cancel (No) the attribute update.

#### Related Concepts

* [About Modifying Block Attribute Definitions](About-Modifying-Block-Attribute-Definitions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*