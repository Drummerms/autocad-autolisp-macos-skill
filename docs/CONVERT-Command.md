# CONVERT (Command)

Optimizes 2D polylines and associative hatches created in AutoCAD Release 13 or earlier.

## Summary

Hatches are not updated automatically when a drawing from a previous release is opened in Release 14 or later. Information
about the rotation of a hatch pattern may not be updated properly if you have changed the UCS since creating the hatch. When
updating hatches with CONVERT, it is recommended that you use the Select option so that you can check your results.

In most cases, you do not need to update polylines with CONVERT. By default, the
 [PLINETYPE](PLINETYPE-System-Variable.md) system variable specifies that polylines are updated automatically when you open an older drawing. Polylines may be created
in the old format by third-party applications, and they may be contained in an older drawing that was inserted as a block
and then exploded.

NOTE:Polylines containing curve-fit or splined segments always retain the old format, as do polylines that store extended object
data on their vertices. Editing commands make no distinction between the two formats.

## List of Prompts

The following prompts are displayed.

Enter type of objects to convert [[Hatch](CONVERT-Command.md)/[Polyline](CONVERT-Command.md)/[All](CONVERT-Command.md)] <All>:
*Enter**h* *for hatches,**p* *for polylines, or**a* *for both*

Hatch
:   Converts all hatches in the drawing.

Polyline
:   Converts all polylines in the drawing.

All
:   Converts all polylines and hatches in the drawing.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*