# SECTIONPLANE (Command)

Creates a section object that acts as a cutting plane through 3D objects.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Section Plane drop-down ![](../images/ac.menuaro.gif) Section Plane.
![](../images/GUID-EFEADBD7-601A-4BFF-9459-6F20FC6A74E7-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Section Plane.

## Summary

Section plane objects create sections of 3D solids, surfaces, and meshes. Use live sectioning with section plane objects to
analyze a model, and save sections as blocks for use in layouts.

![](../images/GUID-18B3675B-C94A-4062-BDC1-A296CD9FD87B-low.gif)

## List of Options

The following options are displayed.

Face or Any Point to Locate Section Line
:   Specifies a face to establish the plane of the section object.

    Alternatively, you can select any point on the screen that is not on a face to create a section object independent of the
    solid or surface. The first point establishes a point around which the section object rotates.

    * *Through point.*Sets a second point that defines the plane of the section object.

Draw section
:   Defines the section object with multiple points to create a section line with jogs.

    This option creates a section object in the Section Boundary state with live sectioning turned off.

Orthographic
:   Aligns the section object to an orthographic orientation relative to the UCS.

    ![](../images/GUID-C3FA0A04-9E65-4709-930C-790579ABAAFC-low.png)

    A section object that contains all 3D objects is created with the specified orientation relative to the UCS (not the current
    view). This option creates a section object in the Section Plane state with live sectioning turned on.

    * *Align section to.*Sets the position of the section object to align with one of the following UCS orientations that you specify:
      + Front
      + Back
      + Top
      + Bottom
      + Left
      + Right

Type
:   Specifies a plane, slice, boundary or volume as the parameter when creating the section plane. Once you choose a style, the
    command reverts back to the first prompt, with the selected type set as default.

    * *Plane.* Allows you to specify a planar segment of a 3D solid, surface, mesh, or point cloud and place the section plane.

      ![](../images/GUID-EDBAA659-77F6-49AC-901F-6B838C37E421-low.png)
    * *Slice.* Allows you to select a planar segment with depth of a 3D solid, surface, mesh or point cloud to place the section plane.

      ![](../images/GUID-86560ABF-3109-474F-BC33-0E9960E3A32D-low.png)

      NOTE:The slice cannot contain any jogs and the draw selection option is disabled.
    * *Boundary.* Allows you to select the boundary of a 3D solid, surface, mesh, or point cloud and place the section plane.

      ![](../images/GUID-9C7FCEF9-EEB0-46A5-9468-E1A678B57537-low.png)
    * *Volume.* Allows you to create a bounded volume section plane.

      ![](../images/GUID-613253C4-B499-436D-86A0-F555A77BBD60-low.png)

#### Related Concepts

* [About Jogged Segments in Section Objects](About-Jogged-Segments-in-Section-Objects.md)
* [About Live Sectioning](About-Live-Sectioning.md)

#### Related Information

* [About Section Objects](About-Section-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*