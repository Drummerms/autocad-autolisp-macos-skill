# Section Settings Dialog Box

Sets display options for section planes.

SECTIONPLANESETTINGS (Command)

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Section Plane drop-down ![](../images/ac.menuaro.gif) Section Plane Settings.
![](../images/GUID-96950BDA-DB2D-46FC-B877-42437F9D31E9-low.png)

![](../images/GUID-A6E1FD6D-7D34-4EAD-A244-A608C7A9CA87-low.png)

## Summary

Contains display settings for creating 2D and 3D sections from the
[Generate Section / Elevation dialog box](GUID-E96D99C0-079E-424A-92C8-4EBCB3A096A5.htm#WSFACF1429558A55DEF27E5F106B5723EEC-7D4E) and for live sectioning. All settings are stored with the section object.

## List of Options

The following options are displayed.

Section Plane

If a section plane has not been selected, specifies a selection plane to be modified.

Select Section Plane
:   Temporarily closes the Section Settings dialog box so that you can select a section object in the drawing area.

Setting Type

Specifies which setting types are displayed in the properties list.

2D Section / Elevation Block Creation Settings
:   Determines how a 2D section from a 3D object is displayed when generated.

3D Section Block Creation Settings
:   Determines how a 3D object is displayed when generated.

Live Section Settings
:   Determines how sectioned objects are displayed in the drawing when live sectioning is turned on.

Activate Live Section
:   Turns on live sectioning for the selected section object.

Properties

Sets the properties to be applied to the new section block.

Intersection Boundary
:   Sets the appearance of line segments that outline the intersection surface of the section object plane.

    * *Color.* Sets the color of the intersection boundary.
    * *Layer.* Sets the layer. Select an existing layer, or select <Component\_Name>\*LayerByObject\* to split the block component onto a separate
      layer. If you want to add a customized prefix or suffix to the \*LayerByObject\* name, click New Layer Name Settings to open
      the
      [New Layer Name dialog box](GUID-C0E8142B-D32A-48D2-803B-D3DEB416A0A2.htm#WS73099CC142F487557579AB9211CB86298F7-60BD). (2D and 3D section blocks only)
    * *Linetype.* Sets the linetype to be ByLayer, ByBlock, or a type that you specify.
    * *Linetype Scale.* Sets the scale of the linetype.
    * *Plot Style.* Displays the current plot style. (2D and 3D section blocks only)
    * *Lineweight.* Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.
    * *Division Lines.* Sets whether division lines are displayed. (2D section blocks only)
    * *Show.* Sets whether the intersection boundary is displayed. (3D section blocks only)

Intersection Fill
:   Sets the optional fill that is displayed inside the boundary area of the cut surface where the section object intersects the
    3D object.

    * *Show.* Sets whether the intersection fill is displayed.
    * *Face Hatch.*Sets the hatch pattern to be used for the face of the cut surface. To select a pattern from a list, click Select Hatch Pattern
      Type.
    * *Angle.* Sets the hatch angle.
    * *Hatch Scale.* Sets the hatch scale.
    * *Hatch Spacing.* Sets the distance between hatch lines.
    * *Color.* Sets the color of the intersection fill.
    * *Layer.* Sets the layer. Select an existing layer, or select <Component\_Name>\*LayerByObject\* to split the block component onto a separate
      layer. If you want to add a customized prefix or suffix to the \*LayerByObject\* name, click New Layer Name Settings to open
      the
      [New Layer Name dialog box](GUID-C0E8142B-D32A-48D2-803B-D3DEB416A0A2.htm#WS73099CC142F487557579AB9211CB86298F7-60BD). (2D and 3D section blocks only.)
    * *Lineweight.* Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.
    * *Linetype Scale.* Sets the scale of the linetype.
    * *Plot Style.* Displays the current plot style. (2D and 3D section blocks only)
    * *Lineweight.* Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.
    * *Surface Transparency.*Sets the percentage of transparency for the intersection fill. (Live Section only)

Background Lines
:   Controls the display of background lines. (2D and 3D section blocks only)

    * *Show.* Sets whether the component is displayed. (2D section blocks only)
    * *Hidden Line.* Sets whether hidden lines (lines that are behind other lines in the 3D view) are displayed. (2D section blocks only)
    * *Color.* Sets the color of the component.
    * *Layer.* Sets the layer of the component. Select an existing layer, or select <Component\_Name>\*LayerByObject\* to split the block component
      onto a separate layer. If you want to add a customized prefix or suffix to the \*LayerByObject\* name, click New Layer Name
      Settings to open the
      [New Layer Name dialog box](GUID-C0E8142B-D32A-48D2-803B-D3DEB416A0A2.htm#WS73099CC142F487557579AB9211CB86298F7-60BD).
    * *Linetype.* Sets the linetype to be ByLayer, ByBlock, or Continuous.
    * *Linetype Scale.* Sets the scale of the linetype.
    * *Plot Style.* Displays the current plot style.
    * *Lineweight.* Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.

Cut-away Geometry
:   Sets properties for the cut-away objects.

    * *Show.* Sets whether the component is displayed.
    * *Hidden Line.* Sets whether hidden lines (lines that are behind other lines in the 3D view) are displayed. (2D section blocks only)
    * *Color.* Sets the color of the cutaway geometry.
    * *Layer.* Sets the layer of the cutaway geometry. Select an existing layer, or select <Component\_Name>\*LayerByObject\* to split the
      block component onto a separate layer. If you want to add a customized prefix or suffix to the \*LayerByObject\* name, click
      New Layer Name Settings to open the
      [New Layer Name dialog box](GUID-C0E8142B-D32A-48D2-803B-D3DEB416A0A2.htm#WS73099CC142F487557579AB9211CB86298F7-60BD). (2D and 3D section blocks only)
    * *Linetype.*Sets the linetype to be ByLayer, ByBlock, or Continuous.
    * *Linetype Scale.*Sets the scale of the linetype.
    * *Plot Style.* Displays the current plot style. (2D and 3D section blocks only)
    * *Lineweight.*Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.
    * *Face Transparency.*Sets the percentage of transparency of the face created where the live section object interfaces with the 3D objects. (Live
      Section only)
    * *Edge Transparency.* Sets the percentage of transparency of the edges of the foreground lines. (Live Section only)

Curve Tangency Lines
:   Controls the inclusion of curved lines that are tangent to the section plane. (2D section blocks only)

    * *Show.* Sets whether the curve tangency lines are displayed.
    * *Color.* Sets the color of the curve tangency lines.
    * *Layer.* Sets the layer of the curve tangency lines. Select an existing layer, or select <Component\_Name>\*LayerByObject\* to split
      the block component onto a separate layer. If you want to add a customized prefix or suffix to the \*LayerByObject\* name, click
      New Layer Name Settings to open the
      [New Layer Name dialog box](GUID-C0E8142B-D32A-48D2-803B-D3DEB416A0A2.htm#WS73099CC142F487557579AB9211CB86298F7-60BD).
    * *Linetype.* Sets the linetype to be ByLayer, ByBlock, or Continuous.
    * *Linetype Scale.*Sets the scale of the linetype.
    * *Plot Style.* Displays the current plot style.
    * *Lineweight.*Sets whether the lineweight is ByLayer, ByBlock, matches the default, or has a unique value.

Apply Settings to All Section Objects

When selected, applies all the settings to all section objects in the drawing. When cleared, applies settings to the current
section object only.

Reset

Resets all settings in the dialog box to their default values.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*