# In-Place Text Editor

Creates or modifies single or multiline text objects.

![](../images/GUID-92D71167-82F6-403D-BA68-4D1F63E1A819-low.png)

## Summary

You can import or paste text from other files to use in multiline text, set tabs, adjust paragraph and line spacing and alignment,
and create and modify columns.

The In-Place Text Editor includes

* [Text Editor visor](Text-Editor-Visor.md)
* [Paragraph dialog box](GUID-90F5A530-BB66-4264-86F0-D5F670EC8519.htm#WS1A9193826455F5FF1C45DBE10E3ADF05A7-7C86)
* [Column Settings dialog box](Column-Settings-Dialog-Box.md)
* [Background Mask dialog box](Background-Mask-Dialog-Box.md)
* [Columns menu](GUID-6DF5368A-5F2F-44BE-8B80-F35FFEF80204.htm#WS1A9193826455F5FF1C45DBE10E3ADF05A7-7C85)

When a table cell is selected for editing, the In-Place Text Editor displays column letters and row numbers.

NOTE:Not all options available when creating single-line text.

## List of Options

The following options are displayed.

Text Editor Shortcut Menu

Select All
:   Selects all the text in the text editor.

Clipboard
:   Contains options to Cut, Copy, and Paste text to or from the clipboard. The Paste Special option allows you to paste without
    character or paragraph formatting.

Insert Field
:   Displays the
    [Insert Field dialog box](GUID-1B6DD22B-10D1-44ED-BAA2-E6D79FE52327.htm#WSC30CD3D5FAA8F6D8B82368FFC2D60192-7FFF).

Symbol
:   Displays a list of available symbols. You can also select a Non-breaking space and open the Characters dialog box for additional
    symbols.

Import Text
:   Displays the Select File dialog box (a
    [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)). Select any file that is in ASCII or RTF format. Imported text retains its original character formatting and style properties,
    but you can edit and format the imported text in the editor. After you select a text file to import, you can replace either
    selected text or all text, or append the inserted text to text selected within the text boundary. The file size for imported
    text is limited to 32 KB. (Not available for single-line text.)

    The editor automatically sets the text color to BYLAYER. When black characters are inserted and the background color is black,
    the editor automatically changes to white or the current color.

Paragraph Alignment
:   Sets alignment for the multiline text object. You can choose to align your text to the left, center, or right. You can justify
    your text, or align the first and last characters of your text with the margins of your mtext box, or center each line of
    text within the margins of your mtext box. Spaces entered at the end of a line are included as part of the text and affect
    the justification of the line. (Not available for single-line text.)

Paragraph
:   Displays options for paragraph formatting. See the
    [Paragraph dialog box](Paragraph-Dialog-Box.md). (Not available for single-line text.)

Bullets and Lists
:   Displays the options for numbering lists. (Not available for single-line text.)

    Displays options for creating lists. (Not available for table cells.) The list is indented to align with the first selected
    paragraph.

    * *Off:* When selected, removes letters, numbers, and bullets from selected text that has list formatting applied. Indentation is
      not changed.
    * *Lettered:* Applies list formatting that uses letters with periods for the items in the list. If the list has more items than the alphabet
      has letters, the sequence continues by using double letters.
    * *Numbered:* Applies list formatting that uses numbers with periods for the items in the list.
    * *Bulleted:* Applies list formatting that uses bullets for the items in the list.
    * *Restart:* Starts a new letter or number sequence in list formatting. If the selected items are in the middle of a list, unselected
      items below them also become part of the new list.
    * *Continue:* Adds the selected paragraphs to the last list above and continues the sequence. If list items rather than paragraphs are
      selected, unselected items below the selected items continue the sequence.
    * *Allow Auto-list:* Applies list formatting as you type. The following characters can be used as punctuation after letters and numbers and cannot
      be used as bullets: period (.), comma (,), close parenthesis ()), close angle bracket (>), close square bracket (]), and close
      curly bracket (}).
    * *Use Tab Delimiter Only:* Limits the Allow Auto-list and Allow Bullets and Lists options. List formatting is applied to text only when the space after
      the letter, number, or bullet character was created by Tab, not Space.
    * *Allow Bullets and Lists:* When this option is selected, list formatting is applied to all plain text in the multiline text object that looks like a
      list. Text that meets the following criteria is considered to be a list. The line begins with (1) one or more letters or numbers
      or a symbol, followed by (2) punctuation after a letter or number, (3) a space created by pressing Tab, and (4) some text
      before the line is ended by Enter or Shift+Enter.

      When you clear the check mark, any list formatting in the multiline text object is removed and the items are converted to
      plain text. Allow Auto-list is turned off, and all the Bullets and Lists options are unavailable except Allow Bullets and
      Lists.

Columns
:   Displays options for columns. See the
    [Columns menu](Columns-Menu.md). (Not available for single-line text.)

Find and Replace
:   Displays the
    [Find and Replace dialog box](GUID-39B391F5-F74D-4D6F-988D-61B24DEFEE52.htm#WSC30CD3D5FAA8F6D813D93F4FFC2D60E2B-7FB5).

Change Case
:   Changes the case of selected text. Options are Uppercase and Lowercase.

AutoCAPS
:   Converts all new and imported text to uppercase. AutoCAPS does not affect existing text. To change the case of existing text,
    select the text and right-click. Click Change Case.

Character Set
:   Displays a menu of code pages. Select a code page to apply it to the selected text. (Not available for single-line text.)

Combine Paragraphs
:   Combines selected paragraphs into a single paragraph and replaces each paragraph return with a space. (Not available for single-line
    text.)

Remove Formatting
:   Removes character formatting for selected characters, paragraph formatting for a selected paragraph, or all formatting from
    a selected paragraph. (Not available for single-line text.)

Background Mask
:   Displays the
    [Background Mask dialog box](GUID-3448A24E-E18B-4C8C-B8AB-84F4CD4EBC81.htm#WSFACF1429558A55DE1A7524C1004E616F8B-5262). (Not available for table cells and single-line text.)

Stack
:   Creates stacked text, for example, fractions, if the selected text contains stack characters. Also, unstacks text if stacked
    text is selected. When the stack characters, carat (^), forward slash (/), and pound sign (#), are used, the text to the left
    of the stack character is stacked on top of the text to the right.

    By default, text that contains a carat converts to left-justified tolerance values. Text that contains the forward slash converts
    to center-justified fractional numbers; the slash is converted to a horizontal bar the length of the longer text string. Text
    that contains the pound sign converts to a fraction separated by a diagonal bar the height of the two text strings. The characters
    above the diagonal fraction bar are bottom-right aligned; the characters beneath the diagonal bar are top-left aligned.

Editor Settings
:   Displays a list of options for the text editor.

Editor Settings

Provides options for changing the behavior of the text editor and provides additional editing options. Options are specific
to the Editor Settings menu and are not available elsewhere in the text editor.

NOTE:Some options may not be available depending on what you are editing.

Always Display As WYSIWYG (What You See Is What You Get)
:   Controls display of the In-Place Text Editor and the text within it. When unchecked, the drawing view is zoomed and rotated
    if need so the text that would otherwise be difficult to read (if it is very small, very large, or is rotated) is displayed
    at a legible size and is oriented horizontally so that you can easily read and edit it.

    When this option is checked, the
    [MTEXTFIXED](MTEXTFIXED-System-Variable.md) system variable will be set to 0. Otherwise, MTEXTFIXED will be set to 2.

Show Ruler
:   Controls the display of the ruler.

Opaque Background
:   When selected, makes the background of the editor opaque. (Not available for table cells.)

Check Spelling
:   Determines whether
    [As-You-Type](About-Spelling-Check.md) spell checking is on or off.

Check Spelling Settings
:   Displays the
    [Check Spelling Settings dialog box](Check-Spelling-Settings-Dialog-Box.md), where you can specify text options that will be checked for spelling errors within your drawing.

Text Highlight Color
:   Specifies the highlight color when text is selected.

#### Related References

* [Text Editor Visor](Text-Editor-Visor.md)

#### Related Concepts

* [About Text Styles](About-Text-Styles.md)
* [About Creating Notes Using Text](About-Creating-Notes-Using-Text.md)

#### Related Information

* [MTEXT (Command)](MTEXT-Command.md)
* [MTEDIT (Command)](MTEDIT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*