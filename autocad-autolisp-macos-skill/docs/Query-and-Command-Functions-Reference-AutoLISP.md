# Query and Command Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP query and command functions.

| Query and command functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(acad\_colordlg colornum [flag])](acad_colordlg-AutoLISP.md) | Displays the standard AutoCAD Color Selection dialog box | ✓ | ✓ | -- | -- | -- |
| [(acad\_helpdlg helpfile topic)](acad_helpdlg-AutoLISP.md) | Invokes the Help facility (obsolete) | ✓ | -- | -- | -- | -- |
| [(command [arguments] ...)](command-AutoLISP.md) | Executes an AutoCAD command | ✓ | ✓ | ✓ | -- | ✓ |
| [(command-s [arguments] ...)](command-s-AutoLISP.md) | Executes an AutoCAD command and the supplied input | ✓ | ✓ | ✓ | -- | ✓ |
| [(getcfg cfgname)](getcfg-AutoLISP.md) | Retrieves application data from the AppData section of the *acadXXXX.cfg* file (obsolete) | ✓ | ✓ | ✓ | -- | ✓ |
| [(getcname cname)](getcname-AutoLISP.md) | Retrieves the localized or English name of an AutoCAD command | ✓ | ✓ | ✓ | -- | ✓ |
| [(getenv "variable-name")](getenv-AutoLISP.md) | Returns the string value assigned to an environment variable | ✓ | ✓ | ✓ | -- | ✓ |
| [(getvar "varname")](getvar-AutoLISP.md) | Retrieves the value of an AutoCAD system variable | ✓ | ✓ | ✓ | -- | ✓ |
| [(help [helpfile [topic [command]]])](help-AutoLISP.md) | Invokes the Help facility | ✓ | ✓ | ✓ | -- | / - supported, but doesn't do anything |
| [(setcfg cfgname cfgval)](setcfg-AutoLISP.md) | Writes application data to the AppData section of the  *acadXXXX.cfg* file (obsolete) | ✓ | ✓ | ✓ | -- | ✓ |
| [(setenv "varname" "value")](setenv-AutoLISP.md) | Sets an environment variable to a specified value | ✓ | ✓ | ✓ | -- | ✓ |
| [(setfunhelp "c:fname" ["helpfile" ["topic" ["command"]]])](setfunhelp-AutoLISP.md) | Registers a user-defined command with the Help facility so the appropriate help file and topic are called when the user requests help on that command | ✓ | ✓ | ✓ | -- | / - supported, but doesn't do anything |
| [(setvar "varname" value)](setvar-AutoLISP.md) | Sets an AutoCAD system variable to a specified value | ✓ | ✓ | ✓ | -- | ✓ |
| [(ver)](ver-AutoLISP.md) | Returns a string that contains the current AutoLISP version number | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-cmdf [arguments] ...)](vl-cmdf-AutoLISP.md) | Executes an AutoCAD command after evaluating *arguments* | ✓ | ✓ | ✓ | -- | ✓ |
| [(vlax-add-cmd global-name func-sym [local-name cmd-flags])](vlax-add-cmd-AutoLISP-ActiveX.md) | Adds commands to a group | ✓ | ✓ | ✓ | -- | ✓ |
| [(vlax-remove-cmd global-name)](vlax-remove-cmd-AutoLISP-ActiveX.md) | Removes a single command or command group | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*