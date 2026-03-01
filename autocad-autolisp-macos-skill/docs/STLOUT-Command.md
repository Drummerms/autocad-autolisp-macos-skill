# STLOUT (Command)

Stores solids in an ASCII or binary file.

## Summary

The [FACETRES](FACETRES-System-Variable.md) system variable determines how the solid is triangulated. A higher value creates a finer mesh that more accurately represents
the model. This also results in a much larger file.

Select solids or watertight meshes

You can select blocks or external references (xrefs) that contain solids or watertight meshes. Only solids and watertight
meshes of the selected blocks of xrefs are included in the STL file. All other geometry is discarded.

Create a binary STL file? [Yes/No] <Yes>: *To create a STL file, enter* *y* *or press* Enter*. To create an ASCII file, enter* *n*

The [Create STL File dialog box](Create-STL-File-Dialog-Box.md) displays.

The file is created with the *.stl* file name extension. The STL file format is compatible with stereolithography apparatus (SLA). The solid data is transferred
to the SLA as a faceted representation of the model. The facets consist of a set of triangles (with outward pointing normals)
that approximate the faces of the model. From the faceted data, the SLA workstation produces a set of contours that defines
a series of layers representing the part to be built.

#### Related Concepts

* [Create STL File Dialog Box](Create-STL-File-Dialog-Box.md)
* [About Exporting Stereolithography STL Files](About-Exporting-Stereolithography-STL-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*