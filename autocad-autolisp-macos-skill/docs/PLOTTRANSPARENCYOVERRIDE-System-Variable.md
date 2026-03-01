# PLOTTRANSPARENCYOVERRIDE (System Variable)

Controls whether object transparency is plotted.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 1 |

| 0 | Does not plot object transparency |
| 1 | Uses the setting specified in the Page Setup or the Plot dialog boxes |
| 2 | Plots object transparency |

Setting the PLOTTRANSPARENCYOVERRIDE system variable to 0 or 2 overrides the Print Transparency option in the Page Setup dialog
box.

WARNING:Because this system variable can affect global plot performance, it is strongly advised that you leave the value set to 1
and manage plot transparency when plotting.

#### Related Concepts

* [About Setting Options for Plotted Objects](About-Setting-Options-for-Plotted-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*