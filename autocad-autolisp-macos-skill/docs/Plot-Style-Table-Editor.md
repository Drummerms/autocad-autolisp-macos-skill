# Plot Style Table Editor

Edits the properties of a plot style table file.

![](../images/GUID-7EB6F638-EF70-4038-824F-91C5D45D824E-low.png)

## Summary

Lists all of the plot styles in the plot style table and their settings.

Plot styles are displayed in columns from left to right. Color-dependent plot styles control printing parameters through color.
Identified by their .ctb file extension, color-dependent plot-style tables map each of the 255 index colors.

## List of Options

The following options are displayed.

Plot Styles

Displays the names of plot styles in named plot style tables. Plot styles in named plot style tables can be changed. Plot
style names in color-dependent plot style tables are tied to object color and cannot be changed. The program accepts up to
255 characters for style names.

Add Style (+)
:   Adds a new plot style to a named plot style table.

    The plot style is based on Normal, which uses an object's properties and doesn't apply any overrides by default. You must
    specify the overrides you want to apply after you create the new plot style. You cannot add a new plot style to a color-dependent
    plot style table; a color-dependent plot style table has 255 plot styles mapped to color. You also cannot add a plot style
    to a named plot style table that has a translation table.

Delete Style (-)
:   Deletes the selected style from a named plot style table.

    Objects assigned this plot style retain the plot style assignment but plot as Normal because the plot style is no longer defined
    in the plot style table. You cannot delete a plot style from a named plot style table that has a translation table, or from
    a color-dependent plot style table.

Color

Specifies the plotted color for an object. The default setting for plot style color is Use Object Color. If you assign a plot
style color, the color overrides the object's color at plot time.

You can choose Select Color to display the
[Color Palette dialog box](Color-Palette-Dialog-Box.md) and select one of the 255 AutoCAD Color Index (ACI) colors, a true color, or a color from a color book. The color you specify
is displayed in the plot style color list as Custom Color. If the plot device does not support the color you specify, it plots
the nearest available color or, in the case of monochrome devices, black.

Dithering

Enables dithering. A plotter uses dithering to approximate colors with dot patterns, giving the impression of plotting more
colors than available in the AutoCAD Color Index (ACI). If the plotter does not support dithering, the dithering setting is
ignored.

Dithering is usually turned off in order to avoid false line typing that results from dithering of thin vectors. Turning off
dithering also makes dim colors more visible. When you turn off dithering, the program maps colors to the nearest color, resulting
in a smaller range of colors when plotting.

Grayscale

Converts the object's colors to grayscale if the plotter supports grayscale. If you clear Convert to Grayscale, the RGB values
are used for object colors. Dithering is available whether you use the object's color or assign a plot style color.

Screening

Specifies a color intensity setting that determines the amount of ink placed on the paper while plotting. Selecting 0 reduces
the color to white. Selecting 100 displays the color at its full intensity. The Dithering option must be selected for screening.

Linetype

Displays a list with a sample and a description of each linetype. If you assign a plot style linetype, the linetype overrides
the object's linetype at plot time.

Adaptive

Adjusts the scale of the linetype to complete the linetype pattern.

If you do not select Adaptive, the line might end in the middle of a pattern. Turn off Adaptive if linetype scale is important.
Turn on Adaptive if complete linetype patterns are more important than correct linetype scaling.

Lineweight

Displays a sample of the lineweight as well as its numeric value. You can specify the numeric value of each lineweight in
millimeters.

If you assign a plot style lineweight, the lineweight overrides the object's lineweight when it is plotted.

Edit Lineweights
:   Modifies the widths values of existing lineweights.

    Displays the Edit Lineweights dialog box.

    There are 28 lineweights available to apply to plot styles in plot style tables. If the lineweight you need does not exist
    in the list of lineweights stored in the plot style table, you can edit an existing lineweight. You cannot add or delete lineweights
    from the list in the plot style table.

Line End Style

If you assign a line end style, the line end style overrides the object's line end style at plot time.

Line Join Style

If you assign a line join style, the line join style overrides the object's line join style at plot time.

Fill Style

If you assign a fill style, the fill style overrides the object's fill style at plot time.

Pen#

Specifies a pen to use when plotting objects that use this plot style. Available pens range from 1 to 32. If plot style color
is set to Use Object Color, or you are editing a plot style in a color-dependent plot style table, the value is set to Automatic.

If you specify 0, the field updates to read Automatic. The program determines the pen of the closest color to the object you
are plotting using the information specified as part of the plotter.

Virtual Pen#

Specifies a virtual pen number between 1 and 255. Many non-pen plotters can simulate pen plotters using virtual pens. For
many devices, you can program the pen's width, fill pattern, end style, join style, and color/screening from the front panel
on the plotter.

Enter 0 or Automatic to specify that the program should make the virtual pen assignment from the AutoCAD Color Index.

The virtual pen setting in a plot style is used only by non-pen plotters and only if they are configured for virtual pens.
If this is the case, all the other style settings are ignored and only the virtual pen is used. If a non-pen plotter is not
configured for virtual pens, then the virtual and physical pen information in the plot style is ignored and all the other
settings are used.

Description

Provides a description for each plot style.

Details

Displays additional information and properties of the plot style being edited.

File name
:   Displays the name of the plot style file.

Description
:   Provides a description for the plot style file.

Number of Styles
:   Lists the number of plot styles contained in the plot style file.

Path
:   Displays the path in which the plot style file is stored.

Version
:   Displays the file format version of the plot style file.

Apply Global Scale Factor to Non-ISO Linetypes
:   Scales all the non-ISO linetypes and fill patterns in the plot styles of objects controlled by this plot style table.

Scale Factor
:   Specifies the amount to scale non-ISO linetypes and fill patterns.

Save As

Displays the Save dialog box and saves the plot style table to a new name.

#### Related References

* [STYLESMANAGER](STYLESMANAGER.md)

#### Related Concepts

* [About Plot Styles](About-Plot-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*