# About Recovering from a System Failure

A hardware problem, power failure, or software problem can cause this program to terminate unexpectedly. If this happens,
you can restore the drawing files that were open.

If the program fails, you can save your current work to a different file. This file uses the format,
*DrawingFileName\_recover.dwg*, where
*DrawingFileName* is the file name of your current drawing.

After a program or system failure, the Files Recovered dialog box opens the next time you start AutoCAD.

The Files Recovered dialog box displays a list of all drawing files that were open, including the following drawing file types:

## Resolve Drawing Files

After a program or system failure, the Files Recovered dialog box opens the next time you start the application. The Files
Recovered dialog box displays a list of all drawing files that were open, including:

* Drawing files (DWG)
* Drawing template files (DWT)

NOTE: Unsaved drawings that are open at the time of an unexpected failure are not tracked by the Files Recovered dialog box. Be
sure to save your work after you begin, and regularly thereafter.

For each drawing, you can open and choose from the following files if they exist:

* *DrawingFileName*\_*a*\_*b*\_*nnnn*.sv$
* *DrawingFileName*.dwg
* *DrawingFileName*.bak

NOTE: The drawing, backup, and recover files are listed in the order they were last saved.

If you close the Files Recovered dialog box before resolving all affected drawings, you can reopen the dialog box at a later
time with the DRAWINGRECOVERY command.

## Send an Error Report Automatically to Autodesk

If the program encounters a problem and closes unexpectedly, you can send an error report to help Autodesk diagnose problems
with the software. The error report includes information about the state of your system at the time the error occurred. You
can also add other information, such as what you were doing at the time of the error. The REPORTERROR system variable controls
whether error-reporting is enabled.

#### Related Tasks

* [To Control Error Reporting](To-Control-Error-Reporting.md)

#### Related Information

* [To Open the Files Recovered Dialog Box](To-Open-the-Files-Recovered-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*