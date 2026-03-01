# vlisp-compile (AutoLISP/Visual LISP IDE)

Compiles AutoLISP source code into a FAS file

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows

## Signature

```
(vlisp-compile 'mode filename [output-filename])
```

*mode*
:   *Type:* Symbol

    The compiler mode, which can be one of the following symbols:

    *st* Standard build mode - Produces the smallest output file and is suitable for programs consisting of a single file.

    *lsm* Optimize and link indirectly - Optimizes the compiled files, but does not create direct references to the compiled functions
    in the compiled code.

    *lsa* Optimize and link directly - Optimizes the compiled files and creates direct references to the compiled function in the compiled
    code, instead of to the function symbol.

    NOTE:Both the optimization options are best suited for large and complex programs.

    The basic functions of optimization are as follows:

    * Link function calls to create direct references to the compiled function in the compiled code, instead of to the function
      symbol. This feature improves the performance of the compiled code and protects the code against function redefinition at
      runtime.
    * Drop function names to make the compiled code more secure and to decrease program size and load time.
    * Drop the names of all local variables and directly link their references. This also makes the compiled code more secure and
      decreases program size and load time.

*filename*
:   *Type:* String

    AutoLISP source file name. If the source file is in the AutoCAD support file search path, you can omit the path when specifying
    the file name. If you omit the file extension,
    *.lsp*is assumed.

*output-filename*
:   *Type:* String

    Compiled output file name. If you do not specify an output file,
    vlisp-compile names the output with the same name as the input file, but replaces the extension with
    *.fas*.

    NOTE:If you specify an output file name but do not specify a path name for either the input or the output file,
    vlisp-compile places the output file in the AutoCAD installation directory.

## Return Values

*Type:* T or nil

T, if compilation is successful; otherwise
nil.

## Remarks

Starting with
AutoCAD 2021-based products, FAS files can be compiled into two different file formats; Unicode and Multi-byte Character Strings (MBSCs).
Unicode format FAS files are not compatible with
AutoCAD 2020-based and earlier product releases, but are required to properly support Unicode strings. Use the LISPSYS system variable
to control the format in which to compile FAS files.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows

## History

*AutoCAD 2021*

* Updated to support the Unicode file format.

## Examples

Assuming that
*yinyang.lsp* resides in a directory that is in the AutoCAD support file search path, the following command compiles this program:

```
(vlisp-compile 'st "yinyang.lsp")
T
```

The output file is named
*yinyang.fas* and resides in the same directory as the source file.

The following command compiles
*yinyang.lsp* and names the output file
*GoodKarma.fas*:

```
(vlisp-compile 'st "yinyang.lsp" "GoodKarma.fas")
```

Note that the output file from the previous command resides in the AutoCAD installation directory,
*not* the directory where
*yinyang.lsp* resides. The following command compiles
*yinyang.lsp* and directs the output file to the
*c:\my documents* directory:

```
(vlisp-compile 'st "yinyang.lsp" "c:/my documents/GoodKarma")
```

This last example identifies the full path of the file to be compiled:

```
(vlisp-compile 'st "<AutoCAD installation directory>/Sample/yinyang.lsp")
```

The output file from this command is named
*yinyang.fas* and resides in the same directory as the input file.

#### Related References

* [vl-get-resource (AutoLISP/Visual LISP IDE)](vl-get-resource-AutoLISP-Visual-LISP-IDE.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*