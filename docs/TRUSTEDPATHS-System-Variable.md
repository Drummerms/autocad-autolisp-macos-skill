# TRUSTEDPATHS (System Variable)

Specifies the folders from which AutoCAD has permission to load and execute files that contain code.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Registry |
| Initial value: | Varies |

To minimize the possibility of loading and executing malicious code, always set the TRUSTEDPATHS system variable to unique,
read-only folders where your authorized applications are located. This includes the following file types:

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

NOTE:The AutoCAD install folder, the
*ApplicationPlugins* (Windows) or
*ApplicationAddins* (Mac OS) folder, and all their subfolders are always implicitly trusted.

Valid strings include the following:

* When TRUSTEDPATHS is set to one or more folder paths in quotes and separated by semicolons, the previously listed file types
  are loaded from the specified folders.
* When TRUSTEDPATHS is set to "" (an empty string) or "." (a period), there are no trusted folder paths in addition to the implicitly
  trusted ones.
* When TRUSTEDPATHS includes a folder that ends with \... (backslash and three dots) or /... (backslash and three dots), all
  of its subfolders are also trusted.

NOTE:When using AutoLISP, note that TRUSTEDPATHS does not
*add* a path to the Support File Search Path. It simply provides
*permission* use to an existing support path. Thus, an AutoLISP file must be located in a path listed in the Support File Search Path.
In some circumstances, it might be more convenient to specify the relative file path in the
*Filename* parameter when using the LOAD function.

The setting of the SECURELOAD system variable determines whether other locations, including the current drawing folder, are
trusted. Signed DLLs are automatically trusted on Windows only.

NOTE:Beginning with AutoCAD 2013 SP1 on Windows and AutoCAD 2014 for Mac, the reserved
*acad<release>.lsp* and
*acad<release>doc.lsp* files and their successors are loaded only from their default installation folders:
*<install folder>/Support and <install folder>/Support/<language>* respectively.
*<release>* is a numeric value of four digits. For example, 2013 for AutoCAD 2013, 2014 for AutoCAD 2014, and so on.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*