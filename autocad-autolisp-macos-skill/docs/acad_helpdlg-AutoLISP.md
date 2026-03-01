# acad\_helpdlg (AutoLISP)

Invokes the help facility (obsolete)

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows

## Signature

```
(acad_helpdlg helpfile topic)
```

*helpfile*
:   *Type:* String

    The path and file name of the help file to open.

*topic*
:   *Type:* String

    The name of the topic to display in the help file.

## Return Values

*Type:* String or nil

Returns the file name of the help file if it is found; otherwise,
nil is returned if the file is not found.

## Remarks

This externally defined function has been replaced by the built-in
help function. It is provided for compatibility with earlier releases of AutoCAD.

#### Related References

* [help (AutoLISP)](help-AutoLISP.md)
* [setfunhelp (AutoLISP)](setfunhelp-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*