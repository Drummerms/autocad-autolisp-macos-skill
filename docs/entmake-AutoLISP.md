# entmake (AutoLISP)

Creates a new entity in the drawing

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entmake [elist])
```

*elist*
:   *Type:* List (dotted pairs)

    Entity definition data in a format similar to that returned by the
    entget function. The
    *elist* argument must contain all of the information necessary to define the entity. If any required definition data is omitted,
    entmake returns
    nil and the entity is rejected. If you omit optional definition data (such as the layer),
    entmake uses the default value.

    The entity type (for example,
    CIRCLE or
    LINE) must be the first or second field of the
    *elist*. If entity type is the second field, it can be preceded only by the entity name. The
    entmake function ignores the entity name when creating the new entity. If the
    *elist* contains an entity handle,
    entmake ignores that too.

## Return Values

*Type:* List (dotted pairs)

If successful,
entmake returns the entity's list of definition data. If
entmake is unable to create the entity, it returns
nil.

Completion of a block definition (entmake of an endblk) returns the block's name rather than the entity data list normally returned.

## Remarks

The
entmake function can define both graphical and nongraphical entities.

You cannot create viewport objects with
entmake and a number of objects are not supported by
entmake in AutoCAD LT; see the Objects Not Supported By
entmake in AutoCAD LT section for a list of the objects that are not supported.

A group 66 code is honored only for insert objects (meaning
*attributes follow*). For polyline entities, the group 66 code is forced to a value of 1 (meaning
*vertices follow*), and for all other entities it takes a default of 0. The only entity that can follow a polyline entity is a vertex entity.

The group code 2 (block name) of a dimension entity is optional for the
entmake function. If the block name is omitted from the entity definition list, AutoCAD creates a new one. Otherwise, AutoCAD creates
the dimension using the name provided.

For legacy reasons,
entmake ignores DXF group code 100 data for the following entity types:

| * AcDb2dPolyline * AcDb2dVertex * AcDb3dPolyline * AcDb3dPolylineVertex * AcDbArc * AcDbAttribute * AcDbAttributeDefinition | * AcDbBlockBegin * AcDbBlockEnd * AcDbBlockReference * AcDbCircle * AcDbFace * AcDbFaceRecord * AcDbLine | * AcDbMInsertBlock * AcDbPoint * AcDbPolyFaceMesh * AcDbPolyFaceMeshVertex * AcDbPolygonMesh * AcDbPolygonMeshVertex | * AcDbSequenceEnd * AcDbShape * AcDbSolid * AcDbText * AcDbTrace * AcDbViewport |

NOTE:In AutoCAD 2004 and later releases, the
entmod function has a new behavior in color operations. DXF group code 62 holds AutoCAD Color Index (ACI) values, but code 420 holds
true color values. If the true color value and ACI value conflict, AutoCAD uses the 420 value, so the code 420 value should
be removed before attempting to use the code 62 value.

## Examples

The following code creates a green circle (group code 62 is for color, 3 is for green), centered at (4,4) with a radius of
1. The optional layer and linetype fields have been omitted and therefore assume default values.

```
(entmake '((0 . "CIRCLE") (62 . 3) (10 4.0 4.0 0.0) (40 . 1.0)))
((0 . "CIRCLE") (62 . 1) (10 4.0 4.0 0.0) (40 . 1.0))
```

## Objects Not Supported By entmake in AutoCAD LT

| Graphical Objects | | Nongraphgical Objects | |
| Class Name | DXF Name | Class Name | DXF Name |
| AcDb3dSolid | 3DSOLID | AcDbIBLBackground | RAPIDRTRENDERENVIRONMENT |
| AcDbAssocExternalPersSubentIdHolder | ACDBASSOCEXTERNALPERSSUBENTIDHOLDER | AcDbLightList | LIGHTLIST |
| AcDbCamera | CAMERA | AcDbMotionPath | ACDBMOTIONPATH |
| AcDbExtrudedSurface | EXTRUDEDSURFACE | AcDbMaterial | MATERIAL |
| AcDbFace | 3DFACE | AcDbMentalRayRenderSettings | MENTALRAYRENDERSETTINGS |
| AcDbHelix | HELIX | AcDbMlineStyle | MLINESTYLE |
| AcDbLight | LIGHT | AcDbNavisworksModelDef | AcDbNavisworksModelDef |
| AcDbLoftedSurface | LOFTEDSURFACE | AcDbRapidRTRenderSettings | RAPIDRTRENDERSETTINGS |
| AcDbMInsertBlock | INSERT | AcDbRenderEnvironment | RENDERENVIRONMENT |
| AcDbMline | MLINE | AcDbRenderGlobal | RENDERGLOBAL |
| AcDbNavisworksModel | Coordination Model | AcDbRenderSettings | RENDERSETTINGS |
| AcDbNurbSurface | NURBSURFACE | AcDbSectionManager | SECTION\_MANAGER |
| AcDbPlaneSurface | PLANESURFACE | AcDbSectionSettings | SECTION\_SETTINGS |
| AcDbPointCloudEx | ACDBPOINTCLOUDEX | AcDbSectionViewStyle | ACDBSECTIONVIEWSTYLE |
| AcDbPolyFaceMesh | POLYLINE | AcDbSun | SUN |
| AcDbPolygonMesh | POLYLINE | AcDbSolidBackground | SOLID\_BACKGROUND |
| AcDbRevolvedSurface | REVOLVEDSURFACE | AcDbSkyBackground | SKYLIGHT\_BACKGROUND |
| AcDbSection | SECTIONOBJECT | AcDbVbaProject | XRECORD |
| AcDbShape | SHAPE | AcDbXrecord | XRECORD |
| AcDbSubDMesh | MESH | AcDbPointCloudDefEx | ACDBPOINTCLOUDDEF\_EX |
| AcDbSurface | SURFACE | AcDbPointCloudDefReactorEx | ACDBPOINTCLOUDDEF\_REACTOR\_EX |
| AcDbSweptSurface | SWEPTSURFACE | AcDbPointCloudColorMap | ACDBPOINTCLOUDCOLORMAP |
|  |  | AcDbPersSubentManager | ACDBPERSSUBENTMANAGER |
|  |  | AcDbEvalGraph | ACAD\_EVALUATION\_GRAPH |
|  |  | AcDbDictionaryVar | DICTIONARYVAR |
|  |  | AcDbAssocPersSubentManager | ACDBASSOCPERSSUBENTMANAGER |
|  |  | AcDbAssocNamespace | ACDBASSOCNAMESPACE |
|  |  | AcDbAssocManager | ACDBASSOCMANAGER |
|  |  | AcDbAssocDependency | ACDBASSOCDEPENDENCY |
|  |  | AcDbAssocValueDependency | ACDBASSOCVALUEDEPENDENCY |
|  |  | AcDbAssocGeomDependency | ACDBASSOCGEOMDEPENDENCY |
|  |  | AcDbAssocDimDependencyBody | ASSOCDIMDEPENDENCYBODY |
|  |  | AcDbAssocAction | ACDBASSOCACTION |
|  |  | AcDbAssocVariable | ACDBASSOCVARIABLE |
|  |  | AcDbAssocNetwork | ACDBASSOCNETWORK |
|  |  | AcDbAssoc2dConstraintGroup | ACDBASSOC2DCONSTRAINTGROUP |
|  |  | AcDbAssocSetObjectPropertyActionBody | ACDBASSOCSETOBJECTPROPERTYACTIONBODY |
|  |  | AcDbAssocRestoreEntityStateActionBody | ACDBASSOCRESTOREENTITYSTATEACTIONBODY |
|  |  | AcDbAssocPositionEntityActionBody | ACDBASSOCPOSITIONENTITYACTIONBODY |
|  |  | AcDbAssocImpliedSurfaceOrSolidActionBody | ACDBASSOCIMPLIEDSURFACEORSOLIACTIONBODY |
|  |  | AcDbAssocCloneAndPositionEntityActionBody | ACDBASSOCCLONEANDPOSITIONENTITYACTIONBODY |
|  |  | AcDbAssocBoolOperActionBody | ACDBASSOCBOOLOPERACTIONBODY |
|  |  | AcDbAssocRadialDimLargeActionBody | ACDBASSOCRADIALDIMLARGEACTIONBODY |
|  |  | AcDbAssocLeaderActionBody | ACDBASSOCLEADERACTIONBODY |
|  |  | AcDbAssocMLeaderActionBody | ACDBASSOCMLEADERACTIONBODY |
|  |  | AcDbAssocArcDimensionActionBody | ACDBASSOCARCDIMENSIONACTIONBODY |
|  |  | AcDbAssocAlignedDimActionBody | ACDBASSOCALIGNEDDIMACTIONBODY |
|  |  | AcDbAssocEntityCloneActionBody | ACDBASSOCENTITYCLONEACTIONBODY |
|  |  | AcDbAssocArrayActionBody | ACDBASSOCARRAYACTIONBODY |
|  |  | AcDbAssocArrayModifyActionBody | ACDBASSOCARRAYMODIFYACTIONBODY |
|  |  | AcDbAssocTrimSurfaceActionBody | ACDBASSOCTRIMSURFACEACTIONBODY |
|  |  | AcDbAssocSweptSurfaceActionBody | ACDBASSOCSWEPTSURFACEACTIONBODY |
|  |  | AcDbAssocRevolvedSurfaceActionBody | ACDBASSOCREVOLVEDSURFACEACTIONBODY |
|  |  | AcDbAssocPlaneSurfaceActionBody | ACDBASSOCPLANESURFACEACTIONBODY |
|  |  | AcDbAssocNetworkSurfaceActionBody | ACDBASSOCNETWORKSURFACEACTIONBODY |
|  |  | AcDbAssocLoftedSurfaceActionBody | ACDBASSOCLOFTEDSURFACEACTIONBODY |
|  |  | AcDbAssocExtrudedSurfaceActionBody | ACDBASSOCEXTRUDEDSURFACEACTIONBODY |
|  |  | AcDbAssocEdgeFilletActionBody | ACDBASSOCEDGEFILLETACTIONBODY |
|  |  | AcDbAssocEdgeChamferActionBody | ACDBASSOCEDGECHAMFERACTIONBODY |
|  |  | AcDbAssocBlendSurfaceActionBody | ACDBASSOCBLENDSURFACEACTIONBODY |
|  |  | AcDbAssocObjectActionParam | ACDBASSOCOBJECTACTIONPARAM |
|  |  | AcDbAssocFaceActionParam | ACDBASSOCFACEACTIONPARAM |
|  |  | AcDbAssocTrimmingBodyActionParam | ACDBASSOCTRIMMINGBODYACTIONPARAM |
|  |  | AcDbAssocEdgeActionParam | ACDBASSOCEDGEACTIONPARAM |
|  |  | AcDbAssocCompoundActionParam | ACDBASSOCCOMPOUNDACTIONPARAM |
|  |  | AcDbAssocOsnapPointRefActionParam | ACDBASSOCOSNAPPOINTREFACTIONPARAM |
|  |  | AcDbAssocPathActionParam | ACDBASSOCPATHACTIONPARAM |
|  |  | AcDbAssocTrimmingPathActionParam | ACDBASSOCTRIMMINGPATHACTIONPARAM |
|  |  | AcDbAssocCoordSystemActionParam | ACDBASSOCCOORDSYSTEMACTIONPARAM |
|  |  | AcDbAssocAsmBodyActionParam | ACDBASSOCASMBODYACTIONPARAM |
|  |  | AcDbAssocVertexActionParam | ACDBASSOCVERTEXACTIONPARAM |
|  |  | AcDbSectionViewStyle | ACDBSECTIONVIEWSTYLE |

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)
* [entmakex (AutoLISP)](entmakex-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*