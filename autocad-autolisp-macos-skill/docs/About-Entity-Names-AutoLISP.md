# About Entity Names (AutoLISP)

An entity name is a numeric label assigned to objects in a drawing.

It is actually a pointer into a file maintained by AutoCAD, and can be used to find the object's database record and its vectors
(if they are displayed). This label can be referenced by AutoLISP functions to allow selection of objects for processing in
various ways. Internally, AutoCAD refers to objects as entities.

NOTE:You can use the
vlax-ename->vla-object function to convert an entity name to a VLA-object when working with ActiveX functions. The
vlax-vla-object->ename function converts a VLA-object to an entity name. ActiveX is not supported on Mac OS and Web.

The following functions are useful when working with entity names:

* entget - Retrieves an object's (entity's) definition data.
* entlast - Returns the name of the last non-deleted main object (entity) in the drawing.
* ssname - Returns the object (entity) name of the indexed element of a selection set.
* entsel - Prompts the user to select a single object (entity) by specifying a point.
* nentsel - Prompts the user to select an object (entity) by specifying a point, and provides access to the definition data contained
  within a complex object.
* nentselp - Provides similar functionality to that of the
  nentsel function without the need for user input.
* handent - Returns an object (entity) name based on its handle.

The following example uses the
entlast function to get the name of the last object created in the drawing.

```
(entlast)
<Entity name: 27f0540>
```

Entity names assigned to objects in a drawing are only in effect during the current editing session. The next time you open
the drawing, AutoCAD assigns new entity names to the objects. You can use an object's handle to refer to it from one editing
session to another.

#### Related Concepts

* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*