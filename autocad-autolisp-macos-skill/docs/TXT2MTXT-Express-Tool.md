# TXT2MTXT (Express Tool)

Converts or combines single-line or multiline text objects into one or more multiline text objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Convert Text to Mtext.
![](../images/GUID-547349A1-E4A8-4B4D-A78C-3E1AA7615E67-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Express Tools ![](../images/ac.menuaro.gif) Convert Text to Mtext.

Command: TXT2MTXT

The selected text objects are replaced by one or more multiline text objects. If possible, the text size, font, and color
differences between text objects are maintained.

Select objects or [SEttings]:
*Use an object selection method to select text or specify the Settings option to display the Text to Mtext Options dialog box*.

## Dialog Box Options

| Combine into a single mtext object | Combines selected text objects into a single mtext object. |
| Text ordering - Sort top-down | Specifies the order of the selected text by descending vertical position. |
| Text ordering - Selection set order | Specifies the order of the selected text by manual selection. |
| Create word-wrap MText | Combines all the lines of text into a single line, and then wraps any text that exceeds the width of the mtext object to the next line. |
| Force uniform line spacing | Applies consistent interline spacing and paragraph spacing when word wrap is turned on. Paragraph spacing is 50% larger than interline spacing. |

## Example

Select three text objects and convert them to a single multiline text object.

*Select the text objects:*

![](../images/GUID-2EBDB5E2-EF58-4D2F-9B68-8EE901FD4F12-low.gif)

The text objects are converted to a single MTEXT object:

![](../images/GUID-9EF9ACDA-4699-4BA2-B18B-CC86CCA62603-low.gif)

NOTE: The mtext object retains the multiple lines because the three text objects were aligned vertically. If the text objects were
not aligned, the result would have been an mtext object with all the text on a single line, or possibly wrapped if the word-wrap
option is turned on.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [PDFSHXTEXT (Command)](PDFSHXTEXT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*