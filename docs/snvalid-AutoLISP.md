# snvalid (AutoLISP)

Checks the symbol table name for valid characters

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(snvalid sym_name [flag])
```

*sym\_name*
:   *Type:* String

    Symbol table name.

*flag*
:   *Type:* Integer

    Specifies whether the vertical bar character is allowed within
    *sym\_name*. The
    *flag* argument can be one of the following:

    *0* -- Do not allow vertical bar characters anywhere in
    *sym\_name*. This is the default.

    *1* -- Allow vertical bar characters in
    *sym\_name*, as long as they are not the first or last characters in the name.

## Return Values

*Type:* T or nil

T, if
*sym\_name* is a valid symbol table name; otherwise
nil.

## Remarks

The
snvalid function inspects the AutoCAD EXTNAMES system variable to determine the rules to enforce for the active drawing. If EXTNAMES
is 0,
snvalid validates using the symbol name rules in effect prior to AutoCAD 2000. If EXTNAMES is 1 (the default value),
snvalid validates using the rules for extended symbol names introduced with AutoCAD 2000. The following are not allowed in symbol
names, regardless of the setting of EXTNAMES:

* Control and graphic characters
* Null strings
* Vertical bars as the first or last character of the name

AutoLISP does not enforce restrictions on the length of symbol table names if EXTNAMES is 1.

If EXTNAMES is 1, all characters are allowed except control and graphic characters and the following:

| Characters disallowed in symbol table names | |
| < > | less-than and greater-than symbol |
| / \ | forward slash and backslash |
| " | quotation mark |
| : | colon |
| ? | question mark |
| \* | asterisk |
| | | vertical bar |
| , | comma |
| = | equal sign |
| ` | backquote |
| ; | semicolon (ASCII 59) |

A symbol table name may contain spaces.

If EXTNAMES is 0, symbol table names can consist of uppercase and lowercase alphabetic letters (e.g., A-Z), numeric digits
(e.g., 0-9), and the dollar sign ($), underscore (\_), and hyphen (-) characters.

## Examples

The following examples assume EXTNAMES is set to 1:

```
(snvalid "hocus-pocus")
T

(snvalid "hocus pocus")
T

(snvalid "hocus%pocus")
T
```

The following examples assume EXTNAMES is set to 0:

```
(snvalid "hocus-pocus")
T

(snvalid "hocus pocus")
nil

(snvalid "hocus%pocus")
nil
```

The following example includes a vertical bar in the symbol table name:

```
(snvalid "hocus|pocus")
nil
```

By default, the vertical bar character is considered invalid in all symbol table names.

In the following example, the
*flag* argument is set to 1, so
snvalid considers the vertical bar character to be valid in
*sym\_name*, as long as it is not the first or last character in the name:

```
(snvalid "hocus|pocus" 1)
T
```

#### Related References

* [tblobjname (AutoLISP)](tblobjname-AutoLISP.md)
* [tblsearch (AutoLISP)](tblsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*