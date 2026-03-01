# acad\_truecolorcli (AutoLISP)

Prompts for colors at the Command prompt

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(acad_truecolorcli color [allowbylayer] [alternatePrompt])
```

*color*
:   *Type:* List

    A dotted pair that describes the default color. The first element of the dotted pair must be one of the color-related DXF
    group codes (62, 420, or 430); for example,
    (62 .
    *ColorIndex*),
    (420 .
    *TrueColor*), or
    (430 .
    *"colorbook$colorname"*).

*allowbylayer*
:   *Type:* T or nil

    Omitting the
    *allowbylayer* argument or setting it to a non-nil value enables entering ByLayer or ByBlock to set the color. If set to
    nil, an error results if ByLayer or ByBlock is entered.

*alternateprompt*
:   *Type:* T or nil

    An optional prompt string. If this string is omitted, the default value is “New color”.

## Return Values

*Type:* List or nil

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

Prompt for a color selection at the command line with a purple color index default selection and alternative text for the
command prompt:

```
(acad_truecolorcli '(62 . 215) 1 "Pick a color")
```

New Color [Truecolor/COlorbook] <215>:

```
((62 . 256))
```

Prompt for a color selection at the command line with a yellow color index default selection, then set the color by layer:

```
(acad_truecolorcli '(62 . 2))
```

New Color [Truecolor/COlorbook] <2 (yellow)>: bylayer

```
((62 . 256))
```

#### Related References

* [acad\_colordlg (AutoLISP)](acad_colordlg-AutoLISP.md)
* [acad\_truecolordlg (AutoLISP)](acad_truecolordlg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*