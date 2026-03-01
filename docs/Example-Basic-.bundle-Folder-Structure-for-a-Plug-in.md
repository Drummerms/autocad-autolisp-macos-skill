# Example: Basic .bundle Folder Structure for a Plug-in

This example reflects what a package for a plug-in might contain and how it is structured on disk.

*.bundle* is not a file, but a folder name with a BUNDLE extension. The following is an example of a plug-in that contains a LSP file
as the main program and a DWG support file. The following plug-in example is named OfficeSymbols and its folder structure
might look something like; folders are in bold:

*OfficeSymbols.bundle*

  |- PackageContents.xml

  |- *Contents*

      |- OfficeSymbolsUtilities.lsp

      |- *Resources*

            |- OfficeSymbols.dwg

            |- OfficeSymbols.ico

            |- OfficeSymbols.htm

| File name | Description |
| *OfficeSymbols.bundle* | The folder containing the files for a plug-in and has the BUNDLE extension. |
| *PackageContents.xml* | XML file that contains metadata about the plug-in. |
| *OfficeSymbolsUtilities.lsp* | Example of a custom application file that might define the behavior of the plug-in.  An application file can be an AutoLISP, ObjectARX, or .NET assembly file.  NOTE:AutoCAD LT doesn't support ObjectARX and .NET assembly files. |
| *OfficeSymbols.dwg* | DWG file that contains symbols used by the functionality defined in *OfficeSymbolsUtilities.lsp*. |
| *OfficeSymbols.ico* | Icon used by the App Manager and Autodesk App Store website. |
| *OfficeSymbols.htm* | Help documentation for the plug-in. Can be a redirect to where the documentation might be stored on the local drive or an online location. |

## Definition of the PackageContents.xml

```
<?xml version="1.0" encoding="utf-8" ?>
<ApplicationPackage SchemaVersion="1.0" AppVersion="1.0"
    ProductCode="[Add Unique Plug-in GUID Here]"
    Name="Office Symbols"
    Icon="./Contents/Resources/OfficeSymbols.ico"
    Helpfile="./Contents/Resources/OfficeSymbols.htm"
>

  <CompanyDetails
    Name="ABC Indoor CAD, Inc."
    Email="support@abcindoorcad.com"
  />

  <Components>
    <ComponentEntry
      ModuleName="./Contents/LISP/OfficeSymbolsUtilities.lsp"
    />
  </Components>
</ApplicationPackage>
```

#### Related References

* [Example: Using Folders to Organize Components for a Plug-in](Example-Using-Folders-to-Organize-Components-for-a-Plug-in.md)
* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*