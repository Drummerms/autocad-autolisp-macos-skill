# About Searching for Files (AutoLISP)

An application can use the
findfile function to search for a particular file name.

The application can specify the directory to search, or it can use the current AutoCAD library paths.

In the following example code,
findfile searches for the
*acad.pgp* file in the AutoCAD library paths:

```
(setq pgpname "acad.pgp")
(setq fil (findfile pgpname))
(if fil
  (setq pgpname fil)
  (princ (strcat "\
Could not find file " pgpname ". " ))
)
```

If the call to
findfile is successful, the variable
refname is set to a fully qualified path name string, as follows:

```
; On Windows
"<drive>:\\Users\\<username>\\appdata\\roaming\\autodesk\\
 <product>\\<release>\\<language>\\support\\acad.pgp"

; or

; On Mac
"/Users/<username>/Library/Application Support/Autodesk/Roaming/
 <product>/<release>/<language>/support/acad.pgp"
```

When specifying a path name, you must precede the backslash ( *\* ) with another backslash so the path name will be recognized by AutoLISP. Alternatively, you can use the slash character ( */* ) as a directory separator. The
getfiled function displays a dialog box containing a list of available files of a specified extension type in the specified directory.
This gives AutoLISP routines access to the AutoCAD Get File dialog box, a standard file navigation dialog box.

A call to
getfiled takes four arguments that determine the appearance and functionality of the dialog box. The application must specify the
following string values, each of which can be
nil: a title, placed at the top of the dialog box; a default file name, displayed in the edit box at the bottom of the dialog
box; and an extension type, which determines the initial files provided for selection in the list box. The final argument
is an integer value that specifies how the dialog box interacts with selected files.

This following example uses
getfiled to let the user browse the directory structure and select a file:

```
(defun C:DDIR ( )
  (setq *dfil (getfiled "Directory Listing" "" "" 2))
  (princ (strcat "\
Variable '*dfil' set to selected file " *dfil ))
 (princ)
)
```

The
\*dfil variable is set to the file you select, which can then be used by other AutoLISP functions or as a response to a command
prompt for a file name. To use this variable in response to a command prompt, enter
*!\*dfil*.

#### Related Concepts

* [About File Descriptors (AutoLISP)](About-File-Descriptors-AutoLISP.md)
* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*