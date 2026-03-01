# vl-filename-base (AutoLISP)

Returns the name of a file, after stripping out the directory path and extension

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-filename-base filename)
```

*filename*
:   *Type:* String

    File name. The
    vl-filename-base function does not check to see if the file exists.

## Return Values

*Type:* String

Textual value containing
*filename* in uppercase, with any directory and extension stripped from the name.

## Examples

Windows
:   ```
    (vl-filename-base "c:\\acadwin\\acad.exe")
    "ACAD"

    (vl-filename-base "c:\\acadwin")
    "ACADWIN"
    ```

Mac OS and Web
:   ```
    (vl-filename-base "/myutilities/lsp/utilities.lsp")
    "utilities"

    (vl-filename-base "/myutilities/support")
    "support"
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-size (AutoLISP)](vl-file-size-AutoLISP.md)
* [vl-file-systime (AutoLISP)](vl-file-systime-AutoLISP.md)
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*