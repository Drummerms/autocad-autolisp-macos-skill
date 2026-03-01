# About Handling Edit Boxes (DCL)

Actions and callbacks to handle edit boxes allow you to get the current value and know when focus is lost.

However, because characters in edit boxes are already visible, there is no need for action on interim results. Edit boxes
only return a callback code when the focus to that tile is lost. The following code example checks the value but does not
redisplay it:

```
(action_tile "myeditbox" "(edit_action $value $reason)")
  .
  .
  .
(defun edit_action (val why)
  (if (or (= why 2) (= why 4))
    . ; Do range checking on
    . ; transient value here.
    .
  )
)
```

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [Example: Requesting a Password (DCL)](Example-Requesting-a-Password-DCL.md)
* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*