# PDFIMPORTIMAGEPATH (System Variable)

Specifies the folder where referenced image files are extracted and saved when importing PDF files.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Registry |
| Initial value: | "PDF Images" |

When you import a PDF file that contains raster images, the images are extracted and saved as PNG files. These extracted images
are attached to the drawing file.

By default, the images are saved in a subfolder of the current drawing file named PDF Images. You can change the folder location
of these referenced image files with the PDFIMPORTIMAGEPATH system variable or by using the Application Preferences dialog
box, Application tab, PDF Import Image Location node.

Whether raster images are generated depends on the PDFIMPORTFILTER system variable.

#### Related Tasks

* [To Work with Importing PDF Data](To-Work-with-Importing-PDF-Data.md)

#### Related References

* [Commands for Importing PDF Files](Commands-for-Importing-PDF-Files.md)
* [Application Tab (Application Preferences Dialog Box)](Application-Tab-Application-Preferences-Dialog-Box.md)

#### Related Concepts

* [About Importing PDF Files](About-Importing-PDF-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*