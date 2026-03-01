# Example: Using Folders to Organize Components for a Plug-in

This example reflects what a package for a plug-in might look like using folders to organize components.

It is recommended to use an organized folder structure for larger applications as this can significantly speed up load times.
The following is an example of a plug-in that contains multiple LSP files and resource files. The plug-in in this example
is named OfficeSymbols and its folder structure might look something like:

*OfficeSymbols.bundle*

  |- PackageContents.xml

  |- *Contents*

      |- OfficeSymbolsMain.lsp

      |- OfficeSymbolsUtilities.lsp

      |- *Resources*

          |- OfficeSymbols.dwg

          |- OfficeSymbols.cuix

          |- OfficeSymbols.ico

      |- *Help*

          |- OfficeSymbols.htm

## Definition of the PackageContents.xml

```
<?xml version="1.0" encoding="utf-8" ?>
<ApplicationPackage
    SchemaVersion="1.0"
    AppVersion="1.0"
    Author="ABC Indoor CAD, Inc."
    ProductCode="[Add Unique Plug-in GUID Here]"
    Name="Office Symbols (contains Full version)"
    Icon="./Contents/Resources/OfficeSymbols.ico"
    Helpfile="./Contents/Help/OfficeSymbols.htm"
>

  <CompanyDetails
    Name="ABC Indoor CAD, Inc."
    Phone="1 (555)-415-1234"
    PhoneEsp="34 5554 151234"
    Url="www.abcindoorcad.com"
    UrlEsp="www.abcindoorcad.es"
    Email="support@abcindoorcad.com"
  />

  <Components>
    <RuntimeRequirements SupportPath="./Contents/Support"/>
    <ComponentEntry
      AppName="MainLISP"
      ModuleName="./Contents/OfficeSymbolsMain.lsp"
    />
    <ComponentEntry
      AppName="UtilitiesLISP"
      ModuleName="./Contents/OfficeSymbolsUtilities.lsp"
    />
    <ComponentEntry
      ModuleName="./Contents/Resources/OfficeSymbols.cuix"
    />
  </Components>
</ApplicationPackage>
```

#### Related References

* [Example: Basic .bundle Folder Structure for a Plug-in](Example-Basic-.bundle-Folder-Structure-for-a-Plug-in.md)
* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*