# Overview of Express Tools Utility Functions

The
acetutil modules (*acetutil.arx* and
*acetutil\*.fas*) provide a number of utility functions which can be called from AutoLISP on Windows for AutoCAD only.

This documentation covers all the functionality present in version 1.38 of
*acetutil.arx*, along with a few functions provided in
*acetutil.fas*. Functions that do not have a specific library designation appear in
*acetutil.arx*.

Starting with AutoCAD 2025, you might need to initialize the Express Tools Utility functions before they can be used by your
AutoLISP programs. The
acet-load-expresstools function is used to initialize the Express Tools Utility functions, which is similar to initializing the ActiveX/COM library
for use with the
vl-load-com function.

NOTE:The
acet-util-ver function can be called to identify the module version of the Express Tools Utility functions. This function returns a REAL
value containing the current version number of the
*acetutil.arx* library.

```
(acet-util-ver)
1.38
```

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*