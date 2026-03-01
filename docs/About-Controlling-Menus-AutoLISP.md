# About Controlling Menus (AutoLISP)

The
menucmd function controls the display of the menus on the menu bar, drawing area, or an image title menu.

It displays, modifies, or queries one of the submenus of the current menu, and accepts a string argument that specifies the
submenu and the action to perform on that submenu. The
menucmd function takes a string argument that consists of two fields, separated by an equal sign, in the following form:

```
(menucmd "menu_area=action")
```

The
*menu\_area* field specifies which part of the menu is to receive the action. This field can specify a menu area, such as
P0 (for the shortcut menu) or a specific menu item. The
*action* field specifies the action to perform on the menu area or menu item, or a submenu to load into the menu area. The menu areas
that can receive an action are the same as those used in customization file submenu references.

Every menu area has a currently loaded submenu. By default, the first submenu following a menu section label is loaded into
that menu area.

If
*menu\_area* specifies a pull-down menu or image tile menu,
*action* can be an asterisk ( *\** ). This causes the menu to be displayed; pull-down menus and image tile menus are not automatically displayed when they are
called.

NOTE:In Windows, only the
P0 (cursor) menu and image tile menus are displayed with the asterisk. Image tile menus are not supported on Mac OS.

The following code loads the menu with the
POP0 alias into the
P0 (cursor) menu area and displays it.

```
(menucmd "P0=POP0") ; Loads the POP0 menu into the P0 menu area
(menucmd "P0=*")    ; Display it
```

If the correct menu is loaded into a particular menu area, you do not need to load it specifically each time you want to display
it.

The following code displays the pull-down menu currently loaded in the
P1 (first pull-down menu) location.

```
(menucmd "P1=*")
```

Using
"P1=\*" without previously loading the menu can result in unexpected behavior. Although you can load virtually any menu at a pull-down
or shortcut menu location, it is best to use only menus specifically designed for that menu area. For example, if you have
a submenu called
MORESTUFF, you can load it at the
P1 location with the following code:

```
(menucmd "P1=MORESTUFF") ; Loads the MORESTUFF menu in the P1 menu location
(menucmd "P1=*")         ; Displays it
```

This menu remains in this location until you replace it by loading another menu, as in the following:

```
(menucmd "P1=POP1")
```

If your menu uses the disabling (graying-out) and marking features, you can retrieve and change the state of a menu item label
with the
menucmd function. The following call retrieves the current state of the fourth label in the pull-down menu
P2.

```
(menucmd "P2.4=#?") ; If disabled returns "P2.4=~"
```

These function calls enable and disable that same menu item label:

```
(menucmd "P2.4=")  ; Enables the label
(menucmd "P2.4=~") ; Disables the label
```

You can also place and remove marks to the left of menu item labels.

The previously described method of menu item handling works relatively well with a single static menu. However, it becomes
unreliable when menu item locations change when you load multiple partial menu files. You can make use of the menu-group and
name-tag features to keep track of menu items. Instead of specifying a menu item by its location on a menu, you specify the
menu group and name tag associated with the menu item.

When you use the menu group to enable, disable, and mark menu item labels, you must precede the group name with a
*G*, as shown in the following examples.

```
(menucmd "Gacad.ID_New=~") ; Disables the label
(menucmd "Gacad.ID_New=")  ; Enables the label
```

Not only can an AutoLISP function enable and disable menu item labels, it can also modify the text displayed in the label
by placing a DIESEL string expression in the label. Because DIESEL accepts only strings as input, you can pass information
to the DIESEL expression through a USERS1-5 system variable that has been set to a value returned by your function.

You can also use the
menucmd function to evaluate DIESEL string expressions within an AutoLISP function. The following routine returns the current time:

```
(defun C:CTIME ( / ctim)
  (setq ctim
  (menucmd "M=$(edtime,$(getvar,date),H:MMam/pm)"))
  (princ (strcat "\
The current time is " ctim ))
 (princ)
)
```

#### Related References

* [DIESEL Functions Reference](DIESEL-Functions-Reference.md)

#### Related Concepts

* [About Calibrating Tablets (AutoLISP)](About-Calibrating-Tablets-AutoLISP.md)
* [About Configuration Files (AutoLISP)](About-Configuration-Files-AutoLISP.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*