# -IMAGE (Command)

Attaches a raster image to the drawing.

## List of Prompts

The following prompts are displayed.

Enter image option [[?](IMAGE-Command.md)/[Detach](IMAGE-Command.md)/[Path](IMAGE-Command.md)/[Reload](IMAGE-Command.md)/[Unload](IMAGE-Command.md)/[Attach](IMAGE-Command.md)] <Attach>: *Enter an option or press* Enter

?—List Images

Lists the images by name in alphabetical order, the number of times each is attached to the drawing, and the path where the
image is stored. Images are listed in alphabetical order, regardless of the setting of the [MAXSORT](MAXSORT-System-Variable.md) system variable.

Detach

Detaches the named image from the drawing, marks it for deletion, and erases all occurrences of the image.

Path

Updates the path name (including file name) associated with a particular image. This option is useful if you change the location
of an image file, rename the file, or replace an old image file with a new file; for instance, you can update *image01.png* and save it as *image02.png*.

If you enter an asterisk (*\**), the following prompt is displayed:

Old path: *Lists the current path name for each image*

Enter New path: *Enter the new path name for the specified image*

Reload

Reloads the selected images, making that information available for display and plotting.

Unload

Removes image data from working memory so that the images are not displayed, thus improving performance. All information associated
with the image remains stored with the drawing. The image frame of each attached image remains visible.

Attach

Attaches a new image or a copy of an attached image to the current drawing. The Select Image File dialog box (a [standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)) is displayed.

The file name without the extension is assigned as the image name. Image names can include up to 255 characters and contain
letters, digits, spaces, and any special characters not used by the operating system or this program. If the file name is
not a valid name for a non-graphical object, the Substitute Image Name dialog box is displayed. A valid image name is generated
from the file name and an underscore and number are appended to the name.

If a definition with the same name and path exists in the drawing, the following prompts are displayed and the image is inserted
as a copy:

Image file name has already been loaded.

Use IMAGE Reload to update its definition.

Specify insertion point <0,0>: *Specify an insertion point*

Base image size: Width: *current width*, Height: *current height*, *current unit*

Specify scale factor: *Enter a value or press* Enter

Specify rotation angle <0>: *Enter a value or press* Enter

If the [FILEDIA](FILEDIA-System-Variable.md) system variable is set to 0, the following prompt is displayed instead of the dialog box:

Enter image file name to attach <*last*>: *Enter an image name*

The last image name attached to the drawing during the current session is the default. To avoid errors when entering an image
name, it is recommended that you specify both the image name and the file name as follows:

*imagename=path name/long file name.bmp*

or

*imagename="path name/long file name.bmp"*

If you enter a valid image name without a file extension, the program searches for the file in this order: first, an existing
image definition in the drawing, and second, an image file in the folders in order of the search path. The program searches
for all the image files with the specified name, regardless of extension, and uses the first name found. If no image name
or image file is found, the message “Image Not Found” is displayed and the prompt is repeated.

To specify a long file name that does not conform to this program's naming rules, enter the name as follows:

"*imagename=filename*"

You can use a dialog box to search for image files but still enter the *imagename=filename* convention at the Command prompt. Enter a tilde (*~*) at the Enter Image File Name to Attach prompt. If you press Esc after the dialog box opens, the Enter Image Name prompt
is displayed.

#### Related References

* [IMAGE (Command)](IMAGE-Command-2.md)

#### Related Concepts

* [About Viewing Raster Image Information](About-Viewing-Raster-Image-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*