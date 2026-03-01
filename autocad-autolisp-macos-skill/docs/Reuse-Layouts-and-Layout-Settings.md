# Reuse Layouts and Layout Settings

When you create a layout, you can choose to apply the information from an existing template.

A layout template is a layout imported from a DWG or DWT file. When you create a layout, you can choose to apply the information
from an existing template. The program has sample layout templates to use when you design a new layout environment. The paper
space objects and page setup in the existing template are used in the new layout. Thus, the layout objects, including any
viewport objects, are displayed in paper space. You can keep any of the existing objects from the template you import, or
you can delete the objects. No model space objects are imported.

The layout templates are identified with a *.dwt* file extension. However, a layout template or layout from any drawing or drawing template can be imported into the current
drawing.

## Save a Layout Template

Any drawing can be saved as a drawing template (DWT file), including all of the objects and layout settings. You can save
a layout to a new DWT file by choosing the Save As option of the LAYOUT command. The template file is saved in the drawing
template file folder as defined in the Application tab (Application Preferences dialog box). The layout template has a *.dwt* or *.dwg* extension like a drawing template or drawing file, but it contains little information not essential to the layout.

When you create a new layout template, any named items, such as blocks, layers, and dimension styles, that are used in the
layout are saved with the template. These definition table items are imported as part of the layout settings if you import
this template into a new layout. It is recommended that you use the Save As option of the LAYOUT command to create a new layout
template. When you use the Save As option, unused definition table items are not saved with the file; they are not added to
the new layout into which you import the template.

If you insert a layout from a drawing or template that was not created using the Save As option of the LAYOUT command, definition
table items that are used in the drawing but not in the layout are inserted with the layout. To eliminate unnecessary definition
table items, use the PURGE command.

#### Related Tasks

* [To Lock the Scale of a Layout Viewport](To-Lock-the-Scale-of-a-Layout-Viewport.md)

#### Related Information

* [To Redefine Layout Viewport Boundaries](To-Redefine-Layout-Viewport-Boundaries.md)
* [To Clip a Layout Viewport Boundary](To-Clip-a-Layout-Viewport-Boundary.md)
* [About Scaling Views in Layout Viewports](About-Scaling-Views-in-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*