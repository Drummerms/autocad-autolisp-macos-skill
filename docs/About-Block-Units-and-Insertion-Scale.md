# About Block Units and Insertion Scale

When a block is defined, it can be assigned a unit of measurement which controls the automatic scaling of the block during
insertion into a drawing.

Whether a block is assigned a specific unit of measurement, or is unitless, there are several settings stored in the current
drawing or user profile that control how the block might be automatically scaled during insertion. Understanding these settings
is important to making sure your blocks are inserted at the correct scale.

NOTE:A block can also be defined without a unit of measurement, meaning it is
*unitless* or
*unspecified*.

The settings that impact the scaling of a block during insertion are:

* *Drawing Insertion Units* - Controls the units at which blocks and drawings are scaled when inserted into the current drawing.

  If you insert a block or drawing that is defined with units that are different from the units used in the current drawing,
  the insertion scale value corrects the mismatch. If you do not want blocks or drawings to be scaled during insertion, specify
  Unitless.
* *Block Insertion Scale Factor* - Additional scale factor applied to the block or drawing during insertion after being scaled based on its assigned units
  of measurement and the Drawing Insertion Unit of the current drawing.
* *Source Content Units* - Sets a units override value to be used when the block or drawing being inserted is unitless.
* *Target Drawing Units* - Sets a units override value to be used when Drawing Insertion Scale is set to Unitless.

## Calculate Block Scale

The following table explains how blocks and drawings are scaled during insertion based on being unitless or assigned a specific
unit of measurement.

NOTE:Some calculations might vary based on the insertion method used: drag 'n drop or double-click while using DesignCenter, Tool
Palettes window, or the Blocks palette. DesignCenter and Tool Palettes window is only available on Windows.

| Unitless Blocks and Drawings | Blocks and Drawings with an Assigned Unit |
| * *Drawing Insertion Units are set to Unitless*  ```   Block Scale = (Source Content Units X Target Drawing Units) X Block Insertion Scale Factor   ```  Examples:  **Block Insertion Scale Factor* = 1*    + *1* = (*Millimeters* X     *Millimeters*) X     *1*   + *0.0394* = (*Millimeters* X     *Inches*) X     *1*   + *1* = (*Inches* X     *Inches*) X     *1*   + *25.4* = (*Inches* X     *Millimeters*) X     *1* **Block Insertion Scale Factor* = 2*    + *2* = (*Millimeters* X     *Millimeters*) X     *2*   + *0.0787* = (*Millimeters* X     *Inches*) X     *2*   + *2* = (*Inches* X     *Inches*) X     *2*   + *50.8* = (*Inches* X     *Millimeters*) X     *2* | * *Drawing Insertion Units are set to Unitless*  ```   Block Scale = (Block Insertion Units X Target Drawing Units) X Block Insertion Scale Factor   ```  Examples:  **Block Insertion Scale Factor* = 1*    + *1* = (*Millimeters* X     *Millimeters*) X     *1*   + *0.0394* = (*Millimeters* X     *Inches*) X     *1*   + *1* = (*Inches* X     *Inches*) X     *1*   + *25.4* = (*Inches* X     *Millimeters*) X     *1* **Block Insertion Scale Factor* = 2*    + *2* = (*Millimeters* X     *Millimeters*) X     *2*   + *0.0787* = (*Millimeters* X     *Inches*) X     *2*   + *2* = (*Inches* X     *Inches*) X     *2*   + *50.8* = (*Inches* X     *Millimeters*) X     *2* |
| * *Drawing Insertion Units are set to a specific unit (Double-click)*  ```   Block Scale = (Drawing Insertion Units X Source Content Units) X Block Insertion Scale Factor   ```  Examples:  **Block Insertion Scale Factor* = 1*    + *1* = (*Millimeters* X     *Millimeters*) X     *1*   + *25.4* = (*Millimeters* X     *Inches*) X     *1*   + *1* = (*Inches* X     *Inches*) X     *1*   + *0.0394* = (*Inches* X     *Millimeters*) X     *1* **Block Insertion Scale Factor* = 2*    + *2* = (*Millimeters* X     *Millimeters*) X     *2*   + *50.8* = (*Millimeters* X     *Inches*) X     *2*   + *2* = (*Inches* X     *Inches*) X     *2*   + *0.0787* = (*Inches* X     *Millimeters*) X     *2* * *Drawing Insertion Units are set to a specific unit (Drag 'n drop)*  NOTE:Drawing Insertion Units are ignored.  ```   Block Scale = Block Insertion Scale Factor   ```  Examples:  **Block Insertion Scale Factor* = 1*    + *1* =     *1* **Block Insertion Scale Factor* = 25.4*    + *25.4* =     *25.4* | * *Drawing Insertion Units are set to a specific unit (Double-click and Drag 'n drop)*  NOTE:This calculation also applies to using the Insert dialog box or -INSERT command.  ```   Block Scale = (Block Insertion Units X Drawing Insertion Units) X Block Insertion Scale Factor   ```  Examples:  **Block Insertion Scale Factor* = 1*    + *1* = (*Millimeters* X     *Millimeters*) X     *1*   + *0.0394* = (*Millimeters* X     *Inches*) X     *1*   + *1* = (*Inches* X     *Inches*) X     *1*   + *25.4* = (*Inches* X     *Millimeters*) X     *1* **Block Insertion Scale Factor* = 2*    + *2* = (*Millimeters* X     *Millimeters*) X     *2*   + *0.0787* = (*Millimeters* X     *Inches*) X     *2*   + *2* = (*Inches* X     *Inches*) X     *2*   + *50.8* = (*Inches* X     *Millimeters*) X     *2* |

#### Related Tasks

* [To Set Block Insertion Scale for a Drawing](To-Set-Block-Insertion-Scale-for-a-Drawing.md)
* [To Set or Change the Block Unit of a Block Definition](To-Set-or-Change-the-Block-Unit-of-a-Block-Definition.md)

#### Related References

* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Concepts

* [Overview of Blocks](Overview-of-Blocks.md)
* [About Defining Blocks](About-Defining-Blocks.md)

#### Related Information

* [About Inserting Blocks](About-Inserting-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*