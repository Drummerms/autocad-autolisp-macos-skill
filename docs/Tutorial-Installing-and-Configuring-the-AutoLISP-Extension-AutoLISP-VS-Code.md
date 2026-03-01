# Tutorial: Installing and Configuring the AutoLISP Extension (AutoLISP/VS Code)

After you have installed Microsoft Visual Studio (VS) Code, you can install and configure the AutoCAD AutoLISP Extension
which will allow you to manage and debug custom AutoLISP programs.

## Prerequisites

1. [Install Visual Studio Code on your workstation.](To-Download-and-Install-VS-Code-AutoLISP-VS-Code.md)

## Topics in this Tutorial

* [Install the AutoCAD AutoLISP Extension](GUID-8EADDE55-CD92-422A-8493-9C7A19880629.htm#SECTION_6370A5A6EE194C258D90A34B8C363E2B)
* [Add a Working Folder](GUID-8EADDE55-CD92-422A-8493-9C7A19880629.htm#SECTION_1073FFA68DCF42FB82BFC8AFA2319ADE)
* [Configure the Debug Configurations (Not available for AutoCAD LT)](GUID-8EADDE55-CD92-422A-8493-9C7A19880629.htm#SECTION_815114D9DDE24D3D804BBEDECEC4B754)

## Install the AutoCAD AutoLISP Extension

The AutoCAD AutoLISP Extension can be found in the Visual Studio Code Marketplace, accessible from inside of the Visual Studio
Code application.

The following steps explain how to install the AutoCAD AutoLISP Extension from the Visual Studio Code Marketplace.

1. Launch Visual Studio Code.

   Do one of the following:

   * *Windows:* Click the Windows Start button, and then click Visual Studio Code > Visual Studio Code.
   * *Mac OS:* In Finder, click Go > Applications and then click Visual Studio Code in the Applications window.
2. In Visual Studio Code, on the Activity Bar, click Extensions (or click View menu > Extensions).

   ![](../images/GUID-F0D8F9E3-EB37-4F41-AE4A-62D4C8BF5DD8-low.png)
3. In the Extensions Search box, type
   *autocad autolisp*.

   ![](../images/GUID-BA809837-256F-404C-B110-D1F55A44DAD4-low.png)
4. From the search results list, click Install under the AutoCAD AutoLISP Extension item.

   After a few moments, the extension should be installed and listed in the Installed Extensions list.

## Add a Working Folder

A working folder is required to store configurations for debugging AutoLISP (LSP) files, but the folder can also be used to
manage your LSP files.

The following steps explain how to create a folder named
*LSP Files* on your local drive in the
*Documents* folder and then how to open that folder in Visual Studio Code.

NOTE:Feel free to use a different name than
*LSP Files* or to store the folder in a different location other than
*Documents*. Just remember to substitute the location and name throughout the remainder of the tutorials.

1. Do one of the following:

   Windows
   :   1. Click the Windows Start button, and then click Windows System > File Explorer or press Windows key + E.
       2. In File Explorer, click in the address bar and type
          *Documents*. Press Enter to open the
          *Documents* folder.
       3. On the Home tab, click New folder from the New panel.
       4. In the in-place editor, type
          *LSP Files* and press Enter.

   Mac OS
   :   1. In Finder, on the Mac OS menu bar, click Go menu > Documents.
       2. In the Documents window, on the Mac OS menu bar, click File menu > New Folder.
       3. In the in-place editor, type
          *LSP Files* and press Enter.
2. Switch to Visual Studio Code.
3. In Visual Studio Code, on the Activity Bar, click Explorer and then click Open Folder (or click File menu > Open Folder/Open).

   ![](../images/GUID-182FA9A4-E0BF-4393-971E-DF8C5E7C6A06-low.png)
4. In the Open Folder dialog box, browse to and select the
   *LSP Files* folder.
5. Click Select Folder on Windows or Open on Mac OS.

## Configure the Debug Configurations (Not supported with AutoCAD LT)

Visual Studio Code needs to be connected to AutoCAD for debugging, this connection is made through the use of a debug configuration.

NOTE:Debugging AutoLISP programs in AutoCAD LT isn't supported with the AutoLISP Extension for Microsoft Visual Studio (VS) Code.

The following steps explain how to add the necessary debug configurations needed to connect Visual Studio Code to AutoCAD.

1. In Visual Studio Code, click File menu > Preferences > Settings.
2. On the User tab, expand Extensions and click AutoCAD AutoLISP Configuration.![](../images/GUID-8910638A-3E86-420C-A6F3-F02FA92690FE-low.png)
3. In the Debug: Attach Process text box, enter one of the following values in bold:
   * (Windows)
     *acad*
   * (Mac OS)
     *AutoCAD*![](../images/GUID-41DC7B29-6818-43DB-B587-8D485F9FD912-low.png)

   NOTE:The process name is case sensitive, so acad or AutoCAD isn’t the same as ACAD or autocad.
4. In the Debug: Launch Program text box, enter the absolute path to the AutoCAD executable.

   The absolute path varies based on the release and platform on which AutoCAD was installed.

   * (Windows)
     *"C:\Program Files\Autodesk\AutoCAD
     2026\acad.exe"*
   * (Mac OS)
     *"/Applications/Autodesk/AutoCAD
     2026/AutoCAD
     2026.app/Contents/MacOS/AutoCAD"*![](../images/GUID-3DBF7FA4-0E6E-4BE1-809C-A6E179FE63AE-low.png)
5. Optionally, in the Debug: Launch Parameter text box, specify any command line switches during the launch of the AutoCAD application.

#### Related Information

* [Configuring VS Code (AutoLISP/VS Code)](Configuring-VS-Code-AutoLISP-VS-Code.md)
* [To Install the AutoCAD AutoLISP Extension (AutoLISP/VS Code)](To-Install-the-AutoCAD-AutoLISP-Extension-AutoLISP-VS-Code.md)
* [To Open a Folder (AutoLISP/VS Code)](To-Open-a-Folder-AutoLISP-VS-Code.md)
* [To Setup the AutoCAD AutoLISP Extension for Debug (AutoLISP/VS Code)](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*