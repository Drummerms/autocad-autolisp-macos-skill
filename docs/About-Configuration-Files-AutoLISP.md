# About Configuration Files (AutoLISP)

AutoCAD uses a configuration file with the name
*acadxxxx.cfg* to store device and application information.

NOTE:The
getcfg and
setcfg functions are obsolete, and it is recommended to store application information using the
vl-registry-read and
vl-registry-write functions.

The
*xxxx* in the file name refers to the AutoCAD release number. The AppData section of this file is provided for users and developers
to store configuration information pertaining to their applications. The
getcfg and
setcfg functions allow AutoLISP applications to inspect and change the value of parameters in the AppData section.

The
setcfg function requires two strings that represent the section and parameter, and the value to assign. The value returned by
setcfg is
nil if the value could not be stored or the value that was being assigned to the parameter. The
getcfg function requires the section and parameter to retrieve a value from and returns the value if the parameter exists.

The following code creates a section under AppData named ArchStuff with a parameter titled WallThk. The value of ”8” is then
assigned to WallThk.

```
(setcfg "AppData/ArchStuff/WallThk" "8")
"8"
```

The following code returns the value assigned to the specified section and parameter.

```
(getcfg "AppData/ArchStuff/WallThk")
"8"
```

NOTE:It is recommend to store values in the Windows Registry or the AutoCAD property list (*HKCU.plist* and
*HKLM.plist*) files on Mac OS. This can be done using the
vl-registry-read and
vl-registry-write functions.

#### Related Concepts

* [About System and Environment Variables (AutoLISP)](About-System-and-Environment-Variables-AutoLISP.md)
* [About Controlling Menus (AutoLISP)](About-Controlling-Menus-AutoLISP.md)
* [About Calibrating Tablets (AutoLISP)](About-Calibrating-Tablets-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*