# Dimension Style Overrides (DXF)

Dimension style overrides can be applied to dimension, leader, and tolerance entities. Any overrides applied to these entities
are stored in the entity as xdata. The overridden dimension variable group codes and the related values are contained within
group 1002 control strings. The following example shows the xdata of a dimension entity where the DIMTOL and DIMCLRE variables
have been overridden.

```
(setq diment (car (entsel))) ; Select dimension entity
(setq elst (entget diment '("ACAD"))) ; Get entity definition list
(assoc -3 elst) ; Extract xdata only
```

This code returns the following:

```
(-3 ("ACAD" Start of the ACAD APPID section of xdata
  (1000 . "DSTYLE") (1002 . "{") Beginning of the dimstyle subsection
  (1070 . 177) (1070 . 3) The DIMCLRE (code 177) override + value (3)
  (1070 . 71) (1070 . 1) The DIMTOL (code 71) override + value (1)
  (1002 . "}") )) End dimstyle subsection and ACAD section
```

#### Related References

* [DIMENSION (DXF)](DIMENSION-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*