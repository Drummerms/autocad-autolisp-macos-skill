# dialog Tile (DCL)

A dialog is the tile that defines the dialog box.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : dialog {
       initial_focus label value
    }
    ```

Mac OS and Web
:   ```
    : dialog {
       label value
    }
    ```

You should not specify both a
label and
value attribute: the
value attribute overrides the
label attribute.

label
:   Specifies the optional title displayed in the title bar of the dialog box.

value
:   Specifies a string to display as the optional dialog box title. However, the value isn't inspected at layout time, so if you
    assign the title this way, make sure the dialog box is wide enough or the text might be truncated.

    For a
    dialog, the
    label and
    value are equivalent except for layout considerations. To change the title in at runtime, use the
    set\_tile function).

initial\_focus
:   Specifies the
    key of the tile that receives the initial keyboard focus.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [initial\_focus Attribute (DCL)](initial_focus-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*