# print (AutoLISP)

Prints an expression to the command line, or writes an expression to an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(print [expr [file-desc]])
```

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Subroutine, Ename (entity name), T, or nil

    A string or AutoLISP expression. Only the specified
    *expr* is printed; no newline or space is included.

*file-desc*
:   *Type:* File or nil

    A file descriptor for a file opened for writing.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The value of the evaluated
*expr*. If called with no arguments,
print returns a null symbol.

## Remarks

This function is the same as
prin1, except it prints a newline character before
*expr*, and prints a space following
*expr*.

## Examples

N/A

#### Related References

* [prin1 (AutoLISP)](prin1-AutoLISP.md)
* [princ (AutoLISP)](princ-AutoLISP.md)
* [prompt (AutoLISP)](prompt-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*