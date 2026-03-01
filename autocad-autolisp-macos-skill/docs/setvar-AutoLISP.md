# setvar (AutoLISP)

Sets an AutoCAD system variable to a specified value

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setvar varname value)
```

*varname*
:   *Type:* String

    System variable name.

    You can find a list of the current AutoCAD system variables in the product Help.

*value*
:   *Type:* Integer, Real, String, List, T, or nil

    An atom or expression whose evaluated result is to be assigned to
    *varname*. For system variables with integer values, the supplied
    *value* must be between -32,768 and +32,767.

## Return Values

*Type:* Integer, Real, String, List, T, or nil

If successful,
setvar returns
*value*.

## Remarks

Some AutoCAD commands obtain the values of system variables before issuing any prompts. If you use
setvar to set a new value while a command is in progress, the new value might not take effect until the next AutoCAD command.

When using the
setvar function to change the AutoCAD ANGBASE system variable, the
*value* argument is interpreted as radians. This differs from the AutoCAD SETVAR command, which interprets this argument as degrees.
When using the
setvar function to change the AutoCAD system variable SNAPANG, the
*value* argument is interpreted as radians relative to the AutoCAD default direction for angle 0, which is
*east* or
*3 o'clock*. This also differs from the SETVAR command, which interprets this argument as degrees relative to the ANGBASE setting.

NOTE:The UNDO command does not undo changes made to the AutoCAD CVPORT system variable by the
setvar function.

## Examples

Set the AutoCAD fillet radius to 0.5 units:

```
(setvar "FILLETRAD" 0.50)
0.5
```

#### Related References

* [getvar (AutoLISP)](getvar-AutoLISP.md)

#### Related Concepts

* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)
* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*