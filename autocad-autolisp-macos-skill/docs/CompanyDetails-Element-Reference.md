# CompanyDetails Element Reference

The
CompanyDetails element is used to specify information about the company that created the plug-in.

The
CompanyDetails element is required when releasing a plug-in through the Autodesk App Store website. You must also populate each of the attributes
for the
CompanyDetails element.

NOTE:For plug-in bundles that target AutoCAD LT for Windows, you can exclude the
CompanyDetails element since plug-in bundles are supported only for local deployment.

A
CompanyDetails element can have any of the following attributes attached to it:

| Attribute | Description |
| Name | Name of the developer or company that authored the plug-in. |
| Phone | Phone number of the developer or company of the plug-in.  International phone numbers can be specified by combining Phone with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |
| URL | Web site for the developer or company of the plug-in.  Localized Web site can be specified by combining URL with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |
| Email | Developer or company contact email address for the plug-in.  An international contact email address can be specified by combining Email with a locale code. See Supported Locale Codes Reference for a full list of supported locale codes. |

#### Related References

* [PackageContents.xml Format Reference](PackageContents.xml-Format-Reference.md)
* [Supported Locale Codes Reference](Supported-Locale-Codes-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*