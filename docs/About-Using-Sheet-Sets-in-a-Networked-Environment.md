# About Using Sheet Sets in a Networked Environment

The associations and information that define a sheet set are stored in a sheet set data (DST) file. The first time you create
a new sheet set, the default sheet set storage folder,
*AutoCAD Sheet Sets*, is created in the default location: your*My Documents* folder.

When you use sheet sets in a team, each member should have network access to the DST file and the drawing template (DWT)
files associated with the sheet set:

* Each team member can open the sheet set to load the sheet set information from the DST file into the Sheet Set Manager.
* If each member of the team has access to the sheet set DWT files, new drawing files and their sheets are created using the
  same drawing template file; page setups for these drawings are also standardized.

Any changes that any team member makes opens the DST file briefly and updates the information stored in that file. When the
DST file is opened, a lock icon is displayed next to the sheet set name in the top left corner of the Sheet Set Manager:

![](../images/GUID-4C2FF607-087E-46C7-BC25-435CE4AFF41E-low.png)A green dot in the lock icon indicates that the Sheet Set Manager session on your computer has temporarily locked the DST
file.

![](../images/GUID-E09F5B39-7870-4012-8CF2-4DD8ECF514DC-low.png)A red dot indicates that the Sheet Set Manager session on a team member's computer has temporarily locked the DST file.

![](../images/GUID-E8996C0A-475C-4CB4-8BB1-8899B9308B8C-low.png)A yellow dot in the lock icon means that the sheet is in a special state; for example, its file properties may be set to Read-Only.

Other members of the team can automatically see changes to the sheet set in the Sheet Set Manager tree view.

## Logical Drive Naming

If two or more users access the same sheet files through different logical drives on a network, each will in turn be prompted
to resave the sheet set using their own logical drive. To avoid unnecessary saving, users should map the same logical drives,
if possible.

## Sheet Status

Status data for sheets in the current sheet set is also available to other team members. This status data is displayed in
the tree view and indicates one of the following conditions:

![](../images/GUID-963B5363-FBB3-44D8-AC2D-74205BE3CC00-low.png)The sheet is available for editing.

![](../images/GUID-7BB73809-C8F6-45AD-A1E7-9F90E0A3E62C-low.png)The sheet is locked.

![](../images/GUID-BD4CFC68-5ABE-4334-B596-86D3D421193E-low.png)The sheet is missing or found in an unexpected folder location.

NOTE:A false lock icon may be displayed if there is a network problem or if the program terminates unexpectedly. If you suspect
a problem, click the sheet to display more information.

The active sheets of other team members are automatically polled for status changes; the tree view is updated in your session
of the Sheet Set Manager. The polling cycle skips the poll interval in your session when a command is active. To force a sheet
status update, click Refresh Sheet Status on the Sheet List tab.

You can click any sheet to display more information in the Details area of the Sheet Set Manager.

## Working without the Sheet Set Manager

With some limitations, you can use sheet sets in a team with members who do not have network access, or do not have access
to the Sheet Set Manager. However, relevant information from the DST file is stored (cached) in each drawing file, and sheet
set information, such as custom properties, is preserved when the drawing file is shared by other team members.

After a member of the team changes information in the DST file, the information in several drawing files might need to be
updated. With the sheet set open, update a sheet by opening and saving the sheet.

You can update all sheets in a sheet set automatically with the Resave All Sheets option in the sheet set shortcut menu. Drawing
files saved in a previous DWG file format are saved without changing the format.

NOTE:In a network environment, make sure that all drawing files used in the current sheet set that are opened by other users are
closed before performing the Resave All Sheets operation.

#### Related Information

* [About Sheet Sets](About-Sheet-Sets.md)
* [To Create a Sheet Set](To-Create-a-Sheet-Set.md)
* [To Create a New Sheet](To-Create-a-New-Sheet.md)
* [To Import Layouts to a Sheet Set](To-Import-Layouts-to-a-Sheet-Set.md)
* [To Reassociate a Sheet in a Sheet Set](To-Reassociate-a-Sheet-in-a-Sheet-Set.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*