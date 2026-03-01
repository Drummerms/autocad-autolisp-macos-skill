# About Exporting and Importing Custom Settings

Custom settings can be transferred between computers with the same release of the product installed. You can also export the
settings to create a backup of custom settings for the product.

NOTE:You must start the program at least once before you can export or import custom settings.

## Export Custom Settings

When exporting custom settings, a zip file is created that contains the custom settings and files. During the import process,
you select the ZIP file that contains the exported custom settings and files.

The following settings are available to transfer from one machine to another:

* User Profile
* CUI user interface files
* Command alias files
* Plot setting files
* Templates
* My properties settings
* Hatch patterns
* Linetypes
* Shapes
* SHX fonts

## Import Custom Settings

After successfully exporting the custom settings you can import them to another machine with the same release of the product
installed.

If the user profile <<Unnamed Profile>> exists, the user profile is automatically backed up before the zip file is imported.

Local locations that exist as part of a user profile in a transfer package are created automatically during the import process,
if the locations do not already exist; locations that are on a network or removable drive are not created automatically.

If custom files were added to a transfer package from a network location, the custom files are copied to a local location
when the original network locations are not available during the import operation. If the custom files from a network location
are found in the same location on the network, the files are not copied to the network location and are ignored during the
import operation.

#### Topics in this section

* [To Export and Import Custom Settings](To-Export-and-Import-Custom-Settings.md)

  Transfer custom settings between computers, or create a backup of your custom settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*