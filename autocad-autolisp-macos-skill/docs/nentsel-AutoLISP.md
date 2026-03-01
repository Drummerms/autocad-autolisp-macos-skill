# nentsel (AutoLISP)

Prompts the user to select an object (entity) by specifying a point, and provides access to the definition data contained
within a complex object

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(nentsel [msg])
```

*msg*
:   *Type:* String

    Message to be displayed as a prompt. If the
    *msg* argument is omitted, the Select Object prompt is issued.

## Return Values

*Type:* Ename (entity name)

When the selected object is not complex (that is, not a 3D polyline or block),
nentsel returns the same information as
entsel. However, if the selected object is a 3D polyline,
nentsel returns a list containing the name of the subentity (vertex) and the pick point. This is similar to the list returned by
entsel, except that the name of the selected vertex is returned instead of the polyline header. The
nentsel function always returns the starting vertex of the selected 3D polyline segment. Picking the third segment of the polyline,
for example, returns the third vertex. The Seqend subentity is never returned by
nentsel for a 3D polyline.

NOTE:A lightweight polyline (lwpolyline entity) is defined in the drawing database as a single entity; it does not contain subentities.

Selecting an attribute within a block reference returns the name of the attribute and the pick point. When the selected object
is a component of a block reference other than an attribute,
nentsel returns a list containing four elements.

The first element of the list returned from picking an object within a block is the selected entity's name.

The second element is a list containing the coordinates of the point used to pick the object.

The third element is called the Model to World Transformation Matrix. It is a list consisting of four sublists, each of which
contains a set of coordinates. This matrix can be used to transform the entity definition data points from an internal coordinate
system called the Model Coordinate System (MCS), to the World Coordinate System (WCS). The insertion point of the block that
contains the selected entity defines the origin of the MCS. The orientation of the UCS when the block is created determines
the direction of the MCS axes.

NOTE:nentsel is the only AutoLISP function that uses a matrix of this type; the
nentselp function returns a matrix similar to those used by other AutoLISP and ObjectARX functions.

The fourth element is a list containing the entity name of the block that contains the selected object. If the selected object
is in a nested block (a block within a block), the list also contains the entity names of all blocks in which the selected
object is nested, starting with the innermost block and continuing outward until the name of the block that was inserted in
the drawing is reported.

## Remarks

The
nentsel function prompts the user to select an object. The current Object Snap mode is ignored unless the user specifically requests
it. To provide additional support at the Command prompt,
nentsel honors keywords defined by a previous call to
initget.

## Examples

Draw a 3D polyline with multiple line segments; then load and run the following function and select different segments of
the line. Pick off the line and then pick the same segments again to see the subentity handle. Try it with a lightweight polyline
to see the difference.

```
(defun c:subent ()
  (while
     (setq Ent (entsel "\
Pick an entity: "))
     (print (strcat "Entity handle is: "
          (cdr (assoc 5 (entget (car Ent))))))
   )
   (while
      (setq Ent (nentsel "\
Pick an entity or subEntity: "))
      (print (strcat "Entity or subEntity handle is:  "
          (cdr (assoc 5 (entget (car Ent))))))
   )
  (prompt "\
Done.")
 (princ)
)
```

#### Related References

* [nentselp (AutoLISP)](nentselp-AutoLISP.md)
* [entsel (AutoLISP)](entsel-AutoLISP.md)
* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssgetfirst (AutoLISP)](ssgetfirst-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)
* [About Entity Context and Coordinate Transform Data (AutoLISP)](About-Entity-Context-and-Coordinate-Transform-Data-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*