# button Title (DCL)

A Button tile resembles a push button.

*Supported Platforms:* Windows, Mac OS, and Web

Windows
:   ```
    : button {
       action alignment fixed_height fixed_width
       height is_cancel is_default is_enabled
       is_tab_stop key label mnemonic width
    }
    ```

Mac OS and Web
:   ```
    : button {
       action alignment fixed_height fixed_width
       height is_cancel is_default is_enabled
       key label width
    }
    ```

![](../images/GUID-42D49F97-0F91-4AB9-B3FF-EC5FE83970FF-low.png)

The button's
label specifies text that appears inside the button. Buttons are appropriate for actions that are immediately visible to the user
such as leaving the dialog box, or going into a subdialog box.

Dialog boxes must include an OK button (or its equivalent) for the user to press after using (or reading) the box. Many dialog
boxes also include a Cancel button that enables the user to leave the dialog box without making any changes.

Dialog boxes should use the standard exit button subassemblies when possible.

NOTE:If you make the default button and the cancel button the same, you must make sure at least one other exit button is associated
with an action that calls
done\_dialog. Otherwise, the dialog box is always canceled.

label
:   Specifies the text that appears in the button.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [image\_button Tile (DCL)](image_button-Tile-DCL.md)
* [ok\_cancel Tile (DCL)](ok_cancel-Tile-DCL.md)
* [ok\_cancel\_help Tile (DCL)](ok_cancel_help-Tile-DCL.md)
* [ok\_cancel\_help\_errtile Tile (DCL)](ok_cancel_help_errtile-Tile-DCL.md)
* [ok\_cancel\_help\_info Tile (DCL)](ok_cancel_help_info-Tile-DCL.md)
* [ok\_only Tile (DCL)](ok_only-Tile-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)
* [action Attribute (DCL)](action-Attribute-DCL.md)
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)
* [height Attribute (DCL)](height-Attribute-DCL.md)
* [is\_cancel Attribute (DCL)](is_cancel-Attribute-DCL.md)
* [is\_default Attribute (DCL)](is_default-Attribute-DCL.md)
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)
* [key Attribute (DCL)](key-Attribute-DCL.md)
* [label Attribute (DCL)](label-Attribute-DCL.md)
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)
* [width Attribute (DCL)](width-Attribute-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*