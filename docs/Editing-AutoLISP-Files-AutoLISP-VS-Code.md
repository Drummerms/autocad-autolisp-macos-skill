# Editing AutoLISP Files (AutoLISP/VS Code)

The AutoCAD AutoLISP Extension offers several features that make it easier to write AutoLISP programs and DCL files, such
as IntelliSense and code snippets.

In this topic, you can learn about:

* Entering function names with IntelliSense
* Accessing help for an AutoLISP function or DCL tile/attribute
* Adding comments
* Going to the definition of a function or variable
* Inserting a region
* Inserting code snippets

## Entering Function Names with IntelliSense

As you type in the editor window of an open AutoLISP source (LSP) or DCL file, the AutoCAD AutoLISP Extension displays a list
of suggested functions and code snippets that match the characters typed. The more characters you type, the less items that
will be displayed in the list. Select an item in the list to complete the function name or use the code snippet, you can also
use the arrow keys to highlight the item to use and then press Tab to complete that item.

## Accessing Help for an AutoLISP Function or DCL Tile/Attribute

Help for a built-in AutoLISP function or DCL tile/attribute can be accessed contextually from within an editor window in VS
Code, rather than needing to open and browse to the online help directly. You can open the help for an AutoLISP function or
DCL tile/attribute by clicking in or highlighting its name in an editor window that contains an AutoLISP source (LSP) or DCL
file, and then right-clicking and choosing
Open Online Help.

NOTE:This functionality is available starting with version 1.4.0 of the AutoCAD AutoLISP Extension.

## Adding Comments

AutoLISP source (LSP) or DCL files support line and block comments. Comments can be manually added to any AutoLISP or DCL
statement, but VS Code supports that ability to add and remove line and block comments to and from selected AutoLISP or DCL
statements.

* *AutoLISP line comment* – Starts with one or more semi-colon characters. Functions on the same line and to the right of a semi-colon are ignored
  and not executed. VS Code adds a single semi-colon character when adding line comments to selected statements.

  ```
  ; Returns a CDATE value that includes milliseconds based on release
  ; Usage: (CDate)
  ; Replaces (rtos (getvar "CDATE") 2 8)
  ```
* *AutoLISP block comment* – Starts with the character sequence
  ;| and ends with the character sequence
  |;. All statements between the character sequences are ignored and not executed.

  ```
  ;| Returns a CDATE value that includes milliseconds based on release
        Usage: (CDate)
        Replaces (rtos (getvar "CDATE") 2 8) |;
  ```
* *DCL line comment* – Starts with one or more forward slash characters. Definitions on the same line and to the right of a forward slash are
  ignored and not evaluated. VS Code adds two forward slash characters when adding line comments to selected definitions.

  ```
  // defines the Spacing Between Tiles edit box
  // :edit_box {
  //        label = "&Spacing between tiles";
  //        key = "gp_spac";
  //        edit_width = 6;
  // }
  ```
* *DCL block comment* – Starts with the character sequence
  /\* and ends with the character sequence
  \*/. All definitions between the character sequences are ignored and not evaluated.

  ```
  /* defines the Spacing Between Tiles edit box
  :edit_box {
         label = "&Spacing between tiles";
         key = "gp_spac";
         edit_width = 6;
  } */
  ```

## Going to the Definition of a Function or Variable

VS Code can search for the definition of a user-defined function orvariable used within the open AutoLISP source (LSP) file
in the current editor window. When searching for the definition of a function or variable, VS Code searches the:

* Current and all open LSP files
* LSP files in the open folder or workspace in the Explorer view
* LSP files in the open project within the AutoLISP Project Manager

The definition of a user-defined function or variable is defined as:

Function
:   The definition of a function is defined by the use of the
    defun function.

    ```
    (defun xxx ())
    ```

Variable
:   The definition of a variable is defined by the

    * placement of the variable name within the second element (or atom) of the
      defun function
    * use of the
      setq function

    ```
    (defun xxx ( / varname))

    (setq varname val)
    ```

    Variable definitions are looked for first in the local scope of an AutoLISP statement or
    defun code block and then in the global scope.

You can go to the definition of a user-defined function or variable by clicking in or highlighting its name in an editor window,
and then right-clicking and choosing
Go to Definition or pressing
F12. If the definition is located, focus is moved to the location in which the definition was found. More than one definition
could also be found, and if so, you will be prompted to which instance of the definition focus should be moved.

NOTE:This functionality is available starting with version 1.4.0 of the AutoCAD AutoLISP Extension.

## Inserting a Region

VS Code automatically defines what are known as
*regions* based on AutoLISP statements or DCL definitions that span multiple lines. A region can be expanded or collapsed to minimize
the number of code statements currently displayed in the editor window. User-defined regions can also be inserted to group
multiple statements and regions, also referred to as
*subregions*, into a single collapsible region.

A user-defined region starts with the comment
;#region and ends with the comment
;#endregion. Since these are comments, you can add descriptive text after each to explain the use of the statements and definitions in
the region.

Region Expanded
:   ![](../images/GUID-17CC97CB-47B3-42B7-8E79-B30CC83E5717-low.png)

Region Collapsed
:   ![](../images/GUID-AFFEC731-BAA6-4772-8BFC-1D29D9DE0C28-low.png)

NOTE:This functionality is available starting with version 1.4.0 of the AutoCAD AutoLISP Extension.

## Inserting Code Snippets

Small code blocks or samples, known as
*code snippets*, are supported by the AutoCAD AutoLISP Extension. Code snippets can be used to quickly add the necessary syntax for commonly
used functions or complex code blocks. For example, the AutoCAD AutoLISP Extension has a code snippet named
ifp which is short for
If… Progn and it contains an
if statement with a nested
progn statement. Typing
*ifp* in the code editor and pressing Tab allows you to insert the code snippet.

Code snippets are part of the AutoComplete feature in VS Code and are prefixed by a square icon rather than a wrench used
to indicate the name of an AutoLISP function.

![](../images/GUID-FF4A596C-39D2-46AA-987F-22199D27129F-low.png)

The AutoCAD AutoLISP Extension codes ships with 60+ code snippets, here are a few of the code snippets that come with the
AutoCAD AutoLISP Extension:

| getlayer | ``` (setq layer (cdr (assoc 8 entname))) ``` |
| ifp | ``` (if (testexpr)   (progn     (thenexpr)   ) ) ``` |
| line | ``` (command "_line" "pt1" "pt2" "") ``` |
| open | ``` (setq fp "fname.txt") (setq f (open fp "mode"))   (close f) ``` |
| while | ``` (while testexpr [expr ...]) ``` |

Code snippets for the AutoCAD AutoLISP Extension are stored in a file named
*snippets.json* under one of these locations:

* *Windows* –
  *%USERPROFILE%\.vscode\extensions\autodesk.autolispext-n.n.n\snippets*
* *Mac OS* –
  *~/.vscode/extensions/autodesk.autolispext-n.n.n/snippets*

NOTE:*n.n.n* in the previous paths is a placeholder, the actual version of the AutoCAD AutoLISP Extension will vary over time as the extension
is updated.

#### Topics in this section

* [To Insert a Code Snippet (AutoLISP/VS Code)](To-Insert-a-Code-Snippet-AutoLISP-VS-Code.md)
* [To Add or Edit Code Snippet Definitions (AutoLISP/VS Code)](To-Add-or-Edit-Code-Snippet-Definitions-AutoLISP-VS-Code.md)
* [To Add and Remove Comments from Selected AutoLISP Expressions (AutoLISP/VS Code)](To-Add-and-Remove-Comments-from-Selected-AutoLISP-Expressions-AutoLISP-VS-Code.md)
* [To Insert a Region (AutoLISP/VS Code)](To-Insert-a-Region-AutoLISP-VS-Code.md)

#### Related Tasks

* [To Insert a Region (AutoLISP/VS Code)](To-Insert-a-Region-AutoLISP-VS-Code.md)

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)
* [Creating and Opening AutoLISP Files (AutoLISP/VS Code)](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md)
* [Formatting AutoLISP Files (AutoLISP/VS Code)](Formatting-AutoLISP-Files-AutoLISP-VS-Code.md)
* [To Insert a Code Snippet (AutoLISP/VS Code)](To-Insert-a-Code-Snippet-AutoLISP-VS-Code.md)
* [To Add or Edit Code Snippet Definitions (AutoLISP/VS Code)](To-Add-or-Edit-Code-Snippet-Definitions-AutoLISP-VS-Code.md)
* [To Add and Remove Comments from Selected AutoLISP Expressions (AutoLISP/VS Code)](To-Add-and-Remove-Comments-from-Selected-AutoLISP-Expressions-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*