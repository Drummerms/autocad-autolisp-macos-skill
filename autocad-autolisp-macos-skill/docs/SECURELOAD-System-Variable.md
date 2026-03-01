# SECURELOAD (System Variable)

Controls whether AutoCAD loads executable files based on their location.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| 0 | Loads executable files without warning. This option maintains legacy behavior, but is not recommended. |
| 1 | Loads executable files only if their location is in the trusted locations specified in the TRUSTEDPATHS system variable. Displays a warning during load requests from executable files that are not in trusted locations. |
| 2 | Allows executable files to be loaded only if their location is in the trusted locations specified in the TRUSTEDPATHS system variable. |

The executable file types affected by SECURELOAD include the following:

Windows
:   * ARX, DBX, CRX, HDI files
    * LSP, FAS, VLX, MNL, SCR files
    * .NET assemblies
    * VBA macros (DVB files)
    * *acad.rx*
    * JavaScript
    * DLL files

Mac OS
:   * BUNDLE, CRX, DBX files
    * LSP, FAS, MNL, SCR files

NOTE:The ACADLSPASDOC system variable determines whether the
*acad.lsp* file is loaded into every drawing or just the first drawing opened in a session. AutoLISP files must be located in the Support
File Search Path to be found, or else a relative path must be included in the Filename parameter when using the LOAD function.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*