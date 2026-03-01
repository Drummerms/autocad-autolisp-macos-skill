# 3dsin (AutoLISP/External Function)

Imports a 3D Studio (*.3ds*) file

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows

*Prerequisites:*The AcRender ObjectARX application must be loaded before the function can be called,
(arxload "acrender"). Earlier releases might require you to load the
*render.arx* file.

## Signature

```
(c:3dsin mode [multimat create] file)
```

mode
:   *Type:* Integer

    A numeric value that specifies whether the command is to be used interactively (mode = 1) or non-interactively (mode = 0)

multimat
:   *Type:* Integer

    A numeric value that specifies how to treat objects with multiple materials. Required if
    *mode* is set to 0. Allowable values are

    *0* Create a new object for each material

    *1* Assign the first material to the new object

create
:   *Type:* Integer

    A numeric value that specifies how to organize new objects. This mode always imports all the objects in the
    *.3ds*file. Required if
    *mode* is set to 0. Allowable values are

    *0* Create a layer for each 3DS object

    *1* Create a layer for each 3DS color

    *2* Create a layer for each 3DS material

    *3* Place all new objects on a single layer

file
:   *Type:* String

    3DS file to import; the
    *.3ds* file extension is required.

## Return Values

*Type:* Integer or nil

A numeric value if the file was successfully imported; otherwise,
nil is returned if the file could not be imported.

## Examples

Import all of
*shadow.3ds* with no user input, splitting objects with multiple materials and putting all new objects on the same later:

```
(c:3dsin 0 0 3 "c:/my documents/cad drawings/shadow.3ds")
Initializing Render...
Initializing preferences...done.
Processing object B_Leg01
Converting material SKIN
Processing object B_Leg02
Processing object Central_01
Processing object Central_02
Processing object F_Leg01
Processing object F_Leg02
Processing object M_Quad01
Processing object ML_Feele01
Processing object ML_Feele02
Processing object Pre_Quad01
Processing object Pre_Quad02
3D Studio file import completed
1
```

#### Related References

* [Externally Defined Commands (AutoLISP)](Externally-Defined-Commands-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*