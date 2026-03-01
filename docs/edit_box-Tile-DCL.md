# edit\_box Tile (DCL)

An edit box is a field that enables the user to enter or edit a single line of text.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : edit_box {
       action alignment allow_accept edit_limit
       edit_width fixed_height fixed_width height
       is_enabled is_tab_stop key label mnemonic
       value width password_char
    }
    ```

Mac OS and Web
:   ```
    : edit_box {
       action alignment fixed_height
       fixed_width height is_enabled
       key label value width
    }
    ```

![](../images/GUID-79EC97C3-52A6-44D2-B789-28929B78EC01-low.png)

An optional
label can appear to the left of the box. If the entered text is longer than the length of the edit box, the edit box scrolls horizontally.

Left-justifying the
label and right-justifying the edit box makes it easier to align
edit\_box tiles vertically.

label
:   Appears as a title. If specified, the label is left-justified within the width of the
    edit\_box tile.

value
:   The initial ASCII value placed in the box. It is displayed left-justified within the edit (input) part of the box. The value
    of an edit box is terminated by the null character. If the user enters more characters than the
    edit\_limit and the string is truncated, the null character is appended.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [popup\_list Tile (DCL)](popup_list-Tile-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [allow\_accept Attribute (DCL)](allow_accept-Attribute-DCL.md)
* [edit\_limit Attribute (DCL)](edit_limit-Attribute-DCL.md)
* [edit\_width Attribute (DCL)](edit_width-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [password\_char Attribute (DCL)](password_char-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*