# namedobjdict (AutoLISP)

Returns the entity name of the current drawing's named object dictionary, which is the root of all nongraphical objects in
the drawing

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(namedobjdict)
```

No arguments.

## Return Values

*Type:* Ename (entity name)

Always returns an ename.

## Remarks

Using the name returned by this function and the dictionary access functions, an application can access the nongraphical objects
in the drawing.

## Examples

```
(namedobjdict)
<Entity name: 7ffffb038c0>
```

#### Related References

* [dictadd (AutoLISP)](dictadd-AutoLISP.md)
* [dictnext (AutoLISP)](dictnext-AutoLISP.md)
* [dictsearch (AutoLISP)](dictsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*