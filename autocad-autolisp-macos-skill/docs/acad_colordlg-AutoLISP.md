# acad\_colordlg (AutoLISP)

Displays the standard AutoCAD color selection dialog box

*Supported Platforms:* Windows only

## Signature

```
(acad_colordlg colornum [flag])
```

*colornum*
:   *Type:* Integer

    An integer in the range 0-256 (inclusive), specifying the AutoCAD color number to display as the initial default.

    A *colornum* value of 0 defaults to ByBlock, and a value of 256 defaults to ByLayer.

*flag*
:   *Type:* T or nil

    If set to nil, disables the ByLayer and ByBlock buttons. Omitting the *flag* argument or setting it to a non-nil value enables the ByLayer and ByBlock buttons.

## Return Values

*Type:* Integer or nil

The user-selected color number; otherwise nil, if the user cancels the dialog box.

## Examples

Prompt the user to select a color, and default to green if none is selected:

```
(acad_colordlg 3)
```

#### Related References

* [acad\_truecolorcli (AutoLISP)](acad_truecolorcli-AutoLISP.md)
* [acad\_truecolordlg (AutoLISP)](acad_truecolordlg-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*