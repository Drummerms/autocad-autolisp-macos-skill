# About Hatch Pattern Scaling

The scale of hatch patterns can be set individually, or it can be set automatically based on the scale of each layout viewport.

* If you create hatch patterns exclusively for a single view or at a constant scale, you can set the current hatch scale manually
  in the interface or with the HPSCALE system variable.
* If you work with layout viewports in different scales, you can apply scale factors automatically by creating *annotative* hatches. This method is more efficient than creating duplicate hatch pattern objects with different scale factors.

NOTE:To prevent accidentally creating an enormous number of hatch lines, the maximum number of hatch lines created in a single
hatch operation is controlled by the HPMAXLINES system variable. This limit prevents memory and performance problems. Similarly
the number of enclosed areas in single hatch is limited by the HPMAXAREAS system variable. Starting in the 2012 release, hatches
that are too *sparse* are also changed to solid fills. This is not always desired, so to restore the legacy behavior, which leaves sparse hatches
blank, set HPMAXAREAS to 0.

#### Related Concepts

* [About Annotative Objects and Styles](About-Annotative-Objects-and-Styles.md)

#### Related Information

* [To Set the Scale of a Hatch Pattern](To-Set-the-Scale-of-a-Hatch-Pattern.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*