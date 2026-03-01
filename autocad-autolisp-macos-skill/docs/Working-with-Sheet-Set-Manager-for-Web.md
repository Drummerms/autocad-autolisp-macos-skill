# Working with Sheet Set Manager for Web

Use Sheet Set Manager for Web to manage sheet sets stored in Autodesk Docs.

With Desktop Connector for Autodesk Docs, you can navigate and manage sheet sets locally that are stored in Autodesk Docs.

NOTE:You need an Autodesk Docs account before you can connect to a project. For more information on how to set up and use Autodesk
Docs, see
[Docs Help](https://help.autodesk.com/view/DOCS/ENU/).

## Open a Sheet Set Saved in Autodesk Docs

Browse your sheet sets in Autodesk Docs by doing one of the following:

* In the Start tab, click Autodesk Projects.
* Double-click a sheet set in File Explorer.
* In the AutoCAD web app ([https://web.autocad.com/](https://web.autocad.com/?ref=hyt19&utm_source=desktop&utm_medium=messagectr&utm_campaign=hyt19)), connect to Autodesk Docs projects and open a sheet set as desired.
* In the Sheet Set Manager for Web, click Open Sheet Set.
  ![](../images/GUID-A875C064-61EE-451C-9B70-328312D6E6CF-low.png)

NOTE:Opening a sheet set using the Open Sheet Set dialog box from the Start tab may trigger unnecessary syncing of all files in
the sheet set. It's recommended to use other methods to open the sheet set stored in Autodesk Docs.

## Display the Sheet Set Manager for Web

Opening a sheet set saved in Autodesk Docs displays the Sheet Set Manager for Web by default. Otherwise, do the following
to control the display of the Sheet Set Manager for Web.

1. At the Command prompt, enter
   *ssmdetectmode*.
2. Enter
   *on*.

## Create a Sheet Set in the Cloud

Use the following steps to create a sheet set for use in cloud.

![](../images/GUID-CBAC9562-11AF-4ADB-AE0A-3B8DA839A3E6-low.png)

1. In AutoCAD desktop, click Application menu
   ![](../images/GUID-B9F8DC29-105A-477F-AE00-AA16C15A874E-low.png)![](../images/ac.menuaro.gif)New![](../images/ac.menuaro.gif)Sheet Set.
   ![](../images/GUID-5BDF409F-713A-4708-82E5-11DF2E1056EF-low.png) Find

   In the AutoCAD web app, click
   ![](../images/GUID-86FC210E-2469-4BF1-A188-9C7431C774E4-low.png) (Create Sheet Set) on the Sheet Set Manager.
2. Follow the steps in the Create Sheet Set wizard.
3. Choose the option to create a cloud sheet set using an example sheet set.
4. Click Next.
5. In the Create Sheet Set dialog box, enter the name, description, and location of the new sheet set.
6. Choose a sheet set template.
7. Click Next.
8. Review the sheet set properties and click Create.

NOTE:

* Sheets with existing sheet set references can't be imported using the Create Sheet Set wizard.
* Creating folders based on subsets does not work with Autodesk Docs.

## Create a New Sheet Set Subset

1. In the Sheet Set Manager for Web, right-click the sheet set node (at the top of the list), or an existing subset node. Choose
   New subset.

   ![](../images/GUID-051E57E2-698B-41F3-8A98-00A8D2026AEE-low.png)
2. Select the new subset, if necessary.
3. At the bottom of the Sheet Set Manager for Web, Subset Properties, enter the name and other properties of the new subset.

## Remove a Subset

1. In the Sheet Set Manager for Web, remove any sheets the subset contains, if necessary.

   NOTE:You can only remove an empty subset.
2. Right-click the subset and choose Remove subset.

## Create a New Sheet

1. In the Sheet Set Manager for Web, right-click the sheet set node (at the top of the list), or an existing subset node. Choose
   New sheet.
2. (Optional) Specify a different template.
3. Select the new sheet, if necessary.
4. At the bottom of the Sheet Set Manager for Web, Sheet Properties, enter the name and other properties of the new sheet.

## Specify a Location for New Sheets

1. In the Sheet Set Manager for Web, select a sheet set or a subset.
2. At the bottom of the Sheet Set Manager for Web, Sheet Set Properties pane, expand Sheet Creation and click Sheet Storage Location
   drop-down.

   ![](../images/GUID-CD69BDCF-35BD-4959-8E70-E97B46E40F5E-low.png)

   If you've selected a subset, under Subset Properties pane, expand Subset and click New Sheet Location drop-down.

   ![](../images/GUID-EFE0CB5C-A3B4-4312-AAB2-82F789F6902B-low.png)
3. Click Browse.
4. In the Specify sheet storage location dialog box, click the appropriate checkbox to choose a folder.

   IMPORTANT:When selecting a sheet location folder, do NOT click the folder name. Clicking the folder name displays the contents in the
   folder but does not select it.
5. Click Select.

## Remove a Sheet from a Sheet Set

1. In the Sheet Set Manager for Web, right-click a sheet in the list.

   To remove multiple sheets, hold down the Ctrl key while selecting sheets, and then right-click.
2. Choose Remove sheet.

   NOTE:
   * Removing sheets disassociates the sheets from the sheet set; it doesn't delete the drawing files or the layouts associated
     with the sheets.
   * Removing sheets does not unlock the drawing file.

## Reorder a Sheet or Subset

1. In the Sheet Set Manager for Web, select a sheet or a subset.

   To move multiple sheets, hold down the Ctrl key while selecting each sheet.

   NOTE:Multiple subsets cannot be moved simultaneously.
2. Drag the selected sheet or subset anywhere on the sheet list or under other subsets.

## Rename or Renumber a Sheet

1. In the Sheet Set Manager for Web, right-click a sheet. Choose Rename and renumber.
2. In the Rename and Renumber dialog box, specify the following:
   * *Sheet number.* Specifies the sheet number of the selected sheet.
   * *Sheet title.* Specifies the sheet title of the selected sheet.
   * *Layout name.* Specifies the name of the layout associated with the selected sheet.
   * *File name.* Specifies the name of the drawing file associated with the selected sheet.
   * *Path*. Displays the folder path for the drawing file.
3. To renumber or retitle a series of sheets, click Previous or Next.

## Automatically Number New Sheets

1. In the Sheet Set Manager for Web, right-click a sheet set or subset.
2. In the Auto Numbering dialog box, specify the following:
   * *Prefix.* Adds a number, letter, or word to the new sheets of the selected sheet set or subset.
   * *Start number.* Specifies the first number in the sequence of the newly created sheets. This field only accepts zero or positive integers.

## Modify Properties

1. In the Sheet Set Manager for Web, select a sheet set or subset, or sheet.
2. At the bottom of the Sheet Set Manager for Web, Properties pane, make any changes to the sheet set, subset, or sheet properties.

## Add Custom Properties

1. In the Sheet Set Manager for Web, select a sheet set.
2. At the bottom of the Sheet Set Manager for Web, at the right of the Sheet Set Properties pane, click
   ![](../images/GUID-9853ACE5-01DF-445B-8547-F48A6D6E2E1F-low.png) to create a new sheet set or sheet property.

   ![](../images/GUID-02172D4B-A80C-4CCF-81AF-12600893DCEA-low.png)

   * Sheet set properties are typically specific to a
     *project*, for example, the contract number.
   * Sheet properties are typically specific to each sheet, for example, the name of the designer.
3. To remove a custom property, right-click a property and choose Remove.

## Import a Layout to a Sheet Set

NOTE:You cannot import sheets from locked drawings.

1. In the Sheet Set Manager for Web, right-click a sheet set or a subset.
2. Choose Import sheet.
3. Browse to the cloud location and select one or more drawings that you want to use.
4. Click Select.
5. Select the layouts to be imported as sheets in the current sheet set or subset.

   ![](../images/GUID-AFD5C86C-F7CE-4E32-AA9D-4E741D8F6F54-low.png)
6. Click Import.

## Specify a Support File Location

1. In the Sheet Set Manager for Web, select a sheet set.
2. At the bottom of the Sheet Set Manager for Web, Sheet Set Properties pane, expand Sheet Set and click Support File Location
   drop-down.

   ![](../images/GUID-0E9DDA78-C957-48E2-AD37-682F775A20DE-low.png)

   NOTE:By default, cloud sheet sets use the support files such as drawing templates, plot styles, and fonts (.*shx* and .*ttf*) stored in the AutoCAD web app. For more information about uploading and managing support files, see the
   [File Management](https://help.autodesk.com/view/ACADWEB/ENU/?guid=AutoCAD_Web_Help_File_Management_html) topic in the AutoCAD web app Help.
3. Click Browse.
4. In the Browse to a support file location dialog box, choose a folder.

   ![](../images/GUID-C0971916-ECC0-496E-A7FD-DFAD5BBC9883-low.png)

   IMPORTANT:When selecting a support file folder, do NOT click the folder name. Clicking the folder name displays the contents in the
   folder but does not select it.
5. Click Select.

## Specify a Page Setup Overrides File

When you publish a sheet set, you can use the page setups defined in each drawing file or you can apply the page setup overrides
to all drawing files.

1. In the Sheet Set Manager for Web, select a sheet set.
2. At the bottom of the Sheet Set Manager for Web, Sheet Set Properties pane, expand Sheet Set and click Page Setup Overrides
   File drop-down list.

   NOTE:The drop-down list displays the drawing template (DWT) files that are stored in the configured support files folder for the
   cloud sheet set.

   ![](../images/GUID-97EBB82E-DF2E-4D03-A5E8-D52ED0C3F3F3-low.png)
3. From the drop-down list, choose a DWT file. If the desired file is not available, click Browse to explore folders outside
   the support files folder.
4. In the Specify page setup overrides file dialog box, browse to the drawing template (DWT) file containing the page setup overrides.
5. Click Select.

## Publish to PDF

You can easily publish an entire sheet set, a subset of a sheet set, a single sheet.

1. In the Sheet Set Manager for Web, right-click a sheet set, subset, or sheet.

   To publish multiple sheets, hold down the Ctrl key while selecting subsets or sheets, and then right-click.
2. Choose Publish to PDF.
3. In the Publish Settings dialog box, specify the following:
   * *Output format.* Defines how to publish the files. You can publish the sheets to a single multi-page PDF file or to multiple single-page PDF
     files.
   * *File name.* Specifies the name of the single multi-paged PDF file or the ZIP file name containing multiple PDF files.
   * *Storage location.* Specifies the folder where the PDF or ZIP file is created.

     IMPORTANT:When selecting a storage location folder, do NOT click the folder name. Clicking the folder name displays the contents in
     the folder but does not select it.
   * *Page setup overrides.* Specifies the named page setup from the page setup overrides file to be used for the selected sheets.
4. Specify whether to overwrite the file if a duplicate name exists in the specified storage location.
5. Click Publish to start the publishing process.

   Keep an eye on any notifications that might display during the process.
6. Once the publishing process is finished, on the notification, click Details to view information including any errors or warnings
   about the published job.

   ![](../images/GUID-DAE11874-73B8-4AF5-A64A-8199AFE8109B-low.png)

## Transmit a Sheet Set

You can package and send a sheet set or a portion of a sheet set electronically.

1. In the Sheet Set Manager for Web, right-click a sheet set, subset, or sheet.

   To include multiple sheets in the transmittal, hold down the Ctrl key while selecting subsets or sheets, and then right-click.
2. Choose eTransmit.
3. In the eTransmit Settings dialog box, specify the following:
   * *File name.* Specifies the name of the zipped transmittal package.
   * *Storage location.* Specifies the folder where the transmittal package is created.

     IMPORTANT:When selecting a storage location folder, do NOT click the folder name. Clicking the folder name displays the contents in
     the folder but does not select it.
   * *Transmittal setup.* Specifies the setup to use for the transmittal package.
4. Specify whether to overwrite the file if a duplicate name exists in the specified storage location.
5. Click Transmit.

## Add a Sheet List Table

Use the following steps to add a sheet list table for sheet sets stored in Autodesk Docs.

1. In AutoCAD desktop, close Sheet Set Manager for Web.
2. At the Command prompt, set SSMDETECTMODE to off.
3. In Autodesk Docs, navigate to the location of the desired DST file. Manually lock the file to keep others from editing the
   DST file.
4. Open the cloud DST file.

   With SSMDETECTMODE turned off, the legacy Sheet Set Manager should display when opening a cloud-based DST file.
5. In the legacy Sheet Set Manager, right-click a sheet set name, subset, or multiple sheet set names and subsets. Click Insert
   List Table.
6. In the Sheet List Table dialog box, do the following:
   * Set the table style in the Table Style Settings group.
   * On the Table Data tab, specify title text for the table and add, remove, or change the order of the column entries.
   * On the Subsets and Sheets tab, select the subsets and sheets to be included in the sheet list table.

     NOTE:If you add a sheet to a subset later on, you will be automatically prompted to update the sheet list table.
7. Click OK.
8. In the Sheet Set Manager, right-click the sheet set and choose Close Sheet Set.
9. In Autodesk Docs, navigate to the DST file location and manually unlock the file.
10. In Autodesk desktop, set SSMDETECTMODE to on.
11. Re-open the DST file.

    The Sheet Set Manager for Web now displays when the cloud-based DST file is opened.

#### Related Information

* [About Sheet Set Manager for Web](About-Sheet-Set-Manager-for-Web.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*