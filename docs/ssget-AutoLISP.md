# ssget (AutoLISP)

Creates a selection set from the selected object

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(ssget [sel-method] [pt1 [pt2]] [pt-list] [filter-list])
```

*sel-method*
:   *Type:* String

    Object selection method.

    Valid selection methods are

    | *A* | All objects are selected. |
    | *C* | Crossing selection; all objects crossing and inside of the specified rectangle. |
    | *CP* | Crossing polygon selection; all objects crossing and inside of the specified polygon. |
    | *F* | Fence selection. |
    | *I* | Implied selection; objects selected while the AutoCAD PICKFIRST system variable is in effect.  NOTE:The ssget function returns a valid selection set or nil. If an object is selected when the function is called, a valid selection set is returned. |
    | *L* | Last visible object added to the database. |
    | *P* | Previous selection set is selected. |
    | *W* | Window selection (all objects within the specified rectangle). |
    | *WP* | Window polygon (all objects within the specified polygon). |
    | *X* | Entire database. If you specify the X selection method and do not provide a *filter-list*, ssget selects all entities in the database, including entities on layers that are off, frozen, and out of the visible screen. |
    | *:D* | Allows for the selection of duplicate objects. |
    | *:E* | Everything within the cursor's object selection pickbox is selected and added to the select set. |
    | *:L* | Allows for the selection of unlocked layers only. |
    | *:N* | Call ssnamex for additional information on container blocks and transformation matrices for any entities selected during the ssget operation. This additional information is available only for entities selected through graphical selection methods such as Window, Crossing, and point picks.  Unlike the other object selection methods, *:N* may return multiple entities with the same entity name in the selection set. For example, if the user selects a subentity of a complex entity such as a BlockReference, PolygonMesh, or "legacy" polyline, ssget looks at the subentity that is selected when determining if it has already been selected. However, ssget actually adds the main entity (BlockReference, PolygonMesh, and so on) to the selection set. The result could be multiple entries with the same entity name in the selection set (each will have different subentity information for ssnamex to report). |
    | *\_:R* | Allows entities in a long transaction to be selected. |
    | *:S* | Allows for a single selection only, one or more objects can be selected.  NOTE:Use "+." with ":S" to force single object selection. |
    | *\_:U* | Enables subentity selection.  Cannot be combined with the duplicate (":D") or nested (":N") selection modes. In this mode, top-level entities are selected by default, but the user can attempt to select subentities by pressing the CTRL key while making the selection. This option is supported only with interactive selections, such as window, crossing, and polygon. It is not supported for all, filtered, or group selections. |
    | *\_:V* | Forces subentity selection.  Treats all interactive, graphic selections performed by the user as subentity selections. The returned selection set contains subentities only. This option cannot be combined with the duplicate (":D") or nested (":N") selection modes. This option is supported only with interactive selections, such as window and crossing. It is not supported for all, filtered, or group selections. |
    | *#* | Controls which object selection modes are allowed.   * "+" allows for the addition of the keywords "Last", "All", and "Previous". * "-" allows for the removal of the keywords "Last", "All", "Group", and "Previous". * "." forces the user to "pick" with the pointing device or enter a valid coordinate value to select an object. This is not an explicit keyword, but rather an implied keyword.   In combination with "+" and "-", use the following keywords to control the corresponding selection modes:   * *A* - All * *B* - Box and AUto * *C* - Crossing and CPolygon * *F* - Fence * *G* - Group * *L* - Last * *M* - Multiple * *P* - Previous * *W* - Window and WPolygon   ``` ;; Allow for a single selection (ssget "_:S")  Select objects: ? *Invalid selection* Expects a point or Window/Last/Crossing/BOX/ALL/Fence/WPolygon/CPolygon/Group/Previous/AUto  ;; Allow the user to only pick a single object (ssget "_:S+.")  Select objects: ? *Invalid selection* Expects a single object.  ;; Allow the user to only pick a single object or  ;; use the Last or Previous selection modes  (ssget "_:S+L+P")  Select objects: ? *Invalid selection* Valid keywords: Last/Previous  ;; Remove the Multiple and All selection modes (ssget "-M-A")  Select objects: ? *Invalid selection* Expects a point or Window/Last/Crossing/BOX/Fence/WPolygon/CPolygon/Group/Add/Remove/Previous/Undo/AUto/SIngle ``` |

*pt1*
:   *Type:* List

    A point relative to the selection.

*pt2*
:   *Type:* List

    A point relative to the selection.

*pt-list*
:   *Type:* List

    A list of points.

*filter-list*
:   *Type:* List

    An association list that specifies object properties. Objects that match the
    *filter-list* are added to the selection set.

## Return Values

*Type:* Pickset (selection set) or nil

The name of the created selection set if successful; otherwise
nil if no objects were selected.

## Remarks

Selection sets can contain objects from both paper and model space, but when the selection set is used in an operation,
ssget filters out objects from the space not currently in effect. Selection sets returned by
ssget contain main entities only (no attributes or polyline vertices).

If you omit all arguments,
ssget prompts the user with the Select Objects prompt, allowing interactive construction of a selection set.

If you supply a point but do not specify an object selection method, AutoCAD assumes the user is selecting an object by picking
a single point.

* When using the
  :N selection method, if the user selects a subentity of a complex entity such as a BlockReference, PolygonMesh, or "legacy"
  polyline,
  ssget looks at the subentity that is selected when determining if it has already been selected. However,
  ssget actually adds the main entity (BlockReference, PolygonMesh, etc.) to the selection set. It is therefore possible to have
  multiple entries with the same entity name in the selection set (each will have different subentity information for
  ssnamex to report). Because the
  :N method does not guarantee that each entry will be unique, code that relies on uniqueness should not use selection sets created
  using this option.
* When using the
  L selection method in an MDI environment, you cannot always count on the last object drawn to remain visible. For example,
  if your application draws a line, and the user subsequently minimizes or cascades the AutoCAD drawing window, the line may
  no longer be visible. If this occurs,
  ssget with the
  "L" option will return
  nil.

## Examples

Prompt the user to select the objects to be placed in a selection set:

```
(ssget)
<Selection set: 2>
```

Create a selection set of the object passing through (2,2):

```
(ssget '(2 2))
nil
```

Create a selection set of the most recently selected objects:

```
(ssget "_P")
<Selection set: 4>
```

Create a selection set of the objects crossing the box from (0,0) to (1,1):

```
(ssget "_C" '(0 0) '(1 1))
<Selection set: b>
```

Create a selection set of the objects inside the window from (0,0):

```
(ssget "_W" '(0 0) '(5 5))
<Selection set: d>
```

By specifying filters, you can obtain a selection set that includes all objects of a given type, on a given layer, or of a
given color. The following example returns a selection set that consists only of blue lines that are part of the implied selection
set (those objects selected while the AutoCAD PICKFIRST system variable is in effect):

```
(ssget "_I" '((0 . "LINE") (62 . 5)))
<Selection set: 4>
```

The following examples of
ssget require that a list of points be passed to the function. The
pt\_list variable cannot contain points that define zero-length segments.

Create a list of points:

```
(setq pt_list '((1 1)(3 1)(5 2)(2 4)))
((1 1) (3 1) (5 2) (2 4))
```

Create a selection set of all objects crossing and inside the polygon defined by
*pt\_list*:

```
(ssget "_CP" pt_list)
<Selection set: 13>
```

Create a selection set of all blue lines inside the polygon defined by
*pt\_list*:

```
(ssget "_WP" pt_list '((0 . "LINE") (62 . 5)))
<Selection set: 8>
```

The selected objects are highlighted only when
ssget is used with no arguments. Selection sets consume AutoCAD temporary file slots, so AutoLISP is not permitted to have more
than 128 open at one time. If this limit is reached, AutoCAD cannot create any more selection sets and returns
nil to all
ssget calls. To close an unnecessary selection set variable, set it to
nil.

A selection set variable can be passed to AutoCAD in response to any Select objects prompt at which selection by Last is valid.
AutoCAD then selects all the objects in the selection set variable.

The current setting of Object Snap mode is ignored by
ssget unless you specifically request it while you are in the function.

#### Related References

* [ssgetfirst (AutoLISP)](ssgetfirst-AutoLISP.md)
* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssdel (AutoLISP)](ssdel-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*