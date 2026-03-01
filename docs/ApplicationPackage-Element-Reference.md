# ApplicationPackage Element Reference

Each
*PackageContents.xml* file must contain an
ApplicationPackage element. The
ApplicationPackage element, in the form of XML attributes, contains general information about the plug-in. It also encapsulates other element
types that help to define the contents of the plug-in.

An
ApplicationPackage element can have any of the following attributes attached to it:

| Attribute | Description |
| SchemaVersion | *PackageContents.xml* format version number. The value should always be 1.0 until a newer version of the schema is introduced. |
| AppVersion | Application version number. AutoCAD-based products and AutoCAD LT use this value to determine if the installed version is the latest version. If an updated version is available, the user is informed and able to download and install the latest version. It is recommended to use an application version that includes major and minor values, such as “1.0.0.0”. |
| Author | Name of the plug-in author. |
| Name | Plug-in name.  A localized plug-in name can be specified by combining Name with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |
| Description | Short description of the plug-in.  Localized descriptions can be specified by combining Description with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |
| Icon | Icon for the plug-in; used in the App Manager, installer and the Autodesk App Store website.  The icon should be 32x32 pixels in size and support 32-bit (Truecolor) color depth. Recommend using a BMP or ICO file format.  NOTE:All path specifiers are '/' and not '\', and paths are relative to the root *.bundle* folder. |
| HelpFile | Help file that explains how to use the plug-in and provides additional information about the plug-in.  It is recommended to create a How To section that explains how to use the plug-in. The file can be an ASCII text, a HTML document, or PDF file that contains the full documentation for the plug-in or contains a set of redirects to where the content might be located online.  Localized help files can be specified by combining HelpFile with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes.  NOTE:All path specifiers are '/' and not '\', and paths are relative to the root *.bundle* folder. |
| ProductCode | Unique GUID for the plug-in. A GUID must be generated for each unique plug-in, and is used for first run notifications and as the installer ID for Add/Remove Programs in Windows when installed from the Autodesk App Store website.  ProductCode should be updated if the AppVersion is changed. This is so upgrade installs work properly and a notification is displayed for the upgrade when loaded into an AutoCAD-based product or AutoCAD LT.  On Windows, you can use the MSI installer ProductCode or generate a GUID using an application such as GuidGen.exe. There are also websites that allow you to generate a GUID. |
| UpgradeCode | Unique GUID for the plug-in that must never be changed. The GUID is used by the Autodesk App Store website to allow for upgrading from an old version to a newer version of a plug-in without the need to uninstall the plug-in first.  NOTE:You must increment AppVersion in order to allow for proper upgrading of a plug-in. |

An
ApplicationPackage element can contain, or encapsulate, the following elements:

* CompanyDetails
* Components
* DependentBundles
* RuntimeRequirements

IMPORTANT:For the plug-in bundle to work properly with AutoCAD LT, the
RuntimeRequirements element is required. This will also work for AutoCAD-based products.

#### Related References

* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [CompanyDetails Element Reference](CompanyDetails-Element-Reference.md)
* [Components Element Reference](Components-Element-Reference.md)
* [RuntimeRequirements Element Reference](RuntimeRequirements-Element-Reference.md)
* [Supported Locale Codes Reference](Supported-Locale-Codes-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

#### Related Information

* [Dependencies Element Reference](Dependencies-Element-Reference.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*