# 3D Graphics

This release includes the new cross platform 3D graphics system, leveraging all the power of modern GPUs and multi-core CPUs
to offer a smooth navigation experience for much larger drawings.

This graphics system is available for Shaded and Shaded with Edges visual styles and is on by default.

![](../images/GUID-7D1E802C-EA45-4DAA-8DE9-2F9235F12CE4-low.png)

## Activating and Deactivating

By default, the graphics system is
*ON*. To turn it
*OFF*, enter the following at the command line:

![](../images/GUID-25300A33-DB07-4413-9797-5063AB8D57C9-low.png)

In the
*Shaded* or
*Shaded with Edges* visual styles,
*(Fast)* is shown in the viewport control to indicate that the modern 3D graphics system is being used.

![](../images/GUID-3A9875BC-8870-4872-A36A-DA726A4C8DCC-low.png)

## Limitations

The modern graphics system does not currently support the following features:

* TrueType text fonts
* Materials
* Lineweights (LWDISPLAY=ON)
* Block editor (BEDIT)
* Draw order in transparency
* Fence and lasso selection
* Display and sub entity selection of edges in 3D objects
* Drawings that are saved with an active
  *Shaded* or
  *Shaded with Edges* viewport will not have a valid preview

It is also limited to model space. In paper space, a viewport continues to use the existing graphics system.

## *New System Variables*

[FASTSHADEDMODE](FASTSHADEDMODE-System-Variable.md) - Specifies whether the 3D graphics system is turned on or off.

#### Related Concepts

* [What's New in AutoCAD for Mac 2023](What's-New-in-AutoCAD-for-Mac-2023.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*