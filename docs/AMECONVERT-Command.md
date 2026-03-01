# AMECONVERT (Command)

Converts AME solid models to AutoCAD solid objects.

## Summary

The objects you select must be Advanced Modeling Extension (AME) Release 2 or 2.1 regions or solids. All other objects are
ignored.

![](../images/GUID-4E1B4559-B91C-4616-8F7E-6309A7B90988-low.png)

Because of increased accuracy in the new solid modeler, AME models may look slightly different after conversion. This difference
is noticeable where the previous version of the solid modeler identified the surfaces of two different shapes as so close
as to be considered in the same plane. The new solid modeler's finer tolerance may interpret these surfaces as being slightly
offset. This phenomenon is most apparent with aligned features such as fillets, chamfers, and through-holes.

Holes might become blind holes when the new modeler, with its much finer approximation capability, interprets what was once
a through-hole as being slightly less wide than the solid. Typically, the length of the remaining solid material is the difference
between the tolerance of the previous modeler and that of the new modeler.

Likewise, updated fillets or chamfers can occasionally be placed slightly below the surface, creating a hole through the solid,
leaving the original shape unaltered. Also, drawing fillets or chamfers slightly above the original surface creates an uneven
transition between the solid and the fillet or chamfer.

#### Related Concepts

* [About Using Models With Other Autodesk Applications](About-Using-Models-With-Other-Autodesk-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*