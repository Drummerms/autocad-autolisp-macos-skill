# vl-prin1-to-string (AutoLISP)

Returns the string representation of LISP data as if it were output by the
prin1 function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-prin1-to-string data)
```

*data*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Any AutoLISP data.

## Return Values

*Type:* String

A textual value containing the printed representation of
*data* as if displayed by
prin1.

## Examples

Windows
:   ```
    (vl-prin1-to-string "abc")
    "\"abc\""

    (vl-prin1-to-string "c:\\acadwin")
    "\"C:\\\\ACADWIN\""

    (vl-prin1-to-string 'my-var)
    "MY-VAR"
    ```

Mac OS
:   ```
    (vl-prin1-to-string "abc")
    "\"abc\""

    (vl-prin1-to-string "/myutilities")
    "\"/myutilities\""

    (vl-prin1-to-string 'my-var)
    "MY-VAR"
    ```

#### Related References

* [vl-princ-to-string (AutoLISP)](vl-princ-to-string-AutoLISP.md)
* [prin1 (AutoLISP)](prin1-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*