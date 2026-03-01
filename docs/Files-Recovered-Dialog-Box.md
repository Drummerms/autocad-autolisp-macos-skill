# Files Recovered Dialog Box

Displays a list of all drawing files that were open at the time of a program or system failure.

DRAWINGRECOVERY (Command)

*Menu*:
Help ![](../images/ac.menuaro.gif) Recover Files.

## Summary

You can preview and open each drawing or backup file to choose which one should be saved as the primary DWG file.

## List of Options

The following options are displayed.

Backup Files

Displays the drawings that may need to be recovered after a program or system failure. A top-level drawing node contains a
set of files associated with each drawing. If available, up to four files are displayed including

* The recovered drawing file saved at the time of a program failure (DWG)
* The automatic save file, also called the “autosave” file (SV$)
* The drawing backup file (BAK)
* The original drawing file (DWG)

Once a drawing or backup file is opened and saved, the corresponding top-level drawing node is removed from the Backup Files
area.

Preview

Displays a thumbnail preview of the currently selected drawing or backup file.

Click the arrows below the current thumbnail preview to cycle through the previews of all the drawing or backup files that
can be recovered.

Shortcut Menu Options

Right-click a drawing node, drawing or backup file, or a blank area in the Backup Files area to display a shortcut menu with
relevant options.

Reveal in Finder
:   Opens Finder to the location of the selected drawing or backup file.

Select All
:   Selects all the drawing or backup files that can be recovered.

Select None
:   Deselects all the currently selected drawing or backup files.

Select Most Recent
:   Selects the most recent drawing or backup files that can be recovered. All other files are deselected.

Delete File
:   Moves the selected file to the Trash. Applies to SV$ or BAK files only.

Show this screen after crash

Specifies whether the Files Recovered dialog box is displayed the next time
AutoCAD 2026 is started after a program or system failure.

#### Related References

* [DRAWINGRECOVERYHIDE (Command)](DRAWINGRECOVERYHIDE-Command.md)

#### Related Concepts

* [About Recovering from a System Failure](About-Recovering-from-a-System-Failure.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*