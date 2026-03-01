# acet-str-format (AutoLISP/Express Tools)

Formats a message with embedded arguments.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-str-format format [args ...])
```

format
:   *Type:* String

    A string containing plain text and argument specifiers. Argument insertions appear in the format string as the percent (%)
    character followed by an argument number.

args
:   *Type:* Integer, real, or string

    Multiple argument values to be converted and inserted. Only integer, real and string arguments can be converted. Other argument
    types must be converted to one of these three. Real arguments are converted using the current
    LUNITS and
    LUPREC values; you may wish to first use the
    angtos or
    rtos functions for proper display.

## Return Values

*Type:* String

A string with appropriate substitutions.

## Example

```
(acet-str-format "%1/%2 or %2/%1." "one" "two")
"one/two or two/one."
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*