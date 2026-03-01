# V Functions

#### Topics in this section

* [ver (AutoLISP)](ver-AutoLISP.md)

  Returns a string that contains the current AutoLISP version number
* [vl-acad-defun (AutoLISP)](vl-acad-defun-AutoLISP.md)

  Defines an AutoLISP function symbol as an external subroutine
* [vl-acad-undefun (AutoLISP)](vl-acad-undefun-AutoLISP.md)

  Undefines an AutoLISP function symbol so it is no longer available to ObjectARX applications
* [vl-arx-import (AutoLISP)](vl-arx-import-AutoLISP.md)

  Imports ObjectARX functions into a separate-namespace VLX
* [vl-bb-ref (AutoLISP)](vl-bb-ref-AutoLISP.md)

  Returns the value of a variable from the blackboard namespace
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)

  Sets a variable in the blackboard namespace
* [vl-catch-all-apply (AutoLISP)](vl-catch-all-apply-AutoLISP.md)

  Passes a list of arguments to a specified function and traps any exceptions
* [vl-catch-all-error-message (AutoLISP)](vl-catch-all-error-message-AutoLISP.md)

  Returns a string from an error object
* [vl-catch-all-error-p (AutoLISP)](vl-catch-all-error-p-AutoLISP.md)

  Determines whether an argument is an error object returned from
  vl-catch-all-apply
* [vl-cmdf (AutoLISP)](vl-cmdf-AutoLISP.md)

  Executes an AutoCAD command
* [vl-consp (AutoLISP)](vl-consp-AutoLISP.md)

  Determines whether or not a list is nil
* [vl-directory-files (AutoLISP)](vl-directory-files-AutoLISP.md)

  Lists all files in a given directory
* [vl-doc-export (AutoLISP)](vl-doc-export-AutoLISP.md)

  Makes a function available to the current document
* [vl-doc-import (AutoLISP)](vl-doc-import-AutoLISP.md)

  Imports a previously exported function into a VLX namespace
* [vl-doc-ref (AutoLISP)](vl-doc-ref-AutoLISP.md)

  Retrieves the value of a variable from the current document's namespace
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)

  Sets the value of a variable in the current document's namespace
* [vl-every (AutoLISP)](vl-every-AutoLISP.md)

  Checks whether the predicate is true for every element combination
* [vl-exit-with-error (AutoLISP)](vl-exit-with-error-AutoLISP.md)

  Passes control from an error handler to the \*error\* function of the calling namespace
* [vl-exit-with-value (AutoLISP)](vl-exit-with-value-AutoLISP.md)

  Returns a value to the function that invoked the
  \*error\* handler from another namespace
* [vl-file-copy (AutoLISP)](vl-file-copy-AutoLISP.md)

  Copies or appends the contents of one file to another file
* [vl-file-delete (AutoLISP)](vl-file-delete-AutoLISP.md)

  Deletes a file
* [vl-file-directory-p (AutoLISP)](vl-file-directory-p-AutoLISP.md)

  Determines if a file name refers to a directory
* [vl-file-rename (AutoLISP)](vl-file-rename-AutoLISP.md)

  Renames a file
* [vl-file-size (AutoLISP)](vl-file-size-AutoLISP.md)

  Determines the size of a file, in bytes
* [vl-file-systime (AutoLISP)](vl-file-systime-AutoLISP.md)

  Returns last modification time of the specified file
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)

  Returns the name of a file, after stripping out the directory path and extension
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

  Returns the directory path of a file, after stripping out the name and extension
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)

  Returns the extension from a file name, after stripping out the rest of the name
* [vl-filename-mktemp (AutoLISP)](vl-filename-mktemp-AutoLISP.md)

  Calculates a unique file name to be used for a temporary file
* [vl-list\* (AutoLISP)](vl-list-AutoLISP.md)

  Constructs and returns a list
* [vl-list->string (AutoLISP)](vl-list-string-AutoLISP.md)

  Combines the characters associated with a list of integers into a string
* [vl-list-length (AutoLISP)](vl-list-length-AutoLISP.md)

  Calculates list length of a true list
* [vl-list-loaded-vlx (AutoLISP)](vl-list-loaded-vlx-AutoLISP.md)

  Returns a list of all separate-namespace VLX files associated with the current document
* [vl-load-all (AutoLISP)](vl-load-all-AutoLISP.md)

  Loads a file into all open AutoCAD documents, and into any document subsequently opened during the current AutoCAD session
* [vl-member-if (AutoLISP)](vl-member-if-AutoLISP.md)

  Determines if the predicate is true for one of the list members
* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)

  Determines if the predicate is nil for one of the list members
* [vl-mkdir (AutoLISP)](vl-mkdir-AutoLISP.md)

  Creates a directory
* [vl-position (AutoLISP)](vl-position-AutoLISP.md)

  Returns the index of the specified list item
* [vl-prin1-to-string (AutoLISP)](vl-prin1-to-string-AutoLISP.md)

  Returns the string representation of LISP data as if it were output by the
  prin1 function
* [vl-princ-to-string (AutoLISP)](vl-princ-to-string-AutoLISP.md)

  Returns the string representation of LISP data as if it were output by the
  princ function
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)

  Copies the value of a variable into all open document namespaces (and sets its value in any subsequent drawings opened during
  the current AutoCAD session)
* [vl-registry-delete (AutoLISP)](vl-registry-delete-AutoLISP.md)

  Deletes the specified key from the Windows Registry or property list file on Mac OS
* [vl-registry-descendents (AutoLISP)](vl-registry-descendents-AutoLISP.md)

  Returns a list of subkeys or value names for the specified key of the Windows Registry or property list file on Mac OS
* [vl-registry-read (AutoLISP)](vl-registry-read-AutoLISP.md)

  Returns data stored by a specific key/value pair in the Windows Registry or property list file on Mac OS
* [vl-registry-write (AutoLISP)](vl-registry-write-AutoLISP.md)

  Creates a key in the Windows Registry or property list file on Mac OS
* [vl-remove (AutoLISP)](vl-remove-AutoLISP.md)

  Removes elements from a list
* [vl-remove-if (AutoLISP)](vl-remove-if-AutoLISP.md)

  Returns all elements of the supplied list that fail the test function
* [vl-remove-if-not (AutoLISP)](vl-remove-if-not-AutoLISP.md)

  Returns all elements of the supplied list that pass the test function
* [vl-some (AutoLISP)](vl-some-AutoLISP.md)

  Checks whether the predicate is not nil for one element combination
* [vl-sort (AutoLISP)](vl-sort-AutoLISP.md)

  Sorts the elements in a list according to a given compare function
* [vl-sort-i (AutoLISP)](vl-sort-i-AutoLISP.md)

  Sorts the elements in a list according to a given compare function, and returns the element index numbers
* [vl-string->list (AutoLISP)](vl-string-list-AutoLISP.md)

  Converts a string into a list of character codes
* [vl-string-elt (AutoLISP)](vl-string-elt-AutoLISP.md)

  Returns the character code for the character at a specified position in a string
* [vl-string-left-trim (AutoLISP)](vl-string-left-trim-AutoLISP.md)

  Removes the specified characters from the beginning of a string
* [vl-string-mismatch (AutoLISP)](vl-string-mismatch-AutoLISP.md)

  Returns the length of the longest common prefix for two strings, starting at specified positions
* [vl-string-position (AutoLISP)](vl-string-position-AutoLISP.md)

  Looks for a character with the specified character code in a string
* [vl-string-right-trim (AutoLISP)](vl-string-right-trim-AutoLISP.md)

  Removes the specified characters from the end of a string
* [vl-string-search (AutoLISP)](vl-string-search-AutoLISP.md)

  Searches for the specified pattern in a string
* [vl-string-subst (AutoLISP)](vl-string-subst-AutoLISP.md)

  Substitutes one string for another, within a string
* [vl-string-translate (AutoLISP)](vl-string-translate-AutoLISP.md)

  Replaces characters in a string with a specified set of characters
* [vl-string-trim (AutoLISP)](vl-string-trim-AutoLISP.md)

  Removes the specified characters from the beginning and end of a string
* [vl-symbol-name (AutoLISP)](vl-symbol-name-AutoLISP.md)

  Returns a string containing the name of a symbol
* [vl-symbol-value (AutoLISP)](vl-symbol-value-AutoLISP.md)

  Returns the current value bound to a symbol
* [vl-symbolp (AutoLISP)](vl-symbolp-AutoLISP.md)

  Identifies whether or not a specified object is a symbol
* [vl-unload-vlx (AutoLISP)](vl-unload-vlx-AutoLISP.md)

  Unload a VLX application that is loaded in its own namespace
* [vl-vbaload (AutoLISP)](vl-vbaload-AutoLISP.md)

  Loads a VBA project
* [vl-vbarun (AutoLISP)](vl-vbarun-AutoLISP.md)

  Runs a VBA macro
* [vl-vlx-loaded-p (AutoLISP)](vl-vlx-loaded-p-AutoLISP.md)

  Determines whether a separate-namespace VLX is currently loaded
* [vports (AutoLISP)](vports-AutoLISP.md)

  Returns a list of viewport descriptors for the current viewport configuration

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*