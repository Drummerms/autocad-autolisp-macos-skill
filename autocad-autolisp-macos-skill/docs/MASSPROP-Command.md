# MASSPROP (Command)

Calculates the mass properties of regions or 3D solids.

## Access Methods

*Menu*:Tools
![](../images/ac.menuaro.gif) Inquiry
![](../images/ac.menuaro.gif) Region/Mass Properties.

## Summary

Refer to the Help system for a complete list of definitions for each of the region or mass properties computed.

## List of Prompts

The following prompts are displayed.

Select objects:
*Use an object selection method*

If you select multiple regions, only those that are coplanar with the first selected region are accepted.

MASSPROP displays the mass properties in the text window, and then asks if you want to write the mass properties to a text
file (.*mpr*).

The properties that MASSPROP displays depend on whether the selected objects are regions, and whether the selected regions
are coplanar with the
*XY* plane of the current user coordinate system (UCS), or 3D solids. For a list of the parameters that control the MASSPROP units,
see
[Calculations Based on the Current UCS](MASSPROP-Command.md).

Regions

The following table shows the mass properties that are displayed for all regions.

| Mass properties for all regions | |
| Mass property | Description |
| Area | The surface area of solids or the enclosed area of regions. |
| Perimeter | The total length of the inside and outside loops of a region. The perimeter of a solid is not calculated. |
| Bounding box | The two coordinates that define the bounding box. For regions that are coplanar with the *XY* plane of the current user coordinate system, the bounding box is defined by the diagonally opposite corners of a rectangle that encloses the region. For regions that are not coplanar with the *XY* plane of the current UCS, the bounding box is defined by the diagonally opposite corners of a 3D box that encloses the region. |
| Centroid | A 2D or 3D coordinate that is the center of area for regions. For regions that are coplanar with the *XY* plane of the current UCS, this coordinate is a 2D point. For regions that are not coplanar with the *XY* plane of the current UCS, this coordinate is a 3D point. |

If the regions are coplanar with the
*XY* plane of the current UCS, the additional properties shown in the following table are displayed.

| Additional mass properties for coplanar regions | |
| Mass property | Description |
| Moments of inertia | A value used when computing the distributed loads, such as fluid pressure on a plate, or when calculating the forces inside a bending or twisting beam. The formula for determining area moments of inertia is    area\_moments\_of\_inertia = area\_of\_interest \* radius 2    The area moments of inertia has units of distance to the fourth power. |
| Products of inertia | Property used to determine the forces causing the motion of an object. It is always calculated with respect to two orthogonal planes. The formula for product of inertia for the *YZ* plane and *XZ* plane is    product\_of\_inertia YZ,XZ  = mass \* dist centroid\_to\_YZ  \* dist centroid\_to\_XZ    This *XY* value is expressed in mass units times the length squared. |
| Radii of gyration | Another way of indicating the moments of inertia of a 3D solid. The formula for the radii of gyration is    gyration\_radii = (moments\_of\_ inertia/body\_mass) 1/2    Radii of gyration are expressed in distance units. |
| Principal moments and *X,Y,Z* directions about centroid | Calculations that are derived from the products of inertia and that have the same unit values. The moment of inertia is highest through a certain axis at the centroid of an object. The moment of inertia is lowest through the second axis that is normal to the first axis and that also passes through the centroid. A third value included in the results is somewhere between the high and low values. |

3D Solids

The following table shows the mass properties that are displayed for solids.

| Mass properties for solids | |
| Mass property | Description |
| Mass | The measure of inertia of a body. Because a density of one is used, mass and volume have the same value. |
| Volume | The amount of 3D space that a solid encloses. |
| Bounding box | The diagonally opposite corners of a 3D box that encloses the solid. |
| Centroid | A 3D point that is the center of mass for solids. A solid of uniform density is assumed. |
| Moments of inertia | The mass moments of inertia, which is used when computing the force required to rotate an object about a given axis, such as a wheel rotating about an axle. The formula for mass moments of inertia is    mass\_moments\_of\_inertia = object\_mass \* radius axis  2    Mass moments of inertia unit is mass (grams or slugs) times the distance squared. |
| Products of inertia | Property used to determine the forces causing the motion of an object. It is always calculated with respect to two orthogonal planes. The formula for product of inertia for the *YZ* plane and *XZ* plane is    product\_of\_inertia YZ,XZ  = mass \* dist centroid\_to\_YZ  \* dist centroid\_to\_XZ    This *XY* value is expressed in mass units times the length squared. |
| Radii of gyration | Another way of indicating the moments of inertia of a solid. The formula for the radii of gyration is    gyration\_radii = (moments\_of\_inertia/body\_mass) 1/2    Radii of gyration are expressed in distance units. |
| Principal moments and *X,Y,Z* directions about centroid | Calculations that are derived from the products of inertia and that have the same unit values. The moment of inertia is highest through a certain axis at the centroid of an object. The moment of inertia is lowest through the second axis that is normal to the first axis and that also passes through the centroid. A third value included in the results is somewhere between the high and low values. |

Calculations Based on the Current UCS

The following table shows the parameters that control the units in which mass properties are calculated.

| Parameters that control MASSPROP units | |
| Parameter | Used to calculate |
| DENSITY | Mass of solids |
| LENGTH | Volume of solids |
| LENGTH\*LENGTH | Area of regions and surface area of solids |
| LENGTH\*LENGTH\*LENGTH | Bounding box, radii of gyration, centroid, and perimeter |
| DENSITY\*LENGTH\*LENGTH | Moments of inertia, products of inertia, and principal moments |

#### Related References

* [Commands for Areas and Mass Properties](Commands-for-Areas-and-Mass-Properties.md)
* [Commands for Regions and Areas](Commands-for-Regions-and-Areas.md)

#### Related Information

* [About Finding Area and Mass Properties Information](About-Finding-Area-and-Mass-Properties-Information.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*