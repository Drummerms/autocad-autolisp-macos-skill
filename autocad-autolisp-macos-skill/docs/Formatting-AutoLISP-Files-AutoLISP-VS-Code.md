# Formatting AutoLISP Files (AutoLISP/VS Code)

AutoLISP expressions can be formatted to make them easier to read.

You can automatically format select or all AutoLISP expressions in the active editor window. When using the Format Selection
and Format Document tools of VS Code, comments are aligned with the statement that follows and open/close parenthesis pairs
on different lines are aligned in the same column to help identify balancing parenthesis.

The following shows an example of a custom function before and after being formatted:

Before formatting
:   ```
    (defun CDate ( / ms)
    ; Check to see which AutoCAD release is being used
    (if (<= (atof (getvar "ACADVER")) 22.0)
    (rtos (getvar "CDATE") 2 8)
    (progn
    ; Get the current milliseconds and append it to the CDATE value
    (setq ms (itoa (getvar "MILLISECS")))
    (strcat (rtos (getvar "CDATE") 2 6)(substr ms (- (strlen ms) 2)))
    )
    )
    )
    ```

After formatting
:   ```
    (defun CDate ( / ms)
      ; Check to see which AutoCAD release is being used
      (if (<= (atof (getvar "ACADVER")) 22.0)
        (rtos (getvar "CDATE") 2 8)
        (progn
          ; Get the current milliseconds and append it to the CDATE value
          (setq ms (itoa (getvar "MILLISECS")))
          (strcat (rtos (getvar "CDATE") 2 6)(substr ms (- (strlen ms) 2)))
        )
      )
    )
    ```

## Control Format Styles

The AutoCAD AutoLISP Extension defines how VS Code should format AutoLISP code statements in an open LSP file. Many of the
formatting rules can't be changed, but there are several rules that can be changed based on your preference. The following
formatting settings can be changed as part of the extension:

Close Parenthesis Style
:   Controls the style of closing parenthesis. A closing parenthesis is placed on the same line as the function or aligned with
    the function's opening parenthesis.

Long List Format Style
:   Controls the format style of long lists. Each or multiple parameters of a function are placed on separate lines.

Maximum Line Characters
:   Suggested maximum number of characters to display on each line. Value must be 60 or greater.

Narrow Style Indent
:   Indentation value used in the Narrow Formatting Style of function arguments. Value must be in the range of 1 and 6.

For information on how to access the format settings of the AutoCAD AutoLISP Extension, see
[To Format AutoLISP Expressions in the Current Editor Window](To-Format-AutoLISP-Expressions-in-the-Current-Editor-Window-AutoLISP-VS-Code.md).

#### Topics in this section

* [To Format AutoLISP Expressions in the Current Editor Window (AutoLISP/VS Code)](To-Format-AutoLISP-Expressions-in-the-Current-Editor-Window-AutoLISP-VS-Code.md)

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)
* [Creating and Opening AutoLISP Files (AutoLISP/VS Code)](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md)
* [Editing AutoLISP Files (AutoLISP/VS Code)](Editing-AutoLISP-Files-AutoLISP-VS-Code.md)
* [Tutorial: Formatting LSP Files with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Formatting-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*