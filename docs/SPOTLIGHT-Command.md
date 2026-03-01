# SPOTLIGHT (Command)

Creates a spotlight that emits a directional cone of light.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Render panel ![](../images/ac.menuaro.gif) Light drop-down ![](../images/ac.menuaro.gif) New Spotlight.
![](../images/GUID-7002CB13-2ADA-4FB8-8D7E-D4E46FE84116-low.png)

*Menu*:
View ![](../images/ac.menuaro.gif) Render ![](../images/ac.menuaro.gif) Light ![](../images/ac.menuaro.gif) New Spotlight.

## Summary

A spotlight distribution casts a focused beam of light like a flashlight, a follow spot in a theater, or a headlight.

## List of Prompts

The following prompts are displayed.

Specify source location <0,0,0>:
*Enter coordinate values or**use the pointing device*

Specify target location <1,1,1>:
*Enter coordinate values or**use the pointing device*

If the LIGHTINGUNITS system variable is set to 0, the following prompt is displayed:

Enter an option to change [[Name](SPOTLIGHT-Command.md)/[Intensity](SPOTLIGHT-Command.md)/[Status](SPOTLIGHT-Command.md)/[Hotspot](SPOTLIGHT-Command.md)/[Falloff](SPOTLIGHT-Command.md)/[shadoW](SPOTLIGHT-Command.md)/[Attenuation](SPOTLIGHT-Command.md)/[Color](SPOTLIGHT-Command.md)/[eXit](SPOTLIGHT-Command.md)] <eXit>:

If the LIGHTINGUNITS system variable is set to 1 or 2, the following prompt is displayed:

Enter an option to change [[Name](SPOTLIGHT-Command.md)/[Intensity factor](SPOTLIGHT-Command.md)/[Photometry](SPOTLIGHT-Command.md)/[Status](SPOTLIGHT-Command.md)/[Hotspot](SPOTLIGHT-Command.md)/[Falloff](SPOTLIGHT-Command.md)/[shadoW](SPOTLIGHT-Command.md)/[Attenuation](SPOTLIGHT-Command.md)/[filterColor](SPOTLIGHT-Command.md)/[eXit](SPOTLIGHT-Command.md)] <eXit>:

NOTE:When the LIGHTINGUNITS system variable is set to 1 or 2, the Attenuation option has no affect on the creation of the light.
It is only maintained for scripting compatibility.

Name

Specifies the name of the light. You can use uppercase and lowercase letters, numbers, spaces, hyphens (-), and underscores
(\_) in the name.

Intensity/Intensity Factor

Sets the intensity or brightness of the light. The range is 0.00 to the maximum value that is supported by your system.

Hotspot

Specifies the angle that defines the brightest cone of light, which is known to lighting designers as the beam angle. This
value can range from 0 to 160 degrees or the equivalent values based on
[AUNITS](AUNITS-System-Variable.md).

Falloff

Specifies the angle that defines the full cone of light, which is also known as the field angle. This value can range from
0 to 160 degrees. The default is 50 degrees or the equivalent values based on
 [AUNITS](AUNITS-System-Variable.md). The falloff angle must be greater than or equal to the hotspot angle.

Status

Turns the light on and off.

Photometry

Photometry is the measurement of the luminous intensities of visible light sources. Photometry is available when the LIGHTINGUNITS
system variable is set to 1 or 2.

In photometry, luminous intensity is a measure of the perceived power emitted by a light source in a particular direction.
Luminous flux is the perceived power per unit of solid angle. The total luminous flux for a lamp is the perceived power emitted
in all directions. Luminance is the total luminous flux incident on a surface, per unit area.

Intensity
:   Enter an intensity value in candelas, the perceived power in a luminous flux value, or illuminance value for the total luminous
    flux incident on a surface.

    * Candela (symbol: cd) is the SI unit of luminous intensity (perceived power emitted by a light source in a particular direction).
      Cd/Sr
    * Lux (symbol: lx) is the SI unit of illuminance. Lm/m^2
    * Foot-candle (symbol: fc) is the American unit of illuminance. Lm/ft^2

    Enter
    *f* to specify the perceived power in a luminous flux value.

    If you enter
    *i*, you can specify the intensity of the light based on an illuminance value.

    The illuminance value can be specified in either lux or foot-candles. Enter
    *d* to specify a distance to use to calculate illuminance.

Color
:   Specify the color of the light based on a color name or a Kelvin temperature. Enter ? to display a list of color names.

    Enter a text string using wild card characters to display a partial listing of color names, or an asterisk (\*) to display
    all the possible choices.

    If you enter
    *k*, you can specify the color of the light based on a Kelvin temperature value.

Shadow

Makes the light cast shadows.

Off
:   Turns off display and calculation of shadows for the light. Turning shadows off increases performance.

Sharp
:   Displays shadows with sharp edges. Use this option to increase performance.

Soft Mapped
:   Displays realistic shadows with soft edges.

    * *Map Size*. Specifies the amount of memory to use to calculate the shadow map.
    * *Softness*. Specifies the softness to use to calculate the shadow map.

Soft Sampled
:   Displays realistic shadows with softer shadows (penumbra) based on extended light sources.

    Specify the shape of the shadow by entering
    *s* and then the dimensions of the shape. (For example, the radius of the sphere or the length and width of a rectangle.)

    Specify the sample size by entering
    *a.*

    Specify the visibility of the shape by for the shadow by entering
    *v.*

Attenuation

Attenuation Type
:   Controls how light diminishes over distance. The farther away an object is from a spotlight, the darker the object appears.
    Attenuation is also known as decay.

    * *None*. Sets no attenuation. Objects far from the spotlight are as bright as objects close to the light.
    * *Inverse Linear.* Sets attenuation to be the inverse of the linear distance from the light. For example, at a distance of 2 units, light is
      half as strong as at the spotlight; at a distance of 4 units, light is one quarter as strong. The default value for inverse
      linear is half the maximum intensity.
    * *Inverse Squared.* Sets attenuation to be the inverse of the square of the distance from the light. For example, at a distance of 2 units, light
      is one quarter as strong as at the spotlight; at a distance of 4 units, light is one sixteenth as strong.

Use Limits
:   Specifies whether to use limits.

Attenuation Start Limit
:   Specifies the point where light starts as an offset from the center of the light. The default is 0.

Attenuation End Limit
:   Specifies the point where light ends as an offset from the center of the light. No light is cast beyond this point. Setting
    an end limit increases performance where the effect of lighting is so minimal that the calculations are wasted processing
    time.

Color/Filter Color

Controls the color of the light.

True Color
:   Specifies a True Color. Enter in the format R,G,B (red, green, blue).

Index
:   Specifies an ACI (AutoCAD Color Index) color.

HSL
:   Specifies an HSL (hue, saturation, luminance) color.

Color Book
:   Specifies a color from a color book.

Exit

Exits the command.

#### Related Concepts

* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)
* [About Spotlights](About-Spotlights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*