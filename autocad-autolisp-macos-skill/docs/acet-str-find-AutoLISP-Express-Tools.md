# acet-str-find (AutoLISP/Express Tools)

Finds a substring in string.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-str-find find string [ignoreCase [useRegExp]])
```

find
:   *Type:* String

    The substring to locate.

string
:   *Type:* String

    The string to search.

ignoreCase
:   *Type:* T or
    nil

    If provided and non-nil, indicates that case insensitive comparisons should be performed.

useRegExp
:   *Type:* T or
    nil

    If provided and non-nil, indicates that regular expressions should be used for searching.

## Regular Express Syntax

This function uses the following definitions for regular expressions:

| . | Matches any single character. |
| \* | Preceding item 0 or more times. |
| + | Preceding item 1 or more times. |
| ^ | Matches empty string at beginning of text. |
| $ | Matches empty string at end of text. |
| [chars] | Matches any character in the given class. If the first character is ^, match any character not in the given class. A range of character may be specified by first-last, as in [A-Z] to specify upper case alphabetic characters. |
| \( | Mark the beginning of a sub-expression. |
| \) | Mark the end of a sub-expression. |
| \digit | Matches a repeat of the text matched earlier by the sub-expression inside the nth opening parenthesis. Sub-expressions may also be referenced in replace strings. |

## Return Values

*Type:* Integer or
nil

The 1-based index if found, or
nil if not found.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*