# Lighting Properties

Sets the properties of the lights.

## Summary

Different properties area available depending on the lighting units (standard or photometric) and lighting type (Spotlight,
Pointlight, or Weblight). Other lighting types such as Freespot, Targetpoint, and Freeweb display similar properties. By right-clicking
on a light and clicking Properties, the Lighting category of the
[Properties Inspector](GUID-0AA644F1-1165-492F-A4D1-3EDA8598C644.htm#WSC30CD3D5FAA8F6D81BCA5F1FFC2D6150D-7F64) is displayed.

## List of Options

The following options are displayed.

General Properties

The following property settings are available:

Name
:   Specifies the name of the light.

Type (Light Distribution)
:   Specifies the type of light. Determines the distribution of light from the . The type of lighting can be changed after the
    light has been added to the drawings.

    * Spotlight - Default value for Spotlight and Freespot lights.
    * Point - Default for Pointlight and Targetpoint lights.
    * Web - Default for Weblight and Freeweb lights.

On/Off Status
:   Indicates whether the light is on or off.

Shadows
:   Indicates if the light is casting a shadow.

Hotspot Angle (Spotlight and Freespot only)
:   Specifies the angle of the brightest cone of light.

Falloff Angle (Spotlight and Freespot only)
:   Specifies the outer extremity of the light, where it meets the darkness.

Filter Color
:   Specifies the secondary color of the light. Represents the color of a physical filter over the lamp. Default color is white.

    When lighting is set to photometric units this represents a secondary color filter on the light. When lighting is set to generic
    lighting this represents the total color of the light.

Plot Glyph
:   Allows the ability to plot the drawing with the glyphs on.

Photometric Properties

The following property settings are available:

Lamp Color
:   Specifies the inherent color of the light in Kelvin temperature or standard.

Resulting Color
:   Reports the final color of the light. This is determined by a combination of the Lamp Color and the Filter Color. (Read-only)

Intensity Method
:   Specifies the value in which light intensity should be measured.

    * *Intensity (Candela).* Specifies the number of candelas (cd) is the SI unit of luminous intensity (perceived power emitted by a light source in
      a particular direction).
    * *Flux (Lumen).* Represents the rate of total energy leaving the lamp. It is specified in lumens (SI and American). Mathematically, the flux
      is the integral of the luminous intensity over the sphere. The calculation of flux depends on the distribution of intensities.
      For a point light with constant intensity, the flux is simply the product of the intensity and the solid angle of a sphere:
      4 Pi \* Intensity. For a spot light, the flux is the product of the intensity and the solid angle of the hotspot cone, plus
      the incremental solid angle of the fall-off region. For a weblight, there isn’t any analytical formula. The flux is obtained
      by numerically integrating the intensities provided in the web file.
    * *Illuminance (Foot-candles).* Represents the energy per area arriving at a surface (Area-flux-density). It is specified in lux (SI) and foot-candles (American).
      For a near light, because the light rays are diverging, you have to talk about the illuminance at a specific distance from
      the lamp. So this requires an extra control to specify this distance and an additional affordance in the viewport to show
      the distance.

Lamp Intensity
:   Specifies the brightness of a lamp. More specifically, it represents the luminous intensity, or power in a particular direction.

Intensity Factor
:   Magnifies the effect of the skylight.

Resulting Intensity
:   Reports the final brightness of the light. This is determined by the product of the Lamp Intensity and the Intensity factor.
    (Read-only)

Photometric Web

The following property settings are available for Web and Freeweb lights:

Web File
:   Specifies the data file describing the intensity distribution of the light.

Web Offsets

Under the Web offsets panel, the following property settings are available under the Weblight and Freeweb types of lights:

Rotate X
:   Specifies a rotational offset of the web about the optical X axis.

Rotate Y
:   Specifies a rotational offset of the web about the optical Y axis.

Rotate Z
:   Specifies a rotational offset of the web about the optical Z axis.

Geometry

Under the Geometry panel, the following property settings are available:

Position X
:   Specifies the X coordinate position of the light.

Position Y
:   Specifies the Y coordinate position of the light.

Position Z
:   Specifies the Z coordinate position of the light.

Target X
:   Specifies the X coordinate target position of the light. (Spotlight, Targetpoint, and Weblight only)

Target Y
:   Specifies the Y coordinate target position of the light. (Spotlight, Targetpoint, and Weblight only)

Target Z
:   Specifies the Z coordinate target position of the light. (Spotlight, Targetpoint, and Weblight only)

Targeted
:   Specifies if the light displays a target grip for orienting the light. Disabled is the default for Freespot, Pointlight, and
    Freeweb. Enabled is the default for Spotlight, Targetpoint, and Weblight.

Attenuation

In the real world, the intensity of light diminishes over distance. Objects far from the light source appear darker than objects
near the source. This effect is known as attenuation. Attenuation is available under standard lighting workflow only. Under
the Attenuation panel the following property settings are available:

Type
:   Controls how light diminishes over distance. The farther away an object is from a spotlight, the darker the object appears.
    Attenuation is also known as decay.

    * Inverse Linear (Standard lights only). Sets attenuation to be the inverse of the linear distance from the light. For example,
      at a distance of 2 units, light is half as strong as at the point light; at a distance of 4 units, light is one quarter as
      strong. The default value for inverse linear is half the maximum intensity.
    * Inverse Square (Photometric lights). Sets attenuation to be the inverse of the square of the distance from the light. For
      example, at a distance of 2 units, light is one quarter as strong as at the spotlight; at a distance of 4 units, light is
      one sixteenth as strong.
    * None (Standard lights only). Sets no attenuation. Objects far from the point light are as bright as objects close to the light.

Use Limits
:   Specifies whether to use limits. The default is No. (Standard lights only)

Rendered Shadow Details

Under the Rendered Shadow Details panel, the following property settings are available:

Type
:   Specifies the type of shadow cast by the light.

    * Soft (shadow map). Sets the type to Soft. This selection activates additional options for Map size and Softness.

    * Sharp (default). Sets the rendered shadow to sharp.

    * Soft (sampled). Sets attenuation to be the inverse of the square of the distance from the light. For example, at a distance
      of 2 units, light is one quarter as strong as at the spotlight; at a distance of 4 units, light is one sixteenth as strong.

Map Size
:   Specifies the size of the shadow map. (Soft shadow map type only)

Softness
:   Specifies the softness or fuzziness of the shadow-mapped shadow. (Soft shadow map type only)

Samples
:   Specifies the number of shadow rays for the light. (Soft sampled type only)

Visible in Render
:   Specifies whether the light shape is actually rendered. The default is No. (Soft sampled type only)

Shape
:   Specifies the shape of the lamp bulb. For the Spotlight distribution type selection under the General panel, options are Rectangle
    (default) and Disk. For Point and Web types the options are Linear, Rectangle, Disk, Cylinder and Sphere (default). (Soft
    sampled type only)

Length
:   Specifies spacial dimension of shadow shape for the length of the shadow. (Soft sampled type only)

Width
:   Specifies spacial dimension of shape for the width of the shadow. (Soft sampled type only)

Radius
:   Specifies spacial radius dimension of the shape selection of disk, cylinder, or sphere. (Soft sampled type only)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*