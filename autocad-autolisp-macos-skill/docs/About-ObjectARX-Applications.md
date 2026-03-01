# About ObjectARX Applications

ObjectARX® (AutoCAD Runtime Extension) is a compiled-language programming environment for developing applications that allow you to
load and run compiled projects in the same address space as AutoCAD-based products, enabling your programs to operate directly
with core AutoCAD data structures and code.

The ObjectARX libraries allow you to take advantage of the open architecture of AutoCAD-based products, providing direct
access to the database structures, graphics system, and geometry engine to extend classes and capabilities at runtime. Additionally,
you can define new commands that operate exactly the same way as native commands and new AutoLISP functions.

You can use ObjectARX libraries in conjunction with other programming interfaces supported by the AutoCAD-based product, such
as AutoLISP, ActiveX, or Managed .NET, enabling cross-API integration.

NOTE:ActiveX and Managed .NET are supported on Windows only.

ObjectARX applications require knowledge of C++ or Objective-C, and an integrated development environment (IDE), such as Microsoft
Visual Studio on Windows or Xcode on Mac OS. Unlike AutoLISP applications, you must compile an ObjectARX application before
it can be loaded into an AutoCAD-based product. A compiled ObjectARX application is a Dynamic-Link Library file with an
*.arx* extension. Debugging of an ObjectARX application can be performed from Microsoft Visual Studio or Xcode when a debug version
of an ObjectARX application is loaded into an AutoCAD-based product.

Once an ObjectARX application file has been debugged and is ready to be used by other users, a release version of the ObjectARX
application must be built.

#### Topics in this section

* [About Loading ObjectARX Applications](About-Loading-ObjectARX-Applications.md)

  An ObjectARX application must be loaded before you can use any of its defined commands or functions.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Loading ObjectARX Applications](About-Loading-ObjectARX-Applications.md)
* [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*