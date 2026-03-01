# About AutoLISP Applications

AutoLISP is based on the LISP programming language, which is simple to learn and very powerful for automating design tasks.
Because AutoCAD has a built-in LISP interpreter, you can enter AutoLISP code at the Command prompt or load AutoLISP code from
external files.

NOTE:Even if you are not interested in learning to write AutoLISP applications, the product includes many useful routines. AutoLISP
applications are also available for download from the Internet or third-party developers. Knowing how to load and use these
routines can enhance your productivity.

When an AutoLISP application is loaded, it functions in its own
*namespace* for each drawing that is open. A namespace is an insulated environment keeping AutoLISP applications that are specific to
one drawing from having symbol or variable name and value conflicts with those in another drawing. For example, the following
line of code sets a different value to the symbol
a when executed in each open drawing.

```
(setq a (getvar "DWGNAME"))
```

AutoLISP applications can prompt the user for input, access built-in AutoCAD commands directly, and modify or create objects
directly in the drawing database. By creating AutoLISP routines you can add discipline-specific or workflow driven commands
to AutoCAD. Some of the standard AutoCAD commands are actually AutoLISP applications.

You may choose to experiment by entering code at the Command prompt, which allows you to see the results immediately. This
makes AutoLISP an easy language to experiment with, regardless of your programming experience.

AutoLISP provides three file formats for applications:

* AutoLISP Source Code (.*lsp*) file—an ASCII text file that contains AutoLISP program code.
* Fast-load AutoLISP (.*fas*) file—a binary, compiled version of a single LSP program file.
* Visual LISP Compiled (.*vlx*) file—a compiled set of one or more LSP and/or dialog control language (DCL) files.

NOTE:VLX files are supported on Windows only.

#### Topics in this section

* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)

  AutoLISP files need to be loaded into the program before they can be used.
* [About Auto-Loading and Running AutoLISP Routines](About-Auto-Loading-and-Running-AutoLISP-Routines.md)

  Load AutoLISP routines at start up and execute commands or functions at specific times during a drawing session.
* [About -TEXT and TEXTEVAL in AutoLISP](About-TEXT-and-TEXTEVAL-in-AutoLISP.md)

  The -TEXT command checks the setting of the TEXTEVAL system variable setting only if it is used in a script or AutoLISP expression
  and all the command prompts are responded to within the script or an AutoLISP expression.
* [About AutoLISP Errors When Loading Startup Files](About-AutoLISP-Errors-When-Loading-Startup-Files.md)

  If an AutoLISP error occurs while you are loading a startup file, the remainder of the file is ignored and is not loaded.

#### Related References

* [About -TEXT and TEXTEVAL in AutoLISP](About-TEXT-and-TEXTEVAL-in-AutoLISP.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)
* [About Auto-Loading and Running AutoLISP Routines](About-Auto-Loading-and-Running-AutoLISP-Routines.md)
* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*