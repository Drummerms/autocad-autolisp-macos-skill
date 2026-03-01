# About Improving Performance When Using Xrefs

## Unload Xrefs in Large Drawings

When a referenced drawing (xref) is unloaded from the current drawing, the drawing opens much faster and uses less memory.

The xref definition is unloaded from the drawing file, but the internal pointer to the referenced drawing remains. The xref
is not displayed, and nongraphical object information does not appear in the drawing. However, you can restore all the information
by reloading the xref. If XLOADCTL (demand loading) is set to 1, unloading the drawing unlocks the original file.

You should unload a reference file if it is not needed in the current drawing session but may be used later for plotting.
You can maintain a working list of unloaded xrefs in the drawing file that you can load as needed.

## Overview of Demand Loading

The program uses
*demand loading* and saving drawings with internal indexes to increase performance with large referenced drawings that have been clipped,
or that have many objects on frozen layers. With demand loading, only the data from the reference drawing that is necessary
to regenerate the current drawing is loaded into memory. In other words, referenced data is read in “on demand.”

Demand loading works in conjunction with the INDEXCTL, XLOADCTL, and XLOADPATH system variables.

To maximize the benefits of demand loading, save referenced drawings with layer and spatial indexes. The performance benefits
of demand loading are most noticeable when you do one of the following:

* Clip the xref to display a small fraction of it. A spatial index is saved in the externally referenced drawing.
* Freeze several layers of the xref. The externally referenced drawing is saved with a layer index.

If demand loading is turned on, and you have clipped xrefs with spatial indexes, objects in the referenced drawing database
contained within the clip volume comprise the majority of the objects read into the drawing. If the clip volume is modified
more objects are loaded as needed from the reference drawing. Similarly, if you have xrefs with many layers frozen that were
saved with layer indexes, only the objects on those thawed layers are read into the current drawing. If those xref-dependent
layers are thawed, the program reads in that geometry from the reference drawing as required.

When demand loading is enabled, the program places a lock on all reference drawings so that it can read in any geometry it
needs to on demand. Other users can open those reference drawings, but they cannot save changes to them. If you want other
users to be able to modify an xref that is being demand loaded into another drawing, use demand loading with the Copy option.

If you turn on demand loading with the Enable with Copy option, the program makes a temporary copy of the referenced drawing
and demand loads the temporary file. You can then demand load the xref while allowing the original reference drawing to be
available for modification. When you turn off demand loading, the program reads in the entire reference drawing regardless
of layer visibility or clip instances.

Layer and spatial indexes were added in AutoCAD Release 14 and AutoCAD LT 97. If you externally reference a drawing saved
in a release previous to this, you do not see the same performance benefit as drawings saved with the indexes. For maximum
performance, use demand loading with referenced drawings saved with layer and spatial indexes turned on in AutoCAD Release
14, AutoCAD LT 97, or more recent versions.

#### Related Concepts

* [About Layer and Spatial Indexes](About-Layer-and-Spatial-Indexes.md)

#### Related Information

* [To Unload an Xref](To-Unload-an-Xref.md)
* [About Changing the Temporary Xref File Path](About-Changing-the-Temporary-Xref-File-Path.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*