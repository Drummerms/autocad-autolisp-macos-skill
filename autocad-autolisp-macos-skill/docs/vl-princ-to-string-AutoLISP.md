# vl-princ-to-string (AutoLISP)

Returns the string representation of LISP data as if it were output by the
princ function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-princ-to-string data)
```

*data*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Any AutoLISP data.

## Return Values

*Type:* String

A string containing the printed representation of
*data* as if displayed by
princ.

## Examples

Windows
:   ```
    (vl-princ-to-string "abc")
    "abc"

    (vl-princ-to-string "c:\\acadwin")
    "C:\\ACADWIN"

    (vl-princ-to-string 'my-var)
    "MY-VAR"
    ```

Mac OS
:   ```
    (vl-princ-to-string "abc")
    "abc"

    (vl-princ-to-string "/myutilities")
    "/myutilities"

    (vl-princ-to-string 'my-var)
    "MY-VAR"
    ```

#### Related References

* [vl-prin1-to-string (AutoLISP)](vl-prin1-to-string-AutoLISP.md)
* [princ (AutoLISP)](princ-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*