# About Logging External Reference Operations

You can maintain a record of actions while attaching, detaching, and reloading xrefs, and while loading a drawing containing
xrefs.

This log is maintained only if the XREFCTL system variable is set to 1. The default setting is 0.

The log file is an ordinary ASCII text file with the same name as the current drawing and the file extension *.xlg*. If you load a drawing with the file name *sample.dwg*, for example, the program searches for a log file named *sample.xlg* in the current folder. If the file does not exist, a new file is created with that name.

Once a log file has been created for a drawing, the program continues to append information to it. The program writes a title
section to the log file each time the file is opened. If the log file becomes too large, you can delete it.

## Sample Title Section from an Xref Log File

This title section contains the name of the current drawing, the date and time, and the operation being performed.

```
=============================
Drawing: detail
Date/Time: 09/28/99 10:45:20
Operation: Attach Xref
=============================
```

During a detaching or reloading operation, the program includes the nesting level of all affected xrefs immediately following
the title section. To see a reference tree for a set of xrefs in your current drawing, use Detach or Reload and check the
resulting entries in the log file.

## Sample Log File Entry Showing Nested Xrefs

In the following example, the xref ENTRY\_DR contains two nested xrefs: HARDWARE and PANELS. The xrefs HARDWARE and PANELS
also each contain two xrefs.

```
==============================
Drawing: detail
Date/Time: 10/05/99 15:47:39
Operation: Reload Xref
=============================
Reference tree for ENTRY_DR:
ENTRY_DR Xref
-HARDWARE Xref
--LOCKSET Xref
--HINGES Xref
-PANELS Xref
--UPPER Xref
--LOWER Xref
```

The program writes an entry in the log file for each xref-dependent named object temporarily added to the current drawing
and for any errors that occur. Most error messages are written both to the screen and to the log file.

## Sample Log File That Shows the Results of Attaching an Xref

The following example shows a partial listing of the log file entries generated when the external reference STAIR is attached
to the working drawing *test.dwg*. The log file lists the definition (symbol) table affected and the name of the definition added, along with a status message.

```
==============================
Drawing: test
Date/Time: 12/18/99 14:06:34
Operation: Attach Xref
=============================
Attach Xref STAIR: ACADDWGSSTAIR.dwg
Searching in ACAD search path
Update block symbol table:
Appending symbol: STAIR|BOLT
Appending symbol: STAIR|BOLT-HALF
...
block update complete.
Update Ltype symbol table:
Appending symbol: STAIR|DASHED
Appending symbol: STAIR|CENTER
Appending symbol: STAIR|PHANTOM
Ltype update complete.
Update Layer symbol table:
Appending symbol: STAIR|STEEL-HIDDEN
Appending symbol: STAIR|OAK
...
Layer update complete.
STAIR loaded.
```

#### Related Tasks

* [To Toggle Xref Logging](To-Toggle-Xref-Logging.md)

#### Related Information

* [About Missing or Circular External References](About-Missing-or-Circular-External-References.md)
* [About Name Conflicts in External References](About-Name-Conflicts-in-External-References.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*