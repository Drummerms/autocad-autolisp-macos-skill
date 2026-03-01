# About Creating Complex Entities without Using the Command Function (AutoLISP)

Complex entities (a block, polyface mesh, or "legacy" polyline) can be created by making multiple calls to
entmake, using a separate call for each subentity.

When
entmake first receives an initial component for a complex entity, it creates a temporary file in which to gather the definition data
and extended data, if present. For each subsequent
entmake call, the function checks if the temporary file exists. If it does, the new subentity is appended to the file. When the definition
of the complex entity is complete (that is, when
entmake receives an appropriate Seqend or Endblk subentity), the entity is checked for consistency; if valid, it is added to the
drawing. The file is deleted when the complex entity is complete or when its creation has been canceled. You can cancel the
creation of a complex entity by entering
entmake with no arguments. This clears the temporary file and returns
nil.

No portion of a complex entity is displayed in a drawing until its definition is complete; that is not until the final Seqend
or Endblk subentity has been passed to
entmake. The
entlast function cannot retrieve the most recently created subentity for a complex entity that has not been completed.

As the previous paragraphs imply,
entmake can construct only one complex entity at a time. If a complex entity is being created and
entmake receives invalid data or an entity that is not an appropriate
subentity, both the invalid entity and the entire complex entity are rejected.

Complex entities can exist in either model space or paper space, but not both. If you have changed the current space by invoking
either of the AutoCAD MSPACE or PSPACE commands (with command) while a complex entity is being constructed, a subsequent call
to entmake cancels the complex entity. This can also occur if the subentity has a 67 dxf group code whose value does not match
the 67 dxf group code of the entity header.

## Working with Polylines

The following example contains five calls to the
entmake function which creates a single complex entity, an old-style polyline. The polyline has three vertices located at coordinates
(1,1,0), (4,6,0), and (3,2,0), and has a linetype of DASHED and a color of BLUE. All other optional definition data assume
default values.

```
(entmake '((0 . "POLYLINE") ; Object type
  (62 . 5)                  ; Color
  (6 . "dashed")            ; Linetype
  (66 . 1)                  ; Vertices follow
 ))

(entmake '((0 . "VERTEX")   ; Object type
  (10 1.0 1.0 0.0)          ; Start point
))

(entmake '((0 . "VERTEX")   ; Object type
  (10 4.0 6.0 0.0)          ; Second point
))

(entmake '((0 . "VERTEX")   ; Object type
  (10 3.0 2.0 0.0)          ; Third point
))

(entmake '((0 . "SEQEND"))) ; Sequence end
```

NOTE:For the previous example code to execute properly, the linetype DASHED must be loaded.

When defining dotted pairs, as in the above example, there must be a space on both sides of the dot. Otherwise, you will get
an invalid dotted pair error message. If you want to use values stored in variables to create a dotted pair, you must use
the list and
cons functions instead of using the
quote ( *‘* ) function.

For example, the following code sets the color and linetype for the polyline object from values to red and dashed using variables:

```
(setq clr 5
         ltype "dashed")

(entmake (list (cons 0 "POLYLINE") ; Object type
  (cons 62 clr)                    ; Color
  (cons 6 ltype)                   ; Linetype
  (cons 66 1)                      ; Vertices follow
))
```

"Legacy" polyline entities always include a vertices-follow flag (also dxf group code 66). The value of this flag must be
1, and the flag must be followed by a sequence of vertex entities, terminated by a Seqend subentity.

Applications can represent polygons with an arbitrarily large number of sides in polyface meshes. However, the AutoCAD entity
structure imposes a limit on the number of vertices that a given face entity can specify. You can represent more complex polygons
by dividing them into triangular wedges. AutoCAD represents triangular wedges as four-vertex faces where two adjacent vertices
have the same value. Their edges should be made invisible to prevent visible artifacts of this subdivision from being drawn.
The AutoCAD PFACE command performs this subdivision automatically, but when applications generate polyface meshes directly,
the applications must do this themselves.

The number of vertices per face is the key parameter in this subdivision process. The AutoCAD PFACEVMAX system variable provides
an application with the number of vertices per face entity. This value is read-only and is set to 4.

## Working with Blocks

Block definitions begin with a block entity and end with an Endblk subentity. Newly created blocks are automatically entered
into the symbol table where they can be referenced. Block definitions cannot be nested, nor can they reference themselves.
A block definition can contain references to other block definitions.

NOTE:Before you use
entmake to create a block, you should use
tblsearch to ensure that the name of the new block is unique. The
entmake function does not check for name conflicts in the block definitions table, so you could inadvertently redefine an existing
block.

Block references can include an attributes-follow flag (dxf group code 66). If present and equal to 1, a series of attribute
(Attrib) entities is expected to follow the Insert object. The attribute sequence is terminated by a Seqend subentity.

#### Topics in this section

* [About Working With Blocks (AutoLISP)](About-Working-With-Blocks-AutoLISP.md)
* [About Anonymous Blocks (AutoLISP)](About-Anonymous-Blocks-AutoLISP.md)

  The block definitions (BLOCK) table in a drawing can contain anonymous blocks (also known as unnamed blocks), that AutoCAD
  creates to support dynamic blocks, tables, hatch patterns, and associative dimensions.

#### Related Concepts

* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [About Deleting an Entity (AutoLISP)](About-Deleting-an-Entity-AutoLISP.md)
* [About Anonymous Blocks (AutoLISP)](About-Anonymous-Blocks-AutoLISP.md)
* [About Non-Graphical Object Handling (AutoLISP)](About-Non-Graphical-Object-Handling-AutoLISP.md)
* [FAQ: What is the Difference Between Lightweight Polylines and "Legacy" Polylines? (AutoLISP)](FAQ-What-is-the-Difference-Between-Lightweight-Polylines-and-Legacy-Polylines-AutoLISP.md)
* [FAQ: How Do I Process Curve-Fit and Spline-Fit Polylines? (AutoLISP)](FAQ-How-Do-I-Process-Curve-Fit-and-Spline-Fit-Polylines-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*