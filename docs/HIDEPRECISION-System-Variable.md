# HIDEPRECISION (System Variable)

Controls the accuracy of hides and shades.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

Hides can be calculated in double precision or single precision. Setting HIDEPRECISION to 1 produces more accurate hides by
using double precision, but this setting also uses more memory and can affect performance, especially when hiding solids.

| 0 | Single precision; uses less memory |
| 1 | Double precision; uses more memory |

#### Related References

* [About Hiding Lines in 3D Objects](About-Hiding-Lines-in-3D-Objects.md)

#### Related Concepts

* [About Using Visual Styles](About-Using-Visual-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*