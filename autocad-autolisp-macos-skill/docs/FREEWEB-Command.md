# FREEWEB (Command)

Creates a free web light which is similar to a web light without a specified target.

## List of Prompts

The following prompts are displayed.

Specify source location <0,0,0>: *Enter coordinate values or* *use the pointing device*

Enter an option to change [[Name](FREEWEB-Command.md)/[Intensity factor](FREEWEB-Command.md)/[Status](FREEWEB-Command.md)/[Photometry](FREEWEB-Command.md)/[weB](FREEWEB-Command.md)/[shadoW](FREEWEB-Command.md)/[filterColor](FREEWEB-Command.md)/eXit] <eXit>:

NOTE:The LIGHTINGUNITS system variable must be set to a value other than 0 to create and use freeweb lights.

Name

Specifies the name of the light. You can use uppercase and lowercase letters, numbers, spaces, hyphens (-), and underscores
(\_) in the name. The maximum length is 256 characters.

Intensity Factor

Sets the intensity or brightness of the light. The range is 0.00 to the maximum value that is supported by your system.

Status

Turns the light on and off. If lighting is not enabled in the drawing, this setting has no effect.

Photometry

Photometry is available when the LIGHTINGUNITS system variable is set to 1 or 2. Photometry is the measurement of the luminous
intensities of visible light sources.

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

    Enter *f* to specify the perceived power in a luminous flux value.

    If you enter *i*, you can specify the intensity of the light based on an illuminance value.

    The illuminance value can be specified in either lux or foot-candles. Enter *d* to specify a distance to use to calculate illuminance.

Color
:   Specify the color of the light based on a color name or a Kelvin temperature. Enter *?* to display a list of color names.

    Enter a text string using wild card characters to display a partial listing of color names, or an asterisk (\*) to display
    all the possible choices.

    If you enter *k*, you can specify the color of the light based on a Kelvin temperature value.

Web

Specifies the intensity for a light at points on a spherical grid.

File
:   Specifies which web file to use to define the properties of the web. Web files have the file extension *.ies*.

X
:   Specifies the X rotation for the web.

Y
:   Specifies the Y rotation for the web.

Z
:   Specifies the Z rotation for the web.

Shadow

Makes the light cast shadows.

Off
:   Turns off display and calculation of shadows for the light. Turning shadows off increases performance.

Sharp
:   Displays shadows with sharp edges. Use this option to increase performance.

Soft Mapped
:   Displays realistic shadows with soft edges.

    Specifies the amount of memory to use to calculate the shadow map.

Softness
:   Specifies the softness that should be used to calculate the shadow map.

Soft Sampled
:   Displays realistic shadows with softer shadows (penumbra) based on extended light sources.

    Specify the shape of the shadow by entering *s* and then the dimensions of the shape. (For example, the radius of the sphere or the length and width of a rectangle.)

    Specify the sample size by entering *a*.

    Specify the visibility of the shape by for the shadow by entering *v*.

Filter Color

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

* [About Weblights](About-Weblights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*