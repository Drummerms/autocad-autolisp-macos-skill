# About Auto-Loading and Running AutoLISP Routines

Load AutoLISP routines at start up and execute commands or functions at specific times during a drawing session.

AutoCAD-based products and AutoCAD LT load the contents of three user-definable files automatically:

| User-definable File | Windows | | Mac OS | |
| AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT |
| *acad.lsp* | ✓ | -- | ✓ | -- |
| *acaddoc.lsp* | ✓ | -- | ✓ | -- |
| *acadlt.lsp* | -- | ✓ | -- | -- |
| *acadltdoc.lsp* | -- | ✓ | -- | -- |
| MNL file accompanied by current customization file | ✓ | -- | ✓ | -- |

By default, the
*acad.lsp* or
*acadlt.lsp* file is loaded only once, when the product starts, whereas the
*acaddoc.lsp* or
*acadltdoc.lsp* file is loaded with each individual document (or drawing). This lets you associate the loading of the
*acad.lsp* or
*acadlt.lsp* file with application startup, and the
*acaddoc.lsp* or
*acadltdoc.lsp* file with document (or drawing) startup. The default method for loading these startup files can be modified by changing the
setting of the ACADLSPASDOC system variable.

If one of these files defines a function of the special type
S::STARTUP, this routine runs immediately after the drawing is fully initialized. As an alternative, the APPLOAD command provides a
Startup Suite option that loads the specified applications without the need to edit any files.

The
*acad.lsp* or
*acadlt.lsp* and
*acaddoc.lsp* or
*acadltdoc.lsp* startup files are not provided with the product. It is up to the user to create and maintain these files.

NOTE:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the product is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Command Autoloader

When you load an AutoLISP file, the command definitions in the file take up memory whether or not you actually use the commands.
The AutoLISP
autoload function makes a command available without loading the entire routine into memory. Adding the following code to your
*acaddoc.lsp* or
*acadltdoc.lsp* file automatically loads the commands CMD1, CMD2, and CMD3 from the
*cmds.lsp* file and the NEWCMD command from the
*newcmd.lsp* file.

```
(autoload "CMDS" '("CMD1" "CMD2" "CMD3"))
(autoload "NEWCMD" '("NEWCMD"))
```

The first time you enter an automatically loaded command at the Command prompt, AutoLISP loads the entire command definition
from the associated file. AutoLISP also provides the
autoarxload function for ObjectARX applications.

NOTE:Like-named AutoLISP startup files are loaded based on their Modified time stamp; the LSP file with the most recent time stamp
is loaded unless you specify the full file name (including the file name extension).

## The ACAD.LSP or ACADLT.LSP File

You can create an
*acad.lsp* or
*acadlt.lsp* file if you regularly use specific AutoLISP routines. When you start AutoCAD, it searches the support file search path for
an
*acad.lsp* or
*acadlt.lsp* file. If an
*acad.lsp* or
*acadlt.lsp* file is found, it is loaded into memory.

Because the
*acad.lsp* or
*acadlt.lsp* file is intended to be used for application-specific startup routines, all functions and variables defined in an
*acad.lsp* or
*acadlt.lsp* file are only available in the first drawing. You will probably want to move routines that should be available in all documents
from your
*acad.lsp* or
*acadlt.lsp* file into the
*acaddoc.lsp* or
*acadltdoc.lsp* file.

The recommended functionality of
*acad.lsp* or
*acadlt.lsp* and
*acaddoc.lsp* or
*acadltdoc.lsp* can be overridden with the ACADLSPASDOC system variable. If the ACADLSPASDOC system variable is set to 0 (the default setting),
the
*acad.lsp* or
*acadlt.lsp* file is loaded just once: upon application startup. If set to 1, the
*acad.lsp* or
*acadlt.lsp* file is reloaded when a new drawing is created or an existing drawing file is opened.

The
*acad.lsp* or
*acadlt.lsp* file can contain AutoLISP code for one or more routines, or just a series of
load function calls. The latter method is preferable, because modification is easier. If you save the following code as an
*acad.lsp* or
*acadlt.lsp* file, the files
*mysessionapp1.lsp*,
*databasesynch.lsp*, and
*drawingmanager.lsp* are loaded every time you start the product.

```
(load "mysessionapp1")
(load "databasesynch")
(load "drawingmanager")
```

NOTE:Do not modify the reserved
*acad<release>.lsp* or
*acadlt<release>.lsp* files. Autodesk provides the
*acad<release>.lsp* or
*acadlt<release>.lsp* file, which contains required, release-specific AutoLISP-defined functions. This file is loaded into memory immediately before
the
*acad.lsp* or
*acadlt.lsp* file is loaded.
*<release>* represents the release of the product; for example,
*acad2026.lsp* would be the file loaded by AutoCAD and AutoCAD
2026-based products and
*acadlt2026.lsp* would be the file loaded by AutoCAD LT
2026.

## The ACADDOC.LSP or ACADLTDOC.LSP File

The
*acaddoc.lsp* or
*acadltdoc.lsp* file is intended to be associated with each document (or drawing) initialization. This file is useful if you want to load
a library of AutoLISP routines to be available every time you start a new drawing (or open an existing drawing).

Each time a drawing opens, AutoCAD searches the library path for an
*acaddoc.lsp* or
*acadltdoc.lsp* file. If it finds one, it loads the file into memory. The
*acaddoc.lsp* or
*acadltdoc.lsp* file is always loaded with each drawing regardless of the settings of ACADLSPASDOC.

Most users will have a single
*acaddoc.lsp* or
*acadltdoc.lsp* file for all document-based AutoLISP routines. The product searches for an
*acaddoc.lsp* or
*acadltdoc.lsp* file in the order defined by the library path; therefore, with this feature, you can have a different
*acaddoc.lsp* or
*acadltdoc.lsp* file in each drawing directory, which would load specific AutoLISP routines for certain types of drawings or jobs.

The
*acaddoc.lsp* or
*acadltdoc.lsp* file can contain AutoLISP code for one or more routines, or just a series of
load function calls. The latter method is preferable, because modification is easier. If you save the following code as an
*acaddoc.lsp* or
*acadltdoc.lsp* file, the files
*mydocumentapp1.lsp*,
*build.lsp*, and
*counter.lsp* are loaded every time a new document is opened.

```
(load "mydocumentapp1")
(load "build")
(load "counter")
```

NOTE:Do not modify the reserved
*acad<release>doc.lsp* or
*acadlt<release>doc.lsp* file. Autodesk provides the
*acad<release>doc.lsp* or
*acadlt<release>doc.lsp* file, which contains required, release-specific, AutoLISP-defined functions. This file is loaded into memory immediately
before the
*acaddoc.lsp* or
*acadltdoc.lsp* file is loaded.
*<release>* represents the release of the product; for example,
*acad2026doc.lsp* would be the file loaded by AutoCAD and AutoCAD
2026-based products and
*acadlt2026doc.lsp* would be the file loaded by AutoCAD LT
2026.

## MNL Files and AutoLISP Menu Customization

When the product loads a customization (CUI/CUIx) file, it searches for an MNL file with a matching file name. If it finds
the file, it loads the file into memory. This function ensures that the AutoLISP functions that are needed for proper operation
of user interface elements are loaded.

NOTE:AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
LOAD function from another LISP file.

For example, if the product loads a customization file named
*custom.cuix* it will looks for a file named
*custom.mnl* which might define numerous AutoLISP functions used by user interface elements in the customization file. The MNL file is
loaded after the
*acaddoc.lsp* file.

NOTE:If a customization file is loaded with the AutoLISP
command function—with syntax similar to
(command "menu" "newmenu")—the associated MNL file is not loaded until the entire AutoLISP routine has run.

```
(command "menu" "newmenu")

(princ "Newmenu utilities… Loaded.")
(Princ)
```

In this example, calls to the
princ function can be used to display status messages. The first use of
princ displays the following at the command prompt:

Newmenu utilities… Loaded.

The second call to
princ exits the AutoLISP function. Without this second call to
princ, the message would be displayed twice. As mentioned previously, you can include the
*onfailure* argument with calls to the
load function as an extra precaution.

## S::STARTUP Function: Postinitialization Execution

You can define an S::STARTUP function to perform any needed setup operations after the drawing is initialized.

The startup LISP files (*acad.lsp* or
*acadlt.lsp*, and
*acaddoc.lsp* or
*acadltdoc.lsp*) are all loaded into memory along with any automatically loaded MNL files before the drawing is completely initialized. Typically,
this does not pose a problem, unless you want to use the
command function, which is not guaranteed to work until after a drawing is initialized.

NOTE:AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
LOAD function from another LISP file.

If the user-defined function
S::STARTUP is included in an
*acad.lsp* or
*acadlt.lsp*,
*acaddoc.lsp* or
*acadltdoc.lsp*, or MNL file, it is called when you enter a new drawing or open an existing drawing. Thus, you can include a definition of
S::STARTUP in the AutoLISP startup file to perform any setup operations.

For example, if you want to override the standard HATCH command by adding a message and then switching to the BHATCH command,
use an
*acaddoc.lsp* or
*acadltdoc.lsp* file that contains the following:

```
(defun C:HATCH ( )
  (alert "Using the BHATCH command!")
  (princ "\
Enter OLDHATCH to get to real HATCH command.\
")
  (command "BHATCH")
  (princ)
)
(defun C:OLDHATCH ( )
  (command ".HATCH")
  (princ)
)
(defun-q S::STARTUP ( )
  (command "undefine" "hatch")
  (princ "\
Redefined HATCH to BHATCH!\
")
)
```

Before the drawing is initialized, new definitions for HATCH and OLDHATCH are defined with the
defun function. After the drawing is initialized, the
S::STARTUP function is called and the standard definition of HATCH is undefined.

NOTE:To be appended, the
S::STARTUP function must have been defined with the
defun-q function rather than
defun.

Because an
S::STARTUP function can be defined in many places (an
*acad.lsp* or
*acadlt.lsp*,
*acaddoc.lsp* or
*acadltdoc.lsp*, or MNL file or any other AutoLISP file loaded from any of these), it's possible to overwrite a previously defined
S::STARTUP function.

The following example shows one method of ensuring that your startup function works with other functions.

```
(defun-q MYSTARTUP ( )
```

*... your startup function ...*

```
)
(setq S::STARTUP (append S::STARTUP MYSTARTUP))
```

The previous code appends your startup function to that of an existing
S::STARTUP function and then redefines the
S::STARTUP function to include your startup code. This works properly regardless of the prior existence of an
S::STARTUP function.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About AutoLISP Applications](About-AutoLISP-Applications.md)
* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)
* [About AutoLISP Errors When Loading Startup Files](About-AutoLISP-Errors-When-Loading-Startup-Files.md)
* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*