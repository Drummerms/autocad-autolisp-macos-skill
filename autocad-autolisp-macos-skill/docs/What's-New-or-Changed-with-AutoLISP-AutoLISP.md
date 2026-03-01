# What's New or Changed with AutoLISP (AutoLISP)

The following is an overview of the changes made to AutoLISP in recent releases.

## AutoCAD 2026

No new or changed functions

## AutoCAD 2025

acet-load-expresstools function was added to AutoCAD for Windows only. This function is used to initialize the Express Tools functions.

## AutoCAD 2024

New
:   * No new or changed functions
    * AutoCAD LT for Windows now supports AutoLISP and DCL

      Here are some of the known limitations or differences from AutoCAD:

      + Most
        VL\*,
        VLA\*,
        VLAX\*, and
        VLR\* functions are supported, but the use of third-party automation libraries is not supported in to AutoCAD LT.

        Here is a high-level summary of the functions that are not supported:

        - vlax-create-object
        - vlax-get-object
        - vlax-get-or-create-object
        - vlax-import-type-library
        - vla-GetInterfaceObject
        - VLA\* functions related to creating and modifying 3D solid and surface, helix, material, multiline objects among others that can
          only be created in AutoCAD
      + entmake,
        entmakex, and
        entmod functions only allow for the creation and modification of objects supported in AutoCAD LT
      + AutoLISP functions exposed by custom ObjectARX and Managed .NET programs can't be used
      + ActiveX limitations:
        - PreferencesProfiles object exists as part of the ActiveX implementation, but all of its methods and properties have been removed since profiles
          are not supported in AutoCAD LT for Windows
        - Creation of 3D meshes, surfaces, and solids is not supported, while support is limited for the modification of 3D objects
      + Developing AutoLISP program limitations:
        - Visual LISP integrated development environment (IDE) and VLIDE/VLISP commands are not available in AutoCAD LT for Windows
        - Debugging with the AutoLISP Extension in Visual Studio Code is not supported in AutoCAD LT for Windows
      + Deploying AutoLISP program limitations:
        - MNL files are not automatically loaded with CUIx files that have the same name, but the files can be loaded using the AutoLISP
          LOAD function from another LISP file
        - Compiled LSP files are supported in AutoCAD LT for Windows, but compiling LSP files can only be done in AutoCAD for Windows
          only

      Programs that utilize functions and commands that are limited to AutoCAD should check which product they are being loaded
      into to avoid compatibility problems. This can be done using the PROGRAM system variable, a value of
      acadlt is returned for AutoCAD LT.

      The following example restricts the loading of a DVB file and the definition of a command that runs a VBA macro based on if
      the code is loaded into AutoCAD or AutoCAD LT:

      ```
      (if (/= (strcase (getvar "PROGRAM") T) "acadlt")
        (progn
          (vl-load-com)

          ;; Load a DVB file
          (setq retVal (vl-catch-all-apply 'vl-vbaload (list (findfile "sample/vba/drawline.dvb"))))

          ;; If the DVB file was found, then define the function to run the function
          (if (not (vl-catch-all-error-p retVal))
            (defun c:DRAWLINE (/)(vl-vbarun "drawline"))
            (prompt "\
      drawline.dvb is missing")
          )

          (prompt "\
      Enter DRAWLINE to run the VBA macro.")(princ)
        )
        (progn (prompt "\
      VBA macros are not supported on AutoCAD LT.")(princ))
      )
      ```

## AutoCAD 2023

* No new or changed functions
* AutoLISP is now available on AutoCAD web for AutoCAD subscribers only

## AutoCAD 2022

No new or changed functions.

## AutoCAD 2021

New
:   * *AutoCAD AutoLISP Extension for Visual Studio (VS) Code* - Allows for the editing and debugging of AutoLISP files with VS Code on Windows or Mac OS. The LISPSYS system variable must
      to set to 1 or 2 in order to debug AutoLISP files with the AutoCAD AutoLISP Extension. When LISPSYS is set to 0, the legacy
      AutoLISP engine and Visual LISP IDE are used for editing and debugging AutoLISP files.
    * *DCL support on Mac OS* - Dialog boxes defined using DCL can now be displayed with AutoLISP. All DCL tiles supported on Windows are also supported
      on Mac OS, but not all tile attributes are supported on Mac OS.

Changed
:   These functions were updated to support Unicode character strings/codes:

    * *[ascii](ascii-AutoLISP.md)* - Returns the conversion of the first character of a string into its Unicode character code (an integer).
    * *[chr](chr-AutoLISP.md)* - Converts an integer representing a Unicode character code into a single-character string.
    * *[load](load-AutoLISP.md)* - Evaluates the AutoLISP expressions in a file.
    * *[open](open-AutoLISP.md)* - Opens a file for access by the AutoLISP I/O functions. A new optional argument has been added which allows for the specification
      of the character encoding to be used when reading/writing the file. When the argument isn't provided, the file is assumed
      to contain a multibyte character set (MBCS) which is the legacy behavior.
    * *[read-char](read-char-AutoLISP.md)* - Returns the integer representing the Unicode character read from the keyboard input buffer or from an open file.
    * *[read-line](read-line-AutoLISP.md)* - Reads a string from the keyboard or from an open file, until an end-of-line marker is encountered.
    * *[strlen](strlen-AutoLISP.md)* - Returns an integer that is the number of characters in a string.
    * *[substr](substr-AutoLISP.md)* - Returns a substring of a string.
    * *[vl-directory-files](vl-directory-files-AutoLISP.md)* - Lists all files in a given directory.
    * *[vl-file-copy](vl-file-copy-AutoLISP.md)* - Copies or appends the contents of one file to another file.
    * *[vl-file-delete](vl-file-delete-AutoLISP.md)* - Deletes a file.
    * *[vl-file-directory-p](vl-file-directory-p-AutoLISP.md)* - Determines if a file name refers to a directory.
    * *[vl-file-rename](vl-file-rename-AutoLISP.md)* - Renames a file.
    * *[vl-file-size](vl-file-size-AutoLISP.md)* - Determines the size of a file, in bytes.
    * *[vl-file-systime](vl-file-systime-AutoLISP.md)* - Returns last modification time of the specified file.
    * *[vl-filename-mktemp](vl-filename-mktemp-AutoLISP.md)* - Calculates a unique file name to be used for a temporary file.
    * *[vl-list->string](vl-list-string-AutoLISP.md)* - Combines the Unicode characters associated with a list of integers into a string.
    * *[vl-mkdir](vl-mkdir-AutoLISP.md)* - Creates a directory.
    * *[vl-string->list](vl-string-list-AutoLISP.md)* - Converts a string into a list of Unicode character codes.
    * *[vl-string-elt](vl-string-elt-AutoLISP.md)* - Returns the Unicode representation of the character at a specified position in a string.
    * *[vl-string-mismatch](vl-string-mismatch-AutoLISP.md)* - Returns the length of the longest common prefix for two strings, starting at specified positions.
    * *[vl-string-position](vl-string-position-AutoLISP.md)* - Looks for a character with the specified Unicode code in a string.
    * *[vl-string-search](vl-string-search-AutoLISP.md)* - Searches for the specified pattern in a string.
    * *[vl-string-subst](vl-string-subst-AutoLISP.md)* - Substitutes one string for another, within a string.
    * *[vl-string-translate](vl-string-translate-AutoLISP.md)* - Replaces characters in a string with a specified set of characters.
    * *[vl-vbaload](vl-vbaload-AutoLISP.md)* - Loads a VBA project.
    * *[vlisp-compile](vlisp-compile-AutoLISP-Visual-LISP-IDE.md)* - Compiles AutoLISP source code into a FAS file.
    * *[write-char](write-char-AutoLISP.md)* - Writes one Unicode character to the screen or an open file.
    * *[write-line](write-line-AutoLISP.md)* - Writes a string to the screen or to an open file.

Obsolete
:   *Visual LISP IDE (AutoCAD for Windows Only)* - The Visual LISP (VL) IDE has been retired and will be removed in a future release. It is recommended to use the AutoCAD
    AutoLISP Extension for Visual Studio (VS) Code creating new and updating existing AutoLISP programs. LISPSYS must be set to
    0 before the VL IDE can be used to edit and debug AutoLISP files.

## AutoCAD 2020

No new or changed functions.

## AutoCAD 2019

No new or changed functions.

## AutoCAD 2018

No new or changed functions.

## AutoCAD 2017

No new or changed functions.

## AutoCAD 2016

Changed
:   *[osnap](osnap-AutoLISP.md)* - Returns a 3D point that is the result of applying an Object Snap mode to a specified point. The function no longer accepts
    the
    qui mode. Using the
    qui mode results in a value of
    nil to be returned, even if other modes are specified.

Obsolete
:   * *[getcfg](getcfg-AutoLISP.md)* - Retrieves application data from the AppData section of the
      *acad20xx.cfg* file.
    * *[setcfg](setcfg-AutoLISP.md)* - Writes application data to the AppData section of the
      *acad20xx.cfg* file.

NOTE:getcfg and
setcfg are still available for compatibility, but might be removed in a future release. It is recommended to use the
vl-registry-read and
vl-registry-write functions as replacements.

## AutoCAD 2015

No new or changed functions.

## AutoCAD 2014

New
:   * *[findtrustedfile](findtrustedfile-AutoLISP.md)* - Searches the AutoCAD trusted file paths for the specified file.
    * *[showHTMLModalWindow](showhtmlmodalwindow-AutoLISP.md)* - Displays a modal window with a HTML document; use in conjunction with the new JavaScript API.

Changed
:   * *[findfile](findfile-AutoLISP.md)* - Searches the AutoCAD support and trusted file paths. Function was updated to search the new trusted applications paths.

## AutoCAD 2013

New
:   * *[vlax-machine-product-key](vlax-machine-product-key-AutoLISP-ActiveX.md)* - Returns the AutoCAD Windows registry path in the HKLM (HKEY\_LOCAL\_MACHINE).

Obsolete
:   * *[vlax-product-key](vlax-product-key-AutoLISP-ActiveX.md)* - Returns the AutoCAD Windows registry path.

## AutoCAD 2012

New
:   * *[command-s](command-s-AutoLISP.md)* - Executes an AutoCAD command and the supplied input.
    * *[\*pop-error-mode\*](pop-error-mode-AutoLISP.md)* - Error-handling function that ends the previous call to
      \*push-error-using-command\* or
      \*push-error-using-stack\*.
    * *[\*push-error-using-command\*](push-error-using-command-AutoLISP.md)* - Error-handling function that indicates the use of the command function within a custom
      \*error\* handler.
    * *[\*push-error-using-stack\*](push-error-using-stack-AutoLISP.md)* - Error-handling function that indicates the use of variables from the AutoLISP stack within a custom
      \*error\* handler.

## AutoCAD 2011

New
:   * *[dumpallproperties](dumpallproperties-AutoLISP.md)* - Retrieves an entity’s supported properties.
    * *[getpropertyvalue](getpropertyvalue-AutoLISP.md)* - Returns the current value of an entity’s property.
    * *[ispropertyreadonly](ispropertyreadonly-AutoLISP.md)* - Returns the read-only state of an entity’s property.
    * *[setpropertyvalue](setpropertyvalue-AutoLISP.md)* - Sets the property value for an entity.

## AutoCAD 2010

Changes
:   * *[help](help-AutoLISP.md)* - Invokes the Help facility. Function was updated to add support for HTML documentation.

## AutoCAD 2009

New
:   * *[initcommandversion](initcommandversion-AutoLISP.md)* - Forces the next command to run with the specified version.

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP and Visual LISP (AutoLISP)](AutoLISP-and-Visual-LISP-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*