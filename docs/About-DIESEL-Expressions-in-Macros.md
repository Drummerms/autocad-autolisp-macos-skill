# About DIESEL Expressions in Macros

You can use DIESEL string expressions in customization (CUI/CUIx) files as an additional method of creating macros and a
way to change a pull-down menu label.

A DIESEL expression can be used with a user interface element and must follow the $section=submenu format; where the section name is M and the submenu is the DIESEL expression you want.

Consider the following example:

```
^C^C^P$M=$(if,$(=,$(getvar,cvport),1),mspace,pspace)
```

This DIESEL expression provides a way to toggle between model space and paper space based on the current value of the CVPORT
system variable. When CVPORT is set to 1, the MSPACE command is executed; otherwise, the PSPACE command is executed. This
expression is evaluated transparently. If the special character ^P (which toggles MENUECHO on and off) is omitted, the expression
displays only the issued command.

The DIESEL expression in the following example is used to multiply the current value of DIMSCALE by a value of 0.5 to calculate
the scale factor when inserting the Note block with the -INSERT command.

```
^C^C-insert;note;0,0;$M=$(*,$(getvar,dimscale),0.5);;0;
```

DIESEL expressions can also be used to define the label of a pull-down menu item, so that you can make menus unavailable
or otherwise alter the way they are displayed. Make sure that the first character is the $ character when using a DIESEL expression in a pull-down menu label.

In this example, the current layer is set to BASE and the following DIESEL expression is used as the label for a pull-down
menu.

```
$(eval,"Current layer: " $(getvar,clayer))
```

The result is that the appropriate pull-down menu is displayed and updated whenever the current layer changes.

Current Layer: BASE

NOTE:The width of pull-down and shortcut menus is determined when the customization file is being loaded. Menu labels generated
or changed by DIESEL expressions after a menu is loaded are truncated to fit within the existing menu width.

If you anticipate that a DIESEL-generated menu label will be too wide, you can use the following example to ensure that the
menu width will accommodate your labels. This example displays the first 10 characters of the current value of the CLAYER
system variable.

```
$(eval,"Current value: " $(substr,$(getvar,clayer),1,10))
```

You cannot use trailing spaces in a menu label to increase the menu width, because trailing spaces are ignored while the menu
is being loaded. Any spaces you use to increase the width of a menu label must be within a DIESEL expression.

The next example uses the same DIESEL expression as the label and a portion of the menu item. It provides a practical way
to enter the current day and date into a drawing.

Menu label

```
$(edtime,$(getvar,date),DDD", "D MON YYYY)
```

Macro

```
^C^Ctext \\\ $M=$(edtime,$(getvar,date),DDD", "D MON YYYY);
```

Also, you can use a DIESEL macro to mark pull-down menu labels or make them unavailable. The following pull-down menu label
displays as unavailable while a command is active. The text is displayed normally when a command is not active.

```
$(if,$(eq,$(getvar,tilemode),1),~)&Polygonal Viewport
```

You can use a similar approach to place a mark beside a pull-down menu item or to interactively change the character used
for the mark.

```
$(if,$(and,$(getvar,ucsicon),1),!.)&On
```

#### Related References

* [DIESEL Functions Reference](DIESEL-Functions-Reference.md)
* [DIESEL Error Message Reference](DIESEL-Error-Message-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Responding to AutoLISP with DIESEL Expressions in Macros](About-Responding-to-AutoLISP-with-DIESEL-Expressions-in-Macros.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*