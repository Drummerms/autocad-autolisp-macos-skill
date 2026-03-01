# -PAGESETUP (Command)

Modifies the current page layout settings for the plotting device, paper size, plot scale, and several other settings in the
command line.

The following prompts are displayed.

## Enter an output device name or [?] <*current*>:

Displays the name of the output device specified in the currently selected page setup. Enter
*?* to display a list of output devices.

## Enter paper size or [?]:

Sets the current paper size. Enter
*?* to display a list of the standard paper sizes that are available for the specified output device. If no plotter is selected,
the full standard paper size list is displayed.

## Enter paper units [Inches/Millimeters]<*current*>:

Sets the current unit convention to be used in the layout, inches or millimeters.

## Enter drawing orientation [Portrait/Landscape]:<*current*>

Orients and plots the drawing so that either the short edge or the long edge of the paper represents the top of the page

## Plot upside down? [Yes/No] <*current*>:

Orients and plots the drawing upside down.

## Enter plot area [Display/Extents/Limits/View/Window] <*current*>:

Specifies how the boundaries of the area to be plotted are determined.

Display
:   Specifies the view in the current viewport in the Model tab or the current paper space view in the layout.

Extents
:   Specifies the portion of the current space of the drawing that contains objects. All geometry in the current space is plotted.

Limits
:   When plotting from the Model tab, specifies the entire drawing area that's defined by the grid limits. If the current viewport
    does not display a plan view, this option has the same effect as the Extents option.

Layout
:   When plotting a layout, specifies everything within the printable area of the specified paper size, with the origin calculated
    from 0,0 in the layout.

View
:   Specifies a view that was previously saved with the VIEW command.

Window
:   Prompts for the upper-left and lower-right corners of the rectangular area to be plotted.

## Enter plot scale (Plotted <*Units*>=Drawing Units) or [Fit] <*current*>:

Determines the scale at which a drawing will be plotted, either from model space or a layout.

Plotted <*units*>
:   Specifies the relative size of plotted units to drawing units.

Fit
:   Specifies the scale of the plot to fit within the specified paper size at a custom scale.

## Enter plot offset (x,y) or [Center] <0.00,0.00>:

Specifies a shift to be applied to the 0,0 origin point at the lower-left corner of the area to be plotted.

Plot Offset
:   Specifies the X and Y distances to shift the area to be plotted. The coordinate values can be positive, negative, or zero.

Center
:   Automatically calculates the X and Y offset values to center the plot on the paper. This option is not available when Plot
    Area is set to Layout.

## Plot with plot styles? [Yes/No] <*current*>:

Specifies whether a plot style table should be referenced.

## Enter plot style table name or [?] (enter . for none) <*current*>:

Specifies a plot style table to be assigned that is assigned to the current Model tab or layout tab. Enter
*?* to display a list of the currently available plot style tables. Enter a period (.) to specify no plot style table.

## Plot with lineweights? [Yes/No] <*current*>:

Specifies that non-zero lineweights should be plotted regardless of the way objects are displayed on the screen.

## Enter shade plot setting [As displayed/legacy Wireframe/legacy Hidden/Visual styles/Rendered] <*current*>:

Specifies whether objects are plotted differently than the way they are displayed on the screen.

As displayed
:   Specifies using the same style for objects the way they are displayed on the screen.

legacy Wireframe
:   Specifies a wireframe style regardless of the way objects are displayed on the screen. Uses the legacy SHADEMODE command.

legacy Hidden
:   Specifies a hidden-lines-removed style regardless of the way objects are displayed on the screen. Uses the legacy SHADEMODE
    command.

Visual styles
:   Specifies that a visual style

Rendered
:   Specifies a rendered style regardless of the way they are displayed on the screen.

#### Related Tasks

* [To Work with Named Page Setups for Plotting](To-Work-with-Named-Page-Setups-for-Plotting.md)
* [To Work With Named Page Setups with Sheet Sets](To-Work-With-Named-Page-Setups-with-Sheet-Sets.md)

#### Related Concepts

* [About Named Page Setups](About-Named-Page-Setups.md)
* [About Screened Plotting](About-Screened-Plotting.md)
* [To Adjust the Plot Offset of a Layout](To-Adjust-the-Plot-Offset-of-a-Layout.md)

#### Related Information

* [About Assigning Plot Style Tables to Layouts](About-Assigning-Plot-Style-Tables-to-Layouts.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*