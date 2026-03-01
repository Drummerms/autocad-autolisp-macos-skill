# Predefined Attributes for Tiles Reference (DCL)

Listing of the attributes used to set the appearance and behavior for tiles and dialog definition.

This section lists the attributes defined by the PDB feature. The following table summarizes the predefined attributes in
alphabetical order. The attributes are described in detail in About User-Defined Attributes (DCL).

| Predefined attributes | | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Attribute name | Associated with | Meaning (if specified or true) | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [action](action-Attribute-DCL.md) | All active tiles | AutoLISP action expression | ✓ | ✓ | ✓ | -- | ✓ |
| [alignment](alignment-Attribute-DCL.md) | All tiles | Horizontal or vertical position in a cluster | ✓ | ✓ | ✓ | -- | ✓ |
| [allow\_accept](allow_accept-Attribute-DCL.md) | edit\_box, image\_button, list\_box | Activates is\_default button when this tile is selected  NOTE:This attribute isn't supported by the edit\_box tile on Mac OS and Web. | ✓ | ✓ | ✓ | -- | ✓ |
| [aspect\_ratio](aspect_ratio-Attribute-DCL.md) | image, image\_button | Aspect ratio of an image | ✓ | ✓ | ✓ | -- | ✓ |
| [big\_increment](big_increment-Attribute-DCL.md) | slider | Incremental distance to move | ✓ | ✓ | -- | -- | -- |
| [children\_alignment](children_alignment-Attribute-DCL.md) | row, column, radio\_row, radio\_column, boxed\_row, boxed\_column, boxed\_radio\_row, boxed\_radio\_column | Alignment of a cluster's children | ✓ | ✓ | ✓ | -- | ✓ |
| [children\_fixed\_height](children_fixed_height-Attribute-DCL.md) | row, column, radio\_row, radio\_column, boxed\_row, boxed\_column, boxed\_radio\_row, boxed\_radio\_column | Height of a cluster's children doesn't grow during layout | ✓ | ✓ | ✓ | -- | ✓ |
| [children\_fixed\_width](children_fixed_width-Attribute-DCL.md) | row, column, radio\_row, radio\_column, boxed\_row, boxed\_column, boxed\_radio\_row, boxed\_radio\_column | Width of a cluster's children doesn't grow during layout | ✓ | ✓ | ✓ | -- | ✓ |
| [color](color-Attribute-DCL.md) | image, image\_button | Background (fill) color of an image | ✓ | ✓ | ✓ | -- | ✓ |
| [edit\_limit](edit_limit-Attribute-DCL.md) | edit\_box | Maximum number of characters users can enter | ✓ | ✓ | -- | -- | -- |
| [edit\_width](edit_width-Attribute-DCL.md) | edit\_box, popup\_list | Width of the edit (input) portion of the tile | ✓ | ✓ | ✓ | -- | ✓ |
| [fixed\_height](fixed_height-Attribute-DCL.md) | All tiles | Height doesn't grow during layout | ✓ | ✓ | ✓ | -- | ✓ |
| [fixed\_width](fixed_width-Attribute-DCL.md) | All tiles | Width doesn't grow during layout | ✓ | ✓ | ✓ | -- | ✓ |
| [fixed\_width\_font](fixed_width_font-Attribute-DCL.md) | list\_box, popup\_list | Displays text in a fixed pitch font | ✓ | ✓ | -- | -- | -- |
| [height](height-Attribute-DCL.md) | All tiles | Height of the tile | ✓ | ✓ | ✓ | -- | ✓ |
| [initial\_focus](initial_focus-Attribute-DCL.md) | Dialog | Key of the tile with initial focus | ✓ | ✓ | -- | -- | -- |
| [is\_bold](is_bold-Attribute-DCL.md) | Text | Displays as bold | ✓ | ✓ | ✓ | -- | ✓ |
| [is\_cancel](is_cancel-Attribute-DCL.md) | Button | Button is activated when the cancel key—usually ESC—is pressed | ✓ | ✓ | ✓ | -- | ✓ |
| [is\_default](is_default-Attribute-DCL.md) | Button | Button is activated when the accept key—usually ENTER—is pressed | ✓ | ✓ | ✓ | -- | ✓ |
| [is\_enabled](is_enabled-Attribute-DCL.md) | All active tiles | Tile is initially enabled | ✓ | ✓ | ✓ | -- | ✓ |
| [is\_tab\_stop](is_tab_stop-Attribute-DCL.md) | All active tiles | Tile is a tab stop | ✓ | ✓ | -- | -- | -- |
| [key](key-Attribute-DCL.md) | All active tiles | Tile name used by the application | ✓ | ✓ | ✓ | -- | ✓ |
| [label](label-Attribute-DCL.md) | boxed\_row, boxed\_column, boxed\_radio\_row, boxed\_radio\_column, button, dialog, edit\_box, list\_box, popup\_list, radio\_button, text, toggle | Displayed label of the tile | ✓ | ✓ | ✓ | -- | ✓ |
| [layout](layout-Attribute-DCL.md) | slider | Whether the slider is horizontal or vertical | ✓ | ✓ | ✓ | -- | ✓ |
| [list](list-Attribute-DCL.md) | list\_box, popup\_list | Initial values to display in list | ✓ | ✓ | ✓ | -- | ✓ |
| [max\_value](max_value-Attribute-DCL.md) | slider | Maximum value of a slider | ✓ | ✓ | ✓ | -- | ✓ |
| [min\_value](min_value-Attribute-DCL.md) | slider | Minimum value of a slider | ✓ | ✓ | ✓ | -- | ✓ |
| [mnemonic](mnemonic-Attribute-DCL.md) | all active tiles | Mnemonic character for the tile | ✓ | ✓ | -- | -- | -- |
| [multiple\_select](multiple_select-Attribute-DCL.md) | list\_box | List box allows multiple items to be selected | ✓ | ✓ | ✓ | -- | ✓ |
| [password\_char](password_char-Attribute-DCL.md) | edit\_box | Masks characters entered in edit\_box | ✓ | ✓ | ✓ | -- | ✓ |
| [small\_increment](small_increment-Attribute-DCL.md) | slider | Incremental distance to move | ✓ | ✓ | ✓ | -- | ✓ |
| [tab\_truncate](tab_truncate-Attribute-DCL.md) | list\_box, popup\_list | Truncates text that is larger than the associated tab stop | ✓ | ✓ | -- | -- | -- |
| [tabs](tabs-Attribute-DCL.md) | list\_box, popup\_list | Tab stops for list display | ✓ | ✓ | ✓ | -- | ✓ |
| [value](value-Attribute-DCL.md) | Text, active tiles (except buttons and image buttons) | Tile's initial value | ✓ | ✓ | ✓ | -- | ✓ |
| [width](width-Attribute-DCL.md) | All tiles | Width of the tile | ✓ | ✓ | ✓ | -- | ✓ |

#### Topics in this section

* [action Attribute (DCL)](action-Attribute-DCL.md)

  Specifies an AutoLISP expression to perform an action when this tile is selected. Also known as a callback.
* [alignment Attribute (DCL)](alignment-Attribute-DCL.md)

  Specifies the horizontal or vertical positioning (justification) of a tile within its cluster.
* [allow\_accept Attribute (DCL)](allow_accept-Attribute-DCL.md)

  Specifies whether the tile is activated when the user presses the accept key (usually Enter).
* [aspect\_ratio Attribute (DCL)](aspect_ratio-Attribute-DCL.md)

  Specifies the ratio of the width of the image to its height (width divided by height).
* [big\_increment Attribute (DCL)](big_increment-Attribute-DCL.md)

  Specifies the value used by the slider's incremental controls.
* [children\_alignment Attribute (DCL)](children_alignment-Attribute-DCL.md)

  Specifies the default alignment (similar to
  alignment) for all tiles in a cluster.
* [children\_fixed\_height Attribute (DCL)](children_fixed_height-Attribute-DCL.md)

  Specifies the default height (similar to
  height) for all tiles in a cluster.
* [children\_fixed\_width Attribute (DCL)](children_fixed_width-Attribute-DCL.md)

  Specifies the default width (similar to width) for all tiles in a cluster.
* [color Attribute (DCL)](color-Attribute-DCL.md)

  Specifies the background (fill) color of the image.
* [edit\_limit Attribute (DCL)](edit_limit-Attribute-DCL.md)

  Specifies the maximum number of characters a user is allowed to enter in the edit box.
* [edit\_width Attribute (DCL)](edit_width-Attribute-DCL.md)

  Specifies the width in character-width units of the edit (input) portion of the box—the actual boxed portion of the
  edit\_box tile.
* [fixed\_height Attribute (DCL)](fixed_height-Attribute-DCL.md)

  Specifies if a tile's height is allowed to fill the available space.
* [fixed\_width Attribute (DCL)](fixed_width-Attribute-DCL.md)

  Specifies if a tile's width is allowed to fill the available space.
* [fixed\_width\_font Attribute (DCL)](fixed_width_font-Attribute-DCL.md)

  Specifies whether a list box or pop-up list will display text in a fixed pitch font.
* [height Attribute (DCL)](height-Attribute-DCL.md)

  Specifies the height of a tile.
* [initial\_focus Attribute (DCL)](initial_focus-Attribute-DCL.md)

  Specifies the key of the tile within the dialog box that receives the initial keyboard focus.
* [is\_bold Attribute (DCL)](is_bold-Attribute-DCL.md)

  Specifies whether the text is displayed in bold characters.
* [is\_cancel Attribute (DCL)](is_cancel-Attribute-DCL.md)

  Specifies whether the button is selected when the user presses the Esc key.
* [is\_default Attribute (DCL)](is_default-Attribute-DCL.md)

  Specifies whether the button is the default button selected ("pushed") when the user presses the accept key.
* [is\_enabled Attribute (DCL)](is_enabled-Attribute-DCL.md)

  Specifies whether or not the tile is initially available.
* [is\_tab\_stop Attribute (DCL)](is_tab_stop-Attribute-DCL.md)

  Specifies whether the tile receives keyboard focus when the user moves between tiles by pressing the Tab key.
* [key Attribute (DCL)](key-Attribute-DCL.md)

  Specifies a name that the program uses to refer to this specific tile.
* [label Attribute (DCL)](label-Attribute-DCL.md)

  Specifies the text displayed within the tile.
* [layout Attribute (DCL)](layout-Attribute-DCL.md)

  Specifies the orientation of a slider.
* [list Attribute (DCL)](list-Attribute-DCL.md)

  Specifies the initial set of lines (choices) to be placed in the
  popup\_list or
  list\_box.
* [max\_value Attribute (DCL)](max_value-Attribute-DCL.md)

  Specifies the upper range of values that a slider returns.
* [min\_value Attribute (DCL)](min_value-Attribute-DCL.md)

  Specifies the lower range of values that a slider returns.
* [mnemonic Attribute (DCL)](mnemonic-Attribute-DCL.md)

  Specifies a keyboard mnemonic character for the tile.
* [multiple\_select Attribute (DCL)](multiple_select-Attribute-DCL.md)

  Specifies whether multiple items in the
  list\_box can be selected (highlighted) at the same time.
* [password\_char Attribute (DCL)](password_char-Attribute-DCL.md)

  Specifies the character to be used to mask user input.
* [small\_increment Attribute (DCL)](small_increment-Attribute-DCL.md)

  Specifies the value used by the slider's incremental controls.
* [tab\_truncate Attribute (DCL)](tab_truncate-Attribute-DCL.md)

  Specifies whether the text in a list box or pop-up list is truncated if it is larger than the associated tab stop.
* [tabs Attribute (DCL)](tabs-Attribute-DCL.md)

  Specifies the placement of tabs in character width units.
* [value Attribute (DCL)](value-Attribute-DCL.md)

  Specifies the initial value of a tile. Possible value is a quoted string.
* [width Attribute (DCL)](width-Attribute-DCL.md)

  Specifies the width of a tile.

#### Related Concepts

* [About User-Defined Attributes (DCL)](About-User-Defined-Attributes-DCL.md)
* [About Restricted Attributes (DCL)](About-Restricted-Attributes-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*