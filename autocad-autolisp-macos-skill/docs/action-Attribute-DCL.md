# action Attribute (DCL)

Specifies an AutoLISP expression to perform an action when this tile is selected. Also known as a callback.

*Supported Platforms:* Windows, Mac OS, and Web

```
action = "(function)";
```

For some kinds of tiles, an action can also occur when the user switches focus to a different tile.

The possible value is a quoted string that is a valid AutoLISP ®  expression. A tile can have only one action. If the application assigns it an action (with
action\_tile), this overrides the
action attribute.

NOTE:You cannot call the AutoLISP
command or
command-s functions from the
action attribute.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*