# VSOBSCUREDLTYPE (System Variable)

Specifies the linetype of obscured (hidden) lines in the visual style applied to the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 |

The range is 1 to 11.

| 1 | Solid ![](../images/GUID-2BD9AB6C-3337-4856-AF73-E8733A8C3607-low.png) |
| 2 | Dashed ![](../images/GUID-BE849E52-7620-4B29-806A-A8F3158D1216-low.png) |
| 3 | Dotted ![](../images/GUID-6840682A-F1CF-47E9-9FEE-024E0D2B3A92-low.png) |
| 4 | Short Dash ![](../images/GUID-6C7F8371-51E3-4C40-9497-10E8BF4CF9B6-low.png) |
| 5 | Medium Dash ![](../images/GUID-1C4A1E04-1E17-4B72-B365-1F7D2B3981FE-low.png) |
| 6 | Long Dash ![](../images/GUID-C9728E02-9AAB-4D06-9D97-5221D02CE111-low.png) |
| 7 | Double Short Dash ![](../images/GUID-60D0CCE3-102F-4C08-9BBD-4A6A981647D1-low.png) |
| 8 | Double Medium Dash ![](../images/GUID-C21A88A8-04D3-40B6-AB94-BA8BB29D74B4-low.png) |
| 9 | Double Long Dash ![](../images/GUID-0F3B606C-505E-4E1F-8DAD-6CBC44B02327-low.png) |
| 10 | Medium Long Dash ![](../images/GUID-BA61C9AF-F8DE-420F-8C79-088908B64ED8-low.png) |
| 11 | Sparse Dot ![](../images/GUID-137ACDA9-60A9-4DB4-BB23-1B63B7071EBA-low.png) |

The initial value of VSOBSCUREDLTYPE varies on the current visual style.

| Visual Style (VSCURRENT) | Initial Value |
| 2D Wireframe | 1 |
| Conceptual | 1 |
| Hidden | 2 |
| Shaded | 1 |
| Shaded with Edges | 2 |
| Shades of Gray | 1 |
| Sketchy | 1 |
| Wireframe | 1 |
| X-ray | 1 |
| Realistic | 1 |

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*