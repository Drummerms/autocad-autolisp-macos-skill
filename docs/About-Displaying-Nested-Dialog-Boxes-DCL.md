# About Displaying Nested Dialog Boxes (DCL)

You create and manage nested dialog boxes by calling
new\_dialog and
start\_dialog from within an action expression or callback function.

For example, by including the following statement, a function can display the “Hello, world” box when the user chooses the
button called
button\_1:

```
(action_tile "button_1" "(c:hello)")
```

The user must exit the nested dialog box before using the previous dialog box again. A limit of no more than eight nested
dialog boxes, but to avoid confusion it is recommended you nest dialog boxes no deeper than four levels.

IMPORTANT:If you display nested dialog boxes by multiple
new\_dialog calls, be careful to balance each
new\_dialog call with a corresponding
done\_dialog call (whether called from a callback or not). Otherwise, your application may fail.

The
term\_dialog function terminates all current dialog boxes as if the user had canceled each of them. You can use this function if you need
to cancel a series of nested dialog boxes.

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)
* [About Functions Restricted When a Dialog Box is Open (DCL)](About-Functions-Restricted-When-a-Dialog-Box-is-Open-DCL.md)
* [About Nested Dialog Boxes (DCL)](About-Nested-Dialog-Boxes-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*