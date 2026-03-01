# DISTANTLIGHT (Command)

Creates a distant light.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Render panel ![](../images/ac.menuaro.gif) Light drop-down ![](../images/ac.menuaro.gif) New Distant Light.
![](../images/GUID-7F345E12-A694-45AA-930C-B18D4104EA58-low.png)

*Menu*:
View
![](../images/ac.menuaro.gif) Render
![](../images/ac.menuaro.gif) Light
![](../images/ac.menuaro.gif) New Distant Light.

## List of Prompts

The following prompts are displayed.

Specify light direction FROM <0,0,0> or [Vector]:
*Specify a point or enter* *v*

Specify light direction TO <1,1,1>:
*Specify a point*

If you enter the Vector option, the following prompt is displayed:

Specify vector direction <0.0000,-0.0100,1.0000>:
*Enter a vector*

After you specify the light direction and if the LIGHTINGUNITS system variable is set to 0, the following prompt is displayed:

Enter an option to change [[Name](DISTANTLIGHT-Command.md)/[Intensity](DISTANTLIGHT-Command.md)/[Status](DISTANTLIGHT-Command.md)/[shadoW](DISTANTLIGHT-Command.md)/[Color](DISTANTLIGHT-Command.md)/eXit] <eXit>:

If the LIGHTINGUNITS system variable is set to 1 or 2, the following prompt is displayed:

Enter an option to change [[Name](DISTANTLIGHT-Command.md)/[Intensity factor](DISTANTLIGHT-Command.md)/[Status](DISTANTLIGHT-Command.md)/[Photometry](DISTANTLIGHT-Command.md)/[shadoW](DISTANTLIGHT-Command.md)/[filterColor](DISTANTLIGHT-Command.md)/eXit] <eXit>:

NOTE:When the LIGHTINGUNITS system variable is set to 1 or 2, the Attenuation option has no affect on the creation of the light.
It is only maintained for scripting compatibility.

Name

Specifies the name of the light. You can use uppercase and lowercase letters, numbers, spaces, hyphens (-), and underscores
(\_) in the name. The maximum length is 256 characters.

Intensity/Intensity Factor

Sets the intensity or brightness of the light. The range is 0.00 to the maximum value that is supported by your system.

Status

Turns the light on and off. If lighting is not enabled in the drawing, this setting has no effect.

Photometry

Photometry is available when the LIGHTINGUNITS system variable is set to 1 or 2. Photometry is the measurement of the luminous
intensities of visible light sources.

In photometry, luminous intensity is a measure of the perceived power emitted by a light source in a particular direction.
Luminous flux is the perceived power per unit of solid angle. The total luminous flux is the perceived power emitted in all
directions. Luminance is the total luminous flux incident on a surface, per unit area.

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

    Enter a text string using wild card characters to display a partial listing of color names, or an asterick (\*) to display
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

    Specifies the amount of memory that should be used to calculate the shadow map.

    Specifies the softness to use to calculate the shadow map.

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

#### Related Concepts

* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*