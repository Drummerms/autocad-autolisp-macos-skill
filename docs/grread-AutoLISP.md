# grread (AutoLISP)

Reads values from any of the AutoCAD input devices

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(grread [track] [allkeys [curtype]])
```

*track*
:   *Type:* T or nil

    If supplied and not
    nil, this argument enables the return of coordinates from a pointing device as it is moved.

*allkeys*
:   *Type:* Integer

    Code that tells
    grread what functions to perform. The
    *allkeys* bit code values can be added together for combined functionality. The following values can be specified:

    *1*(bit 0) -- Return
    *drag mode* coordinates. If this bit is set and the user moves the pointing device instead of selecting a button or pressing a key,
    grread returns a list where the first member is a type 5 and the second member is the
    *(X,Y)* coordinates of the current pointing device (mouse or digitizer) location. This is how AutoCAD implements dragging.

    *2* (bit 1) -- Return all key values, including function and cursor key codes, and do not move the cursor when the user presses
    a cursor key.

    *4* (bit 2) -- Use the value passed in the
    *curtype* argument to control the cursor display.

    *8*(bit 3) -- Do not display the error: console break message when the user presses Esc.

*curtype*
:   An integer indicating the type of cursor to be displayed. The
    *allkeys* value for bit 2 must be set for the
    *curtype* values to take effect. The
    *curtype* argument affects only the cursor type during the current
    grread function call. You can specify one of the following values for
    *curtype*:

    *0* -- Display the normal crosshairs.

    *1* -- Do not display a cursor (no crosshairs).

    *2* -- Display the object-selection “target” cursor.

## Return Values

*Type:* List

The
grread function returns a list whose first element is a code specifying the type of input. The second element of the list is either
an integer or a point, depending on the type of input. The return values are listed in the following table:

| grread return values | | | |
| First element | | Second element | |
| Value | Type of input | Value | Description |
| 2 | Keyboard input | varies | Character code |
| 3 | Selected point | 3D point | Point coordinates |
| 4 | Screen/pull-down menu item (from pointing device) | 0 to 999  1001 to 1999  2001 to 2999  3001 to 3999  … and so on, to  16001 to 16999 | Screen menu box no.  POP1 menu box no.  POP2 menu box no.  POP3 menu box no.  ... and so on, to  POP16 menu box no. |
| 5 | Pointing device (returned only if tracking is enabled) | 3D point | Drag mode coordinate |
| 6 | BUTTONS menu item | 0 to 999  1000 to 1999  2000 to 2999  3000 to 3999 | BUTTONS1 menu button no.  BUTTONS2 menu button no.  BUTTONS3 menu button no.  BUTTONS4 menu button no. |
| 7 | TABLET1 menu item | 0 to 32767 | Digitized box no. |
| 8 | TABLET2 menu item | 0 to 32767 | Digitized box no. |
| 9 | TABLET3 menu item | 0 to 32767 | Digitized box no. |
| 10 | TABLET4 menu item | 0 to 32767 | Digitized box no. |
| 11 | AUX menu item | 0 to 999  1000 to 1999  2000 to 2999  3000 to 3999 | AUX1 menu button no.  AUX2 menu button no.  AUX3 menu button no.  AUX4 menu button no.  NOTE:SHORTCUTMENU must be set to a value of 0. |
| 12 | Pointer button (follows a type 6 or type 11 return) | 3D point | Point coordinates |
| 25 | Pointer secondary button | 0 or greater | Screen coordinate value along the X axis  NOTE:SHORTCUTMENU must be set to a value greater than 0. |

## Remarks

Only specialized AutoLISP routines need this function. Most input to AutoLISP should be obtained through the various
get*XXX* functions.

Entering Esc while a
grread is active aborts the AutoLISP program with a keyboard break (unless the
*allkeys* argument has disallowed this). Any other input is passed directly to
grread, giving the application complete control over the input devices.

If the user presses the pointer button within a screen menu or pull-down menu box,
grread returns a type 6 or type 11 code, but in a subsequent call, it does not return a type 12 code: the type 12 code follows type
6 or type 11 only when the pointer button is pressed while it is in the drawing area.

It is important to clear the code 12 data from the buffer before attempting another operation with a pointer button or an
auxiliary button. To accomplish this, perform a nested
grread like this:

```
(setq code_12 (grread (setq code (grread))))
```

This sequence captures the value of the code 12 list as streaming input from the device.

## Examples

N/A

#### Related References

* [grdraw (AutoLISP)](grdraw-AutoLISP.md)
* [grvecs (AutoLISP)](grvecs-AutoLISP.md)

#### Related Concepts

* [Device Access Functions Reference (AutoLISP)](Device-Access-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*