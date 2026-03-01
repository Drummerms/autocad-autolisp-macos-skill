# IMAGEASYNCWAIT (Command)

Ensures that raster images being loaded in the background during file opening are complete before proceeding.

For scripts and AutoLISP programs that require all raster images to be fully loaded before proceeding, you should ensure
that this command is called at the beginning of the script or AutoLISP program that might call one or more of the affected
commands.

Commands that are affected by raster images being loaded in the background include:

* 3DDWF
* 3DDWFPUBLISH
* AUTOPUBLISH
* BMPOUT
* DXFOUT
* -EXPORT
* EXPORT
* EXPORTDWF
* EXPORTDWFX
* EXPORTPDF
* JPGOUT
* PNGOUT
* PLOT
* PSOUT
* PUBLISH
* +PUBLISH
* -PUBLISH
* SAVE
* SAVEAS
* TIFOUT
* WMFOUT
* QSAVE

#### Related Information

* [About Raster Images in Drawings](About-Raster-Images-in-Drawings.md)
* [About Opening Drawings](About-Opening-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*