# About Finding and Replacing Text

You can easily find and replace text with the FIND command

To search for and replace text, use FIND. Replacement is based on text content only; character formatting and text properties
are not changed.

When searching for text in a 3D environment, the viewport will temporarily change to a 2D viewport so that text isn’t blocked
by 3D objects in your drawing.

With FIND, you can use wild-card characters in your search.

| Character | Definition |
| # (Pound) | Matches any numeric digit |
| @ (At) | Matches any alphabetic character |
| . (Period) | Matches any non-alphanumeric character |
| \* (Asterisk) | Matches any string and can be used anywhere in the search string |
| ? (Question mark) | Matches any single character; for example, ?BC matches ABC, 3BC, and so on |
| ~ (Tilde) | Matches anything but the pattern; for example; ~\*AB\*matches all strings that don't contain AB |
| [ ] | Matches any one of the characters enclosed; for example, [AB]C matches AC and BC |
| [~] | Matches any character not enclosed; for example, [~AB]C matches XC but not AC |
| [-] | Specifies a range for a single character; for example, [A-G]C matches AC, BC, and so on to GC, but not HC |
| ` (Reverse quote) | Reads the next character literally; for example, `~AB matches ~AB |

#### Related Information

* [To Work With Single Line Text Changes](To-Work-With-Single-Line-Text-Changes.md)
* [To Work With Multiline Text Changes](To-Work-With-Multiline-Text-Changes.md)
* [To Scale Multiline Text Objects Without Changing Their Locations](To-Scale-Multiline-Text-Objects-Without-Changing-Their-Locations.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*