# About Callback Reasons (DCL)

The callback reason, returned in the
$reason variable, specifies why the action occurred.

The variable’s value is set for any kind of action, but you need to inspect it only when the action is associated with an
edit\_box,
list\_box,
image\_button, or
slider tile. The following outlines the values of each callback reason code:

Code 1
:   This is the value for most action tiles. The user has selected the tile (possibly by pressing Enter, if the tile is the default
    and the platform recognizes accelerator keys).

Code 2 – Edit Boxes
:   The user has exited the edit box—by pressing the Tab key or by choosing a different tile—but has not made a final selection.
    If this is the reason for an edit box callback, your application should not update the value of the associated variable, but
    should check the validity of the value in the edit box.

Code 3 – Sliders
:   The user has changed the value of the slider by dragging the indicator (or an equivalent action), but has not made a final
    selection. If this is the reason for a slider callback, your application should not update the value of the associated variable
    but should update the text that displays the slider's status.

Code 4 – List Boxes and Image Buttons
:   This callback reason always follows a code 1. It usually means “commit to the previous selection.” It should never undo the
    previous selection; this confuses and annoys the user.

    * *List boxes:* The user has double-clicked on the list box. You can define the meaning of a double-click in your application. If the main
      purpose of the dialog box is to select a list item, a double-click should make a selection and then exit the dialog box. (In
      this case, the
      is\_default attribute of the
      list\_box tile should be
      true.) If the list box is not the primary tile in the dialog box, then a double-click should be treated as equivalent to making
      a selection (code 1).

      List boxes that allow the user to select multiple items (multiple\_select = true) cannot support double-clicking.
    * *Image buttons:* The user has double-clicked on the image button. You can define the meaning of a double-click in your application. In many
      cases it is appropriate for a single-click to select the button, but in others it is better for a single-click (or a keyboard
      action) to highlight the button, and then have the Enter key or a double-click select it.

#### Topics in this section

* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)

  The
  action\_tile function is not the only way to specify an action.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Action Expressions (DCL)](About-Action-Expressions-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)
* [About Handling Edit Boxes (DCL)](About-Handling-Edit-Boxes-DCL.md)
* [About Handling Image Buttons and Tiles (DCL)](About-Handling-Image-Buttons-and-Tiles-DCL.md)
* [About Handling Sliders (DCL)](About-Handling-Sliders-DCL.md)
* [About Processing List Elements (DCL)](About-Processing-List-Elements-DCL.md)
* [About List Operations for List Boxes and Pop-Up Lists (DCL)](About-List-Operations-for-List-Boxes-and-Pop-Up-Lists-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*