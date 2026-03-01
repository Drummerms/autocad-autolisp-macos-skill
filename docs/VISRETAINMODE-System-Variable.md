# VISRETAINMODE (System Variable)

Controls the behavior of the
VISRETAIN system variable when it's set to 1.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 0 |

Use this system variable in conjunction with the
VISRETAIN system variable to control which xref layer properties that you want to automatically sync on reload.

NOTE:Xref layer properties with overrides are not synced when the xref is reloaded. To clear any overrides, use the shortcut menu
option, Reset Xref Layer Properties For, on the Layers palette.

| Value | Description |
| 0 | No settings are synchronized. |
| 1 | On/Off synchronized. |
| 2 | Freeze/Thaw synchronized. |
| 4 | Lock/Unlock synchronized. |
| 8 | Plot/No Plot synchronized. |
| 16 | Color synchronized. |
| 32 | Linetype synchronized. |
| 64 | Lineweight synchronized. |
| 128 | Transparency synchronized. |
| 256 | Plot style synchronized. |
| 512 | New VP Freeze synchronized. |
| 1024 | Description synchronized. |

To specify more than one layer property to sync, enter the sum of the bitcode values. For example, a value of 3 specifies
that both the On/Off (1) and Freeze/Thaw (2) layer properties will automatically sync when the xref is reloaded.

#### Related References

* [VISRETAIN (System Variable)](VISRETAIN-System-Variable.md)
* [Layers Palette](Layers-Palette.md)

#### Related Concepts

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*