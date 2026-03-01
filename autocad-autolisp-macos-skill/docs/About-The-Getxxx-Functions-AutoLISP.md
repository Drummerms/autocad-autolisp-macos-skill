# About The Getxxx Functions (AutoLISP)

Each user-input get*xxx* function pauses for data entry of the indicated type and returns the value entered. The application specifies an optional
prompt to display before the function pauses. The following table lists the get*xxx* functions and the type of user input requested.

| Allowable input to the get*xxx* user-input functions | |
| Function name | Type of user input |
| *getint* | An integer value on the command line |
| *getreal* | A real or integer value on the command line |
| *getstring* | A string on the command line |
| *getpoint* | A point value on the command line or selected from the screen |
| *getcorner* | A point value (the opposite corner of a box) on the command line or selected from the screen |
| *getdist* | A real or integer value (of distance) on the command line or determined by selecting points on the screen |
| *getangle* | An angle value (in the current angle format) on the command line or based on selected points on the screen |
| *getorient* | An angle value (in the current angle format) on the command line or based on selected points on the screen |
| *getkword* | A predefined keyword or its abbreviation on the command line |

NOTE:Although the getvar, getcfg, and getenv functions begin with the letters *g*, *e*, and *t*, they are not user-input functions. They are discussed in About Accessing Commands and Services (AutoLISP).

The functions getint, getreal, and getstring pause for user input on the AutoCAD command line. They return a value only of the same type as that requested.

The getpoint, getcorner, and getdist functions pause for user input on the command line or from points selected on the graphics screen. The getpoint and getcorner functions return 3D point values, and getdist returns a real value.

Both getangle and getorient pause for input of an angle value on the command line or as defined by points selected on the graphics screen. For the getorient function, the 0 angle is always to the right: “East” or “3 o'clock.” For getangle, the 0 angle is the value of ANGBASE, which can be set to any angle. Both getangle and getorient return an angle value (a real) in radians measured counterclockwise from a base (0 angle), for getangle equal to ANGBASE, and for getorient to the right.

For example, ANGBASE is set to 90 degrees (north), and ANGDIR is set to 1 (clockwise direction for increasing angles). The
following table shows what getangle and getorient return (in radians) for representative input values (in degrees).

| Possible return values from getangle and getorient | | |
| Input  (degrees) | getangle | getorient |
| 0 | 0.0 | 1.5708 |
| -90 | 1.5708 | 3.14159 |
| 180 | 3.14159 | 4.71239 |
| 90 | 4.71239 | 0.0 |

![](../images/GUID-DEB3DE8A-968B-4731-9DD4-E6150C31A211-low.png)

The getangle function honors the settings of ANGDIR and ANGBASE when accepting input. You can use getangle to obtain a rotation amount for a block insertion, because input of 0 degrees always returns 0 radians. The getorient function honors only ANGDIR. You use getorient to obtain angles such as the baseline angle for a text object. For example, given the preceding settings of ANGBASE and ANGDIR,
for a line of text created at an angle of 0, getorient returns an angle value of 90.

The user-input functions take advantage of the error-checking capability of AutoCAD. Trivial errors are trapped by AutoCAD
and are not returned by the user-input function. A prior call to initget provides additional filtering capabilities, lessening the need for error-checking.

The getkword function pauses for the input of a keyword or its abbreviation. Keywords must be defined with the initget function before the call to getkword. All user-input functions (except getstring) can accept keyword values in addition to the values they normally return, provided that initget has been called to define the keywords.

All user-input functions allow for an optional  *prompt*  argument. It is recommended you use this argument rather than a prior call to the prompt or princ functions. If a  *prompt*  argument is supplied with the call to the user-input function, that prompt is reissued in the case of invalid user input.
If no  *prompt*  argument is supplied and the user enters incorrect information, the following message appears at the AutoCAD prompt line:

Try again:

This can be confusing, because the original prompt may have scrolled out of the Command prompt area.

The AutoCAD user cannot typically respond to a user-input function by entering an AutoLISP expression. If your AutoLISP routine
makes use of the initget function, arbitrary keyboard input is permitted to certain functions that can allow an AutoLISP statement as response to
a command implemented in AutoLISP.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*