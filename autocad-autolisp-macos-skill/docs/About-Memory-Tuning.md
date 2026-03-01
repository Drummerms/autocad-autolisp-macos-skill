# About Memory Tuning

Performance can also be improved by adding memory to your system. This is especially true when working on larger models.

AutoCAD-based products require at least 2 GB of physical memory (RAM) for working in 2D. For 3D modeling, at least 4 GB of
RAM is required.

The size and complexity of a model often defines how efficiently an application runs. If you notice increased hard drive activity,
it means that physical memory has been exceeded and data is being passed to a swap file (virtual memory).

A swap file is an area on the hard drive that the operating system uses as if it were physical memory (RAM). The swap file
size is basically a limit which restricts the total virtual size of the AutoCAD process. A good rule of thumb for configuring
your swap file is three times the amount of physical memory on your system. This usually sets the limit high enough that AutoCAD
does not run out of swap space.

Graphics cache files are created and maintained to optimize performance and increase the regeneration speed of objects with
complex geometry such as 3D solids, non-mesh surfaces, and regions. These cache files persist between drawing sessions and
are saved in /Users/<user name>/Library/Application Support/Autodesk/local/<product name>/<release>/<language>/GraphicsCache

The maximum number of graphics cache files that are maintained is limited in number and total size by the CACHEMAXFILES and
CACHEMAXTOTALSIZE system variables. If the limits are exceeded, the oldest cache files are automatically deleted.

.

NOTE:If you ever need to delete the graphics cache files, you can temporarily set CACHEMAXFILES or CACHEMAXTOTALSIZE to 0.

#### Related Tasks

* [To Work With Adaptive Degradation](To-Work-With-Adaptive-Degradation.md)

#### Related Information

* [About Using Visual Styles](About-Using-Visual-Styles.md)
* [Hide Lines in 3D Objects](Hide-Lines-in-3D-Objects.md)
* [About Hiding Lines in 3D Objects](About-Hiding-Lines-in-3D-Objects.md)
* [Performance Tuning](Performance-Tuning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*