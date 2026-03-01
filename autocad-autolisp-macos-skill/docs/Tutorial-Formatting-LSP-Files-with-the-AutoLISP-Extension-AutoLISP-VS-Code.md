# Tutorial: Formatting LSP Files with the AutoLISP Extension (AutoLISP/VS Code)

The AutoLISP Extension provides tools to format select AutoLISP code statements, define the indent and alignment of new statements
as they are typed, and mark a statement as a comment.

## Prerequisites

1. [Install Visual Studio Code on your workstation.](To-Download-and-Install-VS-Code-AutoLISP-VS-Code.md)
2. [Install and configure the AutoCAD AutoLISP Extension.](Tutorial-Installing-and-Configuring-the-AutoLISP-Extension-AutoLISP-VS-Code.md)
3. [Open an AutoLISP (LSP) File for edit in Visual Studio Code.](Tutorial-Debugging-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

## Topics in this Tutorial

* [Format AutoLISP Code Statements](GUID-55FA8B38-1748-40D4-BFA6-A135335017DA.htm#SECTION_82A1CD393FB2436892C338B4D9CCAF61)
* [Comment and Uncomment AutoLISP Code Statements](GUID-55FA8B38-1748-40D4-BFA6-A135335017DA.htm#SECTION_EE78548F8229424FA35E599241BC925F)

## Format AutoLISP Code Statements

Visual Studio Code automatically applies some formatting to new AutoLISP code statements as they are typed, but code statements
pasted from another source are not automatically formatted. Visual Studio Code does allow you to format select or all code
statements in the current editor window.

The following steps explain how to format code statements in an LSP file:

1. In Visual Studio Code, open the
   *Create-LSP-Tutorial.lsp* file or make it current.
2. In the editor window, select the following statements that define the
   hello function:

   ```
   (defun c:hello ( / msg)
   (setq msg (getstring T "\
   Enter a message: "))
   (alert msg)
   )
   ```
3. Right-click and choose Format Selection.

   The code statements are reformatted with the nested statements now indented and aligned. The statements should look like the
   following:

   ```
   (defun c:hello (/ msg)
       (setq msg (getstring T "\
   Enter a message: "))
       (alert msg)
   )
   ```
4. Right-click in the editor window and choose Format Document.

   All the code statements in the LSP file are formatted based on the settings of the AutoLISP Extension.
5. Save the changes to the
   *Create-LSP-Tutorial.lsp* file.

The current settings used to indent and format AutoLISP code statements can be viewed and changed by doing the following:

1. In Visual Studio Code, on the Activity Bar, click Extensions.
2. On the Extensions view, click More Actions > Show Installed Extensions.
3. On the AutoCAD AutoLISP Extension item, click Manage (![](../images/GUID-51857ACF-72EA-416C-B411-A799B0F6CC41-low.png)) > Extension Settings.
4. Adjust the extension settings as desired, changes are automatically saved.

   If you want to restore the default value of a setting, move the cursor over the name of the setting, and click More Actions
   (![](../images/GUID-51857ACF-72EA-416C-B411-A799B0F6CC41-low.png)) > Reset Setting.

## Comment and Uncomment AutoLISP Code Statements

Comments are great for describing what a program or specific code statement does in an LSP file. You indicate a comment in
an LSP file by adding one or more semi-colons in front of the text that you want to mark as a comment.

The following steps explain how to use the tools in Visual Studio Code to mark lines as comments or uncomment lines in an
LSP file:

1. In Visual Studio Code, open the
   *Create-LSP-Tutorial.lsp* file or make it current.
2. In the editor window, select the following lines that define the
   hello function:

   ```
   (defun c:hello (/ msg)
       (setq msg (getstring T "\
   Enter a message: "))
       (alert msg)
   )
   ```
3. On the menu bar, click Edit menu > Toggle Line Comment.

   A semi-colon is added to the beginning of each line. The statements should now look like the following:

   ```
   ; (defun c:hello (/ msg)
   ;     (setq msg (getstring T "\
   Enter a message: "))
   ;     (alert msg)
   ; )
   ```
4. Select the lines again and click Edit menu > Toggle Line Comment.

   The semi-colon is removed from each line.

The Toggle Block Comment tool on the Edit menu can also be used to mark a large number of lines as comments. This type of
comment is known as a
*block comment*. A block comment starts with the character sequence ;| and ends with |; rather than each line beginning with a semi-colon.
The following shows the results of a block comment being applied to the
hello function.

```
;| (defun c:hello (/ msg)
    (setq msg (getstring T "\
Enter a message: "))
    (alert msg)
) |;
```

A comment can also be placed after a code statement, this is commonly known as an
*inline comment*.

```
(alert msg)  ; Displays a string in a message box
```

TIP:Comments can be helpful while debugging or making changes to a program. Marking code statements as comments allows you to
suppress them from being executed in the AutoCAD program, while preserving them in the LSP file which allows you to narrow
the focus of the code statements to debug and provide you with a copy of the existing code statements to reference.

#### Related Information

* [Formatting AutoLISP Files (AutoLISP/VS Code)](Formatting-AutoLISP-Files-AutoLISP-VS-Code.md)
* [To Format AutoLISP Expressions in the Current Editor Window (AutoLISP/VS Code)](To-Format-AutoLISP-Expressions-in-the-Current-Editor-Window-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*