# TIME (Command)

Displays the date and time statistics of a drawing.

## Access Methods

*Menu*:
Tools
![](../images/ac.menuaro.gif) Inquiry
![](../images/ac.menuaro.gif) Time.

![](../images/ac.keyboard.gif) Command entry:  *'time* for transparent use

## Summary

The Total Editing Time cannot be reset or stopped. Plotting time is not included in the total editing time, nor is the viewing
time if the drawing is not saved.

The Elapsed Timer controls are separate and can be started, stopped, and reset.

## List of Prompts

The following prompts are displayed.

[Current time](TIME-Command.md): Wednesday, December 31, 2003 9:54:51:406 AM

Times for this drawing:

[Created](TIME-Command.md): Friday, December 12, 2003 1:21:36:203 AM

[Last Updated](TIME-Command.md): Wednesday, December 31, 2003 9:49:19:208 AM

[Total Editing Time](TIME-Command.md): 0 days 06:44:10.520

[Elapsed Timer](TIME-Command.md) (on): 0 days 00:07:05.312

[Next Automatic Save In](TIME-Command.md): 0 days 01:59:15.570

Enter option [[Display](TIME-Command.md)/[On](TIME-Command.md)/[OFF](TIME-Command.md)/[Reset](TIME-Command.md)]:
*Enter an option or press*Enter

Current Time
:   Displays the current date and time to the nearest millisecond using a 24-hour clock.

Created
:   Displays the date and time that the current drawing was created.

Last Updated
:   Displays the date and time of the latest update of the current drawing. This date and time is initially the drawing creation
    time. The time is revised whenever the drawing file is saved.

Total Editing Time
:   Displays the time spent editing the current drawing. This timer is updated by the program and cannot be reset or stopped.
    Plotting time is not included in the total editing time. If you quit the editing session without saving the drawing, the time
    you spent in the editing session is not added to the accumulated editing time.

Elapsed Timer
:   Runs as another timer while the program is running. You can turn it on and off or reset it whenever you like.

Next Automatic Save In
:   Indicates the time remaining until the next automatic save. You can set the time interval using
    [OPTIONS](OPTIONS-Command.md) or the
    [SAVETIME](SAVETIME-System-Variable.md) system variable.

Display
:   Repeats the display with updated times.

On
:   Starts the user elapsed timer if it was off.

Off
:   Stops the user elapsed timer.

Reset
:   Resets the user elapsed timer to 0 days 00:00:00.000.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*