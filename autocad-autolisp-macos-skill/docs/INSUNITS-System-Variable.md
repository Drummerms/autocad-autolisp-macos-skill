# INSUNITS (System Variable)

Specifies a drawing-units value for automatic scaling of blocks, images, or xrefs when inserted or attached to a drawing.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 (imperial) or 4 (metric) |

For information on how the scale of a block or drawing inserted into the current drawing is calculated, see
[About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md).

NOTE:The INSUNITS setting is ignored when inserting annotative blocks into a drawing.

| Value | Description |
| 0 | Unspecified (No units) |
| 1 | Inches |
| 2 | Feet |
| 3 | Miles |
| 4 | Millimeters |
| 5 | Centimeters |
| 6 | Meters |
| 7 | Kilometers |
| 8 | Microinches |
| 9 | Mils |
| 10 | Yards |
| 11 | Angstroms |
| 12 | Nanometers |
| 13 | Microns |
| 14 | Decimeters |
| 15 | Dekameters |
| 16 | Hectometers |
| 17 | Gigameters |
| 18 | Astronomical Units |
| 19 | Light Years |
| 20 | Parsecs |
| 21 | US Survey Feet |
| 22 | US Survey Inch |
| 23 | US Survey Yard |
| 24 | US Survey Mile |

NOTE:

* US Survey Feet is a historical survey unit that's about 2 parts per million larger than the International Feet unit. This
  difference is significant only at scales used for mapping in the U.S. The US Survey Feet setting is supported only for inserting
  or attaching drawings starting with AutoCAD 2017-based products. Drawings opened in prior versions will treat the US Survey
  Feet setting as Unitless.
* US Survey Inch, US Survey Yard, and US Survey Mile are supported on AutoCAD for Mac only.

#### Related Concepts

* [About Block Units and Insertion Scale](About-Block-Units-and-Insertion-Scale.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*