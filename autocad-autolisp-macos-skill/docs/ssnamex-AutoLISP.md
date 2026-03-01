# ssnamex (AutoLISP)

Retrieves information about how a selection set was created.

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssnamex ss [index])
```

*ss*
:   *Type:* Pickset (selection set)

    A selection set.

*index*
:   *Type:* Integer or Real

    Element in a selection set. The first element in the set has an index of zero.

## Return values

*Type:* Ename (entity name) or nil

If successful,
ssnamex returns the name of the entity at
*index*, along with data describing how the entity was selected. If the
*index* argument is not supplied, this function returns a list containing the entity names of the elements in the selection set,
along with data that describes how each entity was selected. If
*index* is negative or greater than the highest-numbered entity in the selection set,
ssnamex returns
nil.

## Remarks

Only selection sets with entities from the current drawing's model space and paper space—*not* nongraphical objects or entities in other block definitions—can be retrieved by this function.

The data returned by
ssnamex is a list made up of sublists that contain information about an entity and the selection method used to select it, or a polygon
used to select one or more entities. Each sublist that describes the selection of a particular entity comprises of three parts:
selection method ID (an integer >= 0), entity name of the selected entity, and selection method specific data that describes
how the entity was selected.

```
((sel_id1 ename1 (data))(sel_id2 ename2 (data)) ... )
```

The following table lists the selection method IDs:

| Selection method IDs | |
| ID | Description |
| 0 | Nonspecific (i.e., Last All) |
| 1 | Pick |
| 2 | Window or WPolygon |
| 3 | Crossing or CPolygon |
| 4 | Fence |

Each sublist that both describes a polygon and is used during entity selection takes the form of a polygon ID (an integer
< 0), followed by point descriptions.

```
(polygon_id point_description_1 point_description_n ...)
```

Polygon ID numbering starts at -1 and each additional polygon ID is incremented by -1. Depending on the viewing location,
a point is represented as one of the following: an infinite line, a ray, or a line segment. A point descriptor comprises three
parts: a point descriptor ID (the type of item being described), the start point of the item, and an optional unit vector
that describes either the direction in which the infinite line travels or a vector that describes the offset to the other
side of the line segment.

```
(point_descriptor_id base_point [unit_or_offset_vector])
```

The following table lists the valid point descriptor IDs:

| Point descriptor IDs | |
| ID | Description |
| 0 | Infinite line |
| 1 | Ray |
| 2 | Line segment |

The
*unit\_or\_offset\_vector* is returned when the view point is something other than 0,0,1.

## Examples

The
*data* associated with Pick (type 1) entity selections is a single point description. For example, the following record is returned
for the selection of an entity picked at 1,1 in plan view of the WCS:

Command:
*(ssnamex ss3 0)*

```
((1 <Entity name: 1d62da0> 0 (0 (1.0 1.0 0.0))))
```

The
*data* associated with an entity selected with the Window, WPolygon, Crossing, or CPolygon method is the integer ID of the polygon
that selected the entity. It is up to the application to associate the polygon identifiers and make the connection between
the polygon and the entities it selected. For example, the following returns an entity selected by Crossing (note that the
polygon ID is -1):

Command:
*(ssnamex ss4 0)*

```
((3 <Entity name: 1d62d60> 0 -1) (-1 (0 (-1.80879 8.85536 0.0)) (0 (13.4004 8.85536 0.0))
(0 (13.4004 1.80024 0.0)) (0 (-1.80879 1.80024 0.0))))
```

The
*data* associated with fence selections is a list of points and descriptions for the points where the fence and entity visually
intersect. For example, the following command returns information for a nearly vertical line intersected three times by a
Z-shaped fence:

Command:
*(ssnamex ss5 0)*

```
((4 <Entity name: 1d62d88> 0 (0 (5.28135 6.25219 0.0)) (0 (5.61868 2.81961 0.0))
(0 (5.52688 3.75381 0.0))))
```

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [sslength (AutoLISP)](sslength-AutoLISP.md)
* [ssmemb (AutoLISP)](ssmemb-AutoLISP.md)
* [ssname (AutoLISP)](ssname-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*