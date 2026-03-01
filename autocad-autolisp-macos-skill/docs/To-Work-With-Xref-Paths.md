# To Work With Xref Paths

Change, remove, or make Xref paths relative. Modify file options to specify a project's name or search path.

## Display the External References Palette

Click
Window menu ![](../images/ac.menuaro.gif) Reference Manager.

## Change the Path of a DWG Reference

1. Display the External References palette.
2. Select a DWG reference name and, under Saved Path, do one of the following:
   * Edit the xref path directly.
   * Click within the edit box, and then click the Browse button (...) that appears. Select the xref in its new path.
3. Click OK.

   The program reloads the xref and then regenerates the drawing with the xref in place.

## Remove an Xref Path

1. Display the External References palette.
2. Right-click the reference name and choose Path ![](../images/ac.menuaro.gif) Remove Path.

## Set an Xref's Path Relative to the Current Drawing

1. Display the External References palette.
2. Right-click the reference name and choose Path ![](../images/ac.menuaro.gif)Make Relative.

NOTE:If the drawing and the referenced file are stored on separate drives, the path should always be absolute.

## Set an Absolute Xref's Path to the Current Drawing

1. Display the External References palette.
2. Right-click the reference name and choose Path ![](../images/ac.menuaro.gif)Make Absolute.

NOTE:If the drawing and the referenced file are stored on separate drives, the path should always be absolute.

## Display Currently Defined Project Names

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, double-click Project Files Search Path.
3. Click each project name folder to display the search paths associated with it and click OK.

## Add a Project Name

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, double-click Project Files Search Path. Click Add.

   A folder named
   *projectx* (where
   *x* indicates the next available number) is created and indented beneath the project folder.
3. Either enter a new name, or press Enter to accept
   *projectx* and click OK.

   The project name must be 31 characters or fewer, and it cannot contain leading spaces or terminating spaces.

## Remove a Project Name

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, double-click Project Files Search Path.
3. Select a project name, click Remove.
4. Click OK.

## Modify a Project Name

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, double-click Project Files Search Path.
3. Select a project name.
4. Enter a new name and click OK.

   You can also modify a project name by selecting the name in the project folder and pressing F2.

## Add a Search Path

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, select a project name and click Add.
3. Enter a new search path beneath the project name, or click Browse and select a new path and click OK

## Delete a Search Path

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, select a project name and Click Remove.

## Change a Search Path

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, select a project name. Click Browse.
3. In the Browse for Folder dialog box, select a new path.
4. Click OK to close each dialog box.

   You can also change a search path by selecting the project path and pressing F2.

## Make a Project Current

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, double-click Project Files Search Path.
3. Select a Project name. Click Set Current.
4. Click OK (or Apply).

   You can also set a project current by entering PROJECTNAME at the Command prompt and then entering the name of the project.

## Clear the Current Project

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. In the Application Preferences dialog box, Application tab, click Project Files Search Path.
3. Click Clear Current and click OK.

   This clears the setting for the current drawing.

   You can also clear the current project at the Command prompt by entering PROJECTNAME and then entering a period (*.*).

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)
* [REFPATHTYPE (System Variable)](REFPATHTYPE-System-Variable.md)

#### Related Concepts

* [About Changing the Temporary Xref File Path](About-Changing-the-Temporary-Xref-File-Path.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Work With Attaching and Detaching Referenced Drawings](To-Work-With-Attaching-and-Detaching-Referenced-Drawings.md)
* [Set Paths to Referenced Drawings](Set-Paths-to-Referenced-Drawings.md)
* [About Updating Referenced Drawing Attachments](About-Updating-Referenced-Drawing-Attachments.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*