# To Setup the AutoCAD AutoLISP Extension for Debug (AutoLISP/VS Code)

NOTE:Debugging is not available in AutoCAD LT.

How you configure the AutoLISP Extension for debug depends on which version you are using. The following steps explain how
to identify which version of the extension you are using:

1. In Visual Studio Code, click File menu > Preferences > Extensions.
2. In the Extensions view, clear any text from the Search box.
3. Under the INSTALLED section, locate AutoCAD AutoLISP Extension in the list.

   The version number of the extension will be next to its name.

   ![](../images/GUID-ABF9B024-2BDE-4DAE-BF26-A1A5B797927C-low.png)

## Setting up attach and launch configurations (Version 1.3.2 and Later)

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

## Setting up attach and launch configurations per folder (Version 1.3.2 and Earlier)

NOTE:A folder must be opened before debug configurations can be added, and debug configurations should not be added to a workspace
but to a folder only. See
[To Open a Folder](To-Open-a-Folder-AutoLISP-VS-Code.md) for steps on opening a folder.

1. In Visual Studio Code, on the Activity Bar, click Debug and then click Create a launch.json File (or click Debug menu > Open
   Configurations).

   ![](../images/GUID-9DCDE0C5-9433-40C4-A285-B2D44C7A5EB1-low.png)
2. On the Configurations menu, choose AutoLISP Debug: Attach.

   ![](../images/GUID-4CA3A813-ECE4-4427-96E5-856B05801BB3-low.png)

   A new file named
   *launch.json* that contains the AutoLISP Debug: Attach configuration should now be open in the current editor window.
3. In the editor window, lower-right corner, click Add Configuration and then choose AutoLISP Debug: Launch from the list that
   is displayed.

   ![](../images/GUID-AEB4FFE7-4D30-4025-9DFB-E07D414C29C9-low.png)
4. In the
   *launch.json* editor window, make the following changes (example edits show in bold) based on your installed OS.
   1. Path attribute of the AutoLISP Debug: Launch configuration needs to be updated to the absolute path to the AutoCAD executable.
   2. Process attribute of the AutoLISP Debug: Attach configuration should be updated to the process name of the AutoCAD application.

      NOTE:The process name is case sensitive, so acad or AutoCAD isn’t the same as ACAD or autocad.
   3. Optionally, the
      Params attribute of the AutoLISP Debug: Launch configuration can be updated to specify any command line switches to use when the
      AutoCAD application is launched.

   launch.json file on Windows
   :   ```
       {
           "configurations":
           [
               {
                   "type": "launchlisp",
                   "request": "launch",
                   "name": "Autolisp Debug: Launch",
                   "attributes": {
                       "path": "C:\\Program Files\\Autodesk\\AutoCAD 2026\\acad.exe",
                       "params": ""
                   }
               },
               {
                   "type": "attachlisp",
                   "request": "attach",
                   "name": "Autolisp Debug: Attach",
                   "attributes": {
                       "process": "acad"
                   }
               }
           ]
       }
       ```

   launch.json file on Mac OS
   :   ```
       {
           "configurations":
           [
               {
                   "type": "launchlisp",
                   "request": "launch",
                   "name": "Autolisp Debug: Launch",
                   "attributes": {
                       "path": "/Applications/Autodesk/AutoCAD 2026/AutoCAD 2026.app/Contents/MacOS/AutoCAD",
                       "params": ""
                   }
               },
               {
                   "type": "attachlisp",
                   "request": "attach",
                   "name": "Autolisp Debug: Attach",
                   "attributes": {
                       "process": "AutoCAD"
                   }
               }
           ]
       }
       ```
5. Click File menu > Save to save the changes to the
   *launch.json* file.

#### Related Information

* [Debugging AutoLISP Files (AutoLISP/VS Code)](Debugging-AutoLISP-Files-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*