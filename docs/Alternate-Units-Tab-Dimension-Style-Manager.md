# Alternate Units Tab (Dimension Style Manager)

Specifies display of alternate units in dimension measurements and sets their format and precision.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-14A5200A-2D43-431D-A391-B63C5DDFB619-low.png)

## List of Options

The following options are displayed.

Display Alternate Units

Adds alternate measurement units to dimension text. Sets the DIMALT system variable to 1.

Alternate Units

Displays and sets the current alternate units format for all dimension types except Angular.

Unit Format
:   Sets the unit format for alternate units. (DIMALTU system variable)

    The relative sizes of numbers in stacked fractions are based on DIMTFAC (in the same way that tolerance values use this system
    variable).

Precision
:   Sets the number of decimal places for alternate units. (DIMALTD system variable)

Multiplier for Alt Units
:   Specifies the multiplier used as the conversion factor between primary and alternate units. For example, to convert inches
    to millimeters, enter
    *25.4*. The value has no effect on angular dimensions, and it is not applied to the rounding value or the plus or minus tolerance
    values. (DIMALTF system variable)

Round Distances To
:   Sets rounding rules for alternate units for all dimension types except Angular. If you enter a value of
    *0.25*, all alternate measurements are rounded to the nearest 0.25 unit. If you enter a value of
    *1.0*, all dimension measurements are rounded to the nearest integer. The number of digits displayed after the decimal point depends
    on the Precision setting. (DIMALTRND system variable)

Prefix
:   Includes a prefix in the alternate dimension text. You can enter text or use control codes to display special symbols. For
    example, entering the control code
    *%%c*displays the diameter symbol. (DIMAPOST system variable)

    For more information, see
    [Control Codes and Special Characters](GUID-968CBC1D-BA99-4519-ABDD-88419EB2BF92.htm#WSC30CD3D5FAA8F6D8DF8F5EFFC2D62051-7FD7).

    ![](../images/GUID-236CBEC9-09DC-48C9-9903-7E909DA70EBE-low.png)

Suffix
:   Includes a suffix in the alternate dimension text. You can enter text or use control codes to display special symbols. For
    example, entering the text
    *cm*results in dimension text similar to that shown in the illustration. When you enter a suffix, it overrides any default suffixes.
    (DIMAPOST system variable)

    For more information, see
    [Control Codes and Special Characters](GUID-968CBC1D-BA99-4519-ABDD-88419EB2BF92.htm#WSC30CD3D5FAA8F6D8DF8F5EFFC2D62051-7FD7).

    ![](../images/GUID-459CA00B-39C2-416E-8C03-DF7F0EA78705-low.png)

Zero Suppression

Controls the suppression of leading and trailing zeros and of feet and inches that have a value of zero. (DIMALTZ system variable)

Leading
:   Suppresses leading zeros in all decimal dimensions. For example, 0.5000 becomes .5000.

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
:   Suppresses the feet portion of a feet-and-inches dimension when the distance is less than 1 foot. For example, 0'-6 1/2" becomes
    6 1/2".

0 Inches
:   Suppresses the inches portion of a feet-and-inches dimension when the distance is an integral number of feet. For example,
    1'-0" becomes 1'.

Placement

Controls the placement of alternate units in dimension text.

After Primary Value
:   Places alternate units after the primary units in dimension text.

Below Primary Value
:   Places alternate units below the primary units in dimension text.

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*