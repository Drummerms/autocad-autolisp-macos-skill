# popup\_list Tile (DCL)

A pop-up list, or simply pop-up, is functionally equivalent to a list box.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : popup_list {
       action alignment edit_width fixed_height
       fixed_width fixed_width_font height
       is_enabled is_tab_stop key label list
       mnemonic tab_truncate tabs value width
    }
    ```

Mac OS and Web
:   ```
    : popup_list {
       action alignment fixed_height fixed_width height
       is_enabled key label list tabs value width
    }
    ```

![](../images/GUID-BBACFD23-6579-4E89-8CA0-CA14B7824CD6-low.png)

When a dialog box is first displayed, the pop-up is in a collapsed state and looks like a button except for the downward-pointing
arrow on the right. When the user selects the text or the arrow, the list pops up and displays more selections. A pop-up list
has a scroll bar on the right that works like the scroll bar of a list box. When a pop-up list is collapsed, the current selection
appears in its display field. Pop-up lists do not allow multiple selection.

NOTE:The popup\_list tile is limited to 32,768 entries with the first element being an index of 0 and the last being 32,767. Once
the limit is reached, the value of any entry that has an index greater than 32,767 is not accurately reported.

label
:   Appears as a title to the left of the pop-up list. If specified, the
    label is left justified within the width of the
    popup\_list tile.

edit\_width
:   Specifies the width of the text portion of the list in character-width units. It does not include the optional label on the
    left or the pop-up arrow (or scroll bar) on the right. If
    edit\_width isn't specified or is zero, and the width of the tile is not fixed, the box expands to fill the available space. Possible
    value is an integer or a real number. If
    edit\_width is nonzero, then the box is right-justified within the space occupied by the tile. If it is necessary to stretch the tile
    for layout purposes, the PDB feature inserts white space between the
    label and the edit portion of the box.

value
:   A quoted string containing an integer (default:
    "0"). The integer is a zero-based index that indicates the currently selected item in the list (the one that is displayed when
    the list is not popped up).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [list\_box Tile (DCL)](list_box-Tile-DCL.md)
* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [edit\_width Attribute (DCL)](edit_width-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [list Attribute (DCL)](list-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [tabs Attribute (DCL)](tabs-Attribute-DCL.md)
* [value Attribute (DCL)](value-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*