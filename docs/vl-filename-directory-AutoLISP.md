# vl-filename-directory (AutoLISP)

Returns the directory path of a file, after stripping out the name and extension

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-filename-directory filename)
```

*filename*
:   *Type:* String

    Complete file name, including the path. The
    vl-filename-directory function does not check to see if the specified file exists. Slashes (/) and backslashes (\) are accepted as directory delimiters.

## Return Values

*Type:* String

A textual value containing the directory portion of
*filename*, in uppercase.

## Examples

Windows
:   ```
    (vl-filename-directory "c:\\acadwin\\template.txt")
    "C:\\ACADWIN"

    (vl-filename-directory "template.txt")
    ""
    ```

Mac OS and Web
:   ```
    (vl-filename-directory "/myutilities/support/template.txt")
    "/myutilities/support"

    (vl-filename-directory "template.txt")
    ""
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-size (AutoLISP)](vl-file-size-AutoLISP.md)
* [vl-file-systime (AutoLISP)](vl-file-systime-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)
* [vl-mkdir (AutoLISP)](vl-mkdir-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*