# About DCL Error Handling (DCL)

The PDB feature checks a DCL file for errors the first time you load it. If a syntax error, a misuse of attributes, or any
other error is encountered (such as failure to specify a key attribute for an active tile), the PDB does not load the DCL
file.

When an error is encountered, one or more dialog boxes alerting you to the error are displayed, or a list of errors are written
to a text file named
*acad.dce*. If the error messages are written to
*acad.dce*, it alerts you to this with a message similar to the following:

![](../images/GUID-4D36B5E7-0AC0-417A-AB17-BE3A17EBA617-low.png)

You can inspect the contents of
*acad.dce* to find the problem. The
*acad.dce* file is placed in the current working directory. When a DCL file is read successfully, the
*acad.dce* file is deleted.

If your application uses multiple DCL files, the
*acad.dce* file is overwritten (or deleted if no errors occur) when each new file is loaded. When you test the program,
*acad.dce* shows errors (if any) from only the DCL file most recently read. You can also load and debug each file manually in AutoCAD
with the
load\_dialog function. The following
load\_dialog function loads the DCL file
*hellofile.dcl*:

Command:  *(load\_dialog "hellofile")*

3

If the dialog box loads successfully,
load\_dialog returns a positive integer that identifies the DCL file. You pass this value to the
new\_dialog function to initialize individual dialog boxes in the file.

The
new\_dialog function returns
T if it succeeds; otherwise it returns nil. If
new\_dialog returns
T, call the
start\_dialog function to display the dialog box.

Once you have debugged each DCL file, you can load your program and test the dialog boxes in combination. If your program
calls a restricted function between the
start\_dialog and
done\_dialog calls, AutoCAD terminates all dialog boxes and displays the following error message:

AutoCAD rejected function

#### Topics in this section

* [About Setting the Auditing Level to Affect Error Messages (DCL)](About-Setting-the-Auditing-Level-to-Affect-Error-Messages-DCL.md)

  The level of semantic auditing affects which messages are issued for a DCL file.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Semantic Auditing of DCL Files (DCL)](About-Semantic-Auditing-of-DCL-Files-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*