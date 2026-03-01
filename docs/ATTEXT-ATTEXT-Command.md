# ATTEXT (-ATTEXT) (Command)

Extracts attribute data, informational text associated with a block, into a file.

## List of Prompts

Enter extraction type or enable object selection [[Cdf](ATTEXT-ATTEXT-Command.md)/[Sdf](ATTEXT-ATTEXT-Command.md)/[Dxf](ATTEXT-ATTEXT-Command.md)/[Objects](ATTEXT-ATTEXT-Command.md)] <C>:
*Enter an option or press* Enter

CDF: Comma-Delimited File
:   Generates a file containing one record for each block reference in the drawing. Commas separate the fields of each record.
    Single quotation marks enclose the character fields.

    In the Select Template File dialog box, enter the name of an existing attribute extraction template file.

    In the Create Extract File dialog box, enter the name for the output file. The extract file's file name extension is .*txt* for CDF or SDF format.

SDF: Space-Delimited File
:   Generates a file containing one record for each block reference in the drawing. The fields of each record have a fixed width;
    therefore, field separators or character string delimiters are not used.

    In the Select Template File dialog box, enter the name of an existing attribute extraction template file.

    In the Create Extract File dialog box, enter the name for the output file. The extract file's file name extension is .*txt* for CDF or SDF format.

DXF: Drawing Interchange File
:   Produces a subset of the AutoCAD Drawing Interchange File format containing only block reference, attribute, and end-of-sequence
    objects. DXF-format extraction requires no template. The file name extension .*dxx* distinguishes the output file from normal DXF files.

    In the Create Extract File dialog box, enter the name for the output file. The extract file's file name extension is .*dxx* for DXF format.

Objects
:   Selects objects whose attributes you want to extract.

#### Related Concepts

* [About Setting Up an Attribute Extraction Template File](About-Setting-Up-an-Attribute-Extraction-Template-File.md)

#### Related Information

* [About Defining and Attaching Block Attributes](About-Defining-and-Attaching-Block-Attributes.md)
* [About Extracting Data from Block Attributes](About-Extracting-Data-from-Block-Attributes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*