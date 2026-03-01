# About Using Formulas in Table Cells

Table cells can contain formulas that do calculations using the values in other table cells.

With a table cell selected, you can insert formulas from the Table Cell visor
![](../images/GUID-2DDDD11D-9FC9-45A4-A301-49FA78ECA3BE-low.png). You can also open the In-Place Text Editor and enter a formula in a table cell manually.

## Insert a Formula

In formulas, cells are referred to by their column letter and row number. For example, the cell at top left in the table
is A1. Merged cells use the number of what would be the top-left cell. A range of cells is defined by the first and last cells,
with a colon between them. For example, the range A5:C10 includes cells in rows 5 through 10 in columns A, B, and C.

A formula must start with an equal sign (=). The formulas for sum, average, and count ignore empty cells and cells that do
not resolve to a numeric value. Other formulas display an error (#) if any cell in the arithmetic expression is empty or contains
nonnumeric data.

Use the Cell option to select a cell in another table in the same drawing. When you have selected the cell, the In-Place Text
Editor opens so you can enter the rest of the formula.

## Copy a Formula

When you copy a formula to another cell in the table, the range changes to reflect the new location. For example, if the formula
in A10 sums A1 through A9, when you copy it to B10, the range of cells changes so that it sums B1 through B9.

If you don't want a cell address to change when you copy and paste the formula, add a dollar sign ($) to the column or row
part of the address. For example, if you enter $A10, the column stays the same and the row changes. If you enter $A$10, both
column and row stay the same.

## Insert Data Automatically

You can automatically increment data in adjacent cells within a table by using the AutoFill grip.

![](../images/GUID-1DAD5986-3622-4339-9CA8-3333FB53D432-low.png)

For example, a table with a date column can have the dates automatically entered by entering the first necessary date and
dragging the AutoFill grip.

Numbers will fill automatically by increments of 1 if one cell is selected and dragged. Similarly, dates will resolve by increments
of one day if only one cell is selected. If two cells are manually filled with dates one week apart, the remaining cells are
incremented by one week.

#### Related Tasks

* [To Define Data Formats in Table Cells](To-Define-Data-Formats-in-Table-Cells.md)

#### Related References

* [Commands for Tables](Commands-for-Tables.md)

#### Related Concepts

* [About Tables](About-Tables.md)

#### Related Information

* [To Add a Formula to Table Cells](To-Add-a-Formula-to-Table-Cells.md)
* [To Insert a Formula Field in a Table Cell](To-Insert-a-Formula-Field-in-a-Table-Cell.md)
* [To Automatically Fill Cells With Incremented Data](To-Automatically-Fill-Cells-With-Incremented-Data.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*