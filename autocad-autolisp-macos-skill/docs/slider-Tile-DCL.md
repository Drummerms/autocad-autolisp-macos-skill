# slider Tile (DCL)

A slider obtains a numeric value.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : slider {
       action alignment big_increment fixed_height
       fixed_width height key label layout
       max_value min_value mnemonic small_increment
       value width
    }
    ```

Mac OS and Web
:   ```
    : slider {
       action alignment fixed_height fixed_width
       height key label layout max_value
       min_value small_increment value width
    }
    ```

![](../images/GUID-44566F9D-5550-4DE6-80B6-A5B20035CF9D-low.png)

The user can drag the slider's indicator to the left or right (or up or down) to obtain a value whose meaning depends on
the application. This value is returned as a string containing a signed integer within a specified range (the integer is a
16-bit value, so the maximum range is -32,768 to 32,767). The application can scale this value as required.

value
:   A quoted string that contains the current (integer) value of the slider (default:
    min\_value).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [edit\_box Tile (DCL)](edit_box-Tile-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [big\_increment Attribute (DCL)](big_increment-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [max\_value Attribute (DCL)](max_value-Attribute-DCL.md)
* [min\_value Attribute (DCL)](min_value-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [small\_increment Attribute (DCL)](small_increment-Attribute-DCL.md)
* [value Attribute (DCL)](value-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*