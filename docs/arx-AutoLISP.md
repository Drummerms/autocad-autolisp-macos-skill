# arx (AutoLISP)

Returns a list of the currently loaded ObjectARX® applications

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(arx)
```

No arguments.

## Return Values

*Type:* String

A list of ObjectARX application file names; the path is not included in the file name.

## Examples

```
(arx)
```

Windows and Web
:   ```
    ("acapp.arx" "acmted.arx" ...)
    ```

Mac OS
:   ```
    ("acapp.bundle" "acmted.crx" ...)
    ```

#### Related References

* [arxload (AutoLISP)](arxload-AutoLISP.md)
* [arxunload (AutoLISP)](arxunload-AutoLISP.md)

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*