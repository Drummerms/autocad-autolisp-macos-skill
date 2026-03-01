# About Customizing Exit Buttons (DCL)

You may want to change the text of one of the exit buttons for some dialog boxes.

For example, if you create a dialog box capable of destroying data, it is safer to label the button Destroy instead of OK.
To do this, use the
retirement\_button prototype as follows:

```
destroy_button : retirement_button {
  label = "&Destroy";
  key = "destroy";
}
```

Notice the use of the ampersand ( *&* ) in the text being assigned to the label attribute. This assigns a mnemonic to the tile. In this case the letter D is underscored
in the button label and becomes the mnemonic.

NOTE:When customizing existing button subassemblies, you should obtain the proper DCL code from your
*base.dcl* file.

Once you have defined a custom exit button, you need to embed it in a subassembly that matches the appearance and functionality
of the standard clusters. The following example shows the default definition of
ok\_cancel\_help:

```
ok_cancel_help : column {
  : row {
    fixed_width = true;
    alignment = centered;
    ok_button;
    : spacer { width = 2; }
    cancel_button;
    : spacer { width = 2; }
    help_button;
  }
}
```

The new subassembly that replaces the
ok\_button with the new button might look like the following:

```
destroy_cancel_help : column {
  : row {
    fixed_width = true;
    alignment = centered;
    destroy_button;
    : spacer { width = 2; }
    cancel_button;
    : spacer { width = 2; }
    help_button;
  }
}
```

In the standard subassembly, the OK button is the default, but this attribute was not added to
destroy\_button. Where the dialog box's action can be destructive (or very time-consuming), it is strongly recommended to make the Cancel
button the default. For example, the following defines the Cancel button as both the Default and Abort button:

```
destroy_cancel_help : column {
  : row {
    fixed_width = true;
    alignment = centered;
    destroy_button;
    : spacer { width = 2; }
    : cancel_button { is_default = true; }
    : spacer { width = 2; }
    help_button;
  }
}
```

Because an attribute has been changed, the original Cancel button is used as a prototype, requiring a colon in front of
cancel\_button.

NOTE:When the Cancel button and the Default button are the same (both
is\_default and
is\_cancel are
true) and you neglect to assign an action that calls
done\_dialog to any other button, then no other button can exit the dialog box and it will always be canceled.

#### Related Concepts

* [About Error Handling in Dialog Boxes (DCL)](About-Error-Handling-in-Dialog-Boxes-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [About Alert Boxes (DCL)](About-Alert-Boxes-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Predefined Active Tiles (DCL)](About-Predefined-Active-Tiles-DCL.md)
* [Predefined Attributes for Tiles Reference (DCL)](Predefined-Attributes-for-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*