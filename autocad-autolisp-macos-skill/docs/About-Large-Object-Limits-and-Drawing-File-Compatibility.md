# About Large Object Limits and Drawing File Compatibility

Drawings saved to legacy drawing file formats (AutoCAD 2007 or earlier) do not support objects larger than 256MB. With the
AutoCAD 2010 drawing file format, these limitations have been removed allowing you to save objects that are greater in size.

When saving to a legacy drawing file format ( AutoCAD 2007 or earlier), the drawing cannot contain large objects; there might
be compatibility issues with trying to open the drawing.The LARGEOBJECTSUPPORT system variable controls the object size limits
and the warning messages displayed when a drawing is saved.

If either of the following limits are exceeded, the drawing cannot be saved to a 2007 DWG format or earlier drawing file format
until the issues are resolved. Resolve the size limits by breaking the drawing or objects up into several drawings or objects.

The following explains how object size limits for drawings is determined:

* Drawing files cannot exceed an internal size limit of 4GB. This size is based on the total size of all objects in a drawing
  when uncompressed. Since a drawing file is normally compressed, the final size of a saved drawing file on disk will vary based
  on the size and number of objects in a drawing.
* Each individual object in a drawing cannot exceed an uncompressed size limit of 256MB. For example, a mesh object, when the
  drawing is saved and compressed, might be 75MB in size while the same object when uncompressed might be 257MB.

In these situations, the drawing cannot be saved to an AutoCAD 2007 or earlier file format until the issues are resolved.
You can resolve the size limits by breaking the drawing or objects up into several drawings or objects.

#### Related Information

* [About Saving Drawings](About-Saving-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*