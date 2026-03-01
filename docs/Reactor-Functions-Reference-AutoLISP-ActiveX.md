# Reactor Functions Reference (AutoLISP/ActiveX)

NOTE:ActiveX support in AutoLISP is limited to Windows only; not available on Mac OS or Web.

Reactor functions define, query, and delete reactors and reactor properties. Before you can use these functions, you must
load AutoLISP reactor support by issuing the following function:

```
(vl-load-com)
```

The
vl-load-com function initializes reactor support and a number of other AutoLISP extensions.

| Reactor functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vl-load-com)](vl-load-com-AutoLISP-ActiveX.md) | Loads AutoLISP reactor support functions and other AutoLISP extensions | ✓ | ✓ | -- | -- | -- |
| [(vlr-acdb-reactor data callbacks)](vlr-acdb-reactor-AutoLISP-ActiveX.md) | Constructs a database (global) reactor object | ✓ | ✓ | -- | -- | -- |
| [(vlr-add obj)](vlr-add-AutoLISP-ActiveX.md) | Enables a disabled reactor object | ✓ | ✓ | -- | -- | -- |
| [(vlr-added-p obj)](vlr-added-p-AutoLISP-ActiveX.md) | Tests to determine whether a reactor object is enabled | ✓ | ✓ | -- | -- | -- |
| [(vlr-beep-reaction [args])](vlr-beep-reaction-AutoLISP-ActiveX.md) | Produces a beep sound | ✓ | ✓ | -- | -- | -- |
| [(vlr-command-reactor data callbacks)](vlr-command-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor that notifies of a command event | ✓ | ✓ | -- | -- | -- |
| [(vlr-current-reaction-name)](vlr-current-reaction-name-AutoLISP-ActiveX.md) | Returns the name (symbol) of the current event, if called from within a reactor's callback | ✓ | ✓ | -- | -- | -- |
| [(vlr-data obj)](vlr-data-AutoLISP-ActiveX.md) | Returns application-specific data associated with a reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-data-set obj data)](vlr-data-set-AutoLISP-ActiveX.md) | Overwrites application-specific data associated with a reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-deepclone-reactor obj data)](vlr-deepclone-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of deep clone events | ✓ | ✓ | -- | -- | -- |
| [(vlr-docmanager-reactor obj data)](vlr-docmanager-reactor-AutoLISP-ActiveX.md) | Constructs a reactor object that provides notification of MDI-related events | ✓ | ✓ | -- | -- | -- |
| [(vlr-dwg-reactor obj data)](vlr-dwg-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of a drawing event (for example, opening or closing a drawing file) | ✓ | ✓ | -- | -- | -- |
| [(vlr-dxf-reactor obj data)](vlr-dxf-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that notifies of an event related to reading or writing of a DXF file | ✓ | ✓ | -- | -- | -- |
| [(vlr-editor-reactor data callbacks)](vlr-editor-reactor-AutoLISP-ActiveX.md) | Constructs an editor (global) reactor object | ✓ | ✓ | -- | -- | -- |
| [(vlr-insert-reactor data callbacks)](vlr-insert-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that notifies of an event related to block insertion | ✓ | ✓ | -- | -- | -- |
| [(vlr-linker-reactor data callbacks)](vlr-linker-reactor-AutoLISP-ActiveX.md) | Constructs a linker (global) reactor object | ✓ | ✓ | -- | -- | -- |
| [(vlr-lisp-reactor data callbacks)](vlr-lisp-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that notifies of a LISP event | ✓ | ✓ | -- | -- | -- |
| [(vlr-miscellaneous-reactor data callbacks)](vlr-miscellaneous-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that does not fall under any of the other editor reactor types | ✓ | ✓ | -- | -- | -- |
| [(vlr-mouse-reactor data callbacks)](vlr-mouse-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of a mouse event (for example, a double-click) | ✓ | ✓ | -- | -- | -- |
| [(vlr-notification reactor)](vlr-notification-AutoLISP-ActiveX.md) | Determines whether or not a reactor's callback function will execute if its associated namespace is not active | ✓ | ✓ | -- | -- | -- |
| [(vlr-object-reactor owners data callbacks)](vlr-object-reactor-AutoLISP-ActiveX.md) | Constructs an object reactor object | ✓ | ✓ | -- | -- | -- |
| [(vlr-owner-add reactor owner)](vlr-owner-add-AutoLISP-ActiveX.md) | Adds an object to the list of owners of an object reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-owner-remove reactor owner)](vlr-owner-remove-AutoLISP-ActiveX.md) | Removes an object from the list of owners of an object reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-owners reactor)](vlr-owners-AutoLISP-ActiveX.md) | Returns the list of owners of an object reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-pers reactor)](vlr-pers-AutoLISP-ActiveX.md) | Makes a reactor persistent | ✓ | ✓ | -- | -- | -- |
| [(vlr-pers-list [reactor])](vlr-pers-list-AutoLISP-ActiveX.md) | Returns a list of persistent reactors in the current drawing | ✓ | ✓ | -- | -- | -- |
| [(vlr-pers-p reactor)](vlr-pers-p-AutoLISP-ActiveX.md) | Determines whether or not a reactor is persistent | ✓ | ✓ | -- | -- | -- |
| [(vlr-pers-release reactor)](vlr-pers-release-AutoLISP-ActiveX.md) | Makes a reactor transient | ✓ | ✓ | -- | -- | -- |
| [(vlr-reaction-name reactor-type)](vlr-reaction-name-AutoLISP-ActiveX.md) | Returns a list of all callback conditions for this reactor type | ✓ | ✓ | -- | -- | -- |
| [(vlr-reaction-set reactor event function)](vlr-reaction-set-AutoLISP-ActiveX.md) | Adds or replaces a callback function in a reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-reactions reactor)](vlr-reactions-AutoLISP-ActiveX.md) | Returns a list of pairs ( *event-name* .  *callback\_function*) for the reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-reactors [reactor-type ...])](vlr-reactors-AutoLISP-ActiveX.md) | Returns a list of reactors of the specified types | ✓ | ✓ | -- | -- | -- |
| [(vlr-remove reactor)](vlr-remove-AutoLISP-ActiveX.md) | Disables a reactor | ✓ | ✓ | -- | -- | -- |
| [(vlr-remove-all reactor-type)](vlr-remove-all-AutoLISP-ActiveX.md) | Disables all reactors of the specified type | ✓ | ✓ | -- | -- | -- |
| [(vlr-set-notification reactor 'range)](vlr-set-notification-AutoLISP-ActiveX.md) | Defines whether or not a reactor's callback function will execute if its associated namespace is not active | ✓ | ✓ | -- | -- | -- |
| [(vlr-sysvar-reactor data callbacks)](vlr-sysvar-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of a change to a system variable | ✓ | ✓ | -- | -- | -- |
| [(vlr-toolbar-reactor data callbacks)](vlr-toolbar-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of a change to the bitmaps in a toolbar | ✓ | ✓ | -- | -- | -- |
| [(vlr-trace-reaction)](vlr-trace-reaction-AutoLISP-ActiveX.md) | A pre-defined callback function that prints one or more callback arguments in the Trace window | ✓ | ✓ | -- | -- | -- |
| [(vlr-type reactor)](vlr-type-AutoLISP-ActiveX.md) | Returns a symbol representing the reactor type | ✓ | ✓ | -- | -- | -- |
| [(vlr-types)](vlr-types-AutoLISP-ActiveX.md) | Returns a list of all reactor types | ✓ | ✓ | -- | -- | -- |
| [(vlr-undo-reactor data callbacks)](vlr-undo-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of an undo event | ✓ | ✓ | -- | -- | -- |
| [(vlr-wblock-reactor data callbacks)](vlr-wblock-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of an event related to writing a block | ✓ | ✓ | -- | -- | -- |
| [(vlr-window-reactor data callbacks)](vlr-window-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that notifies of an event related to moving or sizing an AutoCAD window | ✓ | ✓ | -- | -- | -- |
| [(vlr-xref-reactor data callbacks)](vlr-xref-reactor-AutoLISP-ActiveX.md) | Constructs an editor reactor object that provides notification of an event related to attaching or modifying XREF | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*