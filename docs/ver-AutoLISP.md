# ver (AutoLISP)

Returns a string that contains the current AutoLISP version number

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ver)
```

No arguments.

## Return Values

*Type:* String

Textual value returned takes the following form:

```
"environment version (nn)"
```

where
*environment* is the name of the AutoLISP environment,
*version* is the current version number, and
*nn* is a two-letter language description.

Examples of the two-letter language descriptions are as follows:

(de) German

(en) US/UK

(es) Spanish

(fr) French

(it) Italian

## Remarks

The
ver function can be used to check the compatibility of programs.

## Examples

Windows and Web
:   ```
    (ver)
    "Visual LISP <release> (en)"
    ```

Mac OS
:   ```
    (ver)
    "MacOS AutoLISP <release> (en)"
    ```

#### Related Concepts

* [Application-Handling Functions Reference (AutoLISP)](Application-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*