# About File Organization

The default folder structure for program and support files is designed to efficiently organize those files into logical groups.

If the default organization of program and support files does not suit your needs, you can change it. However, some applications
look for certain files in specific locations, and you should verify that modifications do not conflict with the requirements
of those applications. Without the full path, including drive and folder, the program can locate only those files that are
found in its library search paths.

The program references the user profile of the operating system to identify where local and roamable customizable files should
be stored. The locations of the local and roamable folders can be accessed using the following system variables:

* *LOCALROOTPREFIX* - Stores the full path to the root folder where local customizable files were installed.
* *ROAMABLEROOTPREFIX* - Stores the full path to the root folder where roamable customizable files were installed.

Beginning with AutoCAD 2013 SP1-based products on Windows and AutoCAD 2014 for Mac, the reserved
*acad<release\_number>.lsp* or
*acadlt<release\_number>.lsp* and
*acad<release\_number>doc.lsp* or
*acadlt<release\_number>doc.lsp* files and their successors are loaded only from the product's default installation folders. Depending on the setting of the
SECURELOAD system variable, the TRUSTEDPATHS system variable specifies the folders from where AutoCAD-based products can load
and execute other files that contain code. In addition, the LEGACYCODESEARCH system variable controls whether the Start In
folder will be searched for executable files.

NOTE:AutoLISP applications are not supported by AutoCAD LT on Mac OS.

The following AutoLISP sample code defines the CUSTFILES command, and opens File Explorer to the location where roamable customizable
files were installed.

NOTE:The SHELL command is available in AutoCAD on Windows only and not available in AutoCAD LT on Windows.

```
(defun c:custfiles ()
  (command "shell"
    (strcat "explorer \"" (getvar "roamablerootprefix") "\"")
  )
 (princ)
)
```

## Library Search Path

The library search path specifies where the program searches for files when you do not specify a full path name, as follows:

* Start In folder. This folder is determined either by the folder in which a file is double-clicked (on Windows or Mac OS),
  or by the Start In attribute of a shortcut icon on Windows. (STARTINFOLDER system variable)
* Folder that contains the current drawing file. (DWGPREFIX system variable)
* Folder of the project name for an external reference file, such as an image, xref, or underlay. (PROJECTNAME system variable)
* Folders listed in the program's Support File Search paths. (ACADPREFIX system variable)
* Folder that contains the installed files for the program.

Depending on the current environment, two or more folders may be the same.

IMPORTANT:Beginning with AutoCAD 2016-based products, the LEGACYCODESEARCH system variable controls whether the Start In and Drawing
folders will be searched for executable files. Because the Start In and drawing folders are often targets for malware, it
is recommended that you leave LEGACYCODESEARCH set to 0, off.

If a file is not in this search path, you must specify its full or its relative path name and file name before the program
can find it. For example, if you want to insert the
*part5.dwg* file into your current drawing and it is not in the library search path, you must specify its full path name or a relative
path name based on a valid path in the library search path. A relative path name is shown here:

Command:
*-insert*

Enter block name or [?]:
*/files2/olddwgs/part5*

## Folder Structure

The program uses tree-structured folders and subfolders. It is recommended that you keep supplemental files, such as AutoLISP
applications (not in AutoCAD LT on Mac OS), customization files, or third-party applications, separate from the installed
program and support files. This makes it easier to track possible conflicts and to upgrade each application without affecting
the others.

The default location for the program is in the
*Program Files* folder on Windows and
*Applications* on Mac OS. You can create a new folder on the same level (for example,
*/AcadApps)* and store custom programs, customization files, and other third-party applications in subfolders on the next level. If you
want to maintain multiple drawing folders (for separate job files), you can create a folder such as
*/AcadJobs* with subfolders for each job.

## Command Search Procedure

When you enter a command, the application goes through a series of steps to evaluate the validity of the command name. A
command can be

* A built-in command or system variable
* An external command or alias defined in the
  *acad.pgp* (or
  *acadlt.pgp* in AutoCAD LT) file
* An AutoCorrect entry for a command in the
  *autoCorrectUserDB.pgp* file
* A synonym entry for a command in the
  *acadSynonymsGlobalDB.pgp* file
* A user-defined AutoLISP command
* A user-defined command by an ObjectARX or Managed .NET application
* A device driver command

NOTE:Applications are not supported by or on

* AutoLISP applications are not supported by AutoCAD LT on Mac OS
* ObjectARX and Managed .NET applications are not supported by AutoCAD LT
* Managed .NET applications are not supported on Mac OS

You can enter a command at the Command prompt or start it from the user interface. Commands can also be started from a script
file or by an AutoLISP, ObjectARX, or Managed .NET application.

The following list describes the search order to validate a command name.

1. If the input is a null response (Spacebar or Enter), the program uses the name of the last command issued. HELP is the default.
2. The command is checked against the list of built-in commands. If the command is in the list and is not preceded by a period
   (.), the program then checks the command against a list of undefined commands. If the command is undefined, the search continues.
   Otherwise, the command is run, unless another reason prevents it from doing so. Running it transparently or in Perspective
   mode might be impossible.
3. The command is checked against the names of commands defined by a device driver, and then by those defined by the display
   driver.
4. The command is checked against the external commands defined in the program parameters file. If the command name corresponds
   to a defined external command, that command runs, and the search is complete.
5. The command is checked against the list of commands defined by AutoLISP, ObjectARX, and Managed .NET applications. At this
   point, an autoloaded command is loaded. (Limited availability in AutoCAD LT on Windows and not available in AutoCAD LT on
   Mac OS)
6. The program checks the command name against the list of system variables. If the command name is in the list, the SETVAR command
   is executed, using the input as the variable name.
7. If the command name corresponds to a command alias, AutoCorrect name, or synonym defined in their associated program parameters
   files, the expanded command name is used and the search process starts over with the list of built-in commands.
8. If all the preceding steps fail, the search terminates with a warning message about illegal command names.

#### Related Tasks

* [To Locate Support Files](To-Locate-Support-Files.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Multiple Drawing Folders](About-Multiple-Drawing-Folders.md)
* [About Customized File Locations](About-Customized-File-Locations.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*