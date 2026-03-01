# radio\_row Tile (DCL)

A radio row, like a radio column, contains radio button tiles, only one of which can be selected at a time.

*Supported Platforms:* Windows, Mac OS, and Web

```
: radio_row {
   alignment children_alignment
   children_fixed_height children_fixed_width
   fixed_height fixed_width height label width
}
```

![](../images/GUID-D43DE0B8-7283-44B1-B2F8-138A95AB31A7-low.png)

Radio rows can be assigned an action.

value
:   A quoted string containing the
    key of the currently selected radio button (the one whose value is
    "1").

NOTE:Radio rows are not as easy to use as radio columns, because the mouse has to travel farther. Use radio rows only if they specify
two to four options, or if the labels are short.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [radio\_button Tile (DCL)](radio_button-Tile-DCL.md)
* [radio\_column Tile (DCL)](radio_column-Tile-DCL.md)
* [boxed\_radio\_column Tile (DCL)](boxed_radio_column-Tile-DCL.md)
* [boxed\_radio\_row Tile (DCL)](boxed_radio_row-Tile-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [children\_alignment Attribute (DCL)](children_alignment-Attribute-DCL.md)
* [children\_fixed\_height Attribute (DCL)](children_fixed_height-Attribute-DCL.md)
* [children\_fixed\_width Attribute (DCL)](children_fixed_width-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*