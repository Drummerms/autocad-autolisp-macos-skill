# action\_tile (AutoLISP/DCL)

Assigns an action to evaluate when the user selects the specified tile in a dialog box

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(action_tile key action-expression)
```

*key*
:   *Type:* String

    Names the tile that triggers the action (specified as its
    key attribute). This argument is case-sensitive.

*action-expression*
:   *Type:* String

    Expression evaluated when the tile is selected.

## Return Values

*Type:* T or nil

T if the key was found; otherwise it returns
nil.

## Remarks

The action assigned by
action\_tile supersedes the dialog box's default action (assigned by
new\_dialog) or the tile's
action attribute, if these are specified. The expression can refer to the tile's current value as
$value, its name as
$key, its application-specific data (as set by
client\_data\_tile) as
$data, its callback reason as
$reason, and its image coordinates (if the tile is an image button) as
$x and
$y.

NOTE:You cannot call the AutoLISP
command function from the
action\_tile function.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

If
edit1 is a text box, the action expression in the following
action\_tile call is evaluated when the user exits the text box:

```
(action_tile "edit1" "(setq ns $value)")
```

#### Related References

* [get\_attr (AutoLISP/DCL)](get_attr-AutoLISP-DCL.md)
* [get\_tile (AutoLISP/DCL)](get_tile-AutoLISP-DCL.md)
* [mode\_tile (AutoLISP/DCL)](mode_tile-AutoLISP-DCL.md)
* [set\_tile (AutoLISP/DCL)](set_tile-AutoLISP-DCL.md)

#### Related Concepts

* [Tile- and Attribute-Handling Functions Reference (AutoLISP/DCL)](Tile-and-Attribute-Handling-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*