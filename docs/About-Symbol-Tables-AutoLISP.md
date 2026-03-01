# About Symbol Tables (AutoLISP)

Symbol tables are used to store non-graphical information in a drawing’s database.

The symbol tables that exist in a drawing database are:

| Symbol tables in each drawing database | |
| Symbol table name | Description |
| APPID | Registered applications |
| BLOCK | Blocks (named and anonymous) |
| DIMSTYLE | Dimension styles |
| LAYER | Layers |
| LTYPE | Linetypes |
| STYLE | Text styles |
| UCS | Named User Coordinate Systems (UCSs) |
| VIEW | Named views |
| VPORT | Named viewports |

Symbol table entries can be manipulated using the following functions:

* tblobjname - Returns the entity name of a specified symbol table entry.
* tblsearch - Searches a symbol table for a symbol name.
* tblnext - Returns the next item in a symbol table.
* entdel - Deletes objects (entities) or restores previously deleted objects.
* entget - Retrieves an object's (entity's) definition data list.
* entmake - Creates a new entity in the drawing.
* entmod - Modifies the definition data of an object (entity).
* handent - Returns an object (entity) name based on its handle.

## Symbol Table Limitations

The following rules apply to symbol tables:

* Symbol table entries can be created using entmake with a few restrictions, other than being valid record representations, and name conflicts can only occur in the VPORT table.
  \*ACTIVE entries cannot be created.
* Renaming symbol table entries to duplicate names is not acceptable, except for the VPORT symbol table.
* Symbol table entries cannot be deleted with entdel.
* The object states of symbol tables and symbol table entries may be accessed with entget by passing the entity name. The tblobjname function can be used to retrieve the entity name of a symbol table entry.
* Symbol tables themselves cannot be created with entmake; however, symbol table entries can be created with entmake.
* Handle group codes (5, 105) cannot be changed in entmod, nor specified in entmake.
* Symbol table entries that are not in the APPID symbol table can have many of their fields modified with entmod. Modifying a symbol table record list must include its entity name, which can be obtained from entget but not from the tblsearch and tblnext functions. The 70 group code of symbol table entries is ignored in entmod and entmake operations.

## Accessing Symbol Table Entries

The tblnext function sequentially scans symbol table entries, and the tblsearch function retrieves specific entries. Symbol table names are specified by strings. Both functions return lists with DXF group
codes that are similar to the entity data returned by entget.

The first call to tblnext returns the first entry in the specified symbol table. Subsequent calls that specify the same table return successive entries,
unless the second argument to tblnext (*rewind*) is nonzero, in which case tblnext returns the first entry again.

In the following example code, the function GETBLOCK retrieves the symbol table entry for the first block (if any) in the current drawing, and then displays it in a list format.

```
(defun C:GETBLOCK (/ blk ct)
  (setq blk (tblnext "BLOCK" 1))      ; Gets the first BLOCK entry.
  (setq ct 0)                         ; Sets ct (a counter) to 0.
  (textpage)                          ; Switches to the text screen.
  (princ "\
Results from GETBLOCK: ")
  (repeat (length blk)                ; Repeats for the number of
                                      ; members in the list.
    (print (nth ct blk))              ; Prints a new line, then each
                                      ; list member.
    (setq ct (1+ ct))                 ; Increments the counter by 1.
  )
 (princ)                              ; Exits quietly.
)
```

Entries retrieved from the BLOCK table contain a -2 group code that contains the name of the first entity in the block definition.
If the block is empty, this is the name of the block's Endblk entity, which is never seen on occupied blocks. In a drawing
with a single block named BOX, a call to GETBLOCK displays the following. (The name value varies from session to session.)

```
Results from GETBLOCK:
(0 . "BLOCK")
(2 . "BOX")
(70 . 0)
(10 9.0 2.0 0.0)
(-2 . <Entity name: 40000126>)
```

As with tblnext, the first argument to tblsearch is a string that names a symbol table, but the second argument is a string that names a particular symbol table entry in
the table. If the symbol table entry is found, tblsearch returns its data. This function has a third argument, *setnext*, that you can use to coordinate operations with tblnext. If *setnext* is nil, the tblsearch call has no effect on tblnext, but if *setnext* is non-nil, the next call to tblnext returns the symbol table entry following the symbol table entry found by tblsearch.

The *setnext* option is useful when you are handling the VPORT symbol table, because all viewports in a particular viewport configuration
have the same name (such as \*ACTIVE). If the VPORT symbol table is accessed when the AutoCAD TILEMODE system variable is turned
off, any changes have no visible effect until TILEMODE is turned on. Do not confuse VPORTS, which is described by the VPORT
symbol table with paper space viewport entities.

The following processes all viewports in the 4VIEW configuration:

```
(setq v (tblsearch "VPORT" "4VIEW" T))         ; Finds first VPORT entry.
  (while (and v (= (cdr (assoc 2 v)) "4VIEW"))
  ..
                                               ; ... Processes entry ...
  .
  (setq v (tblnext "VPORT"))                   ; Gets next VPORT entry.
)
```

#### Related Concepts

* [About Non-Graphical Object Handling (AutoLISP)](About-Non-Graphical-Object-Handling-AutoLISP.md)
* [FAQ: What Symbol Table Entries Cannot Be Renamed or Modified? (AutoLISP)](FAQ-What-Symbol-Table-Entries-Cannot-Be-Renamed-or-Modified-AutoLISP.md)
* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Anonymous Blocks (AutoLISP)](About-Anonymous-Blocks-AutoLISP.md)
* [About Accessing an Object’s Entity Name (AutoLISP)](About-Accessing-an-Object’s-Entity-Name-AutoLISP.md)
* [About Dictionary Objects and Entries (AutoLISP)](About-Dictionary-Objects-and-Entries-AutoLISP.md)
* [Symbol Table and Dictionary-Handling Functions Reference (AutoLISP)](Symbol-Table-and-Dictionary-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*