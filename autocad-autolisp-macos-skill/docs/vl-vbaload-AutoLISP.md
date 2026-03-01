# vl-vbaload (AutoLISP)

Loads a VBA project

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(vl-vbaload filename)
```

*filename*
:   *Type:* String

    Name of the VBA project file to be loaded.

## Return Values

*Type:* String or error

A textual value containing the file name and path of the VBA project; otherwise an error occurs if the file is not found.

IMPORTANT:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows

## History

*AutoCAD 2021*

* *filename* argument previously accepted an ASCII text string, but now accepts a Unicode text string.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-vbaload "c:/program files/<AutoCAD installation directory>/sample/vba/drawline.dvb")
"c:\\program files\\<AutoCAD installation directory>\\sample\\vba\\drawline.dvb"
```

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)
* [autoload (AutoLISP)](autoload-AutoLISP.md)
* [autoarxload (AutoLISP)](autoarxload-AutoLISP.md)
* [arxload (AutoLISP)](arxload-AutoLISP.md)
* [arxunload (AutoLISP)](arxunload-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*