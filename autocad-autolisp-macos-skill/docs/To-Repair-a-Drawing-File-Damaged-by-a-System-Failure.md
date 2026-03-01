# To Repair a Drawing File Damaged by a System Failure

1. If the program encounters a problem and cannot continue, it displays an error message and, for some errors, an error code.
   Record the error code number, save changes the drawing if possible, and exit.
2. Restart the product. The Files Recovered dialog box opens up.
3. In the Files Recovered dialog box, click the drawing node to expand it, and click one of the drawing or backup files to open
   it.

   If the program detects that the drawing has been damaged, a message is displayed asking if you want to proceed.
4. Enter *y* to proceed.

   As the program attempts to repair the drawing, a diagnostic report is displayed. The output from the audit is written to an
   audit log (ADT) file if the AUDITCTL system variable is set to 1.

   NOTE:AUDITCTL is set to 0, by default.
5. Depending on whether the repair is successful, do one of the following:
   * If the repair is successful, the drawing opens. Save the drawing file.
   * If the program cannot repair the file, a message is displayed. In that case, choose one of the other drawing or backup files
     listed in the Files Recovered dialog box beginning with step 3.

#### Related Information

* [To Open the Files Recovered Dialog Box](To-Open-the-Files-Recovered-Dialog-Box.md)
* [About Recovering from a System Failure](About-Recovering-from-a-System-Failure.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*