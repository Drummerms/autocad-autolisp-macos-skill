# Object-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP object-handling functions.

| Object-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(dumpallproperties ename [context])](dumpallproperties-AutoLISP.md) | Retrieves an entity’s supported properties | ✓ | ✓ | ✓ | -- | -- |
| [(entdel ename)](entdel-AutoLISP.md) | Deletes objects (entities) or restores previously deleted objects | ✓ | ✓ | ✓ | -- | ✓ |
| [(entget ename [applist])](entget-AutoLISP.md) | Retrieves an object's definition data | ✓ | ✓ | ✓ | -- | ✓ |
| [(entlast)](entlast-AutoLISP.md) | Returns the name of the last non-deleted main object in the drawing | ✓ | ✓ | ✓ | -- | ✓ |
| [(entmake [elist])](entmake-AutoLISP.md) | Creates a new entity (graphical object) in the drawing | ✓ | / - supported objects are limited | ✓ | -- | ✓ |
| [(entmakex [elist])](entmakex-AutoLISP.md) | Makes a new object, gives it a handle and entity name (but does not assign an owner), and then returns the new entity name | ✓ | / - supported objects are limited | ✓ | -- | ✓ |
| [(entmod elist)](entmod-AutoLISP.md) | Modifies the definition data of an object | ✓ | / - supported objects are limited | ✓ | -- | ✓ |
| [(entnext [ename])](entnext-AutoLISP.md) | Returns the name of the next object in the drawing | ✓ | ✓ | ✓ | -- | ✓ |
| [(entupd ename)](entupd-AutoLISP.md) | Updates the screen image of an object | ✓ | ✓ | ✓ | -- | ✓ |
| [(getpropertyvalue ename propertyname [or collectionName index name])](getpropertyvalue-AutoLISP.md) | Returns the current value of an entity’s property | ✓ | ✓ | ✓ | -- | -- |
| [(handent handle)](handent-AutoLISP.md) | Returns an object name based on its handle | ✓ | ✓ | ✓ | -- | ✓ |
| [(ispropertyreadonly ename propertyname [or collectionName index name])](ispropertyreadonly-AutoLISP.md) | Returns the read-only state of an entity’s property | ✓ | ✓ | ✓ | -- | -- |
| [(setpropertyvalue ename propertyname value [or collectionname index name val])](setpropertyvalue-AutoLISP.md) | Sets the property value for an entity | ✓ | ✓ | ✓ | -- | -- |
| [(vlax-dump-object obj)](vlax-dump-object-AutoLISP-ActiveX.md) | Lists an object's methods and properties  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-erased-p obj)](vlax-erased-p-AutoLISP-ActiveX.md) | Determines whether an object was erased  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-get-acad-object)](vlax-get-acad-object-AutoLISP-ActiveX.md) | Retrieves the top-level AutoCAD application object for the current AutoCAD session  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-method-applicable-p obj method)](vlax-method-applicable-p-AutoLISP-ActiveX.md) | Determines whether an object supports a particular method  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-object-released-p obj)](vlax-object-released-p-AutoLISP-ActiveX.md) | Determines whether an object has been released  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-read-enabled-p obj)](vlax-read-enabled-p-AutoLISP-ActiveX.md) | Determines whether an object can be read  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-release-object obj)](vlax-release-object-AutoLISP-ActiveX.md) | Releases a drawing object  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-typeinfo-available-p obj)](vlax-typeinfo-available-p-AutoLISP-ActiveX.md) | Determines whether type library information is present for the specified type of object  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-write-enabled-p obj)](vlax-write-enabled-p-AutoLISP-ActiveX.md) | Determines whether an AutoCAD drawing object can be modified  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*