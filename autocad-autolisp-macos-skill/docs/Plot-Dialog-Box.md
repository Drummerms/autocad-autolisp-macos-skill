# Plot Dialog Box

Specifies device and media settings, and plots your drawing.

PLOT (Command)

*Toolbar*:
![](../images/GUID-E98FB764-041C-4F90-8F08-3FD0683C3611-low.png)

![](../images/GUID-8F40613C-B96D-4B7F-A2AB-6548E583647C-low.png)

Printing allows you to output a single layout at a time. If you want to print more than one layout at a time, use the PUBLISH
command.

## Page Setup

Displays a list of any named and saved page setups in the drawing.

* ![](../images/GUID-11BEF85C-BADE-421A-B018-A4AFE16E0A59-low.png). Imports a page setup from another drawing.
* ![](../images/GUID-1AD93785-6805-43C2-AD24-AC5B5C169D85-low.png). Creates a new named page setup based on the current settings in the Plot dialog box.
* *Default to Previous Plot*. When checked, updates the current settings to match what was used on the previous plot. Then each time you plot, the initial
  settings match what was used on the previous plot.

## Printer

Specifies a configured plotting device to use when plotting layouts. Lists the available PC3 files or system printers from
which you can select to plot the current layout.

If the selected plotter doesn't support the layout's selected paper size, a warning is displayed and you can select the plotter's
default paper size or a custom paper size.

PDF Options or Printer Configuration![](../images/GUID-8A01F33F-D790-424E-9774-A7BEC8D003AA-low.png)
:   * If PDF output is selected, displays the PDF Options dialog box, which gives you the ability to optimize a PDF file for the
      specific purpose you are creating it.
    * If a printer is selected, displays the Print dialog box where you can choose the printer settings. Printer settings are saved
      in a .pc3 file which can be selected the next time you plot.

## Copies

Specifies the number of copies to plot.

## Paper Size

Displays standard paper sizes that are available for the selected plotting device. If no plotter is selected, the full standard
paper size list is displayed and available for selection.

If the selected plotter doesn't support the layout's selected paper size, a warning is displayed, and you can select the plotter's
default paper size or a custom paper size.

A default paper size is set for the plotting device when you create a PC3 file with the Add-a-Plotter wizard. The paper size
that you select in the Page Setup dialog box is saved with the layout and overrides the PC3 file settings.

Orientation
:   * ![](../images/GUID-DC46C1BF-076B-46F9-8CF5-651251A39444-low.png) *Portrait*. Orients and plots the drawing so that the short edge of the paper represents the top of the page.
    * ![](../images/GUID-B4A859C3-3411-4671-81CD-8CCB7FE08A60-low.png) *Landscape*. Orients and plots the drawing so that the long edge of the paper represents the top of the page.

## What to Print

Specifies the portion of the drawing to be plotted.

* *Layout/Limits*. When plotting a layout, plots everything within the printable area of the specified paper size, with the origin calculated
  from 0,0 in the layout. When plotting from the Model tab, plots the entire drawing area that is defined by the grid limits.
  If the current viewport does not display a plan view, this option has the same effect as the Extents option.
* *Display*. Plots the view in the current viewport in the selected Model tab or the current paper space view in the layout.
* *Extents*. Plots the portion of the current space of the drawing that contains objects. All geometry in the current space is plotted.
  The drawing may be regenerated to recalculate the extents before plotting.
* *View*. Plots a view that was previously saved with the VIEW command. You can select a named view from the list. If there are no
  saved views in the drawing, this option is unavailable. When the View option is selected, a View list is displayed that lists
  the named views that are saved in the current drawing. You can select a view from this list to plot.
* *Window*. Plots any portion of the drawing that you specify. When you select Window, use the pointing device to specify the two corners
  of the area to be plotted, or enter coordinate values.

## Fit to Paper

Scales the plot to fit within the selected paper size and displays the custom scale factor in the Scale, Inch =, and Units
boxes.

## Scale

Defines the exact scale for the plot.
*Custom* defines a user-defined scale. You can create a custom scale by entering the number of inches (or millimeters) equal to the
number of drawing units. The default scale setting is 1:1 when plotting a layout. The default setting is Fit to Paper when
plotting from the Model tab.

NOTE:You can modify the list of scales with SCALELISTEDIT.

## Plot Style

Displays the plot style table that is assigned to the current Model tab or layout tab and provides a list of the currently
available plot style tables.

If you select New, the Plot Style Table Editor is displayed, which you can use to create a new plot style table.

Edit ![](../images/GUID-A1A24E28-8DE1-4880-80DF-C6ACB799DCAF-low.png)
:   Displays the Plot Style Table Editor, in which you can view or modify plot styles for the currently assigned plot style table.

Print with Plot Styles
:   Specifies whether plot styles applied to objects and layers are plotted.

## Preview (Area)

A preview area is available making it easy to see how your drawing will appear when plotted.

![](../images/GUID-D7D6612A-7BB2-422F-8A8C-0EB4D9C52B7B-low.png)

## Plot Offset

Specifies an offset of the plot area relative to the lower-left corner of the printable area.

The printable area of a drawing sheet is defined by the selected output device and is represented by a dashed line in a layout.
When you change to another output device, the printable area may change.

You can offset the geometry on the paper by entering a positive or negative value in the X and Y offset boxes. The plotter
unit values are in inches or millimeters on the paper.

X
:   Specifies the plot origin in the
    *X* direction relative to the setting of the Plot Offset Definition option.

Y
:   Specifies the plot origin in the
    *Y* direction relative to the setting of the Plot Offset Definition option.

Center the Plot ![](../images/GUID-716FA881-776B-4EEF-A325-8DE2041A4BEE-low.png)
:   Automatically calculates the
    *X* and
    *Y* offset values to center the plot on the paper. This option is not available when What to Print is set to Layout.

## Expand\Collapse ![](../images/GUID-2BB348E0-50D5-4309-90D2-F6D9D4C15349-low.png) ![](../images/GUID-42D9498E-9624-46A5-BF3D-48CA6CA5BCF1-low.png)

Controls display of additional options in the plot dialog box.

## Print Options

Print Object Lineweights
:   Specifies whether lineweights assigned to objects and layers are plotted.

Scale Lineweights
:   Scales lineweights in proportion to the plot scale. Lineweights normally specify the linewidth of plotted objects and are
    plotted with the linewidth size regardless of the plot scale.

Print Transparency
:   Specifies whether object transparency is plotted. This option should only be used when plotting drawings with transparent
    objects.

    IMPORTANT:For performance reasons, plotting transparency is disabled by default. This setting can be overridden by the PLOTTRANSPARENCYOVERRIDE
    system variable. By default, the system variable honors the setting in the Page Setup and the Plot dialog boxes.

Print Paperspace Last
:   Plots model space geometry first. Paper space geometry is usually plotted before model space geometry.

Hide Paperspace Objects
:   Specifies whether the HIDE operation applies to objects in the paper space viewport. This option is available only from a
    layout tab. The effect of this setting is reflected in the plot preview, but not in the layout.

Print Upside Down
:   Orients and plots the drawing upside down.

Include Plot Stamp
:   Turns on plot stamping. Places a plot stamp on a specified corner of each drawing and/or logs it to a file.

    Plot stamp settings are specified in the Plot Stamp dialog box, in which you can specify the information that you want applied
    to the plot stamp, such as drawing name, date and time, plot scale, and so on. To open the Plot Stamp dialog box, select the
    Plot Stamp On option, and then click the Plot Stamp Settings button that is displayed to the right of the option.

    You can open the Plot Stamp dialog box with the PLOTSTAMP command.

Shading
:   Specifies how views are plotted. To specify this setting for a viewport on a layout tab, select the viewport, right-click
    and then, click Properties.

    From the Model tab, you can select from the following options:

    * *As Displayed.*Plots objects the way they are displayed on the screen. (Available in AutoCAD LT)
    * *Legacy Wireframe.* Objects in wireframe regardless of the way they are displayed on the screen, using the legacy SHADEMODE command. (Available
      in AutoCAD LT)
    * *Legacy Hidden.* Objects with hidden lines removed regardless of the way the objects are displayed on the screen, using the legacy SHADEMODE
      command. (Available in AutoCAD LT)
    * *Conceptual.* Plots objects with the Conceptual visual style applied regardless of the way the objects are displayed on the screen.
    * *Hidden.* Plots objects with hidden lines removed regardless of the way the objects are displayed on the screen.
    * *Realistic.* Plots objects with the Realistic visual style applied regardless of the way the objects are displayed on the screen.
    * *Shaded.* Plots objects with Shaded visual style applied regardless of the way the objects are displayed on the screen
    * *Shaded with Edges.* Plots objects with Shaded with Edges visual style applied regardless of the way the objects are displayed on the screen
    * *Shades of Gray.* Plots objects with Shades of Gray visual style applied regardless of the way the objects are displayed on the screen.
    * *Sketchy.* Plots objects with Sketchy visual style applied regardless of the way the objects are displayed on the screen.
    * *Wireframe.*Plots objects in wireframe regardless of the way they are displayed on the screen.
    * *X-ray.* Plots objects with x-ray visual style applied regardless of the way the objects are displayed on the screen
    * *Rendered.*Plots objects as rendered regardless of the way they are displayed on the screen.

Quality
:   Specifies the resolution at which shaded viewports are plotted.

    You can select from the following resolution options:

    * *Draft*. Sets rendered and shaded model space views to be plotted as wireframe.
    * *Preview*. Sets rendered and shaded model space views to be plotted at one quarter of the current device resolution, to a maximum of
      150 dpi.
    * *Normal*. Sets rendered and shaded model space views to be plotted at one half of the current device resolution, to a maximum of 300
      dpi.
    * *Presentation*. Sets rendered and shaded model space views to be plotted at the current device resolution, to a maximum of 600 dpi.
    * *Maximum*. Sets rendered and shaded model space views to be plotted at the current device resolution with no maximum.
    * *Custom*. Sets rendered and shaded model space views to be plotted at the resolution setting that you specify in the DPI box, up to
      the current device resolution.

DPI
:   Specifies the dots per inch for shaded views, up to the maximum resolution of the current plotting device. This option is
    available if you select Custom in the Quality box.

    NOTE:DPI is disabled if no printer is selected.

#### Related Tasks

* [To Plot a Drawing](To-Plot-a-Drawing.md)
* [To Work with Custom Paper Sizes](To-Work-with-Custom-Paper-Sizes.md)

#### Related Concepts

* [About Plotting](About-Plotting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*