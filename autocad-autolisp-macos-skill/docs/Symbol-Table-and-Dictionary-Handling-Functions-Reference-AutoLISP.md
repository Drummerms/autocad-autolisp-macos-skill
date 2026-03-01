# Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP symbol table and dictionary-handling functions.

| Symbol table and dictionary-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(dictadd ename symbol newobj)](dictadd-AutoLISP.md) | Adds a non-graphical object to the specified dictionary | ✓ | ✓ | ✓ | -- | ✓ |
| [(dictnext ename symbol [rewind])](dictnext-AutoLISP.md) | Finds the next item in a dictionary | ✓ | ✓ | ✓ | -- | ✓ |
| [(dictremove ename symbol)](dictremove-AutoLISP.md) | Removes an entry from the specified dictionary | ✓ | ✓ | ✓ | -- | ✓ |
| [(dictrename ename oldsym newsym)](dictrename-AutoLISP.md) | Renames a dictionary entry | ✓ | ✓ | ✓ | -- | ✓ |
| [(dictsearch ename symbol [setnext])](dictsearch-AutoLISP.md) | Searches a dictionary for an item | ✓ | ✓ | ✓ | -- | ✓ |
| [(layoutlist)](layoutlist-AutoLISP.md) | Returns a list of all paper space layouts in the current drawing | ✓ | ✓ | ✓ | -- | -- |
| [(namedobjdict)](namedobjdict-AutoLISP.md) | Returns the entity name of the current drawing's named object dictionary, which is the root of all non-graphical objects in the drawing | ✓ | ✓ | ✓ | -- | ✓ |
| [(setview view\_description [vport\_id])](setview-AutoLISP.md) | Establishes a view for a specified viewport | ✓ | ✓ | ✓ | -- | ✓ |
| [(snvalid sym\_name)](snvalid-AutoLISP.md) | Checks the symbol table name for valid characters | ✓ | ✓ | ✓ | -- | ✓ |
| [(tblnext table-name [rewind])](tblnext-AutoLISP.md) | Finds the next item in a symbol table | ✓ | ✓ | ✓ | -- | ✓ |
| [(tblobjname table-name symbol)](tblobjname-AutoLISP.md) | Returns the entity name of a specified symbol table entry | ✓ | ✓ | ✓ | -- | ✓ |
| [(tblsearch table-name symbol [setnext])](tblsearch-AutoLISP.md) | Searches a symbol table for a symbol name | ✓ | ✓ | ✓ | -- | ✓ |
| [(vlax-ldata-delete dict key)](vlax-ldata-delete-AutoLISP-ActiveX.md) | Erases AutoLISP data from a drawing dictionary  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-ldata-get dict key [default-data])](vlax-ldata-get-AutoLISP-ActiveX.md) | Retrieves AutoLISP data from a drawing dictionary  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-ldata-list dict)](vlax-ldata-list-AutoLISP-ActiveX.md) | Lists AutoLISP data in a drawing dictionary  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-ldata-put dict key data)](vlax-ldata-put-AutoLISP-ActiveX.md) | Stores AutoLISP data in a drawing dictionary  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |
| [(vlax-ldata-test data)](vlax-ldata-test-AutoLISP-ActiveX.md) | Determines whether data can be saved over a session boundary  NOTE:Extended AutoLISP extension: requires vl-load-com | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*