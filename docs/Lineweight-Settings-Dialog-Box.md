# Lineweight Settings Dialog Box

Sets the current lineweight, sets the lineweight units, controls the display and display scale of lineweights, and sets the
DEFAULT lineweight value for layers.

LWEIGHT (Command)

*Menu*:
Format
![](../images/ac.menuaro.gif) Lineweight.

![](../images/GUID-CDB8AC44-D37D-43E8-B0E0-EB836FA7EB78-low.png)

## List of Options

The following options are displayed.

Units

Specifies whether lineweights are displayed in millimeters or inches. You can also set Units for Listing by using the LWUNITS
system variable.

Millimeters (mm)
:   Specifies lineweight values in millimeters.

Inches (in.)
:   Specifies lineweight values in inches.

Default

Controls the DEFAULT lineweight for layers. The initial DEFAULT lineweight is 0.01 inches or 0.25 mm. (LWDEFAULT system variable)

Lineweights

Displays the available lineweight values and shows which lineweight is current. The current lineweight is shown highlighted
in the list.

Lineweight values consist of standard settings including BYLAYER, BYBLOCK, and DEFAULT. The DEFAULT value is set by the LWDEFAULT
system variable, which has an initial value of 0.01 inches or 0.25 mm. All new layers use the default setting. The lineweight
value of 0 plots at the thinnest lineweight available on the specified plotting device and is displayed at one pixel wide
in model space.

NOTE:Use the LWDISPLAY system variable or toggle the Show/Hide Lineweights button on the status bar to display lineweights in the
drawing area. Regeneration time increases with lineweights that are represented by more than one pixel. This option does not
affect how objects are plotted.

Preview Scaling

Controls the display scale of lineweights on the Model layout. On the Model layout, lineweights are displayed in pixels. Lineweights
are displayed using a pixel width in proportion to the real-world unit value at which they plot. If you are using a high-resolution
monitor, you can adjust the lineweight display scale to better display different lineweight widths. The Lineweight list reflects
the current display scale.

Objects with lineweights that are displayed with a width of more than one pixel may increase regeneration time. If you want
to optimize performance when working in the Model layout, set the lineweight display scale to the minimum value or turn off
lineweight display altogether.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*