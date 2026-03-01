# About Updating Legacy Rendering Objects and Settings

Legacy drawings containing AutoShade content and rendering settings need to be updated to be usable when rendering the model
to an image.

## Converting Legacy Lights and Materials

Drawings created with AutoCAD 2007-based products and earlier might contain legacy AutoShade information pertaining to lights
and materials. The lights and materials used in these older drawings can be converted to work in AutoCAD 2008-based products
and later.

When the 3DCONVERSIONMODE system variable is set to a value of 1, lights and materials are automatically converted when opening
an older drawing.

## Handling Scene and Camera Blocks

Drawings created with AutoCAD 2007-based products and earlier might contain legacy AutoShade information pertaining to landscape,
scene, and camera blocks. Camera blocks should be converted automatically to named views and camera objects. Landscape and
scene blocks are not migrated forward to newer releases of the product. Landscape can be added to a model using third-party
add-ins, but scene information must be recreated with the available rendering settings and objects.

#### Related Concepts

* [About Rendering](About-Rendering.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*