# Find and Replace Dialog Box - FIND

Specifies the text you want to find, replace, or select and controls the scope and results of the search.

FIND (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Find.
![](../images/GUID-39413D6A-8C8F-4C01-8E1D-6EBB1079C116-low.png)

![](../images/GUID-0D142AEC-0E84-44F3-A700-5934BC97BA52-low.png)

## List of Options

The following options are displayed.

Where to Check
:   Specifies whether to search the entire drawing, the current layout, or the currently-selected object. If an object is already
    selected, then Selected Objects is the default value. If no object is selected, then Entire Drawing is the default value.
    You can use the Select Objects button to temporarily close the dialog box and create or modify the selection set.

Find What
:   Specifies the text string you want to find. Enter a text string, including any wild-card characters, or choose one of the
    six most recently used strings from the list.

Replace With
:   Specifies the text string you want to use to replace the found text. Enter a string, or choose one of the most recently used
    strings from the list.

Select Objects Button
:   Closes the dialog box temporarily so that you can select objects in your drawing. Press Enter to return to the dialog box.

    When you select objects, Where to Check displays Selected Objects by default.

Replace
:   Replaces found text with the text that you enter in Replace With and moves to the next instance of the found text if one exists.

Replace All
:   Finds all instances of the text that you enter in Find What and replaces it with the text in Replace With.

    The Where to Check setting controls whether to find and replace text in the entire drawing or text in the currently selected
    object or objects.

Find
:   Finds the text that you enter in Find What. The first text object that matches the search criteria is zoomed to. Once you
    find the first instance of the text, the Find option acts like a Find Next, which you can use to find the next text object.

Search Options

Defines the type of objects and words to be found.

Match Case
:   Includes the case of the text in Find What as part of the search criteria.

Find Whole Words Only
:   Finds only whole words that match the text in Find What. For example, if you select Find Whole Words Only and search for “Front
    Door,” FIND does not locate the text string “Front Doormat.”

Use Wildcards
:   Allows the use of wild-card characters in searches.

Search XRefs
:   Includes text in externally referenced files in search results.

Search Blocks
:   Includes text in blocks in search results.

Ignore Hidden Items
:   Ignores hidden items in search results. Hidden items include text on layers that are frozen or turned off, text in block attributes
    created in invisible mode, and text in visibility states within dynamic blocks.

Match Diacritics
:   Matches diacritical marks, or accents, in search results.

Match Half or Full Width Forms
:   Matches half- and full-width characters in search results.

Text Types

Specifies the type of text objects you want to include in the search. By default, all options are selected.

Block Attribute Value
:   Includes block attribute text values in search results.

Dimension or Leader Text
:   Includes dimension and leader object text in search results.

Single-Line or Multiline Text
:   Includes text objects such as single-line and multiline text in search results.

Table Text
:   Includes text found in table cells in search results.

Hyperlink Description
:   Includes text found in hyperlink descriptions in search results.

Hyperlink
:   Includes hyperlink URLs in search results.

#### Related References

* [FIND (Command)](FIND-Command.md)

#### Related Concepts

* [About Finding and Replacing Text](About-Finding-and-Replacing-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*