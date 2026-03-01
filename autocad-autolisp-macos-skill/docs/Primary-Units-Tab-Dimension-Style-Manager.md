# Primary Units Tab (Dimension Style Manager)

Sets the format and precision of primary dimension units and sets prefixes and suffixes for dimension text.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-135CC7BD-4698-4928-A6DB-C3939CCDE139-low.png)

## List of Options

The following options are displayed.

Linear Dimensions

Sets the format and precision for linear dimensions.

Unit Format
:   Sets the current units format for all dimension types except Angular. (DIMLUNIT system variable)

    The relative sizes of numbers in stacked fractions are based on the DIMTFAC system variable (in the same way that tolerance
    values use this system variable).

Precision
:   Displays and sets the number of decimal places in the dimension text. (DIMDEC system variable)

Fraction Format
:   Sets the format for fractions. (DIMFRAC system variable)

Decimal Separator
:   Sets the separator for decimal formats. (DIMDSEP system variable)

Round Off
:   Sets rounding rules for dimension measurements for all dimension types except Angular. If you enter a value of
    *0.25*, all distances are rounded to the nearest 0.25 unit. If you enter a value of
    *1.0*, all dimension distances are rounded to the nearest integer. The number of digits displayed after the decimal point depends
    on the Precision setting. (DIMRND system variable)

Prefix
:   Includes a prefix in the dimension text. You can enter text or use control codes to display special symbols. For example,
    entering the control code
    *%%c* displays the diameter symbol. When you enter a prefix, it overrides any default prefixes such as those used in diameter and
    radius dimensioning. (DIMPOST system variable)

    ![](../images/GUID-0103D683-A051-4094-954A-137B4B96B345-low.png)

    If you specify tolerances, the prefix is added to the tolerances as well as to the main dimension.

Suffix
:   Includes a suffix in the dimension text. You can enter text or use control codes to display special symbols. For example,
    entering the text
    *mm* results in dimension text similar to that shown in the illustration. When you enter a suffix, it overrides any default suffixes.
    (DIMPOST system variable)

    ![](../images/GUID-BFE18AB3-EBB1-4300-A38A-22C9B40C0520-low.png)

    If you specify tolerances, the suffix is added to the tolerances as well as to the main dimension.

Scale Factor
:   Sets a scale factor for linear dimension measurements. It is recommended that you do not change this value from the default
    value of 1.00. For example, if you enter
    *2*, the dimension for a 1-inch line is displayed as two inches. The value does not apply to angular dimensions and is not applied
    to rounding values or to plus or minus tolerance values. (DIMLFAC system variable)

Apply to Layout Dimension Only
:   Applies the measurement scale factor only to dimensions created in layout viewports. Except when using nonassociative dimensions,
    this setting should remain unchecked. (DIMLFAC system variable)

Zero Suppression

Controls the suppression of leading and trailing zeros and of feet and inches that have a value of zero. (DIMZIN system variable)

Zero suppression settings also affect real-to-string conversions performed by the AutoLISP ®  *rtos* and
*angtos* functions.

Leading
:   Suppresses leading zeros in all decimal dimensions. For example, 0.5000 becomes .5000. Select leading to enable display of
    dimension distances less than one unit in sub units.

Sub-units factor
:   Sets the number of sub units to a unit. It is used to calculate the dimension distance in a sub unit when the distance is
    less than one unit. For example, enter
    *100* if the suffix is
    *m* and the sub-unit suffix is to display in
    *cm*.

Sub-unit suffix
:   Includes a suffix to the dimension value sub unit. You can enter text or use control codes to display special symbols. For
    example, enter
    *cm* for .96m to display as 96cm.

Trailing
:   Suppresses trailing zeros in all decimal dimensions. For example, 12.5000 becomes 12.5, and 30.0000 becomes 30.

0 Feet
:   Suppresses the feet portion of a feet-and-inches dimension when the distance is less than one foot. For example, 0'-6 1/2"
    becomes 6 1/2".

0 Inches
:   Suppresses the inches portion of a feet-and-inches dimension when the distance is an integral number of feet. For example,
    1'-0" becomes 1'.

Angular Dimensions

Displays and sets the current angle format for angular dimensions.

Units Format
:   Sets the angular units format. (DIMAUNIT system variable)

Precision
:   Sets the number of decimal places for angular dimensions. DIMADEC system variable)

Zero Suppression

Controls the suppression of leading and trailing zeros. (DIMAZIN system variable)

Leading
:   Suppresses leading zeros in angular decimal dimensions. For example, 0.5000 becomes .5000.

    You can also display dimension distances less than one unit in sub units.

Trailing
:   Suppresses trailing zeros in angular decimal dimensions. For example, 12.5000 becomes 12.5, and 30.0000 becomes 30.

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*