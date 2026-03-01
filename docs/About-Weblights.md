# About Weblights

A weblight (web) is a 3D representation of the light intensity distribution of a light source. Weblights can be used to represent
anisotropic (non-uniform) light distributions derived from data provided by manufacturers of real-world lights. This gives
a far more precise representation of the rendered light than either a spotlight or point light is capable of.

This directional light distribution information is stored in a photometric data file in the IES format using the IES LM-63-1991
standard file format for photometric data.

To describe the directional distribution of the light emitted by a source, the source is approximated by a point light placed
at its photometric center. With this approximation, the distribution is characterized as a function of the outgoing direction
only. The luminous intensity of the source for a predetermined set of horizontal and vertical angles is provided, and the
system can compute the luminous intensity along an arbitrary direction by interpolation.

NOTE:Web distribution is used only in rendered images. Weblights are approximated as point lights in the viewport.

## Goniometric Diagrams

Photometric data is often depicted using a goniometric diagram.

![](../images/GUID-28DE6CA6-9036-414B-A143-6B89BAB289C9-low.png)

Goniometric diagram of a web distribution

This type of diagram visually represents how the luminous intensity of a source varies with the vertical angle. However, the
horizontal angle is fixed and, unless the distribution is axially symmetric, more than one goniometric diagram may be needed
to describe the complete distribution.

## Photometric Webs

The photometric web is a three dimensional representation of the light distribution. It extends the goniometric diagram to
three dimensions, so that the dependencies of the luminous intensity on both the vertical and horizontal angles can be examined
simultaneously. The center of the photometric web represents the center of the light object.

The luminous intensity in any given direction is proportional to the distance between this web and the photometric center,
measured along a line leaving the center in the specified direction.

![](../images/GUID-EE4695E1-4048-417D-8BDE-CBEEDF0F9E0A-low.png)

Example of Isotropic distribution

A sphere centered around the origin is a representation of an isotropic distribution. All the points in the diagram are equidistant
from the center and therefore light is emitted equally in all directions.

![](../images/GUID-90DD594C-C991-420F-8068-0E2213049225-low.png)

Example of Ellipsoidal distribution

In this example, the points in the negative Z direction are the same distance from the origin as the corresponding points
in the positive Z direction, so the same amount of light shines upward and downward. No point has a very large X or Y component,
either positive or negative, so less light is cast laterally from the light source.

#### Related Concepts

* [About IES Standard File Format](About-IES-Standard-File-Format.md)

#### Related Information

* [To Create a Web Distribution With a Manufacturer’s IES File](To-Create-a-Web-Distribution-With-a-Manufacturer’s-IES-File.md)
* [To Create a Distant Light](To-Create-a-Distant-Light.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*