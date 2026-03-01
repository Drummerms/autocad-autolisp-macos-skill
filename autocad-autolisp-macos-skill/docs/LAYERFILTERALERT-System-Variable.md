# LAYERFILTERALERT (System Variable)

Deletes excessive dynamic layer group filters to improve performance.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

When a drawing has 100 or more dynamic layer group filters, and the number of filters exceeds the number of layers, LAYERFILTERALERT
provides a method for deleting filters to improve performance.

| 0 | Off |
| 1 | When the Layers palette is opened, deletes all dynamic layer group filters; no message is displayed |
| 2 | When the Layers palette is opened, displays a message that states the problem, recommends deleting all dynamic layer group filters, and offers a choice: “Do you want to delete all dynamic layer group filters now?” |
| 3 | When the drawing is opened, displays a message that states the problem and offers to display a dialog box where you can choose which dynamic layer group filters to delete |

#### Related Tasks

* [To Work with the Layer List in the Layers Palette](To-Work-with-the-Layer-List-in-the-Layers-Palette.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*