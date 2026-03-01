# Application Tab (Application Preferences Dialog Box)

Lists the folders in which the program searches for support, driver, menu, and other files. Also lists optional, user-defined
settings such as which dictionary to use for checking spelling.

OPTIONS (Command)

*Menu*:
AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences

![](../images/GUID-94509F06-13A6-4316-9025-8C0468226637-low.png)

## List of Options

The following options are displayed.

Support File Search Path

Specifies the folders in which the program should look for text fonts, customization files, plug-ins, drawings to insert,
linetypes, and hatch patterns that are not in the current folder.

Working Support File Search Path

Displays the active directories that the program searches for support files specific to your system. The list is read-only
and displays valid paths from the Support Files Search Path that exist within the current directory structure and network
mappings.

Project Files Search Path

Specifies a project name for the drawing. The project name corresponds to a search path for external reference (xref) files
associated with the project. You can create any number of project names with associated folders, but each drawing can have
only one project name.

Trusted Locations

Specifies the folders from where AutoCAD can load and execute files that contain code. (TRUSTEDPATHS system variable)

Customization Files

Specifies the names and locations of various types of files.

Main Customization File
:   Specifies the default location of the main customization file (acad.cuix).

Custom Icon Location
:   Specifies the location for custom icons referenced by your customization files.

Command Aliases
:   Specifies the location of the PGP file that should be loaded when the program is started.

Text Editor, Dictionary, and Font File Names

Specifies a number of optional settings.

Alternate Font File
:   Specifies the alternate font to be used when the specified font file cannot be located. ([FONTALT](FONTALT-System-Variable.md) system variable)

    If you click Browse, the
    [Alternate Font dialog box](Select-Alternate-Font-Dialog-Box.md) is displayed, from which you can choose an available font.

Font Mapping File
:   Specifies the font mapping file to be used. ([FONTMAP](FONTMAP-System-Variable.md) system variable)

Printer Support File Path

Specifies search path settings for printer support files.

Print Spooler File Location
:   Specifies the path for print spool files.

Printer Configuration Search Path
:   Specifies the path for printer configuration files.

Printer Description File Search Path
:   Specifies the path for files with a .*pmp* file extension, or printer description files.

Plot Style Table Search Path
:   Specifies the path for files with an .*stb* or
    *.ctb*extension, or plot style table files (both named plot style tables and color-dependent plot style tables).

Automatic Save File Location

Specifies the path for the file created when you select Automatically Save on the General tab. ([SAVEFILEPATH](SAVEFILEPATH-System-Variable.md) system variable)

Color Book Locations

Specifies the path for color book files that can be used when specifying colors in the
[Color Palette dialog box](Color-Palette-Dialog-Box.md). You can define multiple folders for each path specified. This option is saved with the user profile.

Template Settings

Specifies the drawing template settings.

Drawing Template File Location
:   Specifies the path to locate drawing template files used by the Select Template dialog box.

Sheet Set Template File Location
:   Specifies the path to locate sheet set template files used by the New Sheet Set dialog box.

Default Template File Name for QNEW
:   Specifies the drawing template file used by the
    [QNEW](QNEW-Command.md) command.

Default Template for Layout Creation and Page Setups Overrides
:   Specifies the default template file that is used for creating new layouts and to store page setup overrides that can be applied
    to Publish operations from the Sheet Set Manager.

Log File Location

Specifies the path for the log file created when you select Maintain a Log File on the Open and Save tab. ([LOGFILEPATH](LOGFILEPATH-System-Variable.md) system variable)

Texture Maps Search Path

Specifies the folders to search for rendering texture maps.

Web File Search Path

Specifies the folders to search for photometric web files.

PDF Import Image Location

Specifies the folder where referenced image files are extracted and saved when importing PDF files.

Add

Adds a search path for the selected folder.

Remove

Removes the selected search path or file.

Options

Edits or changes the order of a selected path.

Change Path
:   Displays the Browse for Folder or Select a File dialog box, depending on what you selected in the Files list.

Move Item Up
:   Moves the selected search path above the preceding search path.

Move Item Down
:   Moves the selected search path below the following search path.

Set as Current
:   Makes the selected project or spelling dictionary current.

Reset Hidden Messages

Resets the display of all message boxes that you marked to not display again or to always use a specified option in them.

Reset Application Options

Displays the Reset Application Options dialog box. Click Restart AutoCAD to restore the program defaults.

Before the program is reset, many of the files that you can customize are backed up to an archive file with the naming convention
of
*Settings Backup <Date> <Time>.tgz*. The archive file is saved to
*/Users/<user name>/Library/Application Support/Autodesk*.

The archive contains many of the customization files located in the following folders:

* */Users/<user name>/Library/Application Support/Autodesk/local/AutoCAD {version}*
* */Users/<user name>/Library/Application Support/Autodesk/roaming/AutoCAD {version}*

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [PDFIMPORTIMAGEPATH (System Variable)](PDFIMPORTIMAGEPATH-System-Variable.md)
* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*