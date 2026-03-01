# sssetfirst (AutoLISP)

Sets which objects are selected and gripped

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(sssetfirst gripset [pickset])
```

*gripset*
:   *Type:* nil

    AutoCAD no longer supports grips on unselected objects, so this argument is ignored. However, if
    *gripset* is
    nil and no
    *pickset* is specified,
    sssetfirst turns off the grip handles and selections it previously turned on.

*pickset*
:   *Type:* Pickset (selection set)

    A selection set to be selected.

## Return Values

*Type:* List

The selection set or sets specified.

## Remarks

The
*gripset* argument is ignored; the selection set of objects specified by
*pickset* are selected and gripped.

You are responsible for creating a valid selection set. For example, you may need to verify that a background paper space
viewport (DXF group code 69) is not included in the selection set. You may also need to ensure that selected objects belong
to the current layout, as in the following code:

```
(setq ss (ssget (list (cons 410 (getvar "ctab")))))
```

## Examples

First, draw a square and build three selection sets. Begin by drawing side 1 and creating a selection set to include the line
drawn:

```
(entmake (list (cons 0 "line") '(10 0.0 0.0 0.0)'(11 0.0 10.0 0.0)))
((0 . "line") (10 0.0 0.0 0.0) (11 0.0 10.0 0.0))

(setq pickset1 (ssget "_l"))
<Selection set: a5>
```

Variable
pickset1 points to the selection set created.

Draw side 2 and add it to the
pickset1 selection set:

```
(entmake (list (cons 0 "line") '(10 0.0 10.0 0.0)'(11 10.0 10.0 0.0)))
((0 . "line") (10 0.0 10.0 0.0) (11 10.0 10.0 0.0))

(ssadd (entlast) pickset1)
<Selection set: a5>
```

Create another selection set to include only side 2:

```
(setq 2onlyset (ssget "_l"))
<Selection set: a8>
```

Draw side 3 and add it to the
pickset1 selection set:

```
(entmake (list (cons 0 "line") '(10 10.0 10.0 0.0)'(11 10.0 0.0 0.0)))
((0 . "line") (10 10.0 10.0 0.0) (11 10.0 0.0 0.0))

(ssadd (entlast) pickset1)
<Selection set: a5>
```

Create another selection and include side 3 in the selection set:

```
(setq pickset2 (ssget "_l"))
<Selection set: ab>
```

Variable
pickset2 points to the new selection set.

Draw side 4 and add it to the
pickset1 and
pickset2 selection sets:

```
(entmake (list (cons 0 "line") '(10 10.0 0.0 0.0)'(11 0.0 0.0 0.0)))
((0 . "line") (10 10.0 0.0 0.0) (11 0.0 0.0 0.0))

(ssadd (entlast) pickset1)
<Selection set: a5>

(ssadd (entlast) pickset2)
<Selection set: ab>
```

At this point,
pickset1 contains sides 1-4,
pickset2 contains sides 3 and 4, and
2onlyset contains only side 2.

Turn grip handles on and select all objects in
pickset1:

```
(sssetfirst nil pickset1)
(nil <Selection set: a5>)
```

Turn grip handles on and select all objects in
pickset2:

```
(sssetfirst nil pickset2)
(nil <Selection set: ab>)
```

Turn grip handles on and select all objects in
2onlyset:

```
(sssetfirst nil 2onlyset)
(nil <Selection set: a8>)
```

Each
sssetfirst call replaces the gripped and selected selection set from the previous
sssetfirst call.

NOTE:Do
*not* call
sssetfirst when AutoCAD is in the middle of executing a command.

#### Related References

* [ssget (AutoLISP)](ssget-AutoLISP.md)
* [ssgetfirst (AutoLISP)](ssgetfirst-AutoLISP.md)
* [ssadd (AutoLISP)](ssadd-AutoLISP.md)
* [ssdel (AutoLISP)](ssdel-AutoLISP.md)

#### Related Concepts

* [Selection Set Manipulation Functions Reference (AutoLISP)](Selection-Set-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*