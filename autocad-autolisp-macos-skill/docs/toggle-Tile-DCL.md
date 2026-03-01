# toggle Tile (DCL)

A toggle appears as a small box with an optional
label to the right of the box.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : toggle {
       action alignment fixed_height fixed_width
       height is_enabled is_tab_stop label width
    }
    ```

Mac OS and Web
:   ```
    : toggle {
       action alignment fixed_height fixed_width
       height is_enabled label width
    }
    ```

![](../images/GUID-A46A8356-C66E-4CA4-9B9D-D98B2379F66A-low.png)

A toggle controls a Boolean value ("0" or
"1"). A check mark or
*X* appears (or disappears) when the user selects the box. Toggles enable the user to view or change the state of on/off options.
Toggles are also known as check boxes.

label
:   The text displayed to the right of the toggle box.

value
:   A quoted string containing an integer (default:
    "0") and specifying the initial state of the
    toggle. If the string is
    "0", the toggle box is blank (without a check mark). If it is
    "1", the box contains a check mark (or an
    *X*).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [radio\_button Tile (DCL)](radio_button-Tile-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*