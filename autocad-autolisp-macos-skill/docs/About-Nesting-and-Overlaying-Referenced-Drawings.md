# About Nesting and Overlaying Referenced Drawings

Attached DWG references (xrefs) can be nested: that is, you can attach an xref that contains another xref.

Xrefs can be nested within other xrefs: that is, you can attach an xref that contains another xref. You can attach as many
copies of an xref as you want, and each copy can have a different position, scale, and rotation.

In the following illustration, *master.dwg* references *a.dwg* and *b.dwg*. Drawing *a.dwg* references *c.dwg*. In *master.dwg*, *c.dwg* is a nested xref.

![](../images/GUID-37F300D9-AFC4-43A4-AF67-598BB9480A8A-low.png)

You can also overlay an xref on your drawing. Unlike an attached xref, an overlaid xref is *not* included when the drawing is itself attached or overlaid as an xref to another drawing. Overlaid xrefs are designed for data
sharing in a network environment. By overlaying an xref, you can see how your drawing relates to the drawings of other groups
without changing your drawing by attaching an xref.

In the following illustration, several people are working on drawings referenced by *master.dwg*. The person working on *a.dwg* needs to see the work being completed by the person working on *b.dwg*, but does not want to xref *b.dwg* because it would then appear twice in *master.dwg*. Instead, the person overlays *b.dwg*, which is not included when *a.dwg* is referenced by *master.dwg*.

![](../images/GUID-BD5405D0-0847-4E85-AADB-44457D1579DF-low.png)

NOTE: When using the parametric drawing feature, you can only constrain objects in the drawing to the insertion point of an Xref,
and not its nested objects.

## Relative Saved Paths and Nested Xrefs

The saved path for an xref can be a full path, a relative (partially specified) path, or no path. For a nested xref, a relative
path always references the location of its immediate host and not necessarily the currently open drawing.

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Overlay an Xref](To-Overlay-an-Xref.md)
* [Set Paths to Referenced Drawings](Set-Paths-to-Referenced-Drawings.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*