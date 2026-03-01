# load (AutoLISP)

Evaluates the AutoLISP expressions in a file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(load filename [onfailure])
```

*filename*
:   *Type:* String

    Name of the AutoLISP file to load. If the
    filename argument does not specify a file extension,
    load adds an extension to the name when searching for a file to load. The function will try several extensions, if necessary,
    in the following order:

    * *.vlx*
    * *.fas*
    * .*lsp*

    NOTE:VLX files are supported on Windows only.

    As soon as
    load finds a match, it stops searching and loads the file.

    The
    filename can include a directory prefix, as in
    *c:/function/test1* (Windows) or
    */function/test1* (Mac OS and Web). A forward slash (/) or two backslashes (\\) are valid directory delimiters. If you don't include a directory prefix in the
    filename string,
    load searches the AutoCAD library path for the specified file. If the file is found anywhere on this path,
    load then loads the file.

*onfailure*
:   *Type:* String

    A value returned if
    load fails.

    If the
    *onfailure* argument is a valid AutoLISP function, it is evaluated. In most cases, the
    *onfailure* argument should be a string or an atom. This allows an AutoLISP application calling
    load to take alternative action upon failure.

## Remarks

The
load function can be used from within another AutoLISP function, or even recursively (in the file being loaded).

IMPORTANT:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Return Values

*Type:* String, Subroutine, or Error

Unspecified, if successful. If
load fails, it returns the value of
*onfailure*; if
*onfailure* is not defined, failure results in an error message.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *filename* argument previously accepted an ASCII text string, but now accepts a Unicode text string.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

For the following examples, assume that file
*/fred/test1.lsp* contains the expressions

```
(defun MY-FUNC1 (x)
          ... function body ...
)
(defun MY-FUNC2 (x)
          ... function body ...
)
```

and that no file named
*test2* with a
*.lsp*,
*.fas*, or
*.vlx* extension exists:

```
(load "/fred/test1")
MY-FUNC2

(load "\\fred\\test1")
MY-FUNC2

(load "/fred/test1" "bad")
MY-FUNC2

(load "test2" "bad")
"bad"

(load "test2")
; error: LOAD failed: "test2"
```

#### Related Tasks

* [To load functions across all document namespaces (AutoLISP)](To-load-functions-across-all-document-namespaces-AutoLISP.md)

#### Related References

* [autoload (AutoLISP)](autoload-AutoLISP.md)
* [arxload (AutoLISP)](arxload-AutoLISP.md)
* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [findtrustedfile (AutoLISP)](findtrustedfile-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*