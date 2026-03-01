# is\_cancel Attribute (DCL)

Specifies whether the button is selected when the user presses the Esc key.

*Supported Platforms:* Windows, Mac OS, and Web

```
is_cancel = true-false;
```

Possible values are
true or
false (default:
false).

If the action expression for buttons with the
is\_cancel attribute set to
true does not exit the dialog box (does not call
done\_dialog), the dialog box is automatically terminated after the action expression has been carried out, and the AutoCAD DIASTAT system
variable is set to 0.

Only one button in a dialog box can have the
is\_cancel attribute set to
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