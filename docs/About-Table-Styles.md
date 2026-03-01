# About Table Styles

The appearance of the table is controlled by its table style. You can use the default table style, STANDARD, or create your
own table styles.

When you create a table, you can choose a table style that contains the cell styles you want to use.

## Cell Styles and Properties

A cell style controls the appearance of a cell in three general areas:

* General properties, including fill color, alignment, format, and margins
* Text properties, including text style, height, and color
* Border properties, including lineweight, linetype, color, and border display

Use the TABLESTYLE command to create or access the cell styles stored in a specified table style. As with other styles such
as text styles and dimension styles, table styles are stored within a drawing or drawing template file. Table styles can be
copied from one drawing to another by copying a table that uses that style.

## Default Styles

The default table style, Standard, includes three default cell styles: Title, Header, and Data. The Title and Header cell
styles are a Label
*type* of cell, while the Data cell style is a Data
*type* of cell.

![](../images/GUID-8E38C430-2D54-40B1-BBAD-645CFB77F2CA-low.png)

When you create your own cell styles, you will start from a Label or Data type of cell. While you can modify the settings
for the default cell styles, a better practice is to leave these unchanged as starting points for new cell styles.

## Override the Table Style

Table styles control the appearance of a table and the cells contained in the table, but you can override the style of individual
cells. Select a table and open the Properties Inspector. You can change the appearance of the table under the Table and Table
Breaks sections of the Properties Inspector and Table visor. To display all table properties in the Properties Inspector,
click All above the Object drop-down list. You can assign a different table style to a table using the Table Style property
under the Table section.

Select individual cells to see the Cell and Contents sections of the Properties Inspector. Here you can change the border
styles, text formatting, and the size of the cells. The border properties in a table's cell style control the display of the
gridlines that divide the table into cells. The borders of the title row, the column header row, and the data rows can have
different lineweight and color and can be displayed or not displayed.

The text style assigned to the cell style defines the text appearance. You can use any text style in the drawing or create
one. The type of data and the formatting for that data type is controlled by its Data Type and the Additional Format options
you select.

To revert a table's properties to its table style, select Remove All Property Overrides from the Table visor.

#### Related Tasks

* [To Work with Table and Cell Styles](To-Work-with-Table-and-Cell-Styles.md)
* [To Set the Current Table Style](To-Set-the-Current-Table-Style.md)
* [To Apply a New Table Style to a Table](To-Apply-a-New-Table-Style-to-a-Table.md)
* [To Create a Table](To-Create-a-Table.md)

#### Related References

* [Commands for Tables](Commands-for-Tables.md)

#### Related Concepts

* [About Tables](About-Tables.md)

#### Related Information

* [About Modifying Tables](About-Modifying-Tables.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*