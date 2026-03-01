# About Deleting an Entity (AutoLISP)

Entities can be deleted using the
entdel function or AutoCAD ERASE command (with
command).

Entities are not purged from the database until the end of the current drawing session, so if the application calls
entdel on an entity that was deleted during that session, the entity is undeleted.

Attributes and "legacy" polyline vertices cannot be deleted independently of their parent entities. The
entdel function and AutoCAD ERASE command only operate on main entities. If you need to delete an attribute or vertex, you can use
the AutoCAD ATTEDIT or PEDIT commands with
command.

#### Related Concepts

* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*