# initdia (AutoLISP)

Forces the display of the next command's dialog box

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(initdia [dialogflag])
```

*dialogflag*
:   *Type:* Integer

    A numeric value. If this argument is not present or is present and nonzero, the next use (and next use only) of a command
    will display that command's dialog box rather than its command line prompts.

    If
    *dialogflag* is zero, any previous call to this function is cleared, restoring the default behavior of presenting the command line interface.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

Currently, the following commands make use of the
initdia function: ATTDEF, ATTEXT, BHATCH, BLOCK, COLOR, IMAGE, IMAGEADJUST, INSERT, LAYER, LINETYPE, MTEXT, PLOT, RENAME, STYLE,
TOOLBAR, and VIEW.

## Examples

Issue the PLOT command without calling
initdia first:

Command:
*(command ".\_plot")*

plot

Enter a layout name <Model>: nil

Enter a layout name <Model>:

AutoCAD prompts for user input in the command window.

Use the following sequence of function calls to make AutoCAD display the Plot dialog box:

```
(initdia)
(command "._plot")
```

#### Related References

* [command (AutoLISP)](command-AutoLISP.md)
* [command-s (AutoLISP)](command-s-AutoLISP.md)
* [vl-cmdf (AutoLISP)](vl-cmdf-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*