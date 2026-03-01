# POINTLIGHT (Command)

Creates a point light that radiates light in all directions from its location.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Render panel ![](../images/ac.menuaro.gif) Light drop-down ![](../images/ac.menuaro.gif) New Point Light.
![](../images/GUID-B12DEAEE-5ABC-4685-B80D-AAA31F2E0B6F-low.png)

*Menu*:
View ![](../images/ac.menuaro.gif) Render ![](../images/ac.menuaro.gif) Light ![](../images/ac.menuaro.gif) New Point Light.

## Summary

Use point lights for general lighting effects.

## List of Prompts

The following prompts are displayed.

Specify source location <0,0,0>:
*Enter coordinate values or**use the pointing device*

If the LIGHTINGUNITS system variable is set to 0, the following prompt is displayed:

Enter an option to change [[Name](POINTLIGHT-Command.md)/[Intensity](POINTLIGHT-Command.md)/[Status](POINTLIGHT-Command.md)/[shadoW](POINTLIGHT-Command.md)/[Attenuation](POINTLIGHT-Command.md)/[Color](POINTLIGHT-Command.md)/[eXit](POINTLIGHT-Command.md)] <eXit>:

If the LIGHTINGUNITS system variable is set to 1 or 2, the following prompt is displayed:

Enter an option to change [[Name](POINTLIGHT-Command.md)/[Intensity factor](POINTLIGHT-Command.md)/[Status](POINTLIGHT-Command.md)/[Photometry](POINTLIGHT-Command.md)/[shadoW](POINTLIGHT-Command.md)/[Attenuation](POINTLIGHT-Command.md)/[filterColor](POINTLIGHT-Command.md)/[eXit](POINTLIGHT-Command.md)] <eXit>:

NOTE:When the LIGHTINGUNITS system variable is set to 1 or 2, the Attenuation option has no affect on the creation of the light.
It is only maintained for scripting compatibility.

Name

Specifies the name of the light. You can use uppercase and lowercase letters, numbers, spaces, hyphens (-), and underscores
(\_) in the name. The maximum length is 256 characters.

Enter light name:

Intensity/Intensity Factor

Sets the intensity or brightness of the light. The range is 0.00 to the maximum value that is supported by your system.

Enter intensity (0.00-max float) <1.0000>:

Status

Turns the light on and off. If lighting is not enabled in the drawing, this setting has no effect

Enter status [oN/oFf] <On>:

Photometry

Photometry is available when the LIGHTINGUNITS system variable is set to 1 or 2. Photometry is the measurement of the luminous
intensities of visible light sources.

In photometry, luminous intensity is a measure of the perceived power emitted by a light source in a particular direction.
Luminous flux is the perceived power per unit of solid angle. The total luminous flux for a is the perceived power emitted
in all directions. Luminance is the total luminous flux incident on a surface, per unit area.

Enter a photometric option to change [Intensity/Color/eXit] <I>:

Intensity
:   Enter intensity (Cd) or enter an option [Flux/Illuminance] <1500.0000>:

    Enter an intensity value in candelas, the perceived power in a luminous flux value, or illuminance value for the total luminous
    flux incident on a surface.

    * Candela (symbol: cd) is the SI unit of luminous intensity (perceived power emitted by a light source in a particular direction).
      Cd/Sr
    * Lux (symbol: lx) is the SI unit of illuminance. Lm/m^2
    * Foot-candle (symbol: fc) is the American unit of illuminance. Lm/ft^2

    Enter
    *f* to specify the perceived power in a luminous flux value.

    Enter Flux (Lm) <18849.5556>:

    If you enter
    *i*, you can specify the intensity of the light based on an illuminance value.

    Enter Illuminance ("Lx"|"Fc") or enter an option [Distance] <1500.0000>:

    The illuminance value can be specified in either lux or foot-candles. Enter
    *d* to specify a distance to use to calculate illuminance.

    Enter Distance <1.0000>:

Color
:   Enter color name or enter an option [?/Kelvin] <D65White>:

    Specify the color of the light based on a color name or a Kelvin temperature. Enter ? to display a list of color names.

    Enter color name(s) to list <\*>:

    Enter a text string using wild card characters to display a partial listing of color names, or an asterisk (\*) to display
    all the possible choices.

    If you enter
    *k*, you can specify the color of the light based on a Kelvin temperature value.

    Enter Kelvin temperature <3600.0000>:

Exit
:   Exits the command option.

Shadow

Makes the light cast shadows.

Enter shadow settings [Off/Sharp/soFtmapped/softsAmpled] <Sharp>:

Off
:   Turns off display and calculation of shadows for the light. Turning shadows off increases performance.

Sharp
:   Displays shadows with sharp edges. Use this option to increase performance.

Soft Mapped
:   Displays realistic shadows with soft edges.

    Enter map size [64/128/256/512/1024/2048/4096] <256>:

    Specifies the amount of memory to use to calculate the shadow map.

    Enter softness (1-10) <1>:

    Specifies the softness to use to calculate the shadow map.

Soft Sampled
:   Displays realistic shadows with softer shadows (penumbra) based on extended light sources.

    Enter an option to change [Shape/sAmples/Visible/eXit]<eXit> :

    Specify the shape of the shadow by entering
    *s* and then the dimensions of the shape. (For example, the radius of the sphere or the length and width of a rectangle.)

    Enter shape [Linear, Disk, Rect, Sphere,Cylinder] <Sphere>:

    Specify the sample size by entering
    *a.*

    Enter Shadow Sample <16.0000>:

    Specify the visibility of the shape by for the shadow by entering
    *v*.

    Enter Shape Visibility [Yes/No]<No>:

Attenuation

Enter an option to change [attenuation Type/Use limits/attenuation start Limit/attenuation End limit/eXit]<eXit>:

Attenuation Type
:   Controls how light diminishes over distance. The farther away an object is from a point light, the darker the object appears.
    Attenuation is also known as decay.

    Enter attenuation type [None/Inverse linear/inverse Squared] <Inverse linear>:

    * None. Sets no attenuation. Objects far from the point light are as bright as objects close to the light.
    * Inverse Linear. Sets attenuation to be the inverse of the linear distance from the light. For example, at a distance of 2
      units, light is half as strong as at the point light; at a distance of 4 units, light is one quarter as strong. The default
      value for inverse linear is half the maximum intensity.
    * Inverse Squared. Sets attenuation to be the inverse of the square of the distance from the light. For example, at a distance
      of 2 units, light is one quarter as strong as at the point light; at a distance of 4 units, light is one sixteenth as strong.

Use LimitsAttenuation Start Limit
:   Specifies whether to use limits or not.

    Limits [oN/oFf] <Off>:

    Specifies the point where light starts as an offset from the center of the light. The default is 0.

    Specify start limit offset <1.0000>:

Attenuation End Limit
:   Specifies the point where light ends as an offset from the center of the light. No light is cast beyond this point. Setting
    an end limit increases performance where the effect of lighting is so minimal that the calculations are wasted processing
    time.

    Specify end limit offset <10.0000>:

Color/Filter Color

Controls the color of the light.

Enter true color (R,G,B) or enter an option [Index color/Hsl/colorBook]<255,255,255>:

True Color
:   Specifies a True Color. Enter in the format R,G,B (red, green, blue).

Index
:   Specifies an ACI (AutoCAD Color Index) color.

    Enter color name or number (1-255):

HSL
:   Specifies an HSL (hue, saturation, luminance) color.

    Enter HSL color (H,S,L) <0,0,100>:

Color Book
:   Specifies a color from a color book.

    Enter Color Book name:

Exit

Exits the command.

#### Related Concepts

* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*