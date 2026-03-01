# About Changing the Temporary Xref File Path

When you turn on demand loading with copy, you can control where copies of externally referenced drawings are placed.

When you turn on demand loading with copy, the XLOADPATH system variable can be used to indicate the path where copies of
externally referenced drawings are to be placed. The path you specify remains in effect for all drawing sessions until you
indicate a different path. If no value for XLOADPATH is specified, the temporary file copies are placed in the standard folder
for temporary files.

If you find that referencing drawings over a network is slow, it is recommended that you set XLOADPATH to reference a local
folder, and set XLOADCTL to 2 so that the externally referenced files are demand loaded from your local machine. Conversely,
to minimize the number of temporary files created by multiple users referencing the same drawing, those users can set XLOADPATH
to point to a common folder. In this manner, multiple sessions of the program can share the same temporary copies of reference
drawings.

You can set XLOADPATH in the Application Preferences dialog box, Application tab, Temporary External References File Location
and indicate the path where copies of externally referenced files are to be placed.

#### Related Tasks

* [To Work With Xref Paths](To-Work-With-Xref-Paths.md)

#### Related Concepts

* [About Improving Performance When Using Xrefs](About-Improving-Performance-When-Using-Xrefs.md)

#### Related Information

* [To Set the File Path for Xref Copies](To-Set-the-File-Path-for-Xref-Copies.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*