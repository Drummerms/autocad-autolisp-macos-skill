# About Attaching and Detaching Referenced Drawings (Xrefs)

You can insert any drawing file as an external reference or
*xref* in the current drawing.

When you attach a drawing file as an xref, you link that referenced drawing to the current drawing. Any changes to the referenced
drawing are displayed in the current drawing when it is opened or reloaded.

A drawing file can be attached as an xref to multiple drawings at the same time. Conversely, multiple drawings can be attached
as referenced drawings to a single drawing.

## Tools for Attaching Xrefs

You can use several methods to attach an xref:

* Click
  Window menu ![](../images/ac.menuaro.gif) Reference Manager.
* At the Command prompt, enter EXTERNALREFERENCES.
* At the Command prompt, enter XATTACH.

The saved path used to locate the xref can be a relative (partially specified) path, the full path, or no path.

If an xref contains any variable block attributes, they are ignored.

## Receive Notification of Attached Xrefs

When one or more xrefs are not found, or if any of the xrefs need reloading, a balloon message is displayed near the lower-left
corner of the drawing area. Click the link in the balloon message to reload the xref. If Compare Changes is checked, the xref
is compared to its reference drawing and the comparison results display in the current drawing. When you close the comparison,
the xref is reloaded.

![](../images/GUID-900B6F6C-7A7C-4AF4-965A-C2BAAE0100CB-low.png)

## Compare an Xref

You can compare an xref with the reference drawing file at any time. Right-click an xref in the Reference Manager and select
one of the compare options. Differences are highlighted with color and revision clouds in the current drawing.

## Detaching Referenced Drawings

To completely remove DWG references (xrefs) from your drawing, you need to detach them rather than erase them.

Erasing xrefs does not remove, for example, layer definitions associated with those xrefs. Using the Detach option removes
the xrefs and all associated information.

## Highlight External References in a Drawing

To find an external reference in a complex drawing, select an item in the External References palette to highlight all visible
instances in the drawing. Conversely, select an external reference in the drawing to highlight its name in the External References
palette.

NOTE:The ERHIGHLIGHT system variable controls whether referenced objects are highlighted. You can turn highlighting off to improve
performance.

## Control the Properties of Referenced Layers

You can control the visibility, color, linetype, and other properties of an xref's layers and make these changes temporary
or permanent. If the VISRETAIN system variable is set to 0, these changes apply only to the current drawing session. They
are discarded when you end the drawing session, or when you reload or detach the xref.

You can also control the fade display of the DWG xref. The XDWGFADECTL system variable defines the fade percentage for all
DWG xrefs.

## Xref Clipping Boundaries

Drawings can include xrefs that are clipped. If you want to see the clipping boundary, you can turn on the XCLIPFRAME system
variable.

## Attachments from Educational Products

If you open, insert, or attach an xref from an Autodesk Educational Product, the drawings you plot contain the following
banner: “PRODUCED BY AN AUTODESK EDUCATIONAL PRODUCT.”

#### Related Tasks

* [To Compare Xrefs](To-Compare-Xrefs.md)

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)

#### Related Concepts

* [About Nesting and Overlaying Referenced Drawings](About-Nesting-and-Overlaying-Referenced-Drawings.md)
* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)
* [About Archiving Drawings with Xrefs (Binding)](About-Archiving-Drawings-with-Xrefs-Binding.md)

#### Related Information

* [To Work With Attaching and Detaching Referenced Drawings](To-Work-With-Attaching-and-Detaching-Referenced-Drawings.md)
* [Set Paths to Referenced Drawings](Set-Paths-to-Referenced-Drawings.md)
* [About Updating Referenced Drawing Attachments](About-Updating-Referenced-Drawing-Attachments.md)
* [About Clipping External References and Blocks](About-Clipping-External-References-and-Blocks.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)
* [XREFLAYER (System Variable)](XREFLAYER-System-Variable.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*