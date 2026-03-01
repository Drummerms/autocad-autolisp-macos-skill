# About Creating and Restoring from Backup Files

Backup files help ensure the safety of your drawing data. If a problem occurs, you can restore a drawing backup file.

Computer hardware problems, power failures or surges, user mistakes, or software problems can cause errors in a drawing. By
saving your work frequently, you can ensure a minimum of lost data if your system fails for any reason. If a problem occurs,
you can restore a drawing backup file.

## Use Backup Files

In the Options dialog box Open and Save tab you can specify that backup files are created when you save drawings. If you
do, each time you save a drawing, the previous version of your drawing is saved to a file with the same name and a
*.bak* file extension. The backup file is located in the same folder as the drawing file.

You can revert to your backup version by renaming the .*bak* file in File Explorer to a file with a .*dwg* extension. You may want to copy it to a different folder to avoid overwriting your original file.

## Save Your Drawing Automatically at Specified Intervals

If you turn the automatic save option on, your drawing is saved at specified time intervals. By default, files saved automatically
are temporarily assigned the name
*filename\_a\_b\_nnnn.sv$*.

* *Filename* is the current drawing name.
* *a* is the number of open instances of the same drawing file in the same work session.
* *b* is the number of open instances of the same drawing in different work sessions.
* *nnnn* is a random number.

These temporary files are automatically deleted when a drawing closes normally. In the event of a program failure or a power
failure, these files are not deleted.

To recover a previous version of your drawing from the automatically saved file, rename the file using a
*.dwg* extension in place of the
*.sv$* extension before you close the program.

#### Related Concepts

* [About Repairing Damaged Drawing Files](About-Repairing-Damaged-Drawing-Files.md)

#### Related Information

* [To Control the Creation of Automatic Drawing Backup (.bak) Files](To-Control-the-Creation-of-Automatic-Drawing-Backup-.bakFiles.md)
* [To Save a Drawing Automatically](To-Save-a-Drawing-Automatically.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*