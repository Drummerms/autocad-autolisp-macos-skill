# About Controlling the Display of Menu Items

The way a menu item is displayed indicates its availability in the program.

A menu item can be displayed as:

* Grayed out (disabled)
* Marked with a check mark
* Both grayed out and marked

## Gray Out (Disable) Menu Items

You can gray out a menu item by doing one of the following:

* Beginning a name with a tilde (~)
* Using a DIESEL string expression

When grayed out, the macro and submenus associated with the menu item are made inaccessible.

The following example disables the Copy Link menu item by adding a tilde (~) to the front of the value in the Name property.

![](../images/GUID-4FA7A027-A1AB-4751-834F-0E062033FBF6-low.png)

The following is the result of adding a tilde (~) to the Name property for the Copy Link menu item that appears on the Edit
menu.

![](../images/GUID-FFDCE441-F0E1-4C5E-80D4-C80BBF7B970C-low.png)

DIESEL string expressions can be used to conditionally disable or enable a menu item each time they are displayed. For example,
the DIESEL string expression in the Macros property of the Properties pane disables the MOVE command while another command
is active.

```
$(if,$(getvar,cmdactive),~)MOVE^C^C_move
```

The AutoLISP
menucmd function can also be used to disable and enable items from a macro or AutoLISP application.

## Mark Menu Items

You can mark a menu item by doing one of the following:

* Beginning a menu item name with an exclamation point followed by a period (!.)
* Using a DIESEL string expression

A menu item is marked in one of two ways:

* *A check mark.* Displayed when a menu item does not have an image associated with it.
* *A border.* Displayed when a menu item has an image associated with it; a border is displayed around the image.

The following example shows the OLE Links menu item on the Edit menu marked with a check mark and the Copy Link menu item's
image highlighted with a border around it.

![](../images/GUID-FBA030F6-1E11-44B2-8973-03EF7EFEC1E3-low.png)

DIESEL string expressions can be used to conditionally mark a menu item each time it is displayed. The following DIESEL string
examples, when added to the Macros property of the Properties pane, place a check mark to the left of the menu item when the
related system variable is enabled.

```
$(if,$(getvar,orthomode),!.)Ortho^O
$(if,$(getvar,snapmode),!.)Snap^B
$(if,$(getvar,gridmode),!.)Grid^G
```

## Simultaneously Disable and Mark Menu Items

You can mark and disable a menu item at the same time using either of the following formats:

```
~!.labeltext
!.~labeltext
```

The tilde (~) and exclamation point followed by a period (!.) are placed at the beginning of the Copy Link command label in the Name property of the Properties pane. The following is
the result of the Copy Link marked and grayed out in the Edit menu.

![](../images/GUID-783A0AA6-A65A-4121-9599-A96219B279A7-low.png)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Creating and Managing Pull-down Menus](About-Creating-and-Managing-Pull-down-Menus.md)
* [About Command Macro Strings](About-Command-Macro-Strings.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*