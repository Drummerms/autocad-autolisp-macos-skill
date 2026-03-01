# PackageContents.xml Format Reference

The
*PackageContents.xml* file contains information about the application package, including information about the developer that authored it.

NOTE:Plug-in bundles are not supported in AutoCAD LT for Mac.

The information contained in the file can be used to specify which AutoCAD-based products and AutoCAD LT, and which releases
a plug-in can be loaded into, their supported operating system, and how the application should be loaded, such as load on
startup or when a command is invoked.

The following elements are used to define and describe the plug-in:

* ApplicationPackage
* CompanyDetails
* Components

## PackageContents.xml for Download versus Local Deployment

How you plan to deploy your plug-in determines what should be in the
*PackageContents.xml* file. You need to supply more information when providing a plug-in for download versus a local deployment. The following
table explains which elements and attributes are required, optional, or recommended for the deployment you want to use.

NOTE:AutoCAD LT for Windows only supports plug-in bundles for local deployment.

|  | For Download from the Autodesk App Store Website | For Local Deployment | Supported Releases | Additional Comments |
| ApplicationPackage element | | | AutoCAD 2013-based products and later  AutoCAD LT 2024 and later |  |
| SchemaVersion | Required | Required |  |  |
| AppVersion | Required | Required |  |  |
| Author | Required | Optional |  |  |
| Name | Required | Recommended |  |  |
| Description | Required | Recommended |  |  |
| Icon | Required | Recommended |  |  |
| Helpfile | Required | Recommended |  |  |
| ProductCode | Required | Required |  |  |
| UpgradeCode | Required | Optional |  |  |
| CompanyDetails element | | | AutoCAD 2013-based products and later  AutoCAD LT 2024 and later |  |
| Name | Required | Optional |  |  |
| Phone | Optional | Optional |  |  |
| URL | Optional | Optional |  |  |
| Email | Required | Optional |  |  |
| RuntimeRequirements element – Required, if a Components element is present | | | AutoCAD 2013-based products and later  AutoCAD LT 2024 and later |  |
| OS | Optional | Optional |  |  |
| Platform | Optional | Optional |  |  |
| SeriesMin | Optional | Optional |  |  |
| SeriesMax | Optional | Optional |  |  |
| SupportPath | Optional | Optional |  |  |
| ToolPalettePath | Optional | Optional |  |  |
| ComponentEntry element – Required, if a Components element is present | | | AutoCAD 2013-based products and later  AutoCAD LT 2024 and later |  |
| AppName | Required | Required |  |  |
| AppDescription | Optional | Optional |  |  |
| AppType | Optional | Optional |  | Required to load an ARX file from a bundle into AutoCAD for Mac. |
| ModuleName | Required | Required |  |  |
| PerDocument | Optional | Optional |  |  |
| LoadReasons | Optional | Optional |  |  |
| Commands element | | | AutoCAD 2013-based products and later |  |
| GroupName | Required | Optional |  |  |
| Command element – Required, if a Commands element is present | | | AutoCAD 2013-based products and later  AutoCAD LT 2024 and later |  |
| Global | Required | Required |  |  |
| Local | Required | Required |  |  |
| HelpTopic | Optional | Optional |  |  |
| StartupCommand | Optional | Optional |  |  |
| AssemblyMapping element – Optional, but is required if an AssemblyMappings element is present and it doesn't contain an AssemblyMappingFolder element | | | AutoCAD 2013-based products and later |  |
| Name | Optional | Optional |  |  |
| Path | Optional | Optional |  |  |
| AssemblyMappingFolder element – Optional, but is required if an AssemblyMappings element is present and it doesn't contain an AssemblyMapping element | | | AutoCAD 2022-based products |  |
| Path | Optional | Optional |  |  |
| RegistryEntry element – Required, if a RegistryEntries element is present | | | AutoCAD 2015-based products and later  AutoCAD LT 2024 and later |  |
| Name | Optional | Optional |  |  |
| Value | Optional | Optional |  |  |
| Flags | Optional | Optional |  |  |
| SystemVariable element – Required, if a SystemVariables element is present | | | AutoCAD 2015-based products and later  AutoCAD LT 2024 and later |  |
| Name | Optional | Optional |  |  |
| Value | Optional | Optional |  |  |
| PrimaryType | Optional | Optional |  |  |
| StorageType | Optional | Optional |  |  |
| Owner | Optional | Optional |  |  |
| Flags | Optional | Optional |  |  |
| EnvironmentVariable element – Required, if an EnvironmentVariables element is present | | | AutoCAD 2015-based products and later  AutoCAD LT 2024 and later |  |
| Name | Optional | Optional |  |  |
| Value | Optional | Optional |  |  |
| Type | Optional | Optional |  |  |
| Flags | Optional | Optional |  |  |
| Dependency element – Required, if a Dependencies element is present | | | AutoCAD 2022-based products and later  AutoCAD LT 2024 and later |  |
| UpgradeCode | Optional | Optional |  |  |
| Optional | Optional | Optional |  |  |
| VersionMin | Optional | Optional |  |  |
| VersionMax | Optional | Optional |  |  |

#### Topics in this section

* [Supported Locale Codes Reference](Supported-Locale-Codes-Reference.md)

  AutoCAD-based products and AutoCAD LT are localized into a wide range of languages and the structure of the
  PackageContents.xml file supports these different languages with locale codes.
* [ApplicationPackage Element Reference](ApplicationPackage-Element-Reference.md)

  Each
  PackageContents.xml file must contain an
  ApplicationPackage element. The
  ApplicationPackage element, in the form of XML attributes, contains general information about the plug-in. It also encapsulates
  other element types that help to define the contents of the plug-in.
* [CompanyDetails Element Reference](CompanyDetails-Element-Reference.md)

  The
  CompanyDetails element is used to specify information about the company that created the plug-in.
* [Dependencies Element Reference](Dependencies-Element-Reference.md)

  The
  Dependencies element is used to specify which plug-in bundles must be available in order for another plug-in bundle to load.
* [Components Element Reference](Components-Element-Reference.md)

  The
  Components element is used to specify the components that make up one version of the plug-in.
* [RuntimeRequirements Element Reference](RuntimeRequirements-Element-Reference.md)

  The
  RuntimeRequirements element is recommended and is used to control which operating systems, platforms, releases, and languages
  the
  ApplicationPackage,
  Components, and
  ComponentEntry elements apply to.
* [Example: Basic .bundle Folder Structure for a Plug-in](Example-Basic-.bundle-Folder-Structure-for-a-Plug-in.md)

  This example reflects what a package for a plug-in might contain and how it is structured on disk.
* [Example: Using Folders to Organize Components for a Plug-in](Example-Using-Folders-to-Organize-Components-for-a-Plug-in.md)

  This example reflects what a package for a plug-in might look like using folders to organize components.

#### Related References

* [ApplicationPackage Element Reference](ApplicationPackage-Element-Reference.md)
* [CompanyDetails Element Reference](CompanyDetails-Element-Reference.md)
* [RuntimeRequirements Element Reference](RuntimeRequirements-Element-Reference.md)
* [Components Element Reference](Components-Element-Reference.md)
* [Example: Basic .bundle Folder Structure for a Plug-in](Example-Basic-.bundle-Folder-Structure-for-a-Plug-in.md)
* [Example: Using Folders to Organize Components for a Plug-in](Example-Using-Folders-to-Organize-Components-for-a-Plug-in.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

#### Related Information

* [Dependencies Element Reference](Dependencies-Element-Reference.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*