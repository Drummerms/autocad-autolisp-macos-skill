# DYNMODE (System Variable)

Turns Dynamic Input features on and off.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 3 |

When all features are on, the context governs what is displayed.

When DYNMODE is set to a negative value, the Dynamic Input features are not turned on, but the setting is stored. Press the
Dynamic Input button in the status bar to set DYNMODE to the corresponding positive value.

| 0 | All Dynamic Input features, including dynamic prompts, off |
| 1 | Pointer input on |
| 2 | Dimensional input on |
| 3 | Both pointer input and dimensional input on |

If dynamic prompts are on (DYNPROMPT is set to 1), they are displayed when DYNMODE is set to 1, 2, or 3.

When dimensional input is turned on (DYNMODE = 2 or 3), the program switches to pointer input when you enter a comma or an
angle bracket (<), or when you select multiple grip points.

When DYNMODE is set to 1, 2, or 3, you can turn off all features temporarily by holding down the temporary override key, Fn-F12.

Settings are on the Dynamic Input tab in the Drafting Settings dialog box.

#### Related References

* [Drafting Settings Dialog Box](Drafting-Settings-Dialog-Box.md)
* [DYNPROMPT (System Variable)](DYNPROMPT-System-Variable.md)

#### Related Concepts

* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*