# About Functions for Hiding Dialog Boxes (DCL)

A user cannot interact with the graphics screen while a dialog box is active.

If you want to allow a user to select an object or pick a point from the graphics screen before a dialog box has been closed,
you must close the dialog box momentarily so that the user can interact with the screen and perform the action. This is known
as hiding a dialog box. Once the action is complete, you need to restore the dialog box.

Hiding a dialog box is the same as ending it with
done\_dialog, except your callback function must use the
done\_dialog *status* argument to indicate that the dialog box is hidden—as opposed to ended or canceled. Set
*status* to an application-defined value. The
start\_dialog function returns the application-defined
*status* when the dialog box disappears. Your program must then examine the
*status* returned by
start\_dialog and determine what to do next.

When the action of a button tile causes a dialog box to be hidden, you should not contain an ellipsis or series of three dots.
Instead, use a space followed by a less-than symbol ( *<* ) in the label. When the dialog box hides itself, a prompt should be displayed that explains what the user is expected to
do. In most cases, you will use one of the
getXXX functions to request the desired input from the user. These functions have an argument with which you can specify a prompt.

After the user provides a valid response to the requested input, the dialog box should reappear and provide feedback to the
user that they were successful in providing input. This feedback could be new information in an edit box, an updated list
box, a text message that indicates the status, or a combination of these.

#### Topics in this section

* [Example: Hiding a Dialog Box (DCL)](Example-Hiding-a-Dialog-Box-DCL.md)

  This example demonstrates how to create a simple dialog box that allows the user to click a button and then pick a point
  in the graphics screen.
* [Example: Requesting a Password (DCL)](Example-Requesting-a-Password-DCL.md)

  This example demonstrates how to use a simple dialog box to request a password from users.

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Displaying Nested Dialog Boxes (DCL)](About-Displaying-Nested-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Functions Restricted When a Dialog Box is Open (DCL)](About-Functions-Restricted-When-a-Dialog-Box-is-Open-DCL.md)
* [Example: Hiding a Dialog Box (DCL)](Example-Hiding-a-Dialog-Box-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*