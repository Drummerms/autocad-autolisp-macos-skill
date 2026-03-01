# acad\_truecolordlg (AutoLISP)

Displays the AutoCAD color selection dialog box with tabs for index color, true color, and color books

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(acad_truecolordlg color [allowbylayer] [currentlayercolor])
```

*color*
:   *Type:* List (Dotted pair)

    A dotted pair that describes the default color. The first element of the dotted pair must be one of the color-related DXF
    group codes (62, 420, or 430); for example,
    (62 . ColorIndex),
    (420 . TrueColor), or
    (430 . "colorbook$colorname").

*allowbylayer*
:   *Type:* T or nil

    If set to
    nil, disables the ByLayer and ByBlock buttons. Omitting the
    *allowbylayer* argument or setting it to a non-nil value enables the ByLayer and ByBlock buttons.

*currentlayercolor*
:   *Type:* List (Dotted pair)

    Optional dotted pair in the same form as
    color that sets the value of the ByLayer/ByBlock color in the dialog.

## Return Values

*Type:* List (Dotted pair) or nil

When the operation is successful, the function returns a list of one or more dotted pairs (depending on the tab on which the
color is selected) describing the color selected. The last dotted pair in the list indicates the color selected. The function
returns
nil if the user cancels the dialog box.

Color book color
:   If the last item in the returned list is a 430 pair, then the specified color originates from a color book. This returned
    list will also contain a 420 pair that describes the corresponding true color and a 62 pair that describes the closest matching
    color index value.

True color
:   If the returned list contains a 420 pair as the last item, then a true color was specified (as “Red,Green,Blue”). The list
    will also contain a 62 pair that indicates the closest matching color index. No 430 pair will be present.

Color index
:   If the last item in the list is a 62 pair, then a color index was chosen. No other dotted pairs will be present in the returned
    list.

## Examples

Open the color selection dialog to the Color Index tab and accept the purple default selection:

```
(acad_truecolordlg '(62 . 215))
((62 . 215))
```

Open the color selection dialog to the True Color tab with a green default selection and with the By Layer and By Block buttons
disabled:

```
(acad_truecolordlg '(420 . 2686760) nil)
((62 . 80) (420 . 2686760))
```

Open the color selection dialog to the Color Books tab and accept the mustard default selection:

```
(acad_truecolordlg '(430 . "RAL CLASSIC$RAL 1003"))
((62 . 40) (420 . 16235019) (430 . "RAL CLASSIC$RAL 1003"))
```

#### Related References

* [acad\_colordlg (AutoLISP)](acad_colordlg-AutoLISP.md)
* [acad\_truecolorcli (AutoLISP)](acad_truecolorcli-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*