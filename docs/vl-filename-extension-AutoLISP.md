# vl-filename-extension (AutoLISP)

Returns the extension from a file name, after stripping out the rest of the name

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-filename-extension filename)
```

*filename*
:   *Type:* String

    File name, including the extension. The
    vl-filename-extension function does not check to see if the specified file exists.

## Return Values

*Type:* String or nil

A string containing the extension of
*filename*. The returned string starts with a period (.) and is in uppercase. If
*filename* does not contain an extension,
vl-filename-extension returns
nil.

## Examples

Windows
:   ```
    (vl-filename-extension "c:\\acadwin\\output.txt")
    ".txt"

    (vl-filename-extension "c:\\acadwin\\output")
    nil
    ```

Mac OS and Web
:   ```
    (vl-filename-extension "/myutilities/support/output.txt")
    ".txt"

    (vl-filename-extension "/myutilities/support/output")
    nil
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-size (AutoLISP)](vl-file-size-AutoLISP.md)
* [vl-file-systime (AutoLISP)](vl-file-systime-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*