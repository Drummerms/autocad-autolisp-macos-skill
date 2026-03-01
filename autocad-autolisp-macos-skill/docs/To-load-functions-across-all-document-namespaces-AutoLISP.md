# To load functions across all document namespaces (AutoLISP)

Normally, loading an application file loads it in the current drawing only, but the vl-load-all function can be used to load a file in all drawings.

* At the AutoCAD Command prompt, enter an AutoLISP statement that uses the vl-load-all function and press Enter.

NOTE:The vl-load-all function is useful for testing new functions in multiple documents, but in general you should use *acaddoc.lsp* to load files that are needed in every document.

## Example

1. At the AutoCAD Command prompt, enter *(load "yinyang.lsp")* and press Enter.
2. Invoke a function defined in the AutoLISP source (LSP) file.

   The function should work as expected.
3. Create a new or open an existing drawing.
4. With the second drawing window active, try invoking the function again.

   The response will be an error message saying the function is not defined.
5. At the AutoCAD Command prompt, enter *(vl-load-all "yinyang.lsp")* and press Enter.
6. Create a new or open an existing drawing.
7. Invoke the function again.

   This time the function will work correctly because the vl-load-all function loads the contents of an AutoLISP file into all open documents, and into any documents opened later in the session.

#### Related Concepts

* [About Source Code Files (AutoLISP)](About-Source-Code-Files-AutoLISP.md)
* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)
* [About Namespaces (AutoLISP)](About-Namespaces-AutoLISP.md)
* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*