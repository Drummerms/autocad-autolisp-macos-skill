# vl-load-all (AutoLISP)

Loads a file into all open AutoCAD documents, and into any document subsequently opened during the current AutoCAD session

*Supported Platforms:* Windows, Mac OS, and Web

## Syntax

```
(vl-load-all filename)
```

*filename*
:   *Type:* String

    File to be loaded. If the file is in the AutoCAD support file search path, you can omit the path name, but you must always
    specify the file extension;
    vl-load-all does not assume a file type.

## Return Values

*Type:* nil or error

nil if successful; otherwise, an error occurs when
*filename* is not found.

## Examples

Windows
:   ```
    (vl-load-all "c:/my documents/visual lisp/examples/whichns.lsp")
    nil

    (vl-load-all "yinyang.lsp")
    nil
    ```

Mac OS
:   ```
    (vl-load-all "/myutilities/lsp/utilities.lsp")
    nil

    (vl-load-all "utilities.lsp")
    nil
    ```

#### Related Tasks

* [To load functions across all document namespaces (AutoLISP)](To-load-functions-across-all-document-namespaces-AutoLISP.md)

#### Related References

* [load (AutoLISP)](load-AutoLISP.md)
* [arxload (AutoLISP)](arxload-AutoLISP.md)
* [vl-vbaload (AutoLISP)](vl-vbaload-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*