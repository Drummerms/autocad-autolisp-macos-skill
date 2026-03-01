# PLINETYPE (System Variable)

Specifies whether optimized 2D polylines are used.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

PLINETYPE controls both the creation of new polylines with the PLINE command and the conversion of existing polylines in drawings
from previous releases.

| 0 | Polylines in older drawings are not converted when opened; PLINE creates old-format polylines |
| 1 | Polylines in older drawings are not converted when opened; PLINE creates optimized polylines |
| 2 | Polylines in AutoCAD Release 14 or older drawings are converted when opened; PLINE creates optimized polylines |

For more information on the two formats, see the
[CONVERT](CONVERT-Command.md) command.

PLINETYPE also controls the polyline type created with the following commands:
[BOUNDARY](BOUNDARY-Command.md) (when object type is set to Polyline),
[DONUT](DONUT-Command.md),
[PEDIT](PEDIT-Command.md) (when selecting a line or arc),
[POLYGON](POLYGON-Command.md), and
[SKETCH](SKETCH-Command.md) (when
[SKPOLY](SKPOLY-System-Variable.md) is set to 1).

#### Related Concepts

* [About Polylines](About-Polylines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*