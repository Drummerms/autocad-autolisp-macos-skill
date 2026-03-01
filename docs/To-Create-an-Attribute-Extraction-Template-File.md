# To Create an Attribute Extraction Template File

Using an attribute extraction template file, you can extract attribute information from a drawing and create a separate text
file for use with database software.

1. Start TextEdit.
2. Enter template information such as tag name, data type, field length, and number of decimal places associated with the information
   you want to extract.

   You must include at least one attribute tag field. The attribute tag fields determine which attributes, hence which blocks,
   will be included in the attribute extraction file. If a block does not contain the specified attributes, the values for the
   absent ones are filled with blanks or zeros, depending on whether the field is a character field or a numeric field.

   NOTE:Do not include comments in an attribute template file.
3. Save the text file in ASCII format.

NOTE:You can also extract attribute information from a drawing and create a separate text file.

#### Related Concepts

* [About Setting Up an Attribute Extraction Template File](About-Setting-Up-an-Attribute-Extraction-Template-File.md)

#### Related Information

* [About Extracting Data from Block Attributes](About-Extracting-Data-from-Block-Attributes.md)
* [To Extract Attribute Information](To-Extract-Attribute-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*