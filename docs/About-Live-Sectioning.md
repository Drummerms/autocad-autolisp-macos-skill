# About Live Sectioning

Use live sectioning to move a section object through the 3D model or region dynamically.

## What Is Live Sectioning?

Live sectioning is an analytical tool for viewing cut geometry in a 3D solid, surface, or region.

![](../images/GUID-6C490F7B-44CA-4FE5-BDE4-155A664B6135-low.png)

You can use live sectioning to analyze a model by moving the section object through the object. For example, sliding the
section object through an engine assembly helps you visualize its internal components. You can use this method to create a
cross section view that you can save or reuse.

## Turn on and Use Live Sectioning

Live sectioning works with 3D objects and regions in model space. When live sectioning is activated, you can change the viewing
planes by using grips to adjust the location of the section object or its segments.

By turning on cutaway geometry, you can display the entire object that contains the section plane. This option (available
on the shortcut menu) can only be turned on when section plane is active.

![](../images/GUID-3129B932-364C-422E-90F0-B5905D70FAAF-low.png)

Live sectioning is turned on or off automatically, depending on how you create the section object. For example, when you select
a face to define the section plane, live sectioning is turned on. When you create sections using the Draw Section option of
the SECTIONPLANE command, live sectioning is turned off. Live sectioning can be manually turned on or off after a section
object is created.

A drawing can contain multiple section objects. However, live sectioning can only be active for one section object at a time.
Suppose that your model has two sections objects: *Section A* and *Section B*. If *Section A* has live sectioning turned on and you activate live sectioning for *Section B*, live sectioning for *Section A* is automatically turned off.

Turning off a section object layer does not turn off live sectioning. However, freezing the layer turns off live sectioning.

#### Related Tasks

* [To Change the State of a Section Object](To-Change-the-State-of-a-Section-Object.md)
* [To Create a Region That Represents the Cross Section of a 3D Solid Object](To-Create-a-Region-That-Represents-the-Cross-Section-of-a-3D-Solid-Object.md)
* [To Display Cutaway Geometry](To-Display-Cutaway-Geometry.md)

#### Related Concepts

* [About Grips on Section Objects](About-Grips-on-Section-Objects.md)
* [About Jogged Segments in Section Objects](About-Jogged-Segments-in-Section-Objects.md)
* [About Saving Section Objects as Blocks or Drawings](About-Saving-Section-Objects-as-Blocks-or-Drawings.md)
* [About Section Objects Associated with Named Views](About-Section-Objects-Associated-with-Named-Views.md)

#### Related Information

* [To Add Jogs to a Section](To-Add-Jogs-to-a-Section.md)
* [About Section Objects](About-Section-Objects.md)
* [To Associate a Section Object with a Named View](To-Associate-a-Section-Object-with-a-Named-View.md)
* [To Change the Height of the Section Plane Indicator](To-Change-the-Height-of-the-Section-Plane-Indicator.md)
* [To Change the Transparency and Color of the Section Plane Indicator](To-Change-the-Transparency-and-Color-of-the-Section-Plane-Indicator.md)
* [To Create a Section Object by Selecting a Face](To-Create-a-Section-Object-by-Selecting-a-Face.md)
* [To Create a Section Object by Specifying Two Points](To-Create-a-Section-Object-by-Specifying-Two-Points.md)
* [To Create a Section Object with Jogged Segments](To-Create-a-Section-Object-with-Jogged-Segments.md)
* [To Create a Section Object on a Preset Orthographic Plane](To-Create-a-Section-Object-on-a-Preset-Orthographic-Plane.md)
* [To Modify the Live Section Display Settings](To-Modify-the-Live-Section-Display-Settings.md)
* [To Rename a Section Object](To-Rename-a-Section-Object.md)
* [To Save and Insert a 2D or 3D Section as a Block](To-Save-and-Insert-a-2D-or-3D-Section-as-a-Block.md)
* [To Save Section Block Components on Separate Layers](To-Save-Section-Block-Components-on-Separate-Layers.md)
* [To Turn Live Sectioning On or Off](To-Turn-Live-Sectioning-On-or-Off.md)
* [About Publishing Section Objects](About-Publishing-Section-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*