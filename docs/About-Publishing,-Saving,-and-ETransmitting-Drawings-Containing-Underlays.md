# About Publishing, Saving, and ETransmitting Drawings Containing Underlays

When you eTransmit a file, DWF, DWFx, PDF, and DGN underlays are tracked and managed.

## Plot and Publish

When a drawing file containing an underlay is plotted or published to a new file, any visible geometry is included in the
newly plotted or published file. However, none of the layer data from the original DWF, DWFx, PDF, or DGN attachment gets
published with the new file.

## Save to a Previous DWG Format

If you save a drawing that contains underlays to a previous DWG format, note the following exceptions:

* DWF underlays do not display and are not replaced by a proxy object in releases earlier than AutoCAD 2007.
* DWFx underlays do not display and are not replaced by a proxy object in releases earlier than AutoCAD 2008.
* PDF underlays are not supported in releases earlier than AutoCAD 2010 (unless you have a Bonus Pack installed).
* DGN underlays are only supported in AutoCAD 2008 or later. They will not display in earlier versions of AutoCAD. Also, if
  you save a drawing in AutoCAD 2009, AutoCAD 2008 will only recognize the underlay if it is a V8 MicroStation file.

## eTransmit

Underlay attachments are tracked and managed when you use eTransmit in the same way you track and manage raster image attachments.

#### Related Information

* [About Underlays](About-Underlays.md)
* [To Change the Underlay Path](To-Change-the-Underlay-Path.md)
* [View PDF Underlay Information](View-PDF-Underlay-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*