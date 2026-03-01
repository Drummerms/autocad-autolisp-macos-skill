# About Action Expressions (DCL)

An action expression can access the variables that indicate which tile was selected, and describe the tile's state at the
time of the action.

The variable names are reserved, and their values are read-only and have no meaning except when they are accessed within an
action expression.

| Action expression variables | |
| Variable | Description |
| $key | The key attribute of the tile that was selected.  This variable applies to all actions. |
| $value | The string form of the current value of the tile, such as the string from an edit box, or a "1" or "0" from a toggle.  This variable applies to all actions.  If the tile is a list box (or pop-up list) and no item is selected, the $value variable will be nil. |
| $data | The application-managed data (if any) that was set just after new\_dialog time by means of client\_data\_tile.  This variable applies to all actions, but $data has no meaning unless your application has already initialized it by calling client\_data\_tile. |
| $reason | The reason code that indicates which user action triggered the action. Used with edit\_box, list\_box, image\_button, and slider tiles.  This variable indicates why the action occurred. Its value is set for any kind of action, but you need to inspect it only when the action is associated with an edit\_box, list\_box, image\_button, or slider tile. |

If
edit1 is a text box, the action expression in the following
action\_tile call is evaluated when the user exits the text box:

```
(action_tile "edit1" "(setq ns $value)")
```

The
$value contains the string that the user entered, and the expression saves this in the
ns variable.

The next example saves the name of the selected tile so that the program can refer to it:

```
(action_tile "edit1" "(setq newtile $key)")
```

The
newtile variable is set to the key name of the selected tile, in this case
"edit1". The
$key variable is very useful within a function that serves as the action for several separate tiles. When a tile is named in more
than one
action\_tile call, only the last such call (prior to
start\_dialog) has any effect. (It's as if you were to assign multiple values to the same variable.) The programmable dialog box (PDB)
feature allows only one action per tile.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [About Application-Specific Data (DCL)](About-Application-Specific-Data-DCL.md)
* [About Changing Modes and Values at Callback Time (DCL)](About-Changing-Modes-and-Values-at-Callback-Time-DCL.md)
* [About Default and DCL Actions (DCL)](About-Default-and-DCL-Actions-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*