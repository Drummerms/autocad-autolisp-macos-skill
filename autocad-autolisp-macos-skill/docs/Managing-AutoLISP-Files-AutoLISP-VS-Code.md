# Managing AutoLISP Files (AutoLISP/VS Code)

VS Code provides you with several ways to manage your AutoLISP source code files.

When working in VS Code, you can manage your source code files using a combination of:

* Folders on a local or network drive
* Git repository
* AutoLISP project (recommended)

## Store Source Files in Folders

Source code files are stored in a folder on a local and network drive. A single folder can be used to organize all of your
source code files or you can use multiple folders to logically group your source code files based on their intended purpose.
When working in VS Code, you can
[open a folder](To-Open-a-Folder-AutoLISP-VS-Code.md) which provides access to all files and subfolders in that folder from the Explorer view on the Activity bar.

## Control Source with Git Repositories

The git source control manager (SCM) extension is installed with VS Code. You can access the features of git by opening a
folder that represents a git repository or clone from a URL. Once a git repository or clone has been opened, you can:

* Edit the files and folders that make up the git repository
* Compare current and past versions of a file
* Branch the git repository
* View and commit changes back to the git repository

For more information on the Git extension and other SCM Provider extensions, see
[Using Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol) on the Microsoft.com website.

## Access Source Files with AutoLISP Projects (Recommended)

AutoLISP projects allow you to logically group AutoLISP source (LSP) files. An AutoLISP project is saved to a file with the
*.prj* extension. PRJ files contain references to LSP files that are already stored in a local or network folder, or a folder that
represents a git repository. The AutoCAD AutoLISP Extension defines a view on the Activity bar named AutoLISP Project Manager
from which you can create and open PRJ files.

Once a PRJ file has been opened, you can

* Manage the LSP files in the project
* Edit and debug the LSP files in the project
* Find and replace text across all LSP files in the project

NOTE:In AutoCAD for Windows only, PRJ files can be used to compile several LSP files into a single Visual LISP executable (VLX)
file. (Not available in AutoCAD LT for Windows)

![](../images/GUID-FB5038CE-0728-47FB-8A76-E6C8B6BE5C9B-low.png)

The AutoLISP Project Manager consists of two panes; PROJECT and FIND & REPLACE.

The following explains the tools that are part of each pane.

PROJECT Pane
:   Contains tools used to create and open an AutoLISP project from which you can manage your AutoLISP source (LSP) files.

    *Current Project*

    Name of the project currently open in the AutoLISP Project Manager.

    *Toolbar*

    * [Create a New Project](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md) ![](../images/GUID-545C3059-600F-4F06-83DD-5EF856B5F302-low.png) - Creates a new AutoLISP project.
    * [Open an Existing Project](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md) ![](../images/GUID-A2034A87-B3A9-46DF-B824-A27F88F82578-low.png) - Opens a previously saved AutoLISP project.
    * [Add File to Project](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md) ![](../images/GUID-4A5E07E4-1209-486D-8EAF-242D38B15316-low.png) - Adds an AutoLISP source (LSP) file to the current project.
    * Refresh
      ![](../images/GUID-00D1793E-827A-46BA-9CF6-BA5220F8AFFA-low.png) - Refreshes the current project.

    *Current Project - Secondary Menu*

    * [Add File to Project](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md) - Adds an AutoLISP source (LSP) file to the current project.

      NOTE:Starting with version 1.4.0 of the AutoCAD AutoLISP Extension, you can add one or more an AutoLISP source (LSP) files from
      an open folder on the Explorer view.
    * Refresh - Refreshes the current project.
    * Save Project - Saves changes to the current project. Changes to project are normally automatically saved, but if an error
      occurs the changes might not be automatically saved.
    * Save All - Saves all the LSP files that are currently open in editor windows and associated with the current project.

    *LSP File - Secondary Menu*

    * [Remove File from Project](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md) - Removes an AutoLISP source (LSP) file from the current project. The LSP file is only removed from the project, not from
      the local or network drive.

FIND & REPLACE Pane
:   Contains tools used to find and replace text strings within the AutoLISP source (LSP) files that are in the current project.

    *Toolbar*

    * [Find in Project](To-Find-and-Replace-Text-in-AutoLISP-Source-Files-AutoLISP-VS-Code.md) ![](../images/GUID-0C198290-914D-4A0A-A431-FD819F01D6D0-low.png) - Displays the Find in Project dialog box. This dialog box allows you to enter the text string to search for and specify
      the match options to use during the search.
    * [Replace in Project](To-Find-and-Replace-Text-in-AutoLISP-Source-Files-AutoLISP-VS-Code.md) ![](../images/GUID-6E90986F-562E-4BE5-94F3-70F2302E72CB-low.png) - Displays the Find in Project and Replace in Project dialog boxes. Theses dialog boxes allow you to enter the text string
      to search for and replace with, and specify the match options to use during the search.
    * Stop Search
      ![](../images/GUID-E25E248D-A36B-460E-8CC0-3E5ACF831769-low.png) - Cancels the search for the text string in the LSP files.
    * Clear All Search Results
      ![](../images/GUID-8DB2324B-CD78-427C-A1EE-4EE168F2EF79-low.png) - Clears the entries from the Search results list.

#### Topics in this section

* [To Manage Source Files with an AutoLISP Project (AutoLISP/VS Code)](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md)
* [To Open a Folder (AutoLISP/VS Code)](To-Open-a-Folder-AutoLISP-VS-Code.md)
* [To Work with Workspaces (AutoLISP/VS Code)](To-Work-with-Workspaces-AutoLISP-VS-Code.md)
* [To Find and Replace Text in AutoLISP Source Files (AutoLISP/VS Code)](To-Find-and-Replace-Text-in-AutoLISP-Source-Files-AutoLISP-VS-Code.md)

#### Related Information

* [To Manage Source Files with an AutoLISP Project (AutoLISP/VS Code)](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md)
* [To Create a New AutoLISP or DCL File (AutoLISP/VS Code)](To-Create-a-New-AutoLISP-or-DCL-File-AutoLISP-VS-Code.md)
* [To Open an AutoLISP or DCL File (AutoLISP/VS Code)](To-Open-an-AutoLISP-or-DCL-File-AutoLISP-VS-Code.md)
* [To Open a Folder (AutoLISP/VS Code)](To-Open-a-Folder-AutoLISP-VS-Code.md)
* [To Work with Workspaces (AutoLISP/VS Code)](To-Work-with-Workspaces-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*