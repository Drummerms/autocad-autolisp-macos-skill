# About Alert Boxes (DCL)

A standard alert box with a single OK button can be displayed by calling the
alert function.

Alert boxes should be displayed for serious or potentially fatal errors, but do not overuse them. Alert boxes require user
input. Therefore, they can be annoying, especially when they report minor errors or obscure the entry that needs to be corrected.
The standard alert box works well for providing information to the user, but does not give the user a choice to proceed or
cancel the action. If you want to display an alert box that offers the user a choice, such as Proceed or Cancel, you must
construct it yourself.

An alert box that provides the user with a choice should first describe the problem and then pose the next action as a question.
In such cases, it is important that the button for proceeding be labeled with a verb that describes the action that will be
taken. For example, if you want to provide the user with a choice to overwrite a file, you might want to label the button
Overwrite instead of using the less ambiguous label of OK. Using specific verbs aids users in identifying which specific actions
are available from the alert box.

Unless an error is truly fatal, you should provide a way to return to a previous step or escape from the operation that triggered
the alert box.

The default button for a dialog box should be OK or its equivalent, but if the situation described by the alert box has serious
consequences, make Cancel or its equivalent the default.

#### Related Concepts

* [About Customizing Exit Buttons (DCL)](About-Customizing-Exit-Buttons-DCL.md)
* [About Error Handling in Dialog Boxes (DCL)](About-Error-Handling-in-Dialog-Boxes-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*