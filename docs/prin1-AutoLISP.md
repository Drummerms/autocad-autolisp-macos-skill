# prin1 (AutoLISP)

Prints an expression to the command line or writes an expression to an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(prin1 [expr [file-desc]])
```

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    A string or AutoLISP expression. Only the specified
    *expr* is printed; no newline or space is included.

*file-desc*
:   *Type:* File or nil

    A file descriptor for a file opened for writing.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The value of the evaluated
*expr*. If called with no arguments,
prin1 returns a null symbol.

Used as the last expression in a function,
prin1 without arguments prints a blank line when the function completes, allowing the function to exit “quietly.”

## Remarks

If
*expr* is a string containing control characters,
prin1 expands these characters with a leading \, as shown in the following table:

| Control codes | |
| Code | Description |
| \\ | \ character |
| \" | " character |
| \e | Escape character |
| \ | Newline character |
| \r | Return character |
| \t | Tab character |
| \ *nnn* | Character whose octal code is *nnn* |

The following shows how to use control characters:

```
(prin1 (chr 2))
"\002""\002"
```

## Examples

```
(setq a 123 b '(a))
(A)

(prin1 'a)
AA
```

The previous command printed A and returned A.

```
(prin1 a)
123123
```

The previous command printed 123 and returned 123.

```
(prin1 b)
(A)(A)
```

The previous command printed (A) and returned (A).

Each preceding example is displayed on the screen because no
*file-desc* was specified. Assuming that
f is a valid file descriptor for a file opened for writing, the following function call writes a string to that file and returns
the string:

```
(prin1 "Hello" f)
"Hello"
```

#### Related References

* [princ (AutoLISP)](princ-AutoLISP.md)
* [print (AutoLISP)](print-AutoLISP.md)
* [prompt (AutoLISP)](prompt-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*