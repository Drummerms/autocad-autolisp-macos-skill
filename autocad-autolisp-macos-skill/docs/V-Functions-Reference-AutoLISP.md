# V Functions Reference (AutoLISP)

These AutoLISP functions all start with 'V'.

## Functions

NOTE:vla-,
vlax-, and
vlr- functions are not supported on AutoCAD LT for Windows or Mac OS.

* [vector\_image](vector_image-AutoLISP-DCL.md)

  Draws a vector in the currently active dialog box image
* [ver](ver-AutoLISP.md)

  Returns a string that contains the current AutoLISP version number
* [vl-acad-defun](vl-acad-defun-AutoLISP.md)

  Defines an AutoLISP function symbol as an external subroutine
* [vl-acad-undefun](vl-acad-undefun-AutoLISP.md)

  Undefines an AutoLISP function symbol so it is no longer available to ObjectARX applications
* [vl-arx-import](vl-arx-import-AutoLISP.md)

  Imports ObjectARX/ADSRX functions into a separate-namespace VLX
* [vl-bb-ref](vl-bb-ref-AutoLISP.md)

  Returns the value of a variable from the blackboard namespace
* [vl-bb-set](vl-bb-set-AutoLISP.md)

  Sets a variable in the blackboard namespace
* [vl-catch-all-apply](vl-catch-all-apply-AutoLISP.md)

  Passes a list of arguments to a specified function and traps any exceptions
* [vl-catch-all-error-message](vl-catch-all-error-message-AutoLISP.md)

  Returns a string from an error object
* [vl-catch-all-error-p](vl-catch-all-error-p-AutoLISP.md)

  Determines whether an argument is an error object returned from vl-catch-all-apply
* [vl-cmdf](vl-cmdf-AutoLISP.md)

  Executes an AutoCAD command
* [vl-consp](vl-consp-AutoLISP.md)

  Determines whether or not a list is
  nil
* [vl-directory-files](vl-directory-files-AutoLISP.md)

  Lists all files in a given directory
* [vl-doc-export](vl-doc-export-AutoLISP.md)

  Makes a function available to the current document
* [vl-doc-import](vl-doc-import-AutoLISP.md)

  Imports a previously exported function into a VLX namespace
* [vl-doc-ref](vl-doc-ref-AutoLISP.md)

  Retrieves the value of a variable from the current document's namespace
* [vl-doc-set](vl-doc-set-AutoLISP.md)

  Sets the value of a variable in the current document's namespace
* [vl-every](vl-every-AutoLISP.md)

  Checks whether the predicate is true for every element combination
* [vl-exit-with-error](vl-exit-with-error-AutoLISP.md)

  Passes control from an error handler to the
  \*error\* function of the calling namespace
* [vl-exit-with-value](vl-exit-with-value-AutoLISP.md)

  Returns a value to the function that invoked the
  \*error\* handler from another namespace
* [vl-file-copy](vl-file-copy-AutoLISP.md)

  Copies or appends the contents of one file to another file
* [vl-file-delete](vl-file-delete-AutoLISP.md)

  Deletes a file
* [vl-file-directory-p](vl-file-directory-p-AutoLISP.md)

  Determines if a file name refers to a directory
* [vl-file-rename](vl-file-rename-AutoLISP.md)

  Renames a file
* [vl-file-size](vl-file-size-AutoLISP.md)

  Determines the size of a file, in bytes
* [vl-file-systime](vl-file-systime-AutoLISP.md)

  Returns last modification time of the specified file
* [vl-filename-base](vl-filename-base-AutoLISP.md)

  Returns the name of a file, after stripping out the directory path and extension
* [vl-filename-directory](vl-filename-directory-AutoLISP.md)

  Returns the directory path of a file, after stripping out the name and extension
* [vl-filename-extension](vl-filename-extension-AutoLISP.md)

  Returns the extension from a file name, after stripping out the rest of the name
* [vl-filename-mktemp](vl-filename-mktemp-AutoLISP.md)

  Calculates a unique file name to be used for a temporary file
* [vl-get-resource](vl-get-resource-AutoLISP-Visual-LISP-IDE.md)

  Returns the text stored in a .txt file packaged in a VLX
* [vl-list\*](vl-list-AutoLISP.md)

  Constructs and returns a list
* [vl-list->string](vl-list-string-AutoLISP.md)

  Combines the characters associated with a list of integers into a string
* [vl-list-exported-functions](vl-list-exported-functions-AutoLISP-Visual-LISP-IDE.md)

  Lists exported functions
* [vl-list-length](vl-list-length-AutoLISP.md)

  Calculates list length of a true list
* [vl-list-loaded-vlx](vl-list-loaded-vlx-AutoLISP.md)

  Returns a list of all separate-namespace VLX files associated with the current document
* [vl-load-all](vl-load-all-AutoLISP.md)

  Loads a file into all open AutoCAD documents, and into any document subsequently opened during the current AutoCAD session
* [vl-load-com](vl-load-com-AutoLISP-ActiveX.md)

  Loads the extended AutoLISP functions related to ActiveX support
* [vl-load-reactors](vl-load-reactors-AutoLISP-ActiveX.md)

  Loads reactor support functions
* [vl-member-if-not](vl-member-if-not-AutoLISP.md)

  Determines if the predicate is
  nil for one of the list members
* [vl-member-if](vl-member-if-AutoLISP.md)

  Determines if the predicate is true for one of the list members
* [vl-mkdir](vl-mkdir-AutoLISP.md)

  Creates a directory
* [vl-position](vl-position-AutoLISP.md)

  Returns the index of the specified list item
* [vl-prin1-to-string](vl-prin1-to-string-AutoLISP.md)

  Returns the string representation of LISP data as if it were output by the
  prin1 function
* [vl-princ-to-string](vl-princ-to-string-AutoLISP.md)

  Returns the string representation of LISP data as if it were output by the
  princ function
* [vl-propagate](vl-propagate-AutoLISP.md)

  Copies the value of a variable into all open document namespaces (and sets its value in any subsequent drawings opened during
  the current AutoCAD session)
* [vl-registry-delete](vl-registry-delete-AutoLISP.md)

  Deletes the specified key or value from the Windows registry or property list file on Mac OS
* [vl-registry-descendents](vl-registry-descendents-AutoLISP.md)

  Returns a list of subkeys or value names for the specified Windows registry key or property list file key on Mac OS
* [vl-registry-read](vl-registry-read-AutoLISP.md)

  Returns data stored in the Windows registry or property list file key on Mac OS for the specified key/value pair
* [vl-registry-write](vl-registry-write-AutoLISP.md)

  Creates a key in the Windows registry or property list file on Mac OS
* [vl-remove-if-not](vl-remove-if-not-AutoLISP.md)

  Returns all elements of the supplied list that pass the test function
* [vl-remove-if](vl-remove-if-AutoLISP.md)

  Returns all elements of the supplied list that fail the test function
* [vl-remove](vl-remove-AutoLISP.md)

  Removes elements from a list
* [vl-some](vl-some-AutoLISP.md)

  Checks whether the predicate is not nil for one element combination
* [vl-sort-i](vl-sort-i-AutoLISP.md)

  Sorts the elements in a list according to a given compare function, and returns the element index numbers
* [vl-sort](vl-sort-AutoLISP.md)

  Sorts the elements in a list according to a given compare function
* [vl-string->list](vl-string-list-AutoLISP.md)

  Converts a string into a list of character codes
* [vl-string-elt](vl-string-elt-AutoLISP.md)

  Returns the character code for the character at a specified position in a string
* [vl-string-left-trim](vl-string-left-trim-AutoLISP.md)

  Removes the specified characters from the beginning of a string
* [vl-string-mismatch](vl-string-mismatch-AutoLISP.md)

  Returns the length of the longest common prefix for two strings, starting at specified positions
* [vl-string-position](vl-string-position-AutoLISP.md)

  Looks for a character with the specified character code in a string
* [vl-string-right-trim](vl-string-right-trim-AutoLISP.md)

  Removes the specified characters from the end of a string
* [vl-string-search](vl-string-search-AutoLISP.md)

  Searches for the specified pattern in a string
* [vl-string-subst](vl-string-subst-AutoLISP.md)

  Substitutes one string for another, within a string
* [vl-string-translate](vl-string-translate-AutoLISP.md)

  Replaces characters in a string with a specified set of characters
* [vl-string-trim](vl-string-trim-AutoLISP.md)

  Removes the specified characters from the beginning and end of a string
* [vl-symbol-name](vl-symbol-name-AutoLISP.md)

  Returns a string containing the name of a symbol
* [vl-symbol-value](vl-symbol-value-AutoLISP.md)

  Returns the current value bound to a symbol
* [vl-symbolp](vl-symbolp-AutoLISP.md)

  Identifies whether or not a specified object is a symbol
* [vl-unload-vlx](vl-unload-vlx-AutoLISP.md)

  Unload a VLX application that is loaded in its own namespace
* [vl-vbaload](vl-vbaload-AutoLISP.md)

  Loads a VBA project
* [vl-vbarun](vl-vbarun-AutoLISP.md)

  Runs a VBA macro
* [vl-vlx-loaded-p](vl-vlx-loaded-p-AutoLISP.md)

  Determines whether a separate-namespace VLX is currently loaded
* [vlax-3D-point](vlax-3D-point-AutoLISP-ActiveX.md)

  Creates ActiveX-compatible (variant) 3D point structure
* [vlax-add-cmd](vlax-add-cmd-AutoLISP-ActiveX.md)

  Adds commands to the AutoCAD built-in command set
* [vlax-create-object](vlax-create-object-AutoLISP-ActiveX.md)

  Creates a new instance of an application object
* [vlax-curve-getArea](vlax-curve-getArea-AutoLISP-ActiveX.md)

  Returns the area inside the curve
* [vlax-curve-getClosestPointTo](vlax-curve-getClosestPointTo-AutoLISP-ActiveX.md)

  Returns the point (in WCS) on a curve that is nearest to the specified point
* [vlax-curve-getClosestPointToProjection](vlax-curve-getClosestPointToProjection-AutoLISP-ActiveX.md)

  Returns the closest point (in WCS) on a curve after projecting the curve onto a plane
* [vlax-curve-getDistAtParam](vlax-curve-getDistAtParam-AutoLISP-ActiveX.md)

  Returns the length of the curve's segment from the curve's beginning to the specified parameter
* [vlax-curve-getDistAtPoint](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)

  Returns the length of the curve's segment between the curve's start point and the specified point
* [vlax-curve-getEndParam](vlax-curve-getEndParam-AutoLISP-ActiveX.md)

  Returns the parameter of the endpoint of the curve
* [vlax-curve-getEndPoint](vlax-curve-getEndPoint-AutoLISP-ActiveX.md)

  Returns the endpoint (in WCS) of the curve
* [vlax-curve-getFirstDeriv](vlax-curve-getFirstDeriv-AutoLISP-ActiveX.md)

  Returns the first derivative (in WCS) of a curve at the specified location
* [vlax-curve-getParamAtDist](vlax-curve-getParamAtDist-AutoLISP-ActiveX.md)

  Returns the parameter of a curve at the specified distance from the beginning of the curve
* [vlax-curve-getParamAtPoint](vlax-curve-getParamAtPoint-AutoLISP-ActiveX.md)

  Returns the parameter of the curve at the point
* [vlax-curve-getPointAtDist](vlax-curve-getPointAtDist-AutoLISP-ActiveX.md)

  Returns the point (in WCS) along a curve at the distance specified by the user
* [vlax-curve-getPointAtParam](vlax-curve-getPointAtParam-AutoLISP-ActiveX.md)

  Returns the point at the specified parameter value along a curve
* [vlax-curve-getSecondDeriv](vlax-curve-getSecondDeriv-AutoLISP-ActiveX.md)

  Returns the second derivative (in WCS) of a curve at the specified location
* [vlax-curve-getStartParam](vlax-curve-getStartParam-AutoLISP-ActiveX.md)

  Returns the start parameter on the curve
* [vlax-curve-getStartPoint](vlax-curve-getStartPoint-AutoLISP-ActiveX.md)

  Returns the start point (in WCS) of the curve
* [vlax-curve-isClosed](vlax-curve-isClosed-AutoLISP-ActiveX.md)

  Determines if the specified curve is closed (that is, the start point is the same as the endpoint)
* [vlax-curve-isPeriodic](vlax-curve-isPeriodic-AutoLISP-ActiveX.md)

  Determines if the specified curve has an infinite range in both directions and there is a period value
  *dT*, such that a point on the curve at (*u + dT*) = point on curve (*u*), for any parameter
  *u*
* [vlax-curve-isPlanar](vlax-curve-isPlanar-AutoLISP-ActiveX.md)

  Determines if there is a plane that contains the curve
* [vlax-dump-object](vlax-dump-object-AutoLISP-ActiveX.md)

  Lists an object's properties, and optionally, the methods that apply to the object
* [vlax-ename->vla-object](vlax-ename-vla-object-AutoLISP-ActiveX.md)

  Transforms an entity to a VLA-object
* [vlax-erased-p](vlax-erased-p-AutoLISP-ActiveX.md)

  Determines whether an object was erased
* [vlax-for](vlax-for-AutoLISP-ActiveX.md)

  Iterates through a collection of objects, evaluating each expression
* [vlax-get-acad-object](vlax-get-acad-object-AutoLISP-ActiveX.md)

  Retrieves the top level AutoCAD application object for the current AutoCAD session
* [vlax-get-object](vlax-get-object-AutoLISP-ActiveX.md)

  Returns a running instance of an application object
* [vlax-get-or-create-object](vlax-get-or-create-object-AutoLISP-ActiveX.md)

  Returns a running instance of an application object, or creates a new instance if the application is not currently running
* [vlax-get-property](vlax-get-property-AutoLISP-ActiveX.md)

  Retrieves a VLA-object's property
* [vlax-import-type-library](vlax-import-type-library-AutoLISP-ActiveX.md)

  Imports information from a type library
* [vlax-invoke-method](vlax-invoke-method-AutoLISP-ActiveX.md)

  Calls the specified ActiveX method
* [vlax-ldata-delete](vlax-ldata-delete-AutoLISP-ActiveX.md)

  Erases LISP data from a drawing dictionary
* [vlax-ldata-get](vlax-ldata-get-AutoLISP-ActiveX.md)

  Retrieves LISP data from a drawing dictionary or an object
* [vlax-ldata-list](vlax-ldata-list-AutoLISP-ActiveX.md)

  Lists AutoLISP data in a drawing dictionary
* [vlax-ldata-put](vlax-ldata-put-AutoLISP-ActiveX.md)

  Stores LISP data in a drawing dictionary or an object
* [vlax-ldata-test](vlax-ldata-test-AutoLISP-ActiveX.md)

  Determines if data can be saved over a session boundary
* [vlax-machine-product-key](vlax-machine-product-key-AutoLISP-ActiveX.md)

  Returns the AutoCAD Windows registry path in the HKLM (HKEY\_LOCAL\_MACHINE)
* [vlax-make-safearray](vlax-make-safearray-AutoLISP-ActiveX.md)

  Creates a safearray
* [vlax-make-variant](vlax-make-variant-AutoLISP-ActiveX.md)

  Creates a variant data type
* [vlax-map-collection](vlax-map-collection-AutoLISP-ActiveX.md)

  Applies a function to all objects in a collection
* [vlax-method-applicable-p](vlax-method-applicable-p-AutoLISP-ActiveX.md)

  Determines if an object supports a particular method
* [vlax-object-released-p](vlax-object-released-p-AutoLISP-ActiveX.md)

  Determines if an object has been released
* [vlax-product-key](vlax-product-key-AutoLISP-ActiveX.md)

  Returns the AutoCAD Windows registry path
* [vlax-property-available-p](vlax-property-available-p-AutoLISP-ActiveX.md)

  Determines if an object has a specified property
* [vlax-put-property](vlax-put-property-AutoLISP-ActiveX.md)

  Sets the property of an ActiveX object
* [vlax-read-enabled-p](vlax-read-enabled-p-AutoLISP-ActiveX.md)

  Determines if an object can be read
* [vlax-release-object](vlax-release-object-AutoLISP-ActiveX.md)

  Releases a drawing object
* [vlax-remove-cmd](vlax-remove-cmd-AutoLISP-ActiveX.md)

  Removes a single command or a command group
* [vlax-safearray->list](vlax-safearray-list-AutoLISP-ActiveX.md)

  Returns the elements of a safearray in list form
* [vlax-safearray-fill](vlax-safearray-fill-AutoLISP-ActiveX.md)

  Stores data in the elements of a safearray
* [vlax-safearray-get-dim](vlax-safearray-get-dim-AutoLISP-ActiveX.md)

  Returns the number of dimensions in a safearray object
* [vlax-safearray-get-element](vlax-safearray-get-element-AutoLISP-ActiveX.md)

  Returns an element from an array
* [vlax-safearray-get-l-bound](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md)

  Returns the lower boundary (starting index) of a dimension of an array
* [vlax-safearray-get-u-bound](vlax-safearray-get-u-bound-AutoLISP-ActiveX.md)

  Returns the upper boundary (end index) of a dimension of an array
* [vlax-safearray-put-element](vlax-safearray-put-element-AutoLISP-ActiveX.md)

  Adds an element to an array
* [vlax-safearray-type](vlax-safearray-type-AutoLISP-ActiveX.md)

  Returns the data type of a safearray
* [vlax-tmatrix](vlax-tmatrix-AutoLISP-ActiveX.md)

  Returns a suitable representation for a 4 x 4 transformation matrix to be used in VLA methods
* [vlax-typeinfo-available-p](vlax-typeinfo-available-p-AutoLISP-ActiveX.md)

  Determines whether TypeLib information is present for the specified type of object
* [vlax-user-product-key](vlax-user-product-key-AutoLISP-ActiveX.md)

  Returns the AutoCAD Windows registry path in the HKCU (HKEY\_CURRENT\_USER)
* [vlax-variant-change-type](vlax-variant-change-type-AutoLISP-ActiveX.md)

  Returns the value of a variant after changing it from one data type to another
* [vlax-variant-type](vlax-variant-type-AutoLISP-ActiveX.md)

  Determines the data type of a variant
* [vlax-variant-value](vlax-variant-value-AutoLISP-ActiveX.md)

  Returns the value of a variant
* [vlax-vla-object->ename](vlax-vla-object-ename-AutoLISP-ActiveX.md)

  Transforms a VLA-object to an AutoLISP entity
* [vlax-write-enabled-p](vlax-write-enabled-p-AutoLISP-ActiveX.md)

  Determines if an AutoCAD drawing object can be modified
* [vlisp-compile](vlisp-compile-AutoLISP-Visual-LISP-IDE.md)

  Compiles AutoLISP source code into a FAS file
* [vlr-acdb-reactor](vlr-acdb-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies when an object is added to, modified in, or erased from a drawing database
* [vlr-add](vlr-add-AutoLISP-ActiveX.md)

  Enables a disabled reactor object
* [vlr-added-p](vlr-added-p-AutoLISP-ActiveX.md)

  Tests to determine if a reactor object is enabled
* [vlr-beep-reaction](vlr-beep-reaction-AutoLISP-ActiveX.md)

  Produces a beep sound
* [vlr-command-reactor](vlr-command-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor that notifies of a command event
* [vlr-current-reaction-name](vlr-current-reaction-name-AutoLISP-ActiveX.md)

  Returns the name (symbol) of the current event, if called from within a reactor's callback
* [vlr-data](vlr-data-AutoLISP-ActiveX.md)

  Returns application-specific data associated with a reactor
* [vlr-data-set](vlr-data-set-AutoLISP-ActiveX.md)

  Overwrites application-specific data associated with a reactor
* [vlr-deepclone-reactor](vlr-deepclone-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a deep clone event
* [vlr-docmanager-reactor](vlr-docmanager-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies of events relating to drawing documents
* [vlr-dwg-reactor](vlr-dwg-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a drawing event (for example, opening or closing a drawing file)
* [vlr-dxf-reactor](vlr-dxf-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to reading or writing a DXF file
* [vlr-editor-reactor](vlr-editor-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object
* [vlr-insert-reactor](vlr-insert-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to block insertion
* [vlr-linker-reactor](vlr-linker-reactor-AutoLISP-ActiveX.md)

  Constructs a reactor object that notifies your application every time an ObjectARX application is loaded or unloaded
* [vlr-lisp-reactor](vlr-lisp-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a LISP event
* [vlr-miscellaneous-reactor](vlr-miscellaneous-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that does not fall under any other editor reactor types
* [vlr-mouse-reactor](vlr-mouse-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a mouse event (for example, a double-click)
* [vlr-notification](vlr-notification-AutoLISP-ActiveX.md)

  Determines whether or not a reactor will fire if its associated namespace is not active
* [vlr-object-reactor](vlr-object-reactor-AutoLISP-ActiveX.md)

  Constructs a drawing object reactor object
* [vlr-owner-add](vlr-owner-add-AutoLISP-ActiveX.md)

  Adds an object to the list of owners of an object reactor
* [vlr-owner-remove](vlr-owner-remove-AutoLISP-ActiveX.md)

  Removes an object from the list of owners of an object reactor
* [vlr-owners](vlr-owners-AutoLISP-ActiveX.md)

  Returns the list of owners of an object reactor
* [vlr-pers-list](vlr-pers-list-AutoLISP-ActiveX.md)

  Returns a list of persistent reactors in the current drawing document
* [vlr-pers-p](vlr-pers-p-AutoLISP-ActiveX.md)

  Determines whether a reactor is persistent
* [vlr-pers](vlr-pers-AutoLISP-ActiveX.md)

  Makes a reactor persistent
* [vlr-pers-release](vlr-pers-release-AutoLISP-ActiveX.md)

  Makes a reactor transient
* [vlr-reaction-name](vlr-reaction-name-AutoLISP-ActiveX.md)

  Returns a list of all possible callback conditions for this reactor type
* [vlr-reaction-set](vlr-reaction-set-AutoLISP-ActiveX.md)

  Adds or replaces a callback function in a reactor
* [vlr-reactions](vlr-reactions-AutoLISP-ActiveX.md)

  Returns a list of pairs (event-name . callback\_function) for the reactor
* [vlr-reactors](vlr-reactors-AutoLISP-ActiveX.md)

  Returns a list of existing reactors
* [vlr-remove-all](vlr-remove-all-AutoLISP-ActiveX.md)

  Disables all reactors of the specified type
* [vlr-remove](vlr-remove-AutoLISP-ActiveX.md)

  Disables a reactor
* [vlr-set-notification](vlr-set-notification-AutoLISP-ActiveX.md)

  Defines whether a reactor's callback function will execute if its associated namespace is not active
* [vlr-sysvar-reactor](vlr-sysvar-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a change to a system variable
* [vlr-toolbar-reactor](vlr-toolbar-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of a change to the bitmaps in a toolbar
* [vlr-trace-reaction](vlr-trace-reaction-AutoLISP-ActiveX.md)

  A predefined callback function that prints one or more callback arguments in the Trace window
* [vlr-type](vlr-type-AutoLISP-ActiveX.md)

  Returns a symbol representing the reactor type
* [vlr-types](vlr-types-AutoLISP-ActiveX.md)

  Returns a list of all reactor types
* [vlr-undo-reactor](vlr-undo-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an undo event
* [vlr-wblock-reactor](vlr-wblock-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to writing a block
* [vlr-window-reactor](vlr-window-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to moving or sizing an AutoCAD window
* [vlr-xref-reactor](vlr-xref-reactor-AutoLISP-ActiveX.md)

  Constructs an editor reactor object that notifies of an event related to attaching or modifying XREFs
* [vports](vports-AutoLISP.md)

  Returns a list of viewport descriptors for the current viewport configuration

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*