# text Tile (DCL)

A text tile displays a text string for titling or informational purposes.

*Supported Platforms:* Windows, Mac OS, and Web

```
: text {
   alignment fixed_height fixed_width height
   is_bold key label value width
}
```

Because most tiles have their own
label attribute for titling purposes, you do not always need to use text tiles. But a text tile that you usually keep blank is
a useful way to display feedback about user actions, error messages, or warnings.

If you intend the message to be static, specify it in the
label attribute and do not specify a
width or
value. If you intend the message to change at run-time, specify it in the
value attribute and assign a
width long enough to contain any strings that you plan to assign the
value. Once the dialog box is laid out, the size of its tiles can't change, so if you use
set\_tile to assign a string longer than the width, the displayed text is truncated.

label
:   The displayed text. When a
    text tile is laid out, its width is the larger of either its
    width attribute, if that is specified in the DCL, or the width required by its
    label attribute, if specified. At least one of these attributes must be specified.

value
:   Like
    label, the
    value attribute specifies a string to display in the text tile. However, it has no effect on the tile's layout.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [concatenation Tile (DCL)](concatenation-Tile-DCL.md)
* [paragraph Tile (DCL)](paragraph-Tile-DCL.md)
* [Text Cluster Tiles (DCL)](Text-Cluster-Tiles-DCL.md)
* [text\_part Tile (DCL)](text_part-Tile-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*