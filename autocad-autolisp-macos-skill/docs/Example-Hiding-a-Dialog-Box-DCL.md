# Example: Hiding a Dialog Box (DCL)

This example demonstrates how to create a simple dialog box that allows the user to click a button and then pick a point
in the graphics screen.

![](../images/GUID-C817A8B6-D51C-4943-BB41-D2B8B075AD8B-low.png)

The dialog box is defined with the following DCL:

```
hidedcl : dialog
{
  label="Hide Example";
  : column
  {
    : text
    {
      key="message";
      label="Click PickMe to pick a point";
      fixed_width=true;
      fixed_height=true;
      alignment=centered;
    }
    :row
    {
      ok_only;
      :retirement_button
      {
        label = "PickMe";
        key = "hide";
        mnemonic = "H";
      }
    }
  }
}
```

The dialog box definition defines two buttons that the user can click. Clicking OK closes the window, while clicking PickMe
executes code that hides the dialog box and prompts the user to specify a point. The following AutoLISP code displays the
dialog box and defines the behavior of the two button tiles:

```
(defun c:hidedcl (/ dcl_id what_next cnt)
  (setq dcl_id (load_dialog "hidedcl.dcl"))  ; Load the dialog box.
  (setq what_next 2)
  (setq cnt 1)
  (while (>= what_next 2)                    ; Begin display loop.
    (if (null (new_dialog "hidedcl" dcl_id)) ; Initialize dialog
      (exit)                                 ; box, exit if nil
    ) ; endif                                ; returned.

    ; Set action to take if a button is pressed. Either button
    ; results in a done_dialog call to close the dialog box.
    ; Each button associates a specific status code with
    ; done_dialog, and this status code is returned by
    ; start_dialog.
    (action_tile "accept" "(done_dialog 1)") ; Set action for OK.
    (action_tile "hide" "(done_dialog 4)")   ; Set action for PickMe.
    (setq what_next (start_dialog))          ; Display dialog box.

    (cond
      ((= what_next 4)                       ; Prompt user to
        (getpoint "\
pick a point")          ; pick pt.
      )
      ((= what_next 0)
        (prompt "\
user cancelled dialog")
      )
    )
  )
  (unload_dialog dcl_id)
 (princ)
)
```

NOTE:The
term\_dialog function terminates all dialog boxes at once but does not return a status code, so there is no way for an application to
distinguish between hiding a nested box and canceling boxes due to an error condition.

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Displaying Nested Dialog Boxes (DCL)](About-Displaying-Nested-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Functions for Hiding Dialog Boxes (DCL)](About-Functions-for-Hiding-Dialog-Boxes-DCL.md)
* [About Functions Restricted When a Dialog Box is Open (DCL)](About-Functions-Restricted-When-a-Dialog-Box-is-Open-DCL.md)
* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*