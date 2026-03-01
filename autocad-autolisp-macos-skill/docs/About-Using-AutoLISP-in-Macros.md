# About Using AutoLISP in Macros

Creating commands that use AutoLISP is a more advanced way to use the program's customization feature.

You can use AutoLISP variables and expressions to create macros that perform complex tasks. When the program loads a CUI/CUIx
file, it also loads a MNL file with the same name and in the same location. Placing AutoLISP code in a MNL file is an efficient
way to load custom commands that can be used in a macro.

NOTE:

* AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
  LOAD function from another LISP file.
* In AutoCAD on Windows only, not available in AutoCAD LT, you can specify additional AutoLISP files to load in the Customize
  User Interface (CUI) Editor. Creating commands that use AutoLISP is a more advanced way to use the program's customization
  feature. Experimentation and practice will help you use this feature effectively.

## Examples

Preset Values
:   This example is composed of three command macros that are used to insert a block.

    Command macro prompts for the window width.

    ```
    ^C^C^P(setq WINWID (getreal "\
    Enter window width: ")) ^P
    ```

    Command macro prompts for the wall thickness.

    ```
    ^C^C^P(setq WALLTHK (getreal "\
    Enter wall thickness: ")) ^P
    ```

    Command macro inserts a block named "window" and prompts for the insertion point and rotation.

    ```
    ^C^C_INSERT window XScale !WINWID YScale !WALLTHK
    ```

    The
    *X* axis of the block is to the current window width and its
    *Y* axis to the current wall thickness.

Resize Grips
:   This example contains two command macros that increase or decrease the current value of the GRIPSIZE system variable.

    Command macro increases the value of the GRIPSIZE system variable by 1.

    ```
    ^P(setvar "gripsize"(1+ (getvar "gripsize")))(redraw)(princ)
    ```

    Command macro decreases the value of the GRIPSIZE system variable by 1.

    ```
    ^P(setvar "gripsize"(1- (getvar "gripsize")))(redraw)(princ)
    ```

    To add validity checking to these command macros, values less than 0 and greater than 255 cannot be used for the GRIPSIZE
    system variable.

Prompt for User Input
:   The following example prompts for two points and draws a rectangular polyline with the specified points as its corners.

    ```
    ^P(setq a (getpoint "Enter first corner: "));\+
    (setq b (getpoint "Enter opposite corner: "));\+
    pline !a (list (car a)(cadr b)) !b (list (car b)(cadr a)) c;^P
    ```

Call a Macro Assigned to a Pull-down Menu Item (Windows only)
:   Using the following syntax, you can programmatically execute a pull-down menu item's macro:

    ```
    (menucmd "Gcustomizationgroup.element_ID=|")
    ```

    The previous syntax works only if the menu item is part of a menu that is on the program's menu bar and is available for use.

#### Related Tasks

* [To Create a Custom Command](To-Create-a-Custom-Command.md)
* [To Edit a Command](To-Edit-a-Command.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Command Macro Strings](About-Command-Macro-Strings.md)
* [About Special Control Characters in Command Macros](About-Special-Control-Characters-in-Command-Macros.md)
* [About Pausing Macros for User Input](About-Pausing-Macros-for-User-Input.md)
* [About Using Conditional Expressions in Macros](About-Using-Conditional-Expressions-in-Macros.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*