# REGION (Command)

Converts an object that encloses an area into a region object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Hatch panel ![](../images/ac.menuaro.gif) Region.
![](../images/GUID-33A37D2E-0385-44DB-A253-834CFAC285CF-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Region.

Regions are 2D areas that you create from closed planar loops of objects. Valid objects include polylines, lines, circular
arcs, circles, elliptical arcs, ellipses, and splines. Each closed loop is converted into a separate region. All crossing
intersections and self-intersecting curves are rejected.

REGION deletes the original objects after converting them to regions unless the system variable DELOBJ is set to 0. If the
original objects were hatched, hatch associativity is lost. To restore associativity, rehatch the region.

After you have converted objects to regions, you can combine them into a complex region using union, subtract, or intersect
operations.

![](../images/GUID-0DD1D793-31EC-427E-A220-7A3272AE4F0F-low.gif)

You can also create a region with the BOUNDARY command.

#### Related Concepts

* [About Regions](About-Regions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*