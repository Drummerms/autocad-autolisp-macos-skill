# About Functions Restricted When a Dialog Box is Open (DCL)

While a dialog box is active—that is, during the
start\_dialog call—you cannot call any function that requires user input on the AutoCAD command line, or affects the display outside the
dialog box (for example, in the graphics window). This restriction includes functions that write text, such as
print,
princ, and
prin1.

You can issue
ssget calls, as long as you do not use any options that require user input. If your program calls one of the restricted functions
between the
start\_dialog and
done\_dialog calls, AutoCAD terminates all dialog boxes and displays the following error message:

AutoCAD rejected function

You can test the CMDACTIVE system variable to determine if a dialog box is active. If CMDACTIVE is greater than 7, a dialog
box is active. The CMDACTIVE system variable has bit-coded values that indicate command, script, and dialog box activity.

NOTE:If your application requires users to enter input based on the graphics screen rather than on the dialog box itself (for example,
to specify a point or select an object), you must hide the dialog box. That is, you must call
done\_dialog so the graphics screen is visible again, and then restart the dialog box after the user has made the selection.

The
term\_dialog function terminates all current dialog boxes as if the user had canceled each of them. This function can be used to cancel
a series of nested dialog boxes.

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Displaying Nested Dialog Boxes (DCL)](About-Displaying-Nested-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*