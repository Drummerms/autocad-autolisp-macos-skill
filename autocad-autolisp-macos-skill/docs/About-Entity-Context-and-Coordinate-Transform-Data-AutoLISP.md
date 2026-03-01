# About Entity Context and Coordinate Transform Data (AutoLISP)

The nentsel and nentselp functions are similar to entsel, except they return two additional values to handle entities nested within block references.

Another difference between these functions is that when the user responds to a nentsel call by selecting a complex entity or a complex entity is selected by nentselp, these functions return the entity name of the selected subentity and not the complex entity's header, as entsel does.

For example, when the user selects a 3D polyline, nentsel returns a vertex subentity instead of the polyline header. You can retrieve the polyline header by making successive calls
to entnext, stepping forward to the Seqend subentity, and then obtain the name of the header from the Deqend subentity's -2 dxf group
code. The same applies when the user selects attributes in a nested block reference.

Selecting an attribute within a block reference returns the name of the attribute and the pick point. When the selected object
is a component of a block reference other than an attribute, nentsel returns a list containing the following elements:

* The selected entity's name.
* A list containing the coordinates of the point used to pick the object.
* The Model to World Transformation Matrix. This is a list consisting of four sublists, each of which contains a set of coordinates.
  This matrix can be used to transform the entity definition data points from an internal coordinate system called the model
  coordinate system (MCS), to the World Coordinate System (WCS). The insertion point of the block that contains the selected
  entity defines the origin of the MCS. The orientation of the UCS when the block is created determines the direction of the
  MCS axes.
* A list containing the entity name of the block that contains the selected object. If the selected object is in a nested block
  (a block within a block), the list also contains the entity names of all blocks in which the selected object is nested, starting
  with the innermost block and continuing outward until the name of the block that was inserted in the drawing is reported.

The list returned from selecting a block with nentsel is summarized as follows:

```
(<Entity Name: ename1>   ; Name of entity.
  (Px Py Pz)             ; Pick point.
  ( (X0 Y0 Z0)           ; Model to World Transformation Matrix.
  (X1 Y1 Z1)
  (X2 Y2 Z2)
  (X3 Y3 Z3)
)
(<Entity name: ename2>   ; Name of most deeply nested block
  .                      ; containing selected object.
  ..
  <Entity name: enamen>) ; Name of outermost block
)                        ; containing selected object.
```

In the following example, create a block to use with the nentsel function.

Command: *line*

Specify first point:  *1,1*

Specify next point or [Undo]:  *3,1*

Specify next point or [Undo]: *3,3*

Specify next point or [Close/Undo]:  *1,3*

Specify next point or [Close/Undo]:  *c*

Command:  *-block*

Enter block name or [?]:  *square*

Specify insertion base point or [Annotative]:  *2,2*

Select objects: *Select the four lines you just drew*

Select objects: *Press Enter*

Then, insert the block in a UCS rotated 45 degrees about the *Z* axis:

Command: *ucs*

Current ucs name: \*WORLD\*

Specify origin of UCS or [Face/NAmed/OBject/Previous/View/World/X/Y/Z/ZAxis] <World>: *z*

Specify rotation angle about Z axis <90>: *45*

Command: *-insert*

Enter block name or [?]:  *square*

Specify insertion point or [Basepoint/Scale/X/Y/Z/Rotate]: *7,0*

Enter X scale factor, specify opposite corner, or [Corner/XYZ] <1>: *Press Enter*

Enter Y scale factor <use X scale factor>: *Press Enter*

Specify rotation angle <0>: *Press Enter*

Use nentsel to select the lower-left side of the square.

```
(setq ndata (nentsel))
```

This code sets ndata equal to a list similar to the following:

```
(<Entity Name: 400000a0>   ; Entity name.
  (6.46616 -1.0606 0.0)    ; Pick point.
  ((0.707107 0.707107 0.0) ; Model to World
  (-0.707107 0.707107 0.0) ; Transformation Matrix.
  (0.0 -0.0 1.0)
  (4.94975 4.94975 0.0)
)
  (<Entity name:6000001c>) ; Name of block containing
                           ; selected object.
)
```

Once you obtain the entity name and the Model to World Transformation Matrix, you can transform the entity definition data
points from the MCS to the WCS. Use entget and assoc on the entity name to obtain the definition points expressed in MCS coordinates. The Model to World Transformation Matrix
returned by nentsel is a 4×3 matrix—passed as an array of four points—that uses the convention that a point is a row rather than a column. The
transformation is described by the following matrix multiplication:

![](../images/GUID-A72BD35B-C21F-4C5B-B655-86B7424CE945-low.png)

So the equations for deriving the new coordinates are as follows:

![](../images/GUID-10591BAA-B24A-4802-9380-B0DFF7E10531-low.png)

The *Mij*, where 0 le; *i*, *j* le; 2, are the Model to World Transformation Matrix coordinates; *X*, *Y*, *Z* is the entity definition data point expressed in MCS coordinates, and *X*', *Y*', *Z*' is the resulting entity definition data point expressed in WCS coordinates.

To transform a vector rather than a point, do not add the translation vector (M30 M31 M32 from the fourth column of the transformation
matrix).

NOTE:This is the only AutoLISP function that uses a matrix of this type. The nentselp function is preferred to nentsel because it returns a matrix similar to those used by other AutoLISP, ObjectARX, and Managed .NET functions.

Using the entity name previously obtained with nentsel, the following example illustrates how to obtain the MCS start point of a line (group code 10) contained in a block definition:

Command: *(setq edata (assoc 10 (entget (car ndata))))*

```
(10 -1.0 1.0 0.0)
```

The following statement stores the Model to World Transformation Matrix sublist in the symbol matrix.

Command: *(setq matrix (caddr ndata))*

```
((0.707107 0.707107 0.0)   ; X transformation
  (-0.707107 0.707107 0.0) ; Y transformation
  (0.0 -0.0 1.0)           ; Z transformation
  (4.94975 4.94975 0.0)    ; Displacement from WCS origin
)
```

The following statement applies the transformation formula for *X*' to change the *X* coordinate of the start point of the line from an MCS coordinate to a WCS coordinate:

```
(setq answer
  (+                                       ; add:
    (* (car (nth 0 matrix))(cadr edata))   ; M00 * X
    (* (car (nth 1 matrix))(caddr edata))  ; M10 * Y
    (* (car (nth 2 matrix))(cadddr edata)) ; M20 * Z
    (car (nth 3 matrix))                   ; M30
  )
)
```

This statement returns 3.53553, the WCS *X* coordinate of the start point of the selected line.

#### Related Concepts

* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Entity Data Functions and the Graphics Screen (AutoLISP)](About-Entity-Data-Functions-and-the-Graphics-Screen-AutoLISP.md)
* [About Entity Handles and Their Uses (AutoLISP)](About-Entity-Handles-and-Their-Uses-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*