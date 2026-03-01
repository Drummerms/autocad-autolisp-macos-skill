# image Tile (DCL)

An image is a rectangle in which a vector graphic picture is displayed.

*Supported Platforms:* Windows and Mac OS only

Windows
:   ```
    : image {
       action alignment aspect_ratio color
       fixed_height fixed_width height is_enabled
       is_tab_stop key mnemonic value width
    }
    ```

Mac OS
:   ```
    : image {
       action alignment aspect_ratio color
       fixed_height fixed_width height is_enabled
       key value width
    }
    ```

![](../images/GUID-07366F96-DAE4-4063-A3BD-007EEEFFA6DA-low.png)

Images are used to display icons, linetypes, text fonts, and color patches in AutoCAD dialog boxes.

You must assign an image tile either an explicit
width and
height attribute, or one of those attributes plus an
aspect\_ratio.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [image\_button Tile (DCL)](image_button-Tile-DCL.md)
* [Image Tile-Handling Functions Reference (AutoLISP/DCL)](Image-Tile-Handling-Functions-Reference-AutoLISP-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [aspect\_ratio Attribute (DCL)](aspect_ratio-Attribute-DCL.md)
* [color Attribute (DCL)](color-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [value Attribute (DCL)](value-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*