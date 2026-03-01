# About Light Properties

Every light in a drawing has general and specific lighting properties that can be changed after the light is placed.

When a light is selected, its properties can be changed from the Properties palette.

Light properties are grouped into the following categories:

* *General.* Properties common to all light types.
* *Photometric Properties.* Photometric related properties that are available when the LIGHTINGUNITS system variable is set to 1 or 2.
* *Geometry.* Properties that define the position, target, or direction of a light.
* *Attenuation.* Properties that control how light is diminished over distance.

## General Properties

The following properties are common to all lights:

* *Name.* Specifies the name assigned to the light.
* *Type.* Specifies the type of light: Point, Spotlight, Distant, or Web.
* *On/Off Status.* Controls whether the light is enabled.
* *Intensity factor.* Sets a multiplier that controls brightness.

  Intensity is not related to attenuation.
* *Filter color.* Sets the color of the light emitted.
* *Plot glyph.* Controls whether light glyphs are plottable.

## Spotlight Properties: Hotspot and Falloff

When light from a spotlight falls onto a surface, the area of maximum illumination is surrounded by an area of lesser intensity.

![](../images/GUID-CD33B74D-9332-4A65-8359-670CFD527408-low.png)

* *Hotspot cone angle.* Defines the brightest part of a light beam. Also known as the *beam angle*.
* *Falloff cone angle.* Defines the full cone of light. Also known as the *field angle*.
* *Rapid decay area.* Consists of the region between the hotspot and falloff angles.

The greater the difference between the hotspot and falloff angles, the softer the edge of the light beam. If the hotspot and
falloff angles are near equal, the edge of the light beam is sharp. Both values can range from 0 to 160 degrees. You can also
adjust these values directly with the Hotspot and Falloff grips.

## Photometric Properties

Photometric lighting offers additional properties to define lighting that represents real world light sources. The following
properties are under the Photometric Properties category:

* *Lamp intensity.* Specifies the inherent brightness of the light. Specifies the intensity, flux, or illuminance of the lamp.
* *Resulting intensity.* Gives the final brightness of the light. (Product of lamp intensity and intensity factor. Read-only.)
* *Lamp color.* Specifies the inherent color of the light in Kelvin temperature or standard.
* *Resulting color.* Gives the final color of the light. This is determined by a combination of the lamp color and filter color. (Product of lamp
  color and filter color. Read-only.)

If the type of light selected is a weblight, additional properties are offered in the Photometric Web and Web Offsets sub-categories.

* *Web file.* Specifies the IES data file describing the intensity distribution of the light.
* *Web preview.* Displays a 2D slice through goniometric data.
* *Rotation of X.* Specifies a rotational offset of the web about the optical X axis.
* *Rotation of Y.* Specifies a rotational offset of the web about the optical Y axis.
* *Rotation of Z.* Specifies a rotational offset of the web about the optical Z axis.

## Attenuation Properties (Point Light and Spotlight)

Attenuation controls how light diminishes over distance. The farther away an object is from a light, the darker the object
appears. You can specify no attenuation, inverse linear, or inverse squared. All photometric lights use inverse squared attenuation
and don't support the use of light limits; the settings under the Attenuation category are disabled when the LIGHTINGUNITS
system variable is set to 1 or 2.

NOTE:Starting with AutoCAD 2016-based products, all lighting is calculated using inverse square attenuation. This option is maintained
for backwards compatibility with AutoCAD 2015-based products and earlier releases.

The following attenuation types are available for standard lights:

* *None.* Attenuation is disabled. Objects far from the point light are as bright as objects close to the light.
* *Inverse Linear.* Sets attenuation to be the inverse of the linear distance from the light. For example, at a distance of 2 units, light is
  half as strong as at the point light; at a distance of 4 units, light is one quarter as strong. The default value for inverse
  linear is half the maximum intensity.
* *Inverse Square.* Sets attenuation to be the inverse of the square of the distance from the light. For example, at a distance of 2 units, light
  is one quarter as strong as at the point light; at a distance of 4 units, light is one sixteenth as strong.

NOTE:Starting with AutoCAD 2016-based products, all standard lights are calculated as photometric lights. It is recommended to
update all standard lights in a scene to photometric lights.

Another way to control the attenuation for standard lights is to use limits. Limits work like clipping planes to control
where light is first emitted and where it stops. Using limits can increase performance by removing the need for the program
to calculate light levels where the light is already practically invisible.

![](../images/GUID-7E0F02FA-275B-4EED-9FE9-36673732803C-low.png)

## Geometry Properties

The Geometry properties of a light define its position and the direction in which light is emitted. If the light is a target
point light, spotlight, or weblight, additional target point properties are available. The *Target* property of a light can also be turned on or off. Distant lights are defined using a from, to, and source vector.

#### Related Information

* [To Work With the Adjustment of Lights](To-Work-With-the-Adjustment-of-Lights.md)
* [To Work With the Display of Light Glyphs](To-Work-With-the-Display-of-Light-Glyphs.md)
* [About the Shape Property of a Light](About-the-Shape-Property-of-a-Light.md)
* [To Specify a Source Vector for a Distant Light](To-Specify-a-Source-Vector-for-a-Distant-Light.md)
* [To Change the Color of a Light](To-Change-the-Color-of-a-Light.md)
* [To Assign a Shape to a Light](To-Assign-a-Shape-to-a-Light.md)
* [To Set Attenuation in a Point Light or a Spotlight](To-Set-Attenuation-in-a-Point-Light-or-a-Spotlight.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*