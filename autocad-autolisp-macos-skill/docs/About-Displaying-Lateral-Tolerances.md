# About Displaying Lateral Tolerances

Lateral tolerances are values indicating the amount a measured distance can vary. You can control whether lateral tolerances
are displayed and you can choose from several styles of lateral tolerances.

A lateral tolerance specifies the amount by which a dimension can vary. By specifying tolerances in manufacturing, you can
control the degree of accuracy needed for a feature. A feature is some aspect of a part, such as a point, line, axis, or surface.

You can apply tolerances directly to a dimension by appending the tolerances to the dimension text. These dimension tolerances
indicate the largest and smallest permissible size of the dimension. You can also apply geometric tolerances, which indicate
deviations of form, profile, orientation, location, and runout.

Lateral tolerances can be specified from theoretically exact measurements. These are called basic dimensions and have a box
drawn around them.

If the dimension value can vary in both directions, the plus and minus values you supply are appended to the dimension value
as deviation tolerances. If the deviation tolerance values are equal, they are displayed with a ± sign and they are known
as symmetrical. Otherwise, the plus value goes above the minus value.

![](../images/GUID-2311631F-1D8C-456B-A4B2-6506D34622E2-low.png)

If the tolerances are applied as limits, the program uses the plus and minus values you supply to calculate a maximum and
minimum value. These values replace the dimension value. If you specify limits, the upper limit goes above the lower.

![](../images/GUID-550AD3FB-BD65-4D50-BECE-33E555612F26-low.png)

## Format Lateral Tolerances

You can control the vertical placement of tolerance values relative to the main dimension text. Tolerances can align with
the top, middle, or bottom of the dimension text.

![](../images/GUID-5D55A583-92EA-45F8-868F-C5FA659ED06A-low.png)

Along with vertical placement of tolerance values, you can also control the horizontal alignment of the upper and lower tolerance
values. The upper and lower tolerance values can be aligned using either the operational symbols or decimal separators.

![](../images/GUID-A0CCAA51-5E62-4AA7-9762-85FFCC8D06C3-low.png)

You can also control zero suppression as you can with the primary and alternate units. Suppressing zeros in lateral tolerances
has the same effect as suppressing them in the primary and alternate units. If you suppress leading zeros, 0.5 becomes .5,
and if you suppress trailing zeros, 0.5000 becomes 0.5.

#### Related Tasks

* [To Specify Style Settings for Lateral Tolerances](To-Specify-Style-Settings-for-Lateral-Tolerances.md)
* [To Align and Suppress Zeros in Tolerance Values](To-Align-and-Suppress-Zeros-in-Tolerance-Values.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*