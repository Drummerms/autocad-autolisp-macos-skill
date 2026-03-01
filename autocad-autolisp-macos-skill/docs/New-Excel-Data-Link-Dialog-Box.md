# New Excel Data Link Dialog Box

Links data from a spreadsheet created in Microsoft Excel to a table within your drawing.

![](../images/GUID-1A0F33B3-2D9E-4AF6-97C5-B7E14271E181-low.png)

## List of Options

The following options are displayed.

Excel File

Specifies the file and file path from which to create a data link.

File Name
:   Displays the Microsoft XLS or XLSX, file name that is linked to your drawing.

    Click the [...] button to browse for another Microsoft Excel file on your Mac.

Select Excel sheet to link to
:   Displays the names of all sheets within the specified XLS or XLSX file. You may click the drop-down menu to select the sheet
    of your choice.

Link Entire Sheet
:   Links the entire sheet to the table.

Link to a Named Range
:   Links a named range of cells already contained within your Excel file to a table in your drawing.

    Clicking the arrow displays the available named ranges found in the linked spreadsheet.

Link to Range
:   Specifies a range of cells in your Excel file to link to a table in your drawing.

    In the text box, enter the range of cells you want linked to your drawing. Valid ranged include:

    * Rectangular regions (for example, A1:D10)
    * Entire columns (for example, A:A)
    * Sets of columns (for example, A:D)

Cell Content

Options in this box will determine how data is imported into your drawing from your external source.

Keep Data Formats and Formulas
:   Imports data with formulas and supported data formats attached.

Keep Data Formats, Solve Formulas in Excel
:   Imports data formats. Data is calculated from formulas in Excel.

Convert Data Formats to Text, Solve Formulas in Excel
:   Imports Microsoft Excel data as text with data calculated from formulas in Excel (supported data formats not attached).

Allow Writing to Source File
:   Specifies that the DATALINKUPDATE command can be used to upload any changes made to linked data in your drawing to the original
    external spreadsheet.

Cell Formatting

Use Excel Formatting
:   Specifies that any formatting specified in the original XLS or XLSX file will be brought into your drawing. If you do not
    select this, the table style in the drawing is applied.

Keep Table Updated to Excel Formatting
:   If the option above is selected, updates any changed formatting when the DATALINKUPDATE command is used.

Start With Excel Formatting, Do Not Update
:   Imports the formatting specified in the original XLS or XLSX file into your drawing, but any changes made to the formatting
    are not included when the DATALINKUPDATE command is used.

Insert Table

Selecting Insert table check box allows you to insert the table in the drawing soon after you click the OK button.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*