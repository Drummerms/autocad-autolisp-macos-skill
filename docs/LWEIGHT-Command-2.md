# -LWEIGHT (Command)

Sets the current lineweight, lineweight display options, and lineweight units.

## List of Prompts

The following prompts are displayed.

Current lineweight:
*current*

Enter
[default lineweight](LWEIGHT-Command-2.md) for new objects or [[?](LWEIGHT-Command-2.md)]:
*Enter a valid lineweight or enter**?*

The current lineweight value is displayed; if the value is not BYLAYER, BYBLOCK or DEFAULT, the value is displayed in millimeters
or inches.

Default Lineweight
:   Sets the current default lineweight. Lineweight values consist of fixed settings, including BYLAYER, BYBLOCK, and DEFAULT.
    Values are calculated in either inches or millimeters; millimeters are the default. If you enter a valid lineweight value,
    the current default lineweight is set to the new value. If you enter any other value, the default is set to the nearest valid
    value.

    To plot an object with a lineweight that is not found in the list of fixed lineweight values, you can use plot styles to control
    plotted lineweights. The DEFAULT value is set by the LWDEFAULT system variable and has an initial value of 0.01 inches or
    0.25 mm. The lineweight value of 0 plots at the thinnest lineweight available on the specified plotting device and is displayed
    at a value of one pixel in model space.

?—List Lineweights
:   Displays a list of valid lineweight values in the current lineweight units.

NOTE:If you save a drawing using the AutoCAD Release 14, or earlier, format, the drawing preview displays lineweights even though
the drawing saved in the earlier format does not display lineweights.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*