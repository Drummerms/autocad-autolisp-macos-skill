# About Layer and Spatial Indexes

To receive the maximum benefit of demand loading, it is recommended that you save any drawings that are used as xrefs with
layer and spatial indexes.

A layer index is a list showing which objects are on which layers. This list is used when the program is referencing the
drawing in conjunction with demand loading to determine which objects need to be read in and displayed. Objects on frozen
layers in a referenced drawing are not read in if the referenced drawing has a layer index and is being demand loaded.

The spatial index organizes objects based on their location in 3D space. This organization is used to efficiently determine
which objects need to be read in when the drawing is being demand loaded and clipped as an xref. If demand loading is turned
on, and the drawing is attached as an xref and clipped, the program uses the spatial index in the externally referenced drawing
to determine which objects lie within the clip boundary. The program then reads only those objects into the current session.

Spatial and layer indexes are best used in drawings that will be used as xrefs in other drawings where demand loading is enabled.
Drawings that are not going to be used as xrefs or partially opened will not benefit from layer and spatial indexing or demand
loading.

#### Related Tasks

* [To Save a Drawing With Layer and Spatial Indexes](To-Save-a-Drawing-With-Layer-and-Spatial-Indexes.md)

#### Related Concepts

* [About Improving Performance When Using Xrefs](About-Improving-Performance-When-Using-Xrefs.md)

#### Related Information

* [About Changing the Temporary Xref File Path](About-Changing-the-Temporary-Xref-File-Path.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*