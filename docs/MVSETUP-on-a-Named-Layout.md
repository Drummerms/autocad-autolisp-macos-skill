# MVSETUP on a Named Layout

On a named layout, you can insert one of several predefined title blocks into the drawing and create a set of layout viewports
within the title block.

You can specify a global scale as the ratio between the scale of the title block in the layout and the drawing on the Model
layout.

To easily specify all layout page settings and prepare your drawing for plotting, you can also use the Page Setup Manager.

## List of Prompts

When the TILEMODE system variable is off, or when you enter
*y* or press Enter at the Enable Paper Space prompt, the following prompts are displayed:

Enter an option [Align/Create/Scale viewports/Options/Title block/Undo]:
*Enter an option or press*Enter *to end the command*

Align

Pans the view in a viewport so that it aligns with a base point in another viewport. The current viewport is the viewport
that the other point moves to.

Angled
:   Pans the view in a viewport in a specified direction.

    The next two prompts specify the distance and angle from the base point to the second point.

Horizontal
:   Pans the view in one viewport until it aligns horizontally with a base point in another viewport. This option should be used
    only if the two viewports are oriented horizontally. Otherwise, the view might be panned outside the limits of the viewport.

Vertical Alignment
:   Pans the view in one viewport until it aligns vertically with a base point in another viewport. This option should be used
    only if the two viewports are oriented vertically. Otherwise, the view might be panned outside the limits of the viewport.

Rotate View
:   Rotates the view in a viewport about a base point.

Undo
:   Reverses operations performed in the current MVSETUP session.

Create

Creates viewports.

Delete Objects

Deletes existing viewports.

Create Viewports

Displays options for creating viewports.

Layout Number to Load
:   Controls creation of viewports.

    Entering
    *0* or pressing Enter creates no viewports.

    Entering
    *1*creates a single viewport whose size is determined by the following prompts.

    Entering
    *2* creates four viewports by dividing a specified area into quadrants. You are prompted for the area to be divided and the distance
    between the viewports.

    The viewing angle for each quadrant is set as shown in the table.

    | Quadrant | View |
    | Upper-left | Top (*XY* plane of UCS) |
    | Upper-right | SE isometric view |
    | Lower-left | Front (*XZ* plane of UCS) |
    | Lower-right | Right side (*YZ* plane of UCS) |

    Entering
    *3* defines a matrix of viewports along the
    *X* and
    *Y* axes. Specifying points at the next two prompts defines the rectangular area of the drawing that contains the viewport configuration.
    If you have inserted a title block, the Specify First Corner prompt also includes an option for selecting a default area.

    If you enter more than one viewport in each direction, the following prompts are displayed:

    Specify distance between viewports in X direction <0.0>: *Specify a distance*

    Specify distance between viewports in Y direction <0.0>: *Specify a distance*

    The array of viewports is inserted into the defined area.

Redisplay
:   Redisplays the list of viewport layout options.

Undo

Reverses operations performed in the current MVSETUP session.

Scale Viewports

Adjusts the zoom scale factor of the objects displayed in the viewports. The zoom scale factor is a ratio between the scale
of the border in paper space and the scale of the drawing objects displayed in the viewports.

Interactively
:   Selects one viewport at a time and displays the following prompts for each:

    For example, for an engineering drawing at a scale of 1:4, or quarter scale, enter
    *1* for paper space units and
    *4* for model space units.

Uniform
:   Sets the same scale factor for all viewports.

Options

Sets the MVSETUP preferences before you change your drawing.

Layer
:   Specifies a layer on which to insert the title block.

Limits
:   Specifies whether to reset the grid limits to the drawing extents after a title block has been inserted.

Units
:   Specifies whether the sizes and point locations are translated to inch or millimeter paper units.

Xref
:   Specifies whether the title block is inserted or externally referenced.

Title Block

Prepares paper space, orients the drawing by setting the origin, and creates a drawing border and a title block.

Delete Objects

Deletes objects from paper space.

Origin

Relocates the origin point for this sheet.

Undo

Reverses operations performed in the current MVSETUP session.

Insert

Displays title block options.

Title Block to Load
:   Inserts a border and a title block. Entering
    *0* or pressing Enter inserts no border. Entering
    *1* through
    *13* creates a standard border of the appropriate size. The list includes ANSI and DIN/ISO standard sheets.

Add
:   Adds title block options to the list. Selecting this option prompts you to enter the title block description to be displayed
    in the list and the name of a drawing to insert.

    A line similar to the following example is added after the last entry in the
    *mvsetup.dfs* default file:

    A/E (24 x 18in),arch-b.dwg,(1.12 0.99 0.00),(18.63 17.02 0.00),in

    The last field of the line specifies whether the title block has been created in inches or in millimeters. The units field
    allows title blocks created in either unit system to be changed by setting the unit type using the Options option.

    You can also add title blocks that have variable attributes.

Delete
:   Removes entries from the list.

Redisplay
:   Redisplays the list of title block options.

Undo

Reverses operations performed in the current MVSETUP session.

#### Related References

* [TILEMODE (System Variable)](TILEMODE-System-Variable.md)

#### Related Concepts

* [About Drawings and Templates](About-Drawings-and-Templates.md)
* [About Units of Measurement](About-Units-of-Measurement.md)
* [About Aligning Views on a Layout](About-Aligning-Views-on-a-Layout.md)
* [About Layout Viewports](About-Layout-Viewports.md)

#### Related Information

* [MVSETUP on the Model Layout](MVSETUP-on-the-Model-Layout.md)
* [About Scaling Views in Layout Viewports](About-Scaling-Views-in-Layout-Viewports.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*