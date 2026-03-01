# SECTION (Command)

Uses the intersection of a plane and solids, surfaces, or mesh to create a region.

## Summary

The SECTION command creates a region object that represents a 2D cross section of 3D objects, including 3D solids, surfaces,
and meshes.

This method does not have the live sectioning capabilities that are available for section plane objects that are created using
the [SECTIONPLANE](SECTIONPLANE-Command.md) command.

## List of Prompts

The following prompts are displayed.

![](../images/GUID-A63C5B4F-0063-46CC-BAB6-58BBF2CAA583-low.png)

Select objects
:   Selects one or more 3D objects. Selecting several objects creates separate regions for each object.

    Specify the first point on the sectioning plane using one of the following methods:

    * [Object](SECTION-Command.md)
    * [Z Axis](SECTION-Command.md)
    * [View](SECTION-Command.md)
    * [XY](SECTION-Command.md)
    * [YZ](SECTION-Command.md)
    * [ZX](SECTION-Command.md)
    * [3points](SECTION-Command.md)

Object
:   Aligns the sectioning plane with a circle, ellipse, circular or elliptical arc, 2D spline, or 2D polyline segment.

    ![](../images/GUID-D72494AE-F775-4BE6-A5A1-0876CE084110-low.png)

Z Axis
:   Defines the sectioning plane by specifying a point on the sectioning plane and another point on the *Z* axis, or normal, of the plane.

    ![](../images/GUID-39CF7D82-169C-475B-9DFD-ABB6D218911D-low.png)

    * *Point on the section plane.* Sets the first point on the plane.
    * *Point on the Z-axis (normal) of the plane.* Specifies a point that defines the axis that is perpendicular to the plane.

View
:   Aligns the sectioning plane with the viewing plane of the current view.

    ![](../images/GUID-E5BF3321-C5B3-472C-AB47-C18119DBD991-low.png)

XY
:   Aligns the sectioning plane with the *XY* plane of the current UCS.

    ![](../images/GUID-40A237C6-F8B4-40AB-801F-5285FE540D1F-low.png)

YZ
:   Aligns the sectioning plane with the *YZ* plane of the current UCS.

    ![](../images/GUID-FE267C8D-BB12-4513-9407-603501546609-low.png)

ZX
:   Aligns the sectioning plane with the *ZX* plane of the current UCS.

    ![](../images/GUID-1251A6B4-613E-4AD6-8BEB-AFDFA875A351-low.png)

3points
:   Uses three points to define the sectioning plane:

    ![](../images/GUID-880D0B48-7C0E-4557-913A-22FFF2E6BDB5-low.png)

#### Related Information

* [About Section Objects](About-Section-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*