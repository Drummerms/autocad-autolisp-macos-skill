# About Spotlights

A spotlight distribution casts a focused beam of light like a flashlight, a follow spot in a theater, or a headlight. A spotlight
emits a directional cone of light. You can control the direction of the light and the size of the cone. Like a point light,
a spot light can be manually set to attenuate its intensity with distance. However, a spotlight's intensity will also always
attenuate based on the angle relative to the spot's target vector. This attenuation is controlled by the hotspot and falloff
angles of the spotlight. Spotlights are useful for highlighting specific features and areas in your model.

![](../images/GUID-CA3390BB-D3BC-4CDF-9BAF-3D3A6048B70C-low.png)

## Spotlights in Photometric Workflow

In photometric workflow, the hotspot intensity falls to 50 percent. The hotspot for standard lighting is at 100 percent.
At its falloff angle, intensity of the spotlight falls to zero. Additional properties become available for a point light when
LIGHTINGUNITS is set to 1 (American units) or 2 (International SI units) for photometric lighting:

* *Lamp Intensity.* Specifies the inherent brightness of the light. Specifies the intensity, flux, or illuminance of the lamp.
* *Resulting Intensity.* Gives the final brightness of the light. (Product of lamp intensity and intensity factor. Read-only.)
* *Lamp Color.* Specifies the inherent color of the light in Kelvin temperature or standard.
* *Resulting Color.* Gives the final color of the light. This is determined by a combination of the lamp color and the filter color. (Product
  of lamp color and filter color. Read-only.)

NOTE:

When the drawing lighting units are photometric, the *attenuation type* property becomes disabled. Photometric lights have fixed, inverse-square attenuation. The hotspot falloff attenuation in
the rendered image varies from standard lighting, as it uses a different mathematical basis.

#### Related Tasks

* [To Create a Free Spotlight in Photometric Lighting Workflow](To-Create-a-Free-Spotlight-in-Photometric-Lighting-Workflow.md)

#### Related Information

* [To Create a Target Point Light From a Point Light](To-Create-a-Target-Point-Light-From-a-Point-Light.md)
* [To Create a Target Point Light in Standard Lighting Workflow](To-Create-a-Target-Point-Light-in-Standard-Lighting-Workflow.md)
* [To Create a Spotlight](To-Create-a-Spotlight.md)
* [To Create a Photometric Spotlight](To-Create-a-Photometric-Spotlight.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*