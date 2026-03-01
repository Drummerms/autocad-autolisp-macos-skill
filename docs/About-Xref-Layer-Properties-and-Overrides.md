# About Xref Layer Properties and Overrides

You can attach any drawing file as an external reference (xref) in the current drawing, also known as the
*host drawing*. Attached xrefs are links to the model space of a specified drawing file. Changes made to the referenced drawing are automatically
reflected in the host drawing when the xref is reloaded. Opening a drawing that contains referenced drawings causes all the
xrefs to be reloaded, unless previously unloaded. You can also reload xrefs from the Reference Manager.

When you attach a drawing file, its layers and layer properties are added to the current drawing. Each layer name is prefixed
with the xref's name, which can be different than the referenced drawing's file name.

![](../images/GUID-9B1FCAE8-F50E-427E-B2CF-4B233F29A066-low.png)

You can change or override the visibility, color, linetype, and other properties of an xref's layers and define how you want
those changes handled when the xref is reloaded.

Use the VISRETAIN and VISRETAINMODE system variables to get the desired behavior for the xref layer properties in the host
drawing.

* *VISRETAIN=0*. Reloads all xref layer properties in the host drawing from the referenced drawing when the xref is reloaded, including any
  xref layer overrides.

  NOTE:VISRETAINMODE is not used when VISRETAIN is set to 0.
* *VISRETAIN=1* and
  *VISRETAINMODE=0*. No xref layer properties are reloaded in the host drawing from the referenced drawing when the xref is reloaded.
* *VISRETAIN=1* and
  *VISRETAINMODE=greater than 0*. Reloads specified xref layer properties in the host drawing from the referenced drawing, except xref layer overrides, when
  the xref is reloaded. To specify which properties to reload from the referenced drawings, set VISRETAINMODE to the sum of
  the bitcode values for each property. For example, to reload only the Freeze\Thaw (bitcode=2) and On\Off (bitcode=4) layer
  properties, set VISRETAINMODE=6.

NOTE:VISRETAIN is a drawing setting, while VISRETAINMODE is a system setting.

The XREFOVERRIDE system variable affects the display and plotting of the objects contained in all xrefs attached to a drawing.

* *XREFOVERRIDE=1*. Treats all objects on xref layers as if their properties are set to ByLayer, which forces the objects to inherit their general
  object properties from the layers in the current drawing.
* *XREFOVERRIDE=0*. Honors the object property assignments for objects on xref layers.

## Legacy Drawings and Xref Layer Property Settings

If you open a drawing created in a release earlier than AutoCAD 2019 for Mac that has a value of VISRETAIN=1, the VISRETAINMODE
system variable is ignored. Changes to the xref layer properties won't update in the current drawing when the xref is reloaded.
This behavior ensures that anytime you open a drawing that was authored in an earlier release of AutoCAD for Mac, it maintains
the visual fidelity between AutoCAD for Mac 2019 and previous AutoCAD releases and there is no change in behavior. You need
to detach and reattach the external reference drawing in AutoCAD 2019 for Mac to see the changes based on the VISRETAINMODE
value.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Change the Layer of Selected Objects](To-Change-the-Layer-of-Selected-Objects.md)
* [To Match the Layer Setting Between Selected Objects](To-Match-the-Layer-Setting-Between-Selected-Objects.md)
* [To Change the Visibility of Layers](To-Change-the-Visibility-of-Layers.md)
* [To Purge All Unused Layers](To-Purge-All-Unused-Layers.md)

#### Related References

* [Layers Palette](Layers-Palette.md)
* [VISRETAIN (System Variable)](VISRETAIN-System-Variable.md)
* [VISRETAINMODE (System Variable)](VISRETAINMODE-System-Variable.md)
* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)
* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [About Overriding Layer Properties in a Layout Viewport](About-Overriding-Layer-Properties-in-a-Layout-Viewport.md)

#### Related Information

* [About Saving and Restoring Layer States and Settings](About-Saving-and-Restoring-Layer-States-and-Settings.md)
* [Overview of Object Properties](Overview-of-Object-Properties.md)
* [Reference Manager Palette](Reference-Manager-Palette.md)
* [Reference Manager Palette Shortcut Menus](Reference-Manager-Palette-Shortcut-Menus.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*