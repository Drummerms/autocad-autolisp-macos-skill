# entsel (AutoLISP)

Prompts the user to select a single object (entity) by specifying a point

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(entsel [msg])
```

*msg*
:   *Type:* String

    A prompt string to be displayed to users. If omitted,
    entsel prompts with the message, "Select object."

## Return Values

*Type:* List or nil

A list whose first element is the entity name of the chosen object and whose second element is the coordinates (in terms of
the current UCS) of the point used to pick the object.

The pick point returned by
entsel does not represent a point that lies on the selected object. The point returned is the location of the crosshairs at the
time of selection. The relationship between the pick point and the object will vary depending on the size of the pickbox and
the current zoom scale.

## Remarks

When operating on objects, you may want to simultaneously select an object and specify the point by which it was selected.
Examples of this can be found with Object Snaps and in the AutoCAD BREAK, TRIM, and EXTEND commands. The
entsel function allows AutoLISP programs to perform this operation. It selects a single object, requiring the selection to be a
pick point. The current Osnap setting is ignored by this function unless you specifically request it while you are in the
function. The
entsel function honors keywords from a preceding call to
initget.

## Examples

The following AutoCAD command sequence illustrates the use of the
entsel function and the list returned:

Command:
*line*

From point:
*1,1*

To point:
*6,6*

To point:
*Press Enter*

Command:
*(setq e (entsel "\
Select an object: "))*

Select an object:
*3,3*

(<Entity name: 60000014> (3.0 3.0 0.0))

#### Related References

* [entget (AutoLISP)](entget-AutoLISP.md)
* [entlast (AutoLISP)](entlast-AutoLISP.md)
* [entnext (AutoLISP)](entnext-AutoLISP.md)

#### Related Concepts

* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*