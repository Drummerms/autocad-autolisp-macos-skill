# Performance Tuning

Performance tuning examines your graphics card and 3D display driver and determines whether to use software or hardware implementation
for features that support both.

Features that cannot work properly on your system are turned off. Some features may work but not be recommended for use with
your graphics card or 3D graphics display driver. Enable these features at your own risk. For information on the options available,
see -3DCONFIG.

*Graphics Caching*

Graphics cache files are created and maintained to optimize performance and increase the regeneration speed of objects with
complex geometry such as 3D solids, non-mesh surfaces, and regions. These cache files persist between drawing sessions and
are saved in /Users/<user name>/Library/Application Support/Autodesk/local/<product name>/<release>/<language>/GraphicsCache. The maximum number of these cache files are limited in number and total size by the CACHEMAXFILES and CACHEMAXTOTALSIZE system
variables. If the limits are exceeded, the oldest cache files are automatically deleted.

NOTE:If you ever need to delete the graphics cache files, you can temporarily set CACHEMAXFILES or CACHEMAXTOTALSIZE to 0.

#### Related Tasks

* [To Work With Adaptive Degradation](To-Work-With-Adaptive-Degradation.md)

#### Related Information

* [About Using Visual Styles](About-Using-Visual-Styles.md)
* [About Memory Tuning](About-Memory-Tuning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*