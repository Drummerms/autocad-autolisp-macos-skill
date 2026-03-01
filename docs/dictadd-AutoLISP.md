# dictadd (AutoLISP)

Adds a nongraphical object to the specified dictionary

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(dictadd ename symbol newobj)
```

*ename*
:   *Type:* Ename (entity name)

    Name of the dictionary the object is being added to.

*symbol*
:   *Type:* String

    The key name of the object being added to the dictionary;
    *symbol* must be a unique name that does not already exist in the dictionary.

*newobj*
:   *Type:* Ename (entity name)

    A nongraphical object to be added to the dictionary.

## Return Values

*Type:* Ename (entity name)

The entity name of the object added to the dictionary.

## Remarks

As a general rule, each object added to a dictionary must be unique to that dictionary. This is specifically a problem when
adding group objects to the group dictionary. Adding the same group object using different key names results in duplicate
group names, which can send the
dictnext function into an infinite loop.

Drawing properties such as Title, Subject, Author, and Keywords, can be accessed only with the
IAcadSummaryInfo interface that is part of the AutoCAD ActiveX/COM library, accessible as a property of the
Document object in the AutoCAD object model. The AutoCAD ActiveX/COM library is available only in AutoCAD for Windows; not available
in AutoCAD LT for Windows.

NOTE:The
entmakex function doesn't support the creation of
AcDbXrecord (Xrecord) objects in AutoCAD LT.

## Examples

The examples that follow create objects and add them to the named object dictionary.

Create a dictionary entry list:

```
(setq dictionary (list '(0 . "DICTIONARY") '(100 . "AcDbDictionary")))
((0 . "DICTIONARY") (100 . "AcDbDictionary"))
```

Create a dictionary object using the
entmakex function:

```
(setq xname (entmakex dictionary))(setq xname (entmakex dictionary))
<Entity name: 1d98950>
```

Add the dictionary to the named object dictionary:

```
(setq newdict (dictadd (namedobjdict) "MY_WAY_COOL_DICTIONARY" xname))
<Entity name: 1d98950>
```

Create an Xrecord list:

```
(setq datalist (append (list '(0 . "XRECORD")
                                 '(100 . "AcDbXrecord"))
                                 '((1 . "This is my data") (10 1. 2. 3.) (70 . 33))))
((0 . "XRECORD") (100 . "AcDbXrecord") (1 . "This is my data") (10 1.0 2.0 3.0) (70 . 33))
```

Make an Xrecord object:

```
(setq xname (entmakex datalist))
<Entity name: 1d98958>
```

Add the Xrecord object to the dictionary:

```
(dictadd newdict "DATA_RECORD_1" xname)
<Entity name: 1d98958>
```

#### Related References

* [dictremove (AutoLISP)](dictremove-AutoLISP.md)
* [dictrename (AutoLISP)](dictrename-AutoLISP.md)
* [dictsearch (AutoLISP)](dictsearch-AutoLISP.md)

#### Related Concepts

* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*