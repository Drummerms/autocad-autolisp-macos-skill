# About Entity Data Functions (AutoLISP)

The functions described in this section operate on entity data and can be used to modify the current drawing database.

#### Topics in this section

* [About Adding an Entity without Using the Command Function (AutoLISP)](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)

  An application can add an entity to the drawing database by calling the
  entmake function.
* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)

  Complex entities (a block, polyface mesh, or "legacy" polyline) can be created by making multiple calls to
  entmake, using a separate call for each subentity.
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)

  The entget function returns the definition data of a specified entity as a list.
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)

  An entity can be modified directly by changing its entity list and posting the changes back to the database.
* [About Deleting an Entity (AutoLISP)](About-Deleting-an-Entity-AutoLISP.md)

  Entities can be deleted using the
  entdel function or AutoCAD ERASE command (with
  command).

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*