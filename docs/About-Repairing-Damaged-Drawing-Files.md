# About Repairing Damaged Drawing Files

If a drawing file is damaged, you can recover some or all of the data by using commands to find and correct errors.

## Repair and Recovery

When an error occurs, diagnostic information is recorded in the *acad.err* file, or*acadlt.err* file for AutoCAD LT, which you can use to report a problem.

A drawing file is marked as damaged if corrupted data is detected, or if you request that the drawing be saved after a program
failure. If the damage is minor, sometimes you can repair the drawing simply by opening it. A recovery notification is displayed
while opening drawing files that are damaged and need recovery. You can

* RECOVER Performs an audit on, and attempts to open, any drawing file.
* RECOVERALL Similar to recover, it additionally operates on all nested xrefs. The results are displayed in the Drawing Recovery
  Log window. (Not available in AutoCAD for Mac.)
* AUDIT Finds and corrects errors in the current drawing.
* RECOVERAUTO Controls the display of recovery notifications before or after opening a damaged drawing file.

## Example: Auditing Files

Auditing a file generates a description of problems with a drawing file and recommendations for correcting them. As you start
the audit, you specify whether you want the program to try to fix the problems it encounters. The report is similar to the
following example:

Auditing Header

DXF NAME Current Value Validation Default

PDMODE 990 - 2040

UCSFOLLOW 811 or 0

Error found in auditing header variables

4 Blocks audited

Pass 1 4 objects audited

Pass 2 4 objects audited

Total errors found 2 fixed 2

If you chose not to correct the errors, the last statement changes to

Total errors found 2 fixed 0.

The output from a recovery audit is written to an audit log (ADT) file if the AUDITCTL system variable is set to 1 (On).

Recovery does not necessarily preserve the high-level consistency of the drawing file. The program extracts as much material
as it can from the damaged file.

#### Related Tasks

* [To Repair a Damaged Drawing File](To-Repair-a-Damaged-Drawing-File.md)
* [To Repair an Open Drawing](To-Repair-an-Open-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*