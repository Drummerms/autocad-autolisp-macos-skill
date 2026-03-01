# VLR Functions

#### Topics in this section

* [vlr-acdb-reactor (AutoLISP/ActiveX)](vlr-acdb-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies when an object is added to, modified in, or erased from a drawing database
* [vlr-add (AutoLISP/ActiveX)](vlr-add-AutoLISP-ActiveX.md)

  Enables a disabled reactor object
* [vlr-added-p (AutoLISP/ActiveX)](vlr-added-p-AutoLISP-ActiveX.md)

  Tests to determine if a reactor object is enabled
* [vlr-beep-reaction (AutoLISP/ActiveX)](vlr-beep-reaction-AutoLISP-ActiveX.md)

  Produces a beep sound
* [vlr-command-reactor (AutoLISP/ActiveX)](vlr-command-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor that notifies of a command event
* [vlr-current-reaction-name (AutoLISP/ActiveX)](vlr-current-reaction-name-AutoLISP-ActiveX.md)

  Returns the name (symbol) of the current event, if called from within a reactor's callback
* [vlr-data (AutoLISP/ActiveX)](vlr-data-AutoLISP-ActiveX.md)

  Returns application-specific data associated with a reactor
* [vlr-data-set (AutoLISP/ActiveX)](vlr-data-set-AutoLISP-ActiveX.md)

  Overwrites application-specific data associated with a reactor
* [vlr-deepclone-reactor (AutoLISP/ActiveX)](vlr-deepclone-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a deep clone event
* [vlr-docmanager-reactor (AutoLISP/ActiveX)](vlr-docmanager-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies of events relating to drawing documents
* [vlr-dwg-reactor (AutoLISP/ActiveX)](vlr-dwg-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a drawing event (for example, opening or closing a drawing file)
* [vlr-dxf-reactor (AutoLISP/ActiveX)](vlr-dxf-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to reading or writing a DXF file
* [vlr-editor-reactor (AutoLISP/ActiveX)](vlr-editor-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object
* [vlr-insert-reactor (AutoLISP/ActiveX)](vlr-insert-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to block insertion
* [vlr-linker-reactor (AutoLISP/ActiveX)](vlr-linker-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies your application every time an ObjectARX application is loaded or unloaded
* [vlr-lisp-reactor (AutoLISP/ActiveX)](vlr-lisp-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a LISP event
* [vlr-miscellaneous-reactor (AutoLISP/ActiveX)](vlr-miscellaneous-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that does not fall under any other editor reactor types
* [vlr-mouse-reactor (AutoLISP/ActiveX)](vlr-mouse-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a mouse event (for example, a double-click)
* [vlr-notification (AutoLISP/ActiveX)](vlr-notification-AutoLISP-ActiveX.md)

  Determines whether or not a reactor will fire if its associated namespace is not active
* [vlr-object-reactor (AutoLISP/ActiveX)](vlr-object-reactor-AutoLISP-ActiveX.md)

  Constructs a drawing object reactor object
* [vlr-owner-add (AutoLISP/ActiveX)](vlr-owner-add-AutoLISP-ActiveX.md)

  Adds an object to the list of owners of an object reactor
* [vlr-owner-remove (AutoLISP/ActiveX)](vlr-owner-remove-AutoLISP-ActiveX.md)

  Removes an object from the list of owners of an object reactor
* [vlr-owners (AutoLISP/ActiveX)](vlr-owners-AutoLISP-ActiveX.md)

  Returns the list of owners of an object reactor
* [vlr-pers-list (AutoLISP/ActiveX)](vlr-pers-list-AutoLISP-ActiveX.md)

  Returns a list of persistent reactors in the current drawing document
* [vlr-pers-p (AutoLISP/ActiveX)](vlr-pers-p-AutoLISP-ActiveX.md)

  Determines whether a reactor is persistent
* [vlr-pers (AutoLISP/ActiveX)](vlr-pers-AutoLISP-ActiveX.md)

  Makes a reactor persistent
* [vlr-pers-release (AutoLISP/ActiveX)](vlr-pers-release-AutoLISP-ActiveX.md)

  Makes a reactor transient
* [vlr-reaction-name (AutoLISP/ActiveX)](vlr-reaction-name-AutoLISP-ActiveX.md)

  Returns a list of all possible callback conditions for this reactor type
* [vlr-reaction-set (AutoLISP/ActiveX)](vlr-reaction-set-AutoLISP-ActiveX.md)

  Adds or replaces a callback function in a reactor
* [vlr-reactions (AutoLISP/ActiveX)](vlr-reactions-AutoLISP-ActiveX.md)

  Returns a list of pairs (event-name . callback\_function) for the reactor
* [vlr-reactors (AutoLISP/ActiveX)](vlr-reactors-AutoLISP-ActiveX.md)

  Returns a list of existing reactors
* [vlr-remove (AutoLISP/ActiveX)](vlr-remove-AutoLISP-ActiveX.md)

  Disables a reactor
* [vlr-remove-all (AutoLISP/ActiveX)](vlr-remove-all-AutoLISP-ActiveX.md)

  Disables all reactors of the specified type
* [vlr-set-notification (AutoLISP/ActiveX)](vlr-set-notification-AutoLISP-ActiveX.md)

  Defines whether a reactor's callback function will execute if its associated namespace is not active
* [vlr-sysvar-reactor (AutoLISP/ActiveX)](vlr-sysvar-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a change to a system variable
* [vlr-toolbar-reactor (AutoLISP/ActiveX)](vlr-toolbar-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a change to the bitmaps in a toolbar
* [vlr-trace-reaction (AutoLISP/ActiveX)](vlr-trace-reaction-AutoLISP-ActiveX.md)

  A predefined callback function that prints one or more callback arguments in the Trace window
* [vlr-type (AutoLISP/ActiveX)](vlr-type-AutoLISP-ActiveX.md)

  Returns a symbol representing the reactor type
* [vlr-types (AutoLISP/ActiveX)](vlr-types-AutoLISP-ActiveX.md)

  Returns a list of all reactor types
* [vlr-undo-reactor (AutoLISP/ActiveX)](vlr-undo-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an undo event
* [vlr-wblock-reactor (AutoLISP/ActiveX)](vlr-wblock-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to writing a block
* [vlr-window-reactor (AutoLISP/ActiveX)](vlr-window-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to moving or sizing an AutoCAD window
* [vlr-xref-reactor (AutoLISP/ActiveX)](vlr-xref-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to attaching or modifying XREFs

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*