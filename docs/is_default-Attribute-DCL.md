# is\_default Attribute (DCL)

Specifies whether the button is the default button selected ("pushed") when the user presses the accept key.

*Supported Platforms:* Windows, Mac OS, and Web

```
is_default = true-false;
```

Possible values are
true or
false (default:
false). If the user is in an
edit\_box,
list\_box, or
image\_button that has the
allow\_accept attribute set to
true, the default button is also selected if the user presses the accept key or (for list boxes and image buttons) double-clicks.
The default button is not selected by the accept key if another button has focus. In this case, the button that has focus
is the one selected.

Only one button in a dialog box can have the
is\_default attribute set to
true.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [button Title (DCL)](button-Title-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*