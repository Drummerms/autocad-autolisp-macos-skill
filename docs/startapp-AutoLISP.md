# startapp (AutoLISP)

Starts an external application

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(startapp appcmd [file])
```

*appcmd*
:   *Type:* String

    Application to execute. If
    *appcmd* does not include a full path name,
    startapp searches the directories in the PATH environment variable on Windows for the application and the equivalent on Mac OS.

*file*
:   *Type:* String

    File name to be opened.

## Return Values

*Type:* Integer or nil

A numeric value greater than 0, if successful; otherwise
nil.

## Examples

Windows
:   The following code starts Notepad and opens the
    *acad.lsp* file.

    ```
    (startapp "notepad" "acad.lsp")
    33
    ```

    If an argument has embedded spaces, it must be surrounded by literal double quotes. For example, to edit the file
    *my stuff.txt* with Notepad, use the following syntax:

    ```
    (startapp "notepad.exe" "\"my stuff.txt\"")
    33
    ```

Mac OS
:   The following code starts TextEdit and opens the
    *acad.lsp* file.

    ```
    (startapp "textedit" "acad.lsp")
    33
    ```

    If an argument has embedded spaces, it must be surrounded by literal double quotes. For example, to edit the file
    *my stuff.txt* with TextEdit, use the following syntax:

    ```
    (startapp "textedit.app" "\"my stuff.txt\"")
    33
    ```

#### Related References

* [showhtmlmodalwindow (AutoLISP)](showhtmlmodalwindow-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*