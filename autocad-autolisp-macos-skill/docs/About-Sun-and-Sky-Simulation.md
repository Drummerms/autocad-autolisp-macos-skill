# About Sun and Sky Simulation

A special light is available to simulate the effect of sunlight. It can be used in conjunction with sky simulation to provide
a dramatic background and show how the shadows cast by a structure affect the surrounding area.

The sun is a light that simulates the effect of sunlight and can be used to show how the shadows cast by a structure affect
the surrounding area.

Sun and sky are the primary sources of natural illumination in AutoCAD. Whereas the rays of the sun are parallel and of a
yellowish hue, the light cast from the atmosphere comes from all directions and is distinctly bluish in color.

When the workflow is photometric (the LIGHTINGUNITS system variable is set to 1 or 2) the sun properties have more properties
available and are rendered using a more physically accurate sunlight model. The sun color is disabled for the photometric
sun; the color is computed automatically based on the time, date, and location specified in the drawing. The color is determined
based on the position in the sky.

NOTE:Starting with AutoCAD 2017-based products, you can no longer set a drawing to standard lighting (LIGHTINGUNITS=0).

The properties of the sun can be modified by using the Properties Inspector (PROPERTIES command).

The rays of the sun are parallel and have the same intensity at any distance. Shadows can be on or off. To improve performance,
turn off shadows when you don't need them. All settings for the sun except geographic location are saved per viewport, not
per drawing. Geographic location is saved per drawing.

The angle of the light from the sun is controlled by the geographic location you specify for your model and by the date and
time of day. These are properties of the sun and can be changed in the Properties Inspector. The time zone used is based on
the location, but you can adjust it independently (TIMEZONE system variable).

#### Related Tasks

* [To Enable the Sunlight System](To-Enable-the-Sunlight-System.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*