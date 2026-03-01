# grtext (AutoLISP)

Writes text to the status line or to screen menu areas

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(grtext [box text [highlight]])
```

*box*
:   *Type:* Integer

    Location in which to write the text.

*text*
:   *Type:* String

    Specifies the text to be written to the screen menu or status line location. The
    *text* argument is truncated if it is too long to fit in the available area.

*highlight*
:   *Type:* Integer

    Selects or deselects a screen menu location.

## Return Values

*Type:* String

The string passed in the
*text* argument, if successful, and
nil if unsuccessful or no arguments are supplied.

## Remarks

This function displays the supplied text in the menu area; it does not change the underlying menu item. The
grtext function can be called with no arguments to restore all text areas to their standard values.

NOTE:This function is supported on Mac OS and Web, but does not affect the program.

If called without arguments,
grtextrestores all text areas to their standard values. If called with only one argument,
grtext results in an error.

Screen Menu Area (Obsolete)
:   Setting
    *box* to a positive or zero value specifies a screen menu location. Valid
    *box* values range from 0 to the highest-numbered screen menu box minus 1. The AutoCAD SCREENBOXES system variable reports the
    maximum number of screen menu boxes. If the
    *highlight* argument is supplied as a positive integer,
    grtext highlights the text in the designated box. Highlighting a box automatically dehighlights any other box already highlighted.
    If
    *highlight* is zero, the menu item is dehighlighted. If
    *highlight* is a negative number, it is ignored. On some platforms, the text must first be written without the
    *highlight* argument and then must be highlighted. Highlighting of a screen menu location works only when the cursor is not in that area.

Status Line Area
:   If
    grtext is called with a
    *box* value of -1, it writes the text into the mode status line area. The length of the mode status line differs from display to
    display (most allow at least 40 characters). The following code uses the
    $(linelen) DIESEL expression to report the length of the mode status area.

    ```
    (setq modelen (menucmd "M=$(linelen)"))
    ```

    If a
    *box* value of -2 is used,
    grtext writes the text into the coordinate status line area. If coordinate tracking is turned on, values written into this field
    are overwritten as soon as the pointer sends another set of coordinates. For both -1 and -2
    *box* values, the
    *highlight* argument is ignored.

## Examples

N/A

#### Related References

* [grdraw (AutoLISP)](grdraw-AutoLISP.md)
* [grvecs (AutoLISP)](grvecs-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*