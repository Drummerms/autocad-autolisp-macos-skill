# Example: Requesting a Password (DCL)

This example demonstrates how to use a simple dialog box to request a password from users.

NOTE:The
password\_char attribute for the
edit\_box tile is supported on Windows only.

The following defines a dialog box named
passdlg, which contains two tiles: the
edit\_box tile where the user enters the password, and the
ok\_cancel tile. It uses the
password\_char DCL attribute to mask the text a user enters:

```
// GETPASS.DCL
//
passdlg : dialog
{
  label = "Password Protected";
  : edit_box
  {
    label = "Password:";
    edit_width = 20;
    key = "password";
    password_char = "?";
  }
  ok_cancel;
}
```

The following defines a function named
GETPASS. This function loads the
*getpass.dcl* file and displays the
passdlg dialog box. When a user enters text into the edit box, it is masked by the
password\_char character defined in the DCL file. The action assigned to the edit box ensures that the characters entered by the user are
set to the
pass variable:

```
;; GETPASS.LSP
;;
(defun GETPASS ( / dcl_id pass )
  (setq dcl_id (load_dialog "getpass.dcl"))
  (if (new_dialog "passdlg" dcl_id)
    (progn
      (action_tile "password" "(setq pass $value)")
      (start_dialog)
      (unload_dialog dcl_id)
    )
    (princ "Error: Unable to load GETPASS.DCL. ")
  )
  pass
)
```

The
GETPASS function returns the string entered by the user.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [About Handling Edit Boxes (DCL)](About-Handling-Edit-Boxes-DCL.md)
* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*