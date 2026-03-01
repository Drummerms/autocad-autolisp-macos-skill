# Symbols

Insert symbols and details into your drawings from commercial online sources or from your own designs.

## Some Basic Definitions

In AutoCAD, symbols and details that you insert into drawings are called
*blocks*. A block is a collection of geometric and text objects plus other data that are combined into a single
*named object*. The following are some examples of a variety of blocks at different scales.

![](../images/GUID-BA0CF256-FDA2-4797-8DCB-5E48A7644B13-low.png)

There are three elements involved for inserting blocks in a drawing.

* A
  *block definition*. This data is stored in a drawing file or drawing template file in a non-graphical format. Block definitions can easily be
  created or imported from any drawing file.
* A
  *block reference*. When you insert a block, you specify a drawing file or a block definition to import. The graphics for the block reference
  are generated from the block definition.
* A
  *block insertion base point* or just
  *base point*. When you insert a block, this is the part of the block attached to your cursor.

  The base point is circled on the block below. Later, if you select a block that's already been inserted, it displays a grip
  at the base point. You can easily move and rotate this block using this grip.

  ![](../images/GUID-C8F6C7E2-1BE0-4D32-8B80-72045DDA269E-low.png)

For example, the following drawing contains only four block
*definitions*: Cubicle, Chair, Table, and Plant. There are three block
*references* to Cubicle, twelve block references to Chair, two block references to Table, and two block references to Plant.

![](../images/GUID-72DA9AA8-D53B-4919-B899-FF965E9CD615-low.png)

Considering this example, what are the advantages of inserting the chair as a block reference 12 times rather than creating
12 copies of a geometry of the chair?

* The block reference of the chair associates the geometry of the chair into a single object, which is easier to move, copy,
  and rotate as a unit.
* The part number, vendor, and other information, which are called
  *block attributes*, can be stored with the block definition or each block insertion. This data can be extracted into a schedule or a report.
* If you make a change to the block definition in a drawing, all the associated block references in the drawing are immediately
  updated.
* For drawings with many repetitive elements, the amount of data stored is significantly less when these elements are stored
  as block references.

NOTE:The commonly used term,
*block*, can refer loosely to either a block definition, a block reference, or both depending on context.

## Sources for Blocks

Typically, you
*insert* a block into the current drawing from one of these sources:

* Any drawing file. For example, you might create a drawing of a standard detail view. You can then use a block insertion tool
  to insert this drawing as a block into your current drawing. In this example, the detail views folder is commonly termed a
  *block library* folder.

  ![](../images/GUID-0B49474D-9E38-457E-92F1-D29AABEC35CD-low.png)
* One or more block definitions contained within a drawing file. For example, you can create a drawing that only contains block
  definitions of trees. You can then insert any of these blocks from that drawing into your current drawing. A drawing file
  that contains a family of related blocks is commonly termed a
  *block library* drawing.

  ![](../images/GUID-BCAD57EC-6BB0-4BB4-BDD4-B461070A08E7-low.png)
* One or more block definitions created in your
  *current* drawing. For example, you might want to create a block from a set of objects that appear repeatedly in that drawing, such
  as the following cubicle arrangement that contains multiple
  *nested* blocks. All the blocks used in the cubicle arrangement can be combined into a
  *single* block for multiple placements.

  ![](../images/GUID-C90D08F3-6563-402E-A4B1-0EC736BC672C-low.png)

Once you insert a block, you can easily move, copy, rotate or scale it.

## Insert a Block

The Blocks palette is used to insert blocks.

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Blocks panel ![](../images/ac.menuaro.gif) Insert.
   ![](../images/GUID-6857E103-73A1-42F1-AA87-3265189DB33B-low.png)

   This opens the Blocks palette and makes it active. By default it is docked on the right-side of the application.

   ![](../images/GUID-2ECA7808-AD4B-4681-AA2B-ED5A212E19D3-low.png)

   Display Options Toolbar

   * ![](../images/GUID-D864EF4F-F367-4F19-A0F0-FEC90A9016BB-low.png) Displays the blocks in the current drawing.
   * ![](../images/GUID-74621D09-5D97-4EB8-AD0F-63B2FCA60602-low.png) Displays recently inserted or created blocks. The recent list persists across drawings and sessions.
   * ![](../images/GUID-A9E5F9C7-C2A7-4C8A-B730-E7600EE4DFA2-low.png) Displays the blocks from a selected block library.
2. Select the display option for block libraries.
   ![](../images/GUID-A9E5F9C7-C2A7-4C8A-B730-E7600EE4DFA2-low.png)
3. Do one of the following:
   * Click the file drop-down list to display the 10 most recently used block libraries (folder or drawing file).
   * Click to select a folder or a file.![](../images/GUID-D803F078-FF46-4D80-895E-A476EB77DD99-low.png)

   NOTE:To share block libraries across AutoCAD platforms, sign in to your Autodesk account and select a folder or drawing from a
   cloud drive.
4. If you have selected a folder that contains multiple drawings, you can double-click on a drawing to view and insert the blocks
   in the drawing.

   NOTE:Click Back to Library to return to the library and display the blocks and drawing in the folder.
   ![](../images/GUID-741CB467-ECF5-4CD9-A008-9A1772E9CEE5-low.png)
5. From the Blocks palette, double-click to place the block, or drag to place it. When you double-click to place the block you
   can use object snaps for more precision.

   ![](../images/GUID-22D9841F-C894-4E91-A9EB-5DE2492E0574-low.png)

You can also browse to a drawing file and insert it as a block or display the blocks on the drawing in the Blocks palette.

1. Select the display option to show the blocks from the current drawing.
   ![](../images/GUID-D864EF4F-F367-4F19-A0F0-FEC90A9016BB-low.png)
2. Click the icon indicated.

   ![](../images/GUID-86289B9B-88DA-48EE-8D87-0052D7CD25B7-low.png)
3. Browse to the drawing file you want to insert.

TIP:The default options at the bottom of the Blocks palette are usually acceptable in most cases, but you can experiment with
them to see what options you might want to use.

![](../images/GUID-C8595C9C-9B1F-4E76-9618-28A5CF1C47D9-low.png)

## Create a Drawing for Use as a Block

Often, individual drawing files are created to be used as blocks and saved in a folder with similar drawing files. This method
is an alternative to accessing the block definitions stored in a single drawing.

When you create a drawing file for use as a block, make sure that you locate an object at the origin point (0,0). This will
serve as the default base point of the block. Later, when you insert the block, it is attached to your cursor at the base
point.

In the following example, a drawing file is inserted into the current drawing to provide a standard detail view.

![](../images/GUID-00C876EC-DA1F-47CF-82E9-65A464081DC5-low.png)

Custom title blocks and drawing borders are also created as drawing files that can be inserted later or included in drawing
template files.

TIP:When you save the drawing, navigate to a folder, right-click, and create several folders to organize the block drawings.

## Manage Block Definitions and Data in a Drawing (Optional)

You can create, remove, and modify block definitions directly in the current drawing for special circumstances.

* Remove unused block definitions from a drawing with the PURGE command. Purging a drawing of unused block definitions can reduce
  the size of a drawing. You can purge only those block definitions that aren't used by any block references in the drawing.
* Create new block definitions directly in the current drawing with the BLOCK command. Creating block definitions is useful
  either if you need a block that's unique to that drawing or if you want to create a block library drawing that contains a
  family of related block definitions.
* Disassemble a block reference into its constituent objects with the EXPLODE command. Exploding block references provides an
  easy way to define new versions of a block definition with the BLOCK command or to save the resulting objects to a new drawing
  file with the WBLOCK command.

TIP:Block definitions can also include objects called
*block attributes* that can store information such as part number, vendor name, and cost. You can extract and export block attribute data to
a table, schedule, or external file. Some blocks called
*dynamic blocks* can change their appearance dynamically depending on the associated data, location, or options chosen.

## Summary of Suggestions and Recommendations

Several different methods are commonly used for saving and organizing block definitions.

* Create an individual drawing file for each block that you intend to use. Save these drawing files in folders that contain
  families of related drawing files.
* Create drawing files called
  *block library* drawings. Each one of these drawings contains a family of related block definitions. When you insert a block library drawing
  into your current drawing, all the blocks that are defined in that drawing become available in your current drawing.
* Include the block definitions for title blocks and commonly used symbols in your drawing template files to make them available
  immediately when starting a new drawing.

TIP:With online access, you can download AutoCAD drawing files from the web sites of commercial vendors and suppliers. This option
can save you a significant amount of time, but always check to make sure that these drawings are drawn correctly and to scale.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Modify](GUID-C4C6369F-879D-4AF4-93E2-17F2E0DBB171.htm " Perform operations such as erase, move, and trim on the objects in a drawing.
")

**Next topic:** [Layout](GUID-775647A9-6289-47B2-84A1-3DD463696FD7.htm " Display one or more scaled views of your design on a standard-size drawing sheet called a layout.
")

#### Related References

* [Blocks Palette](Blocks-Palette.md)
* [BLOCK (Command)](BLOCK-Command.md)
* [INSERT (Command)](INSERT-Command.md)
* [PURGE (Command)](PURGE-Command.md)
* [EXPLODE (Command)](EXPLODE-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*