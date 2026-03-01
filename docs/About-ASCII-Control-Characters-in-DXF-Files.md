# About ASCII Control Characters in DXF Files

SAVEAS handles ASCII control characters in text strings by expanding the character into a caret (^) followed by the appropriate
letter. For example, an ASCII Control-G (BEL, decimal code 7) is written as ^G. If the text itself contains a caret character,
it is expanded to caret, space (^). OPEN and INSERT perform the complementary conversion.

#### Related References

* [About Group Codes in DXF Files (DXF)](About-Group-Codes-in-DXF-Files-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*