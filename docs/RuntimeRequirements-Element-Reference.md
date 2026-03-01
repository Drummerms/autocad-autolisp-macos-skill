# RuntimeRequirements Element Reference

The
RuntimeRequirements element is recommended and is used to control which operating systems, platforms, releases, and languages the
ApplicationPackage,
Components, and
ComponentEntry elements apply to.

If the element is not included, it is assumed that all components are compatible with all supported AutoCAD-based products
and AutoCAD LT releases, and operating systems.

NOTE:Although this element is optional, it is possible that the plug-in might be installed on Mac OS or another platform that the
plug-in was not originally tested on. Therefore, it is recommended that the element is used to control when the plug-in can
be loaded.

A
RuntimeRequirements element can have any of the following attributes attached to it:

| Attribute | Description |
| OS | Target operating system.  Supported values are ‘Mac’, ‘Win32’, or ‘Win64’. If omitted, it is assumed the plug-in supports all operating systems. Multiple operating systems can be specified by separating the values with the '|' symbol. (e.g. OS="Win32|Win64")  NOTE:AutoLISP applications, .NET applications, and CUIx files can be used across multiple operating systems. |
| Platform | Target AutoCAD-based products and AutoCAD LT.  Should be used when using APIs specific to one of the AutoCAD-based products or AutoCAD LT that might not available in all products. Multiple platforms can be specified by separating the values with the '|' symbol.  Valid values are:   * *ACADE* - AutoCAD Electrical * *ACADM* - AutoCAD Mechanical * *ACADLT* - AutoCAD LT * *ADT* - Architectural Desktop * *AIP* - Inventor Professional * *AIPRS* - Inventor Professional for Routed Systems * *AIPSIM* - Inventor Professional for Simulation * *AIS* - Inventor Series * *AOEM* - AutoCAD OEM * *AutoCAD* - AutoCAD * *AutoCAD\** - All AutoCAD-based products * *Civil* - Autodesk Civil * *Civil3D* - Autodesk Civil 3D * *LDT* - Land Desktop * *Map* - AutoCAD Map 3D * *MEP* - AutoCAD MEP * *Plant3D* - AutoCAD Plant 3D * *PNID* - AutoCAD P & ID - 2D |
| SeriesMin | Defines the minimum product release number that the set of components supports.  The value can be a major version number (R24) or a specific version (R24.1). The version number can be found in the Windows Registry or obtained with the ACADVER system variable in AutoCAD-based products.  If this attribute and SeriesMax are not specified, it is assumed all components are compatible with all product releases. If you omit this value, any version before that specified by the SeriesMax attribute is allowed. |
| SeriesMax | Defines the maximum product release number that the set of components supports.  If you omit this value, any version after that specified by the SeriesMin attribute is allowed. |
| SupportPath | List of support paths used by this set of components separated by a semicolon. The support paths should be relative to the plug-in bundle.  Localized support paths can be specified by combining SupportPath with a locale code. |
| ToolPalettePath | List of tool palette paths used by this set of components separated by a semicolon. The tool palette paths should be relative to the plug-in bundle.  Localized tool palette paths can be specified by combining ToolPalettePath with a locale code. |

#### Related References

* [ApplicationPackage Element Reference](ApplicationPackage-Element-Reference.md)
* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [Components Element Reference](Components-Element-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*