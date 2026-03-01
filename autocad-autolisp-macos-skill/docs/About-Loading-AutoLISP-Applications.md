# About Loading AutoLISP Applications

AutoLISP files need to be loaded into the program before they can be used.

AutoLISP applications are stored in editable ASCII or Unicode text files with the
*.lsp* extension. These files generally have a header portion that describes a routine, its use, and any specific instructions.
This header might also include comments that document the author and the legal information regarding the use of the routine.
Comments are preceded by a semicolon (;). You can view and edit these files with a text editor or word processor that can
produce an ASCII or Unicode text file.

IMPORTANT:Starting with
AutoCAD 2021-based products, AutoLISP source files can be saved in either ASCII or Unicode file formats.
AutoCAD 2020-based and earlier products, only support the ASCII file format.

Before you can use an AutoLISP application, it must first be loaded. You can use the APPLOAD command or the AutoLISP
load function to load an application. Loading an AutoLISP application loads the AutoLISP code from the LSP file into your system's
memory. You must specify a relative support path in the Filename parameter if the LSP file is not located in the Support File
Search Path.

NOTE:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations in the Support File Search Path; trusted locations are specified by the TRUSTEDPATHS system variable.

Loading an application with the
load function involves entering AutoLISP code at the command prompt. If the
load function is successful, it displays the value of the last expression in the file at the command prompt. This is usually the
name of the last function defined in the file or instructions on using the newly loaded function. If
load fails, it returns an AutoLISP error message. A
load failure can be caused by incorrect coding in the file or by providing the wrong file name. The syntax for the
load function is

```
(load filename [onfailure])
```

This syntax shows that the
load function has two arguments:
*filename*, which is required, and
*onfailure*, which is optional. When loading an AutoLISP file at the Command prompt, you typically supply only the
*filename* argument.

NOTE:Like-named AutoLISP application files are loaded based on their Modified time stamp; the LSP, FAS, or VLX file with the most
recent time stamp is loaded unless you specify the full file name (including the file name extension). VLX files are supported
on Windows only.

The following example loads the AutoLISP file
*newfile.lsp*.

Command:
*(load "newfile")*

The .*lsp* extension is not required. This format works for any LSP file in the current library path.

To load an AutoLISP file that is not in the library path, you must provide the full path and file name as the
*filename* argument.

Windows
:   Command:
    *(load "d:/files/morelisp/newfile")*

Mac OS and Web
:   Command:
    *(load "/files/morelisp/newfile")*

NOTE:When specifying a directory path, you must use a slash (/) or two backslashes (\\) as the separator, because a single backslash
has a special meaning in AutoLISP.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Auto-Loading and Running AutoLISP Routines](About-Auto-Loading-and-Running-AutoLISP-Routines.md)
* [About AutoLISP Applications](About-AutoLISP-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*