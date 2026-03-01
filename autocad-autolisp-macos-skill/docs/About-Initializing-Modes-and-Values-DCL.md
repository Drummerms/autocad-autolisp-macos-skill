# About Initializing Modes and Values (DCL)

Tile modes and values can be initialized when a dialog box is displayed or when an action is performed.

Initializing a tile can include the following:

* Making it the initial keyboard focus of the dialog box
* Disabling or enabling it
* Highlighting its contents, if it is an edit box or image

These operations are performed by
mode\_tile calls. You can set the value of a tile by using
set\_tile.

To display a default value—such as a surname—in an edit box and set the dialog box's initial focus to that box, use the following
code:

```
(setq name_str "Kenobi")       ; Default.
(set_tile "lastname" name_str) ; Initializes field.
(mode_tile "lastname" 2)       ; 2 sets focus to tile.
```

An additional
mode\_tile call can highlight all the contents of an edit box, so the user has the option to type immediately over the default contents,
as shown in the following example:

```
(mode_tile "lastname" 3)       ; 3 selects box contents.
```

#### Related Concepts

* [Example: Quick Overview of Dialog Boxes (DCL)](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About the Function Sequence to Display and Work with a Dialog (DCL)](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*