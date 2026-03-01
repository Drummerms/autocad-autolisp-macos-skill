# About Saving Section Objects as Blocks or Drawings

Save the representation of the cross-sectional area where a section object intersects a 3D model as a block.

## Save Sections as Blocks or Drawings

You can save the section objects you create as blocks. Working from the Generate Section/Elevation dialog box, you can choose
the type of block that is created.

![](../images/GUID-BEA2B53C-0437-4CC9-9ECA-2B2C47F622B9-low.png)

For example, suppose your project requires 2D elevation drawings or 2D cross sections. The 2D Section / Elevation option creates
an accurate block representation that is ready for dimensioning.

To publish or render a cutaway of the 3D model, select the 3D Section option. 3D section geometry consists of mostly 3D solids
and surfaces. However, profile outlines and hatch patterns consist of 2D lines.

The display properties of 2D section/elevation blocks and 3D section blocks are controlled in the Section Settings dialog
box.

When you create section blocks, you have the following choices for how they are handled:

* *Insert the section blocks.* At the time of creation, you can insert a 2D or 3D section block into the drawing or save it to an external file. A 2D section
  block is inserted on the XY plane of the current UCS, including section blocks that extend into 3D space.

  Inserted section blocks are initially unnamed. You can set the scale, rotation, and base point upon insertion. You can modify
  and rename them later by editing the block with BEDIT.
* *Export section blocks to a file.* Save and name the new section objects so they can be inserted later.
* *Save section block components on separate layers.* By default, section block components such as intersection boundary, intersection fill, background lines, cutaway geometry,
  and curve tangency lines are saved on Layer 0. However, you can separate the components of saved section blocks onto separate
  layers with a suffix or prefix that you specify.

  Assigning a suffix or prefix helps you organize the block components into layers that you can sort and identify quickly. The
  Layer properties lists in the Section Settings dialog box provide the opportunity to customize the layer names.
* *Specify whether to limit the section block to certain objects.* The objects that are included in a section block vary, depending on which section object state is selected. You can also
  select specific objects to be included as you create the section block.

#### Related Concepts

* [About Live Sectioning](About-Live-Sectioning.md)

#### Related Information

* [About Publishing Section Objects](About-Publishing-Section-Objects.md)
* [About Section Objects](About-Section-Objects.md)
* [To Save and Insert a 2D or 3D Section as a Block](To-Save-and-Insert-a-2D-or-3D-Section-as-a-Block.md)
* [To Save Section Block Components on Separate Layers](To-Save-Section-Block-Components-on-Separate-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*