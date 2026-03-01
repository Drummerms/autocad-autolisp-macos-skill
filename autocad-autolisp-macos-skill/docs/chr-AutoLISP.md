# chr (AutoLISP)

Converts an integer representing a character code into a single-character string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(chr int)
```

*int*
:   *Type:* Integer

    A numeric value in the range of 1-65536.

## Return Values

*Type:* String

A single character based on the numeric value of
*int*.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *int* argument previously accepted an ASCII character code, but now accepts a Unicode character code.
* Return value changed from an integer in the range of 1-255 (ASCII character codes) to 1-65536 (Unicode character codes) and
  might be different than earlier releases. For example,
  (chr 128) previously returned "€", but now returns "". If you want to return "€", your code will need to be updated to
  (chr 8364).
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(chr 65)
"A"

(chr 66)
"B"

(chr 97)
"a"

(chr 8364)
"€"
```

#### Related References

* [ascii (AutoLISP)](ascii-AutoLISP.md)

#### Related Concepts

* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*