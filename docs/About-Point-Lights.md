# About Point Lights

A point light radiates light in all directions from its location.

### Point Lights

A point light radiates light in all directions from its location. A point light does not target an object, but illuminates
everything around it. Use such point lights for general lighting effects.

The difference between the target point light and a point light is the additional target properties that are available. A
target light can be pointed to an object. A target point light can also be created from a point light by changing the target
property of the point light from *No* to *Yes*.

In the standard lighting workflow, you can set a point light manually so its intensity diminishes with respect to distance
either linearly, according to the inverse square of the distance, or not at all. By default, the attenuation is set to None.

![](../images/GUID-B7558EE7-E6E9-4252-9ACC-9D81244DF97C-low.png)

## Point Lights in Photometric Workflow

A free point light can have photometric distribution properties. The attenuation for a photometric point light is always
set to inverse square.

When the LIGHTINGUNITS system variable is set to 1 (American units) or 2 (International SI units) for photometric lighting,
additional properties are available for a point light. The following photometric properties can be set via the Properties
Inspector palette:

* *Lamp Intensity.* Specifies the inherent brightness of the light. Specifies the intensity, flux or illuminance of the lamp.
* *Resulting Intensity.* Gives the final brightness of the light. (Product of lamp intensity and intensity factor. Read-only.)
* *Lamp Color.* Specifies the inherent color of the light in Kelvin temperature or standard.
* *Resulting Color.* Gives the final color of the light. This is determined by a combination of the lamp color and the filter color. (Product
  of lamp color and filter color. Read-only.)

NOTE:When the drawing lighting units are photometric, the attenuation type property becomes disabled. Photometric lights have fixed,
inverse-square attenuation.

#### Related Concepts

* [About Lighting](About-Lighting.md)
* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)

#### Related Information

* [To Work With Lighting Settings](To-Work-With-Lighting-Settings.md)
* [To Create a Point Light in Standard Lighting Workflow](To-Create-a-Point-Light-in-Standard-Lighting-Workflow.md)
* [To Create a Point Light in Photometric Workflow](To-Create-a-Point-Light-in-Photometric-Workflow.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*