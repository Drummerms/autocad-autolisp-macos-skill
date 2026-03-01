# About Predefined Active Tiles (DCL)

Predefined controls make it possible to implement commonly used Windows controls.

The AutoCAD PDB feature has a set of built-in, or predefined, tiles that can be used by themselves or as the basis for more
complex tiles. Their definitions appear as comments within the
*base.dcl* file.

When the user chooses an active tile—a button, for example—the dialog box responds by notifying the application controlling
the dialog box. Any predefined active tile can have an associated action. The effect of an action can be visible to the user
or can be purely internal (for example, a status update). Actions are accompanied by a reason code that indicates what triggered
the action. The meaning of the reason depends on which kind of tile triggered it. The following tiles are selectable, active
tiles:

| Decorative and Informative Tiles | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Tile name | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [button](button-Title-DCL.md) | A button tile resembles a push button. | ✓ | ✓ | ✓ | -- | ✓ |
| [edit\_box](edit_box-Tile-DCL.md) | An edit box is a field that enables the user to enter or edit a single line of text. | ✓ | ✓ | ✓ | -- | ✓ |
| [image](image-Tile-DCL.md) | An image is a rectangle in which a vector graphic picture is displayed. | ✓ | ✓ | -- | -- | -- |
| [image\_button](image_button-Tile-DCL.md) | The image button tile is a button that displays a graphic image rather than a label. | ✓ | ✓ | ✓ | -- | ✓ |
| [list\_box](list_box-Tile-DCL.md) | A list box contains a list of text strings, arranged in rows. | ✓ | ✓ | ✓ | -- | ✓ |
| [popup\_list](popup_list-Tile-DCL.md) | A pop-up list, or simply pop-up, is functionally equivalent to a list box. | ✓ | ✓ | ✓ | -- | ✓ |
| [radio\_button](radio_button-Tile-DCL.md) | A radio button is one of a group of buttons composing a radio column or radio row. | ✓ | ✓ | ✓ | -- | ✓ |
| [slider](slider-Tile-DCL.md) | A slider obtains a numeric value. | ✓ | ✓ | ✓ | -- | ✓ |
| [toggle](toggle-Tile-DCL.md) | A toggle appears as a small box with an optional label to the right of the box. | ✓ | ✓ | ✓ | -- | ✓ |

#### Related Concepts

* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [Text Cluster Tiles (DCL)](Text-Cluster-Tiles-DCL.md)
* [Cluster Tiles Reference (DCL)](Cluster-Tiles-Reference-DCL.md)
* [About Restricted Tiles (DCL)](About-Restricted-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*