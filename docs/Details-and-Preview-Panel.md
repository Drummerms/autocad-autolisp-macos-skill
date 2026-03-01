# Details and Preview Panel

The Details and Preview panel, located at the bottom of the Reference Manager palette, displays information about the selected
file reference.

![](../images/GUID-7C1E5F91-2C42-4EFE-979F-BEF391C90037-low.png)

## List of Options

The following options are displayed.

Details

Each file reference shares a common set of properties. Some of the properties can be edited.

Reference Name
:   Displays the file reference name. This property is editable for all file reference types.

Status
:   Shows whether the file reference is loaded, unloaded or not found. This property cannot be edited.

Size
:   Shows the file size of the selected file reference. The size is not displayed for file references that are not found. This
    property cannot be edited.

Type
:   Indicates whether the file reference is an attachment or overlay, or the type of raster image file. This property cannot be
    edited.

    However, if the file reference is a DWG, the property can be toggled from the context menu on the upper panel of the Reference
    Manager.

Date
:   Displays the last date the file reference was modified. This date is not displayed if the file reference is not found. This
    property cannot be edited.

Found At
:   Displays the absolute path of the selected file reference. This property cannot be edited.

Saved Path
:   Displays the save location of the selected file reference. This is where the referenced file is saved and is not necessarily
    the same as the Found At location. Clicking the Open button displays the Open dialog box where you can select a different
    path or file name. You can also type directly into the path field. These changes are stored to the Saved Path property if
    the new path is valid.

DWG Specific Properties

If you select a referenced DWG (xref), additional properties are displayed. None of the added image properties can be edited.

Block Unit
:   Specifies the
    [INSUNITS](INSUNITS-System-Variable.md) value for the inserted block.

Unit factor
:   Displays the unit scale factor, which is calculated based on the
    [INSUNITS](INSUNITS-System-Variable.md) value of the block and the drawing units.

Image Specific Properties

If you select a referenced image, additional properties are displayed. None of the added image properties can be edited.

Color System
:   Displays the color system.

Color Depth
:   The amount of information that is stored in each pixel of a raster image. Higher color depth values produce smoother degrees
    of shading.

Pixel Width
:   The width of the raster image measured in pixels.

Pixel Height
:   The height of the raster image measured in pixels.

Resolution
:   The width and height resolution in dots per inch (dpi).

Default Size
:   The width and height of the raster image measured in
    AutoCAD 2026 units.

Thumbnail Preview

The thumbnail preview displays a small image of the selected file reference. If there is no preview available, the text “Preview
not available” is displayed.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*