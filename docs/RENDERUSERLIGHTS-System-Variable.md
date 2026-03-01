# RENDERUSERLIGHTS (System Variable)

Controls whether to override the setting for viewport lighting during rendering.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

Provides a way of overriding the [DEFAULTLIGHTING](DEFAULTLIGHTING-System-Variable.md) system variable for rendering while retaining the setting for working in a viewport.

| 0 | The current lights in the viewport are used in the rendered scene, either default lights or user lights, as specified by the DEFAULTLIGHTING system variable. |
| 1 | Overrides the setting for the DEFAULTLIGHTING system variable. Only user lights are rendered. |

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*