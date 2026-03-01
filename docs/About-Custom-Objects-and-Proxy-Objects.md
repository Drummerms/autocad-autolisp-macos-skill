# About Custom Objects and Proxy Objects

Custom objects provide additional capabilities to the program and related products. When the application that created the
custom object is not available, a proxy object is substituted in its place.

A custom object is a type of object created by an ObjectARX ®  (AutoCAD Run-Time Extension) application, which typically has more specialized capabilities than standard AutoCAD or AutoCAD
LT objects. Custom objects include parametric solids (AutoCAD ®  Mechanical), intelligently interactive door symbols (AutoCAD ®  Architecture), polygon objects (AutoCAD ®  Map 3D), and associative dimension objects (AutoCAD and AutoCAD LT).

In addition to Autodesk, many software vendors use ObjectARX to write programs that create graphical and nongraphical custom
objects that are useful in their AutoCAD based applications.

## Proxy Objects

A proxy object is a substitute for a custom object when the ObjectARX application that created the custom object is not available
to AutoCAD, AutoCAD LT, or other host applications. Later, when the application is available, the proxy object is replaced
by the custom object.

Proxy objects have significantly reduced capabilities compared to their corresponding custom objects. The extent to which
proxy objects can be edited is determined by the parent ObjectARX application. For example, operations such as erasing and
moving an object, or changing object properties, may or may not be possible on a proxy object, depending on the application
that created it.

When you open a drawing, you might see a message listing the total number of proxy objects in the drawing (both graphical
and nongraphical) and the name of the missing application and provides additional information about the proxy object type
and display state.

## Object Enablers

An object enabler is a tool that provides specific viewing and standard editing access to a custom object in the host applications
when the application that created the custom object is not present.

Object Enablers allow custom objects in a drawing to behave with more intelligence than proxy graphics. Object enablers also
facilitate workgroup collaboration when using other Autodesk products.

To search for currently available Object Enablers, go to
<https://www.autodesk.com/enablers>.

NOTE:Object enablers are not supplied for AutoCAD for Mac. The object enabler for AutoCAD Architecture is integrated into AutoCAD
for Mac.

#### Related Concepts

* [About Saving Drawings to Previous Drawing File Formats](About-Saving-Drawings-to-Previous-Drawing-File-Formats.md)

#### Related Information

* [To Save Drawings With Visual Fidelity for Annotative Objects](To-Save-Drawings-With-Visual-Fidelity-for-Annotative-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*