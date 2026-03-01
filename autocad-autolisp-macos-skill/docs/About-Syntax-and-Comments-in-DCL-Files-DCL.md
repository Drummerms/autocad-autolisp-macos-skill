# About Syntax and Comments in DCL Files (DCL)

Dialog control language (DCL) files are plain ASCII files which define a dialog box and its elements.

Elements in a dialog box, such as buttons and edit boxes, are known as tiles. The size and functionality of each tile is controlled
by the tile's attributes. The size of the dialog box and the layout of its parts are set automatically with a minimum of positioning
information.

A dialog definition starts with the use of the dialog tile. You must prefix each dialog definition in a DCL file with a unique
name; this name is used to reference the dialog box from the AutoLISP program that will be displaying it. The label attribute
of the dialog tile can be used to set the text that will appear in the dialog’s title bar.

The following is an example of a dialog definition that has the name
minimaldcl. This example assigns a title to the dialog box and displays a single OK button.

```
minimaldcl : dialog
{
  label="Minimal Example";
  ok_only;
}
```

NOTE:A dialog definition must have at least a Cancel or OK button to be a valid dialog box.

After you have a basic dialog box defined, you can then add tiles to it which represent the controls that provide information
to the user or allow the user to start an action. The
ok\_only tile in the previous example is a predefined tile definition for a button with the label OK. The appearance and the callback
action for a tile are defined using attribute and attribute value parings. The following illustration shows an example of
a dialog box defined in a DCL file with the title Garden Path Tile Specification.

![](../images/GUID-BC0EE214-C6CD-45DB-A5F1-751BC5EB6755-low.png)

The following shows the contents of the DCL file containing the dialog and its tiles with their attributes for the Garden
Path Tile Specification dialog box:

```
gp_mainDialog : dialog {
  label = "Garden Path Tile Specifications";
  : boxed_radio_column {     // defines the radio button areas
    label = "Outline Polyline Type";
    : radio_button {         // defines the Lightweight radio button
      label = "&Lightweight";
      key = "gp_lw";
      value = "1";
    }
    : radio_button {         // defines the "legacy" polyline radio button
      label = "&Legacy";
      key = "gp_hw";
    }
  }

  : boxed_radio_column {     // defines the radio button areas
    label = "Tile Creation Method";
    : radio_button {         // defines the ActiveX radio button
      label = "&ActiveX Automation";
      key = "gp_actx";
      value = "1";
    }
    : radio_button {         // defines the (entmake) radio button
      label = "&Entmake";
      key = "gp_emake";
    }
    : radio_button {         // defines the (command) radio button
      label = "&Command";
      key = "gp_cmd";
    }
  }

  : edit_box {               // defines the Radius of Tile edit box
    label = "&Radius of tile";
    key = "gp_trad";
    edit_width = 6;
  }
  : edit_box {               // defines the Spacing Between Tiles edit box
    label = "&Spacing between tiles";
    key = "gp_spac";
    edit_width = 6;
  }
  : row {                    // defines the OK/Cancel button row
    : spacer { width = 1; }
    : button {               // defines the OK button
      label = "OK";
      is_default = true;
      key = "accept";
      width = 8;
      fixed_width = true;
   }
   : button {                // defines the Cancel button
     label = "Cancel";
     is_cancel = true;
     key = "cancel";
     width = 8;
     fixed_width = true;
   }
   : spacer { width = 1;}
  }
}
```

## Comments

A statement preceded by two forward slashes ( *//* ) is treated as a comment in a DCL file. Anything that appears between the // and the end of the line is ignored. DCL also
allows C language style comments. These have the form
/\* comment text \*/. The starting
 */\**  and ending
 *\*/*  can be on separate lines.

#### Topics in this section

* [About Tile Definitions (DCL)](About-Tile-Definitions-DCL.md)

  Tile definitions are used to create new prototypes or subassemblies that can be used in your dialog boxes.
* [About Tile References (DCL)](About-Tile-References-DCL.md)

  Tile references are used to add a tile to your dialog box definition.
* [About Attributes and Attribute Values (DCL)](About-Attributes-and-Attribute-Values-DCL.md)

  Attributes are used to control the appearance and placement of a tile definition in a DCL file.
* [About Comments in DCL Files (DCL)](About-Comments-in-DCL-Files-DCL.md)
* [About Semantic Auditing of DCL Files (DCL)](About-Semantic-Auditing-of-DCL-Files-DCL.md)

  AutoCAD provides a choice of four levels (0-3) of semantic auditing for DCL files.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)
* [About Tile Definitions (DCL)](About-Tile-Definitions-DCL.md)
* [About Tile References (DCL)](About-Tile-References-DCL.md)
* [About Referencing DCL Files (DCL)](About-Referencing-DCL-Files-DCL.md)
* [About Semantic Auditing of DCL Files (DCL)](About-Semantic-Auditing-of-DCL-Files-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*