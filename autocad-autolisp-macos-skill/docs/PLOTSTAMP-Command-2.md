# -PLOTSTAMP (Command)

Places a plot stamp on a specified corner of each drawing and logs it to a file.

If you enter -*plotstamp* at the Command prompt, the following prompts are displayed. The settings in the PSS file are displayed as defaults for each
prompt.

You can use -PLOTSTAMP as part of a plotting script to modify plot stamp information for a drawing.

## LIst of Prompts

The following prompts are displayed.

Enter an option [[On](PLOTSTAMP-Command-2.md)/[OFF](PLOTSTAMP-Command-2.md)/[Fields](PLOTSTAMP-Command-2.md)/[User fields](PLOTSTAMP-Command-2.md)/[Log file](PLOTSTAMP-Command-2.md)/[LOCation](PLOTSTAMP-Command-2.md)/[Text properties](PLOTSTAMP-Command-2.md)/[UNits](PLOTSTAMP-Command-2.md)]:

On
:   Turns on the plot stamp for the current drawing.

OFF
:   Turns off the plot stamp for the current drawing.

Fields
:   Specifies the plot stamp field information you want to apply to the current plot stamp.

    Stamp drawing name? [Yes/No] <Yes>:

    Stamp layout name? [Yes/No] <Yes>:

    Stamp date and time? [Yes/No] <Yes>:

    Stamp login name? [Yes/No] <Yes>:

    Stamp plot device name? [Yes/No] <Yes>:

    Stamp paper size? [Yes/No] <Yes>:

    Stamp plot scale? [Yes/No] <Yes>:

User Fields
:   Specifies the user-defined fields you want to apply to the current plot stamp.

    Enter User field 1 <>: *Enter any user-defined field*

    Enter User field 2 <>: *Enter any user-defined field*

Log File
:   Specifies writing the current plot stamp information to a log file rather than applying this information to the current plotted
    drawing. The default log file is *plot.log*, unless you specify another file path.

    Write plot stamp to log file? [Yes/No] <Yes>:

    Enter log file path <plot.log>:

Location
:   Determines the location of the plot stamp on the page based on offset, orientation, and relationship to either the printable
    area or the border of the paper.

    Location selections include and are relative to the printable area or the border of the paper, depending on what you specify
    at the prompt.

    Enter stamp location [TL/TR/BL/BR] <BL>:

    * *TL:* Top Left
    * *TR:* Top Right
    * *BL:* Bottom Left
    * *BR:* Bottom Right

    Text orientation indicates the rotation angle of the plot stamp in relation to the page.

    Enter text orientation [Horizontal/Vertical] <Horizontal>:

    * *Horizontal:* Plot stamp will be horizontal relative to the page.
    * *Vertical:* Plot stamp will be vertical relative to the page.

    Stamp upside-down [Yes/No] <No>:

    Specify plot stamp offset <0.1000,0.1000>:

    Specifying an offset relative to the paper border calculates the offset values that you specify from the corner of the paper.
    Specifying an offset relative to the printable area calculates the offset values that you specify from the corner of the printable
    area.

    Specify offset relative to [paper Border/printable Area] <printable Area>:

Text Properties
:   Determines the font name and text height for the current plot stamp text. You can also specify to place the text on one line
    or to wrap the text to two lines. The placement and offset values you specify for this plot stamp must accommodate the text
    wrapping and the text height.

    Enter font name <>: *Enter a font name*

    Enter text height <0.1500>: *Enter a value*

    Place plot stamp on single line? [Yes/No] <No >:

Units
:   Specifies the units used to measure *X* offset, *Y* offset, and height. You can define units using inches, millimeters, or pixels.

    Enter measurement units [Inches/Millimeters/Pixels] <Inches>:

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*