# SURFACEASSOCIATIVITY (System Variable)

Controls whether surfaces maintain a relationship with the objects from which they were created.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 |

When associativity is on, surfaces automatically adjust to modifications made to other, related surfaces.

| 0 | Surfaces are created with no associativity to other surfaces |
| 1 | Surfaces are created with associativity to other surfaces |

When set to 1, the [DELOBJ](DELOBJ-System-Variable.md) system variable is ignored. Defining geometry are not deleted when an associative surface is created.

#### Related Concepts

* [About Creating Associative Surfaces](About-Creating-Associative-Surfaces.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*