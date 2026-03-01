# radio\_button Tile (DCL)

A radio button is one of a group of buttons composing a radio column or radio row.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : radio_button {
       action alignment fixed_height fixed_width
       height is_enabled is_tab_stop key label
       mnemonic value width
    }
    ```

Mac OS and Web
:   ```
    : radio_button {
       action alignment fixed_height fixed_width
       height is_enabled key label
       value width
    }
    ```

![](../images/GUID-B47304C3-13FB-440A-B71B-092C0206D9A9-low.png)

These work like the buttons on a car radio: only one can be selected at a time, and when one is pressed, any other button
in the column (or row) that is on is turned off. An optional
label appears to the right of the radio button. The PDB feature reports an error if you attempt to place a radio button outside
a radio column or radio row.

label
:   The text displayed to the right of the radio button.

value
:   A quoted string (no default). If the
    value is
    "1", the
    radio\_button is on; if it is
    "0", the
    radio\_button is off; all other values are equivalent to
    "0".

    If by some chance more than one
    radio\_button in a radio cluster has
    value = "1", only the last one is turned on. (This can happen in a DCL file. Once the dialog box starts, the PDB feature manages radio
    buttons and ensures that only one per cluster is turned on at a time.)

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [toggle Tile (DCL)](toggle-Tile-DCL.md)
* [radio\_column Tile (DCL)](radio_column-Tile-DCL.md)
* [radio\_row Tile (DCL)](radio_row-Tile-DCL.md)
* [boxed\_radio\_column Tile (DCL)](boxed_radio_column-Tile-DCL.md)
* [boxed\_radio\_row Tile (DCL)](boxed_radio_row-Tile-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [value Attribute (DCL)](value-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*