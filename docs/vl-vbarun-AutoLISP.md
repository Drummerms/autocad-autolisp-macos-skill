# vl-vbarun (AutoLISP)

Runs a VBA macro

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(vl-vbarun macroname)
```

*macroname*
:   *Type:* String

    Name of a macro in a loaded VBA project.

## Return Values

*Type:* String or error

The value of the
*macroname* argument; otherwise, an error occurs.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows

## Examples

Load a VBA project file:

```
(vl-vbaload "c:/program files/<AutoCAD installation directory>/sample/vba/drawline.dvb")
"c:\\program files\\<AutoCAD installation directory>\\sample\\vba\\drawline.dvb"
```

Run a macro from the loaded project:

```
(vl-vbarun "drawline")
"drawline"
```

#### Related References

* [vl-vbaload (AutoLISP)](vl-vbaload-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*