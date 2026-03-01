# To Export and Import Custom Settings

Transfer custom settings between computers, or create a backup of your custom settings.

## Export Custom Settings in AutoCAD for Mac

1. Click
   Tools menu ![](../images/ac.menuaro.gif) Export Settings.
2. Click OK on the alert.

   The Export Settings dialog box displays.

   ![](../images/GUID-EA828087-F0BF-4F20-B194-C17E5F1B725D-low.png)
3. Select or clear settings as needed and click Export.
4. Enter a file name and location for the export file.
5. Click Save.

   You are prompted to save any unsaved drawings and then AutoCAD closes.

   The dialog box displays.
6. Click View the Report to view details on which files were exported.

   ![](../images/GUID-1DC56296-969F-4EDE-A42F-0C5C67E3378D-low.png)
7. Click Yes to restart AutoCAD.

## Import Custom Settings in AutoCAD for Mac

1. Click
   Tools menu ![](../images/ac.menuaro.gif) Import Settings.
2. Click OK on the alert.
3. Browse to and select the export file created previously and click Open.

   The Import Settings dialog box displays.

   ![](../images/GUID-6516254F-DDDE-41CF-9D21-87E7615F02D3-low.png)
4. Select or clear settings as needed and click Import.

   You are prompted to save any unsaved drawings and then AutoCAD closes.

   The dialog box displays.

   ![](../images/GUID-2E2629AC-86DB-4091-A0F2-7A870F4EBF96-low.png)
5. Click View the Report to view details on which files were imported.
6. Click Yes to restart AutoCAD.

## Export Custom Settings using Terminal

NOTE:Make sure AutoCAD or AutoCAD LT is not running.

1. Click
   *local drive*![](../images/ac.menuaro.gif) Applications ![](../images/ac.menuaro.gif) Utilities ![](../images/ac.menuaro.gif) Terminal.
2. Do one of the following:
   * To export all custom settings and files, enter the following:

     ```
     ./AdMigrator -e
     ```

     NOTE:You may need to supply the full path for the AdMigrator utility, for example /Applications/Autodesk/AutoCAD <release>/AutoCAD
     <release>.app/Contents/Helpers/AdMigrator.app/Contents/MacOS/.
   * To export a specific setting or file, enter the following:

     ```
     ./AdMigrator -e {setting key} -d {destination path]
     ```

     NOTE:A destination path is optional. If a destination path isn't supplied, the zip file is created in your user documents folder.

     | Setting | Key |
     | User profile | profile |
     | CUI | cui |
     | Command alias | alias |
     | Plot files | plot |
     | Templates | template |
     | My properties | property |
     | Line types | ltype |
     | Hatch patterns | hatch |
     | Shape files | shape |
     | SHX font files | shx |

The utility creates a zip file containing the exported custom settings and files which you can then import on another machine.
Each machine must be running the same version of AutoCAD or AutoCAD LT.

## Import Custom Settings using Terminal

Follow these steps to import the custom settings and files after exporting them to a zip file.

NOTE:Make sure AutoCAD or AutoCAD LT is not running.

1. Click
   *local drive*![](../images/ac.menuaro.gif) Applications ![](../images/ac.menuaro.gif) Utilities ![](../images/ac.menuaro.gif) Terminal.
2. Do one of the following:
   * To import all custom settings and files from the export file, enter the following:

     ```
     ./AdMigrator -i -s {zip file path and name}.tar.gz
     ```
   * To import a specific setting or file from the export file, enter the following:

     ```
     ./AdMigrator -i cui {zip file path and name}.tar.gz
     ```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*