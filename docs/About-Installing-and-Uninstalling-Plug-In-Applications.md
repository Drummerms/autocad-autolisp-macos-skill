# About Installing and Uninstalling Plug-In Applications

The plug-in auto loader mechanism allows for easier deployment of custom applications using a package format.

The package format is a common folder structure that has the extension
*.bundle* in its name and has an XML file that defines the various components of the plug-in. By deploying custom applications as a
BUNDLE, it makes it easier to target multiple operating systems and product releases since the parameters of your plug-in
are defined in the XML file of the package. A BUNDLE can be used as a replacement to creating complex installer scripts when
deploying a plug-in.

NOTE:Plug-ins are not supported in AutoCAD LT for Mac.

A plug-in can be deployed by placing it in one of the
*ApplicationPlugins* or
*ApplicationAddins* folders on a local drive.

* *General Installation folder*
  + Windows:
    *%PROGRAMFILES%\Autodesk\ApplicationPlugins*
  + Mac OS:
    */Applications/Autodesk/ApplicationAddins*
* *All Users Profile folders*
  + Windows:
    *%ALLUSERSPROFILE%\Autodesk\ApplicationPlugins*
  + Mac OS:
    *N/A*
* *User Profile folders*
  + Windows:
    *%APPDATA%\Autodesk\ApplicationPlugins*
  + Mac OS:
    *~/Library/Application Support/Autodesk/ApplicationAddins*

When an AutoCAD-based product or AutoCAD LT starts, the
*ApplicationPlugins* or
*ApplicationAddins* folders are checked for plug-ins. The plug-ins found are automatically registered and loaded based on the metadata in the
XML file of each package.

NOTE:While a plug-in can be loaded from any of the
*ApplicationPlugins* folders, it is recommended to place all plug-ins under the
*%PROGRAMFILES%\Autodesk\ApplicationPlugins* folder on Windows. The plug-ins in this location are trusted and are not checked for the presence of a digital signature.
All other
*ApplicationPlugins* folders must be trusted as part of the application's preferences and should to be digitally signed.

## Trusting Plug-in Packages

Starting with AutoCAD 2016-based products on Windows, it is recommended to digitally sign your custom program files. By digitally
signing a custom program file, you inform the user as to who published the custom program file and if any changes were made
to the file after it was digitally signed. For information on digitally signing custom program files, see the "About Digitally
Signing Custom Program Files" topic.

Each custom program file loaded is check for the existence of a digital signature. If a digital signature is found attached
to a custom program file, the user is presented with information about the digital certificate and publisher that signed the
file. The user can choose to continue to load the file, and optionally trust all files by the publisher of the file being
loaded. If no or an invalid digital signature is found, the user is informed that the program file might not be safe to load
and execute.

## Installing Plug-in Packages

A package can be deployed using an installer, such as MSI, or manually copying the files and folder structure to the
*ApplicationPlugins* or
*ApplicationAddins* folder. For Autodesk App Store downloads, deployment of the package is done using an MSI installer on Windows.

## Loading Plug-in Packages

By default, plug-ins are automatically registered with an AutoCAD-based product or AutoCAD LT when a new plug-in is installed
during the current session. The load behavior for plug-ins is controlled with the APPAUTOLOAD system variable. When APPAUTOLOAD
is set to 0, no plug-ins are loaded unless the APPAUTOLOADER command is used.

NOTE:Starting with AutoCAD 2014-based products, custom applications must work under secure mode; when the SECURELOAD system variable
is set to 1 or 2. When operating under secure mode, the program is restricted to loading and executing files that contain
code from trusted locations; trusted locations are specified by the TRUSTEDPATHS system variable.

## Uninstalling Plug-in Packages

A package can be uninstalled by removing the appropriate folder with a .bundle extension from the
*ApplicationPlugins* or
*ApplicationAddins* folder. This can be accomplished by offering an uninstall option with the original installer or to manually delete the
*.bundle* folder.

NOTE:A plug-in downloaded from the Autodesk App Store website can also be uninstalled by re-downloading the plug-in. When the download
completes, you are prompted to uninstall the plug-in.

#### Related References

* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [Example: Basic .bundle Folder Structure for a Plug-in](Example-Basic-.bundle-Folder-Structure-for-a-Plug-in.md)
* [Example: Using Folders to Organize Components for a Plug-in](Example-Using-Folders-to-Organize-Components-for-a-Plug-in.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*