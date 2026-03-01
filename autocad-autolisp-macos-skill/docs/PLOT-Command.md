# -PLOT (Command)

Plots a drawing to a plotter, printer, or file in the command line.

If you enter
*-plot* at the Command prompt, the following prompts are displayed.

## List of Prompts

The following prompts are displayed.

Detailed plot configuration [Yes/No] <No>: *Enter* *y* *or* *n* *or press*Enter

No

Indicates that you do not want a detailed plot configuration for this plot.

Enter a layout name or [?] <*current*>:

Enter a page setup name < >:

Enter an output device name or [?] <*current*>:

Write the plot to a file [Yes/No] <*current*>:

Enter file name: <*dwgname-layoutname.*plt>:

Save changes to layout [Yes/No] <No>:

Proceed with Plot [Yes/No] <Y>:

For information about these prompts, see the description for Yes.

Yes

Specifies detailed page settings for the Model layout or layout you are plotting.

Enter a layout name or [?] <*current*>: *Specify the name of the layout tab you want to plot*

Enter an output device name or [?]
*<**current**>*:
*Specify the name of the output device to which you want to plot the Model tab or layout tab you selected*

If you enter a new device name without an extension, the program assumes that the device is a PC3 file (Autodesk ®  HDI plotter configuration file). If no PC3 file is found, the program searches for a Windows system printer with that device
name.

Enter paper size or [?]
*<**current**>*: *Specify the paper size to use for the plot or enter**?* *to view the actual list of paper sizes defined for the plotter driver*

You must specify a paper size exactly as it is defined by the plotter driver.

Enter paper units [Inches/Millimeters]
*<**current**>*:

The Enter Paper Units prompt is not displayed if you are plotting a raster image, such as a BMP or TIFF file, because the
size of the plot is assumed to be in pixels.

Enter drawing orientation [Portrait/Landscape]
*<**current**>*:

Portrait
:   Orients and plots the drawing so that the short edge of the paper represents the top of the page.

Landscape
:   Orients and plots the drawing so that the long edge of the paper represents the top of the page.

Plot upside down [Yes/No] <No>:

Orients and plots the drawing upside down.

Enter plot area [Display/Extents/Limits/Layout/View/Window] <*current*>:

Display
:   Plots the view in the current viewport on the Model layout or the current view in the layout, depending on which tab you select
    to plot.

Extents
:   Plots all of the objects in the current viewport, except objects on frozen layers. From a layout, plots all the geometry in
    paper space. The drawing may be regenerated to recalculate the extents before plotting.

    If you plot the drawing's extents with a perspective view active and the camera position is within the drawing extents, this
    option has the same effect as the Display option.

Limits
:   Plots the drawing area defined by the grid limits. Available only when the Model tab is selected.

Layout
:   Plots everything within the printable area of the specified paper size, with the origin calculated from 0,0 in the layout.
    Available only when a layout tab is selected.

View
:   Plots a view saved previously with the VIEW command. You can select a named view from the list provided. If there are no saved
    views in the drawing, this option is unavailable.

Window
:   Plots any portion of the drawing you specify. This option prompts you to specify the corners of the window.

    Enter lower left corner of window:
    *Specify a point*

    Enter upper right corner of window:
    *Specify a point*

    Enter plot scale (Plotted Inches = Drawing Units) or [Fit] <*current*>:
    *Specify the scale of the plot*

Plotted Inches = Drawing Units
:   Calculates the plot scale based on the inches or millimeters to drawing units that you specify. You can also enter a real
    number as a fraction (for example, you can enter
    *1=2* or
    *.5*).

Fit
:   Calculates the scale to fit the area on the sheet of paper.

The default scale setting is 1:1 when you are plotting a layout, unless you modified and saved the setting. The default setting
is Fit when plotting a Model tab.

Enter plot offset (x, y) or [Center] <*current*>:
*Specify the plot offset in either the X or Y direction, or enter**c* *to center the plot on the paper*

Plot with plot styles [Yes/No] <*current*>:
*Specify whether to plot using the plot styles applied to objects and defined in the plot style table*

If you specify Yes to plot with plot styles, the following prompt is displayed:

Enter plot style table name or [?] (enter . for none) <*current*>:
*Enter a plot style table name,**?* *to view plot style tables, or**.**(period) for none*

All style definitions with different property characteristics are stored in the current plot style table and can be attached
to the geometry. This setting replaces pen mapping in earlier releases of the program.

Plot with lineweights [Yes/No] <*current*>:

Scale lineweights with plot scale [Yes/No] <*current*>:

NOTE:The Scale Lineweights with Plot Scale prompt is displayed only when you plot from a layout tab. Settings for the shaded plotting
type are available only when you plot from the Model layout. To control shaded plotting settings of viewports in a layout,
use the Shadeplot option of the
*-vports* command when you create a viewport.

Enter shade plot setting [As displayed/Wireframe/Hidden/Visual styles/Rendered] <*As displayed*>:
*Enter a shade plot option*

Specifies how model space views are plotted.

As Displayed
:   Specifies that a model space view is plotted the same way it is displayed.

Wireframe
:   Specifies that a model space view is plotted in wireframe regardless of display.

Hidden
:   Specifies that a model space view is plotted with hidden lines removed regardless of display.

Visual Styles
:   Plots a model space view with the specified visual style applied regardless of the current display in the viewport.

    If you specify Visual Styles, the following prompt is displayed:

    Enter an option [Wireframe/Hidden/Realistic/Conceptual/Shaded/shaded with Edges/shades of Gray/SKetchy/X-ray/Other] <Realistic>:

    These options are the same as the options in VSCURRENT.

Rendered
:   Specifies that model space view plots are rendered regardless of display.

Write the plot to a file [Yes/No] <*current*>:
*Enter* *y* *if you want to write the plotted drawing to a file, or press*Enter
*to plot to an output device*

If you specify Yes, the following prompt is displayed:

Enter file name: <*dwgname-layoutname.*plt>:
*Enter a file name*

Save changes to page setup? Or set shade plot quality? [Yes/No/Quality] <No>:

If you enter
*y*, the current settings in the Page Setup dialog box are saved. If you enter
*q*, you are prompted for the shaded plotting quality and are given the option of providing a custom dpi. Then you are prompted
to save the page setup with the added quality settings.

Enter shade plot quality [Draft/Preview/Normal/pResentation/Maximum/Custom] <Normal>:
*Enter* *c* *if you want to specify a dpi, or to use a preset dpi, specify a different quality option*

Enter custom dpi <150>:

Save changes to page setup [Yes/No]? <No>:

Plot paper space first [Yes/No] <*current*>:

Paper space geometry is usually plotted before model space geometry. If you enter
*n*, the model space geometry is plotted first, and paper space geometry is plotted last. This option is available only if you
are plotting from a layout tab.

Hide paperspace objects? [Yes/No] <*No*>:

Specifies whether the Hide operation applies to objects in the paper space viewport. This option is available only from a
layout tab.

Proceed with plot [Yes/No] <Y>:

#### Related References

* [PLOT (Command)](PLOT-Command-2.md)
* [VIEW (Command)](VIEW-Command-2.md)
* [VSCURRENT (Command)](VSCURRENT-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*