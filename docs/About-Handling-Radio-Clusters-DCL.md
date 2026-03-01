# About Handling Radio Clusters (DCL)

Radio buttons appear in radio clusters and allow the user to make a single choice from multiple options.

The value of each radio button is either "1" for On or "0" for Off. The value of the radio cluster is the key attribute of
the currently selected button. The PDB feature manages the values of radio buttons in a cluster and ensures that only one
button is turned on at a time. You can assign an action to each radio button, but it is more convenient to assign an action
to the radio cluster as a whole and then test the cluster's value to see which radio button was chosen.

Consider the following example, a radio cluster controls the view of a three-dimensional object that is displayed after a
user exits a dialog box. This cluster contains four radio buttons:

```
(action_tile "view_sel" "(pick_view $value)")
...
(defun pick_view (which)
  (cond
    ((= which "front") (setq show_which 0))
    ((= which "top") (setq show_which 1))
    ((= which "left") (setq show_which 2))
    ((= which "right") (setq show_which 3))
  )
)
```

These examples show each radio button associated with a single variable that takes multiple values. These variables may also
cause additional actions, such as disabling selections in your dialog box. If the radio cluster is large, you can store the
associated values in a table. If you use a table, structure it so it doesn't depend on the order of the buttons within the
cluster. The PDB feature does not impose this restriction, and the order can change if the DCL definition changes.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Initializing Modes and Values (DCL)](About-Initializing-Modes-and-Values-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [radio\_button Tile (DCL)](radio_button-Tile-DCL.md)
* [radio\_column Tile (DCL)](radio_column-Tile-DCL.md)
* [radio\_row Tile (DCL)](radio_row-Tile-DCL.md)
* [boxed\_radio\_column Tile (DCL)](boxed_radio_column-Tile-DCL.md)
* [boxed\_radio\_row Tile (DCL)](boxed_radio_row-Tile-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*