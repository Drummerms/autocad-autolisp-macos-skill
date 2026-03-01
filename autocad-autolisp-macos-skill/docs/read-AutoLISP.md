# read (AutoLISP)

Returns the first list or atom obtained from a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(read [string])
```

*string*
:   *Type:* String

    A text value. The
    *string* argument should not contain blanks, except within a list or string.

## Return Values

*Type:* Integer, Real, List, Symbol, File, T, or nil

A list or atom. The
read function returns its argument converted into the corresponding data type. If no argument is specified,
read returns
nil.

If the string contains multiple AutoLISP expressions separated by AutoLISP symbol delimiters such as blanks, newline, tabs,
or parentheses, only the first expression is returned.

## Remarks

The
read function parses the string representation of any AutoLISP data and returns the first expression in the string, converting
it to a corresponding data type.

## Examples

```
(read "hello")
HELLO

(read "hello there")
HELLO

(read "\"Hi Y'all\"")
"Hi Y'all"

(read "(a b c)")
(A B C)

(read "(a b c) (d)")
(A B C)

(read "1.2300")
1.23

(read "87")
87

(read "87 3.2")
87
```

#### Related References

* [getstring (AutoLISP)](getstring-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*