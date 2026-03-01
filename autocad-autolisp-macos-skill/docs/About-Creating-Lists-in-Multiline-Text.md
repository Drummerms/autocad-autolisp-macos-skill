# About Creating Lists in Multiline Text

You can create bulleted lists, lettered or numbered lists, or simple outlines in multiline text.

Lines of multiline text can be formatted as a list. When you add or delete an item, or move an item up or down a level, the
list numbering automatically adjusts. You can remove and reapply list formatting with the same method as used in most text
editors.

## Use Automatic List Formatting

By default, list formatting is applied to all text that looks like a list. Text that meets all the following criteria is considered
to be a list:

* The line begins with one or more letters or numbers or a symbol.
* The letters or numbers is followed by punctuation.
* A space after the punctuation is created by pressing Space (Press Tab when MTEXTDETECTSPACE system variable is set to 0/off).
* The text following the space is ended by Enter or Shift+Enter.

NOTE:If you do not want list formatting applied to all text that fits the criteria, clear the Allow Bullets and Lists option. (Right-click
in the In-Place Text Editor, click Bullets and Lists ![](../images/ac.menuaro.gif) Allow Bullets and Lists.) When Allow Bullets and Lists is not checked, you cannot create new formatted lists in the multiline
text object.

To create a list, use one of the following methods:

* Apply list formatting to new or selected text.
* Use Auto-list (on by default) and type the elements of a list.
* With Auto-list off, type the elements of a list and close and reopen the editor to convert the text to a list.

## Apply List Formatting

When you apply list formatting, you can specify bullets, uppercase or lowercase letters, or numbers. Default settings are
used for the type of list you choose. Letters or numbers are followed by a period. Nested lists use a double bullet, letter,
or number. Items are indented based on the tab stops on the ruler in the In-Place Text Editor.

## Use Match Text Formatting

For any text, you can apply the formatting of one text object to others. In this case, creating list items by matching the
format of an existing list.

## Use Auto-list to Type a List

When Auto-list is on, you can create a list as you type. You can use letters, numbers, or symbols.

For example, in the editor, enter \U+25CB, press Space, and then enter some text. This creates a empty circle style bullet.

Not all symbols are available from the character map for a particular text font. However, if you specify the Unicode text
directly (U+25CB in this case), you can always get the bullet format of your choice.

NOTE:

Press Space after you enter the Unicode text or symbol, or it will remain a separate character.

You can also paste a symbol from the Character Map dialog box

You can also paste a symbol from the Characters dialog box

The following characters can be used as punctuation after the number or letter when you type a list but cannot be used as
bullets:

| Character | Description |
| . | Period |
| : | Colon |
| ) | Close parenthesis |
| > | Close angle bracket |
| ] | Close square bracket |
| } | Close curly bracket |

## Paste a List from Another Document

If you copy a nested bulleted list (a list within a list) from a word processor and paste the list into a multiline text,
the bullets that are displayed as empty circles might not be formatted like other bullets in multiline text. This is because
the bullet might be a letter, such as *o*, instead of a bullet for nested bulleted lists. You can remove formatting from the nested list and reapply to change the
bullets to double bullets.

#### Related Information

* [To Format Multiline Text as a List](To-Format-Multiline-Text-as-a-List.md)
* [To Remove List Formatting From Multiline Text](To-Remove-List-Formatting-From-Multiline-Text.md)
* [To Create a Lettered or Numbered List in Multiline Text as you Type](To-Create-a-Lettered-or-Numbered-List-in-Multiline-Text-as-you-Type.md)
* [To Create a Bulleted List in Multiline Text as you Type](To-Create-a-Bulleted-List-in-Multiline-Text-as-you-Type.md)
* [To Move a List Item in Multiline Text Down a Level](To-Move-a-List-Item-in-Multiline-Text-Down-a-Level.md)
* [To Extract Part of an Existing List](To-Extract-Part-of-an-Existing-List.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*