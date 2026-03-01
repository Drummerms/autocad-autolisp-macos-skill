# dumpallproperties (AutoLISP)

Retrieves an entity’s supported properties

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(dumpallproperties ename [context])
```

*ename*
:   *Type:* Ename (entity name)

    Name of the entity being queried. The
    *ename* can refer to either a graphical or nongraphical entity.

*context*
:   *Type:* Integer

    Value expected is 0 or 1, the default is 0 when a value is not provided. When 1 is provided as the context, some property
    values such as Position, Normal, and StartPoint are promoted from a single value to individual
    *X*,
    *Y*, and
    *Z* values.

    For example, the following displays the StartPoint first as not being promoted and then being as promoted:

    * Not promoted, context = 0

      ```
      StartPoint (type: AcGePoint3d)  (LocalName: StartPoint) = 6.250000   8.750000  0.000000
      ```
    * Promoted, context = 1

      ```
      StartPoint/X (type: double)  (LocalName: Start X) = 6.250000
      StartPoint/Y (type: double)  (LocalName: Start Y) = 8.750000
      StartPoint/Z (type: double)  (LocalName: Start Z) = 0.000000
      ```

## Return Values

*Type:* Nil

nil is returned by the function while the properties and their current values are output to the Command Line history.

## Examples

The following example demonstrates how to list the available properties for a line object with the properties Delta, EndPoint,
Normal, and StartPoint promoted to individual values.

```
Command: (setq e1 (car (entsel "\
Select a line: ")))
Select a line:
<Entity name: 10e2e4b20>
Command: (dumpAllProperties e1 1)

Begin dumping object (class: AcDbLine)
Angle (type: double)  (RO)  (LocalName: Angle) = 5.159347
Annotative (type: bool)  (LocalName: Annotative) = Failed to get value to get value
Area (type: double)  (RO)  (LocalName: Area) = 0.000000
BlockId (type: AcDbObjectId)  (RO) = Ix
CastShadows (type: bool) = 0
ClassName (type: AcString)  (RO) =
Closed (type: bool)  (RO)  (LocalName: Closed) = Failed to get value
CollisionType (type: AcDb::CollisionType)  (RO) = 1
Color (type: AcCmColor)  (LocalName: Color) = BYLAYER
Delta/X (type: double)  (RO)  (LocalName: Delta X) = 3.028287
Delta/Y (type: double)  (RO)  (LocalName: Delta Y) = -6.318026
Delta/Z (type: double)  (RO)  (LocalName: Delta Z) = 0.000000
EndParam (type: double)  (RO) = 7.006281
EndPoint/X (type: double)  (LocalName: End X) = 23.249243
EndPoint/Y (type: double)  (LocalName: End Y) = 11.968958
EndPoint/Z (type: double)  (LocalName: End Z) = 0.000000
ExtensionDictionary (type: AcDbObjectId)  (RO) = Ix
Handle (type: AcDbHandle)  (RO) = 1b2
HasFields (type: bool)  (RO) = 0
HasSaveVersionOverride (type: bool) = 0
Hyperlinks (type: AcDbHyperlink*)
IsA (type: AcRxClass*)  (RO) = AcDbLine
IsAProxy (type: bool)  (RO) = 0
IsCancelling (type: bool)  (RO) = 0
IsEraseStatusToggled (type: bool)  (RO) = 0
IsErased (type: bool)  (RO) = 0
IsModified (type: bool)  (RO) = 0
IsModifiedGraphics (type: bool)  (RO) = 0
IsModifiedXData (type: bool)  (RO) = 0
IsNewObject (type: bool)  (RO) = 0
IsNotifyEnabled (type: bool)  (RO) = 0
IsNotifying (type: bool)  (RO) = 0
IsObjectIdsInFlux (type: bool)  (RO) = 0
IsPeriodic (type: bool)  (RO) = 0
IsPersistent (type: bool)  (RO) = 1
IsPlanar (type: bool)  (RO) = 1
IsReadEnabled (type: bool)  (RO) = 1
IsReallyClosing (type: bool)  (RO) = 1
IsTransactionResident (type: bool)  (RO) = 0
IsUndoing (type: bool)  (RO) = 0
IsWriteEnabled (type: bool)  (RO) = 0
LayerId (type: AcDbObjectId)  (LocalName: Layer) = Ix
Length (type: double)  (RO)  (LocalName: Length) = 7.006281
LineWeight (type: AcDb::LineWeight)  (LocalName: Lineweight) = -1
LinetypeId (type: AcDbObjectId)  (LocalName: Linetype) = Ix
LinetypeScale (type: double)  (LocalName: Linetype scale) = 1.000000
LocalizedName (type: AcString)  (RO) = Line
MaterialId (type: AcDbObjectId)  (LocalName: Material) = Ix
MergeStyle (type: AcDb::DuplicateRecordCloning)  (RO) = 1
Normal/X (type: double) = 0.000000
Normal/Y (type: double) = 0.000000
Normal/Z (type: double) = 1.000000
ObjectId (type: AcDbObjectId)  (RO) = Ix
OwnerId (type: AcDbObjectId)  (RO) = Ix
PlotStyleName (type: AcString)  (LocalName: Plot style) = ByLayer
ReceiveShadows (type: bool) = 0 Failed to get value
StartParam (type: double)  (RO) = 0.000000
StartPoint/X (type: double)  (LocalName: Start X) = 20.220956
StartPoint/Y (type: double)  (LocalName: Start Y) = 18.286984
StartPoint/Z (type: double)  (LocalName: Start Z) = 0.000000
Thickness (type: double)  (LocalName: Thickness) = 0.000000
Transparency (type: AcCmTransparency)  (LocalName: Transparency) = 0
Visible (type: AcDb::Visibility) = 0
End object dump
```

#### Related References

* [getpropertyvalue (AutoLISP)](getpropertyvalue-AutoLISP.md)
* [setpropertyvalue (AutoLISP)](setpropertyvalue-AutoLISP.md)
* [ispropertyreadonly (AutoLISP)](ispropertyreadonly-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*