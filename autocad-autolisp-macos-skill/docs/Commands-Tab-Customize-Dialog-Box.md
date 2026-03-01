# Commands Tab (Customize Dialog Box)

Creates and manages the available commands that can be added to menus.

CUI (Command)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Customize ![](../images/ac.menuaro.gif) Interface (CUI).

![](../images/GUID-874DD0CC-E6BC-4FF0-9AB3-FCB20342DD82-low.png)

The following options are displayed.

Command

* *All*. Show all commands
* *ACAD*. Show just the commands predefined by AutoCAD
* *Custom*. Show just the commands added by the user

Commands List

Displays all the standard and custom commands available.

* *Image* - Thumbnail of the current image assigned to the command.
* *Command* - Name of the command. Displayed on the menu bar when the command is assigned to a menu or in a tooltip when the command
  is assigned to a tool group on the Tool Sets palette.
* *Source* - Name of the customization group that the command is stored in.

Create New Command (+)
:   Adds a new command to the Commands list that can be added to the menus.

    A custom command can be used to start a core
    AutoCAD 2026 command or one defined by a third party. Commands can also contain AutoLISP code.

Options ![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png)
:   Displays a menu which allows you to manage existing commands in the Commands list.

    * *Duplicate* - Creates a copy of the command currently selected in the Commands list. Duplicating a command allows you to modify an existing
      command without changing the original one.
    * *Delete* - Removes the selected command from the Commands list. Commands that are currently assigned to a menu or Workflow cannot
      be deleted.

      NOTE:There is no way to undo the removal of a command, be sure to select the correct command before you click Delete.

Search Commands
:   Filters the commands displayed in the Commands list. Click the ‘X’ in the text box to clear the current filter.

    Enter a text string to control which commands are displayed in the Commands list. Only the names of the commands that contain
    the text string are displayed in the Commands list.

Properties

Displays the properties and values that define the selected command in the Command list.

Name
:   Displays the name of the command. The name you enter is the label or tooltip name displayed in the program.

Description
:   Displays the description for the command. The description you enter is displayed in a tooltip.

Macro
:   Displays the macro assigned to the command. Enter a new or change the existing macro for the command.

Image
:   Specifies the raster image to use for the command when it is added to a tool set.

Preview
:   Displays a thumbnail of the image currently assigned to the command.

Information

Displays some basic information about the field that currently has cursor focus under Properties.

Reset to Default

Resets the commands and user interface elements back to their initial installed default settings.

#### Related References

* [CUI (Command)](CUI-Command.md)
* [Aliases Tab (Customize Dialog Box)](Aliases-Tab-Customize-Dialog-Box.md)
* [Shortcuts Tab (Customize Dialog Box)](Shortcuts-Tab-Customize-Dialog-Box.md)

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

#### Related Information

* [Menus Tab (Customize Dialog Box)](Menus-Tab-Customize-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*