# About Management of Extended Data Memory Use (AutoLISP)

Extended data is limited to 16K per entity.

Because the xdata of an entity can be created and maintained by multiple applications, problems can result when the size of
the xdata approaches its limit. The following functions can be used to help manage the memory that xdata occupies.

* xdsize - Returns the amount of memory (in bytes) that the xdata in a list occupies.
* xdroom - Returns the remaining number of free bytes that can still be appended to the entity.

The xdsize function can be slow when reading a large extended data list, so it is not recommended that you call it frequently. A better
approach is to use it (in conjunction with xdroom) in an error handler. If a call to entmod fails, you can use xdsize and xdroom to find out whether the call failed because the entity did not have enough room for the xdata.

#### Related Concepts

* [About Extended Data - Xdata (AutoLISP)](About-Extended-Data-Xdata-AutoLISP.md)
* [About Attaching Extended Data to an Entity (AutoLISP)](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)
* [About Extended Data Group Codes (AutoLISP)](About-Extended-Data-Group-Codes-AutoLISP.md)
* [About Retrieving Extended Data (AutoLISP)](About-Retrieving-Extended-Data-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Registered Applications (AutoLISP)](About-Registered-Applications-AutoLISP.md)
* [Extended Data-Handling Functions Reference (AutoLISP)](Extended-Data-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*