# strlen (AutoLISP)

Returns an integer that is the number of characters in a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(strlen [str ...])
```

*str*
:   *Type:* String

    A textual value.

## Return Values

*Type:* Integer

A numeric value. If multiple
*str* arguments are provided,
strlen returns the sum of the lengths of all arguments. If you omit the arguments or enter an empty string,
strlen returns 0.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str* argument previously accepted an ASCII text string or character, but now accepts a Unicode text string or character.
* Return value was modified to support Unicode characters and might be different than earlier releases. In earlier releases,
  the length of a Unicode character was improperly calculated. For example,
  (strlen "中国") previously returned 14, but now returns 2.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(strlen "abcd")
4

(strlen "ab")
2

(strlen "one" "two" "four")
10

(strlen "中")
1

(strlen "测试")
2

(strlen)
0

(strlen "")
0
```

#### Related References

* [strcase (AutoLISP)](strcase-AutoLISP.md)
* [strcat (AutoLISP)](strcat-AutoLISP.md)
* [substr (AutoLISP)](substr-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*