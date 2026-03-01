# list\_box Tile (DCL)

A list box contains a list of text strings, arranged in rows.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : list_box {
       action alignment allow_accept fixed_height
       fixed_width fixed_width_font height is_enabled
       is_tab_stopkey label list mnemonic multiple_select
       tab_truncate tabs value width
    }
    ```

Mac OS and Web
:   ```
    : list_box {
       action alignment allow_accept fixed_height
       fixed_width is_enabled key label
       list multiple_select tabs value width
    }
    ```

![](../images/GUID-BA7DE2F2-0993-4F88-88F1-057C3F577C51-low.png)

Usually the list is of variable length, but list boxes can be used for fixed-length lists when a different kind of tile,
such as a set of radio buttons, takes up too much space in the dialog box. When users select a row, it is highlighted. A list
box can contain more rows than can fit in the box, so a scroll bar always appears to the right of the list box. (The scroll
bar is enabled only if the list has more items than can appear at once.) By dragging the scroll bar cursor or clicking on
its arrows, users can scroll through the list box items. Some applications may allow users to select multiple rows.

NOTE:The
list\_box tile is limited to 32,768 entries with the first element being an index of 0 and the last being 32,767. Once the limit is
reached, the value of any entry that has an index greater than 32,767 is not accurately reported.

label
:   Text displayed above the list box.

value
:   A quoted string containing zero ("") or more integers, separated by spaces (no default). Each integer is a zero-based index that indicates a list item that is
    initially selected. If
    multiple\_select is
    false,
    value cannot contain more than one integer.

    If the value string is empty (""), then no items in the list are initially selected. In this case, you don't need to specify the value attribute at all.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [List Box and Pop-Up List-Handling Functions Reference (AutoLISP/DCL)](List-Box-and-Pop-Up-List-Handling-Functions-Reference-AutoLISP-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [allow\_accept Attribute (DCL)](allow_accept-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [list Attribute (DCL)](list-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [multiple\_select Attribute (DCL)](multiple_select-Attribute-DCL.md)
* [tabs Attribute (DCL)](tabs-Attribute-DCL.md)
* [value Attribute (DCL)](value-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*