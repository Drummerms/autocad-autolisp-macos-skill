# About AutoLISP Errors When Loading Startup Files

If an AutoLISP error occurs while you are loading a startup file, the remainder of the file is ignored and is not loaded.

Files specified in a startup file that do not exist or that are not in the product's library paths generally causes an error.
Therefore, you may want to use the
 *onfailure*  argument with the
load function. The following example uses the
 *onfailure*  argument:

```
(princ (load "mydocapp1" "\
MYDOCAPP1.LSP file not loaded."))
(princ (load "build" "\
BUILD.LSP file not loaded."))
(princ (load "counter" "\
COUNTER.LSP file not loaded."))
(princ)
```

If a call to the
load function is successful, it returns the value of the last expression in the file (usually the name of the last defined function
or a message regarding the use of the function). If the call fails, it returns the value of the
*onfailure* argument. In the preceding example, the value returned by the
load function is passed to the
princ function, causing that value to be displayed at the command prompt.

For example, if an error occurs while the product loads the
*mydocapp1.lsp* file, the
princ function displays the following message and the product continues to load the two remaining files:

MYDOCAPP1.LSP file not loaded.

If you use the
command function in an
*acad.lsp* or
*acadlt.lsp*,
*acaddoc.lsp* or
*acadltdoc.lsp*, or MNL file, it should be called only from within a
defun statement. Use the
S::STARTUP function to define commands that need to be issued immediately when you begin a drawing session.

NOTE:AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
LOAD function from another LISP file.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Auto-Loading and Running AutoLISP Routines](About-Auto-Loading-and-Running-AutoLISP-Routines.md)
* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)
* [About AutoLISP Applications](About-AutoLISP-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*