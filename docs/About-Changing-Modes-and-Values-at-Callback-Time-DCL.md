# About Changing Modes and Values at Callback Time (DCL)

At callback time, you can check the value of a tile. If necessary, you can use
set\_tile again to modify this value.

During callbacks, you can also use
mode\_tile to change the status of a tile. The following table shows the values of the
mode\_tile *mode* argument:

| Mode codes for mode\_tile | |
| Value | Description |
| 0 | Enable tile |
| 1 | Disable tile |
| 2 | Set focus to tile |
| 3 | Select edit box contents |
| 4 | Flip image highlighting on or off |

When you use
mode\_tile to disable a tile that has the current focus, you must call
mode\_tile again to set the focus to a different tile (in most cases, the next tab stop in the dialog box). Otherwise, the focus will
remain on a disabled tile, which is illogical and can cause errors.

A good example of a tile disabling itself is a series of dialog box pages that the user steps through by choosing a Next or
Previous button. When the user chooses Next on the next-to-last page, the button is disabled. The same thing happens after
choosing Previous on the second page. In both cases, the code must disable the button that was chosen, and then set focus
to a different tile.

Suppose the tile called
group\_on is a toggle that controls a cluster called
group. When the toggle is turned off, the tiles in the cluster are inactive and should not be modified. In this case, you might
define the following action for the toggle. (Notice the use of the
 *\"*  control character, which allows quotation marks within an
action\_tile argument.)

```
(action_tile "group_on" "(mode_tile \"group\" (- 1 (atoi $value)))")
```

The
subtraction ( *-* )and
atoi call in the action expression set the
mode\_tile function's
*mode* argument. Because a toggle is 0 when it is turned off and 1 when it is turned on, the subtraction inverts its value and the
mode controls whether the cluster is enabled. You can inspect attributes other than a tile's
*value* with the
get\_attr function. For example, you may want to retrieve the label of a button called "pressme":

```
(get_attr "pressme" "label")
```

The
get\_attr function returns the value of the specified attribute as a string.

NOTE:If you use
get\_attr to retrieve a
value attribute, it gets the
value attribute saved in the DCL file (the initial value of the tile). The
get\_tile function, however, gets the current runtime value of the tile. The two values are not necessarily the same.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Callback Reasons (DCL)](About-Callback-Reasons-DCL.md)
* [About Action Expressions (DCL)](About-Action-Expressions-DCL.md)
* [About Action Expressions and Callbacks (DCL)](About-Action-Expressions-and-Callbacks-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*