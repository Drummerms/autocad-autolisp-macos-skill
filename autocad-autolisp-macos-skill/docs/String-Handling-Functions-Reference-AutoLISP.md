# String-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP string-handling functions.

| String-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(read [string])](read-AutoLISP.md) | Returns the first list or atom obtained from a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(strcase string [which])](strcase-AutoLISP.md) | Returns a string where all alphabetic characters have been converted to uppercase or lowercase | ✓ | ✓ | ✓ | -- | ✓ |
| [(strcat [string1 [string2 ...])](strcat-AutoLISP.md) | Returns a string that is the concatenation of multiple strings | ✓ | ✓ | ✓ | -- | ✓ |
| [(strlen [string ...])](strlen-AutoLISP.md) | Returns an integer that is the number of characters in a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(substr string start [length])](substr-AutoLISP.md) | Returns a substring of a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-prin1-to-string object)](vl-prin1-to-string-AutoLISP.md) | Returns the string representation of any LISP object as if it were output by the prin1 function | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-princ-to-string object)](vl-princ-to-string-AutoLISP.md) | Returns the string representation of any LISP object as if it were output by the princ function | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string->list string)](vl-string-list-AutoLISP.md) | Converts a string into a list of Unicode character codes | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-elt string position)](vl-string-elt-AutoLISP.md) | Returns the Unicode representation of the character at a specified position in a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-left-trim character-set string)](vl-string-left-trim-AutoLISP.md) | Removes the specified characters from the beginning of a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-mismatch str1 str2 [pos1 pos2 ignore-case-p])](vl-string-mismatch-AutoLISP.md) | Returns the length of the longest common prefix for two strings, starting at specified positions | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-position char-code str [ start-pos [from-end-p]])](vl-string-position-AutoLISP.md) | Looks for a character with the specified Unicode code in a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-right-trim character-set string)](vl-string-right-trim-AutoLISP.md) | Removes the specified characters from the end of a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-search pattern string [ start-pos])](vl-string-search-AutoLISP.md) | Searches for the specified pattern in a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-subst new-str pattern string [start-pos])](vl-string-subst-AutoLISP.md) | Substitutes one string for another, within a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-translate source-set dest-set str)](vl-string-translate-AutoLISP.md) | Replaces characters in a string with a specified set of characters | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-string-trim char-set str)](vl-string-trim-AutoLISP.md) | Removes the specified characters from the beginning and end of a string | ✓ | ✓ | ✓ | -- | ✓ |
| [(wcmatch string pattern)](wcmatch-AutoLISP.md) | Performs a wild-card pattern match on a string | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*