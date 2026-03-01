# Batch Publish Dialog Box

Specifies drawing sheets that you can assemble, reorder, and publish as a multi-sheet drawing set.

PUBLISH (Command)

*Toolbar*:
![](../images/GUID-4C887873-7EE8-497C-B87D-0D8DFF393268-low.png)

![](../images/GUID-F18AF0CB-1259-4BFD-97AD-CD4B47EC9018-low.png)

## Summary

You can publish the drawing set to a PDF file or send it to the printer named in the page setup for hardcopy output.

## List of Options

The following options are displayed.

Sheet List:

Displays the current drawing set (DSD) file.

Load Sheet List Button ![](../images/GUID-44D260A8-DA47-4BE3-9A26-4CF5C1673DDB-low.png)
:   Displays a standard file selection dialog box, in which you can select a DSD file to load. Displays the Replace or Append
    dialog box if a list of drawing sheets is present in the Batch Publish dialog box. You can either replace the existing list
    of drawing sheets with the new sheets or append the new sheets to the current list.

Save Sheet List Button ![](../images/GUID-F59EC11C-AEDD-4136-A7B9-37B3CD6C233E-low.png)
:   Displays the Save List As dialog box, in which you can save the current list of drawings as a DSD file. DSD files are used
    to describe lists of drawing files and selected lists of layouts within those drawing files.

Publish To:

Defines how to layouts should be published. You can publish to either a PDF file (an electronic drawing set) or to the printer
specified in the page setup (a paper drawing set).

PDF
:   Indicates that the layouts should be published to a PDF file.

Printer from Page Setup
:   Indicates that the output device given for each layout's page setup will be used.

Preview

Displays a preview of the selected layout in the Sheet list. Click the Next and Previous buttons to preview another layout
in the Sheet list.

Sheets to Publish List

Contains the list of drawing sheets to be included for publishing. Click the page setup column to change the sheet’s settings.
Use the shortcut menu and available buttons to add sheets or make other changes to the list.

Sheet Name
:   Combines the drawing name and the layout name with a dash (-). Drawing sheet names must be unique within a single PDF file.

Page Setup
:   Displays the named page setup for the sheet. You can change the page setup by clicking the page setup name and selecting another
    page setup from the list. Only Model page setups can be applied to Model sheets, and only named layout page setups can be
    applied to named layout sheets.

Status
:   Displays the status of the sheet when it is loaded to the list of sheets.

Manage Sheet List

Adds and removes layouts from the Sheet list.

Add Sheets (+)
:   Displays the Select Drawings dialog box (a standard file selection dialog box), in which you can select drawings to add to
    the list of sheets. The layout names from those files are extracted, and one sheet is added to the list for each Model and
    named layout in the drawing. You can use the Add Content list to specify to extract the Model layout only, named layouts only,
    or both.

    The initial sheet names are constructed from the base drawing name and the layout name or the word Model separated by a dash
    (-).

Remove Sheets (-)
:   Deletes the selected sheets from the list.

Add Current Drawing
:   Adds the Model layout and all named layouts from the current drawing.

Add Open Drawings
:   Adds the Model layout and all named layouts from the drawings that are currently open.

Sheet List Shortcut Menu

The following options are available when you right-click a sheet:

Move to Top
:   Moves the selected sheets to the top of the list.

Move Up
:   Moves the selected sheets up one position in the list.

Move Down
:   Moves the selected sheets down one position in the list.

Move to Bottom
:   Moves the selected sheets to the bottom of the list.

Sheet Details

:   Displays the following information about the selected sheet: status, source drawing, drawing location, layout name, plot device,
    plot size, plot scale, and page setup details.

Printer from Page Setup Options

The following options are specific to publishing to a printer.

Number of Copies
:   Specifies the number of copies to publish.

Include Plot Stamp
:   Places a plot stamp on a specified corner of each drawing and logs it to a file. Click Configure Plot Stamp to display the
    Plot Stamp Settings dialog box, and specify the content and look of the plot stamp.

PDF Options

The following options are specific to publishing to a PDF file.

Preset
:   Loads publish options from a plotter configuration file containing settings preconfigured to generate PDF files meant for
    a specific purpose. The name of the PDF preset typically indicates its purpose.

PDF Options ![](../images/GUID-A1A24E28-8DE1-4880-80DF-C6ACB799DCAF-low.png)
:   Opens the PDF Options dialog box where you can specify vector quality, raster image quality, and how to handle overlapping
    lines, layer information, hyperlinks, bookmarks, and TrueType fonts.

Location
:   Specifies the location to save the PDF file to and display the PDF when publishing is complete.

Single PDF with multiple sheets
:   Combines sheets into a single multi-sheet PDF file. If this option is not selected, the system generates multiple PDF files,
    one for each sheet.

Include Plot Stamp
:   Places a plot stamp on a specified corner of each drawing and logs it to a file. The plot stamp data is specified in the Plot
    Stamp Dialog Box.

Plot Stamp Settings ![](../images/GUID-B1077BD3-0873-4A76-AB68-475E9029C224-low.png)
:   Displays the Plot Stamp dialog box, in which you can specify the information, such as drawing name and plot scale, that you
    want applied to the plot stamp

Open when Complete
:   When publishing completes, the PDF file will open in a viewer application.

Publish

Starts the publishing operation.

To display information about the published sheets, including any errors or warnings, click the Plotting Details Report message
balloon to displays the Print Details dialog box. This information is also saved to the Plot and Publish log file.

#### Related References

* [PUBLISH (Command)](PUBLISH-Command.md)
* [PDF Options Dialog Box](PDF-Options-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*