# arxload (AutoLISP)

Loads an ObjectARX application

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(arxload application [onfailure])
```

*application*
:   *Type:* String

    A quoted string or a variable that contains the name of an executable file. You can omit the extension from the file name;
    *.arx/.crx* (Windows) or
    *.bundle* (Mac OS).

    You must supply the full path name of the ObjectARX executable file, unless the file is in a directory that is in the AutoCAD
    support file search path.

*onfailure*
:   *Type:* String

    An expression to be executed if the load fails.

## Return Values

*Type:* String

The application name, if successful. If unsuccessful and the
*onfailure* argument is supplied,
arxload returns the value of this argument; otherwise, failure results in an error message.

If you attempt to load an application that is already loaded,
arxload issues an error message. You may want to check the currently loaded ObjectARX applications with the
arx function before using
arxload.

## Remarks

IMPORTANT:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Examples

Load the
*autoloader.arx* file supplied in the AutoCAD installation directory:

```
(arxload "<AutoCAD installation directory>/autoloader")
"<AutoCAD installation directory>/autoloader"
```

#### Related References

* [arx (AutoLISP)](arx-AutoLISP.md)
* [arxunload (AutoLISP)](arxunload-AutoLISP.md)
* [load (AutoLISP)](load-AutoLISP.md)
* [vl-arx-import (AutoLISP)](vl-arx-import-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*