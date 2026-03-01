# Application-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP application-handling functions.

| Application-handling functions | | Platforms | |  | |  |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(arx)](arx-AutoLISP.md) | Returns a list of the currently loaded ObjectARX applications | ✓ | ✓ | ✓ | -- | ✓ |
| [(arxload application [onfailure])](arxload-AutoLISP.md) | Loads an ObjectARX application | ✓ | ✓ | ✓ | -- | -- |
| [(arxunload application [onfailure])](arxunload-AutoLISP.md) | Unloads an ObjectARX application | ✓ | ✓ | ✓ | -- | -- |
| [(autoarxload filename cmdlist)](autoarxload-AutoLISP.md) | Predefines command names to load an associated ObjectARX file | ✓ | ✓ | ✓ | -- | -- |
| [(autoload filename cmdlist)](autoload-AutoLISP.md) | Predefines command names to load an associated AutoLISP file | ✓ | ✓ | ✓ | -- | -- |
| [(initdia [dialogflag])](initdia-AutoLISP.md) | Forces the display of the next command's dialog box | ✓ | ✓ | ✓ | -- | -- |
| [(load filename [onfailure])](load-AutoLISP.md) | Evaluates the AutoLISP expressions in a file | ✓ | ✓ | ✓ | -- | ✓ |
| [(showhtmlmodalwindow uri)](showhtmlmodalwindow-AutoLISP.md) | Displays a modal dialog box with a specified URI (Uniform Resource Identifier) | ✓ | ✓ | -- | -- | -- |
| [(startapp appcmd file)](startapp-AutoLISP.md) | Starts a Windows application | ✓ | ✓ | ✓ | -- | -- |
| [(vl-load-all filename)](vl-load-all-AutoLISP.md) | Loads a file into all open AutoCAD documents | ✓ | ✓ | ✓ | -- | -- |
| [(vl-vbaload "filename")](vl-vbaload-AutoLISP.md) | Loads a VBA project | ✓ | -- | -- | -- | -- |
| [(vl-vbarun "macroname")](vl-vbarun-AutoLISP.md) | Runs a VBA macro | ✓ | -- | -- | -- | -- |
| [(vlax-add-cmd "global-name" 'func-sym [“local-name" cmd-flags])](vlax-add-cmd-AutoLISP-ActiveX.md) | Adds commands to the AutoCAD built-in command set | ✓ | ✓ | ✓ | -- | / - supported, but doesn't affect the program |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*