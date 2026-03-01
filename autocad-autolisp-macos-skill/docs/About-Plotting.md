# About Plotting

Understanding terms and concepts that relate to plotting makes your first plotting experience in the program easier.

## What is the Difference Between Printing and Plotting?

The terms
*printing* and
*plotting* can be used interchangeably for CAD output. Historically, printers would generate text only, and plotters would generate
vector graphics. As printers became more powerful and could generate high-quality raster images of vector data, the distinction
largely disappeared.

In addition to paper output, electronic delivery of multiple drawing sheets uses the encompassing term,
*publishing*. The process of generating physical models in plastic and metal is called
*3D printing*.

## Layouts

A layout represents a drawing sheet, and typically includes

* A drawing border and title block
* One or more layout viewports that display views of model space
* General notes, labels, and possibly dimensions
* Tables and schedules

Usually a drawing file contains only one layout, but you can create as many layouts as you need. The first time you display
a layout, it is initialized and a default
*page setup* is assigned to it.

Once initialized, layouts can be modified, published, and added to sheet sets as sheets.

## Page Setups

When you create a layout, you specify a plotter, and settings such as paper size and orientation. These settings are saved
in the drawing as a page setup. Each layout can be associated with a different page setup.

You can control these settings for layouts and for model space using the Page Setup Manager. You can name and save page setups
for use with other layouts.

If you do not specify all the settings in the Page Setup dialog box when you create a layout, you can set up the page just
before you plot. Or you can override a page setup at plot time. You can use the new page setup temporarily for the current
plot, or you can save the new page setup.

## Plot Styles

A
*plot style* is an optional method that controls how each object or layer is plotted. Assigning a plot style to an object or a layer
*overrides* properties such as color, lineweight, and linetype when plotting. Only the appearance of plotted objects is affected by plot
style.

*Plot style tables* collect groups of plot styles, and save them in a file that you can later apply when plotting.

The
*Plot Style Manager* is a folder that contains all the available plot style tables.

There are two plot style types: color-dependent and named. A drawing can use only one type of plot style table. You can convert
a plot style table from one type to the other.

For
*color-dependent plot style tables,*an object's color determines how it is plotted. These plot style table files have
*.ctb*extensions. You cannot assign color-dependent plot styles directly to objects. Instead, to control how an object is plotted,
you change its color. For example, all objects assigned the color red in a drawing are plotted the same way.

*Named plot style tables*use plot styles that are assigned directly to objects and layers. These plot style table files have
*.stb* extensions. Using them enables each object in a drawing to be plotted differently, independent of its color.

## Plot Stamps

A plot stamp is a line of text that is added to your plot. You can specify where this text is located on the plot in the
Plot Stamp dialog box. Turn this option on to add specified plot stamp information—including drawing name, layout name, date
and time, and so on—to a drawing that is plotted to any device. You can choose to record the plot stamp information to a log
file instead of plotting it, or in addition to plotting it.

#### Related Tasks

* [To Plot a Drawing](To-Plot-a-Drawing.md)

#### Related Concepts

* [About Plot Styles](About-Plot-Styles.md)

#### Related Information

* [To Change a Layer's Plot Style](To-Change-a-Layer's-Plot-Style.md)
* [To Change an Object's Plot Style](To-Change-an-Object's-Plot-Style.md)
* [To Change a Plot Style's Description](To-Change-a-Plot-Style's-Description.md)
* [To Edit Plot Style Settings](To-Edit-Plot-Style-Settings.md)
* [To Set the Current Plot Style](To-Set-the-Current-Plot-Style.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*