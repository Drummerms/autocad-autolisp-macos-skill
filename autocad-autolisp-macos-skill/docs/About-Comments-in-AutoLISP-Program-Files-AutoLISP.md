# About Comments in AutoLISP Program Files (AutoLISP)

Comments are useful to both the programmer and future users who may need to revise a program to suit their needs.

It is good coding practice to include comments in all AutoLISP program files, small and large. Use comments to do the following:

* Give a title, authorship, and creation date
* Provide instructions on using a routine
* Make explanatory notes throughout the body of a routine
* Make notes to yourself during debugging

Comments begin with one or more semicolons ( *;* ) and continue through the end of the line.

```
; This entire line is a comment
(setq area (* pi r r)) ; Compute area of circle
```

Any text within  *;| ... |;*  is ignored. Therefore, comments can be included within a line of code or extend for multiple lines. This type of comment
is known as an in-line comment.

```
(setq tmode ;|some note here|; (getvar "tilemode"))
```

The following example shows a comment that continues across multiple lines:

```
(setvar "orthomode" 1) ;|comment starts here
and continues to this line,
but ends way down here|; (princ "\
ORTHOMODE set On.")
```

#### Related Tasks

* [To Create and Open AutoLISP Source Code Files (AutoLISP)](To-Create-and-Open-AutoLISP-Source-Code-Files-AutoLISP.md)

#### Related Concepts

* [About Source Code Files (AutoLISP)](About-Source-Code-Files-AutoLISP.md)
* [About Getting Organized (AutoLISP)](About-Getting-Organized-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*