# Tolerances Tab (Dimension Style Manager)

Specifies the display and format of dimension text tolerances.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-D341945F-D6B9-456A-BFB8-89D4CBCC59B8-low.png)

## List of Options

The following options are displayed.

Tolerance Format

Controls the tolerance format.

Method
:   Sets the method for calculating the tolerance. (DIMTOL system variable)

    * *None:* Does not add a tolerance. The DIMTOL system variable is set to 0.
    * *Symmetrical:* Adds a plus/minus expression of tolerance in which a single value of variation is applied to the dimension measurement. A
      plus-or-minus sign appears after the dimension. Enter the tolerance value in Upper Value. The DIMTOL system variable is set
      to 1. The DIMLIM system variable is set to 0.

    ![](../images/GUID-CC6D5BC6-5C7B-4330-924A-A15F2EF4FCA5-low.png)

    * *Deviation:* Adds a plus/minus tolerance expression. Different plus and minus values of variation are applied to the dimension measurement.
      A plus sign (+) precedes the tolerance value entered in Upper Value, and a minus sign (-) precedes the tolerance value entered
      in Lower Value. The DIMTOL system variable is set to 1. The DIMLIM system variable is set to 0.

    ![](../images/GUID-F576DE8C-5CEF-4C9B-8E11-D64CA9C15C17-low.png)

    * *Limits:* Creates a limit dimension. A maximum and a minimum value are displayed, one over the other. The maximum value is the dimension
      value plus the value entered in Upper Value. The minimum value is the dimension value minus the value entered in Lower Value.
      The DIMTOL system variable is set to 0. The DIMLIM system variable is set to 1.

    ![](../images/GUID-2D7048DC-2FE3-4E80-BA06-B415AA30B8B6-low.png)

    * *Basic:* Creates a basic dimension, which displays a box around the full extents of the dimension. The distance between the text and
      the box is stored as a negative value in the DIMGAP system variable.

    ![](../images/GUID-A9615C23-F1D2-4AA9-981A-16DF178290DC-low.png)

Precision
:   Sets the number of decimal places. (DIMTDEC system variable)

Upper Value
:   Sets the maximum or upper tolerance value. When you select Symmetrical in Method, this value is used for the tolerance. (DIMTP
    system variable)

Lower Value
:   Sets the minimum or lower tolerance value. (DIMTM system variable)

Scaling for Height
:   Sets the current height for the tolerance text. The ratio of the tolerance height to the main dimension text height is calculated
    and stored in the DIMTFAC system variable.

Vertical Position
:   Controls text justification for symmetrical and deviation tolerances.

    * *Top:* Aligns the tolerance text with the top of the main dimension text. When you select this option, the DIMTOLJ system variable
      is set to 2.

      ![](../images/GUID-6F58FEC3-2390-43E9-9906-B94E485C961C-low.png)

    * *Middle:* Aligns the tolerance text with the middle of the main dimension text. When you select this option, the DIMTOLJ system variable
      is set to 1.

    ![](../images/GUID-F576DE8C-5CEF-4C9B-8E11-D64CA9C15C17-low.png)

    * *Bottom:* Aligns the tolerance text with the bottom of the main dimension text. When you select this option, the DIMTOLJ system variable
      is set to 0.

      ![](../images/GUID-2E06C647-11E9-40A5-955E-8383F3A16B85-low.png)

Align

Controls the alignment of upper and lower tolerance values when stacked

Decimal Separators
:   Values are stacked by their decimal separators.

Operational Symbols
:   Values are stacked by their operational symbols.

Suppress

Controls the suppression of leading and trailing zeros and of feet and inches that have a value of zero. (DIMTZIN system variable)

Zero suppression settings also affect real-to-string conversions performed by the AutoLISP ® *rtos* and
*angtos* functions.

Leading Zeros
:   Suppresses leading zeros in all decimal dimensions. For example, 0.5000 becomes .5000.

Trailing Zeros
:   Suppresses trailing zeros in all decimal dimensions. For example, 12.5000 becomes 12.5, and 30.0000 becomes 30.

0 Feet
:   Suppresses the feet portion of a feet-and-inches dimension when the distance is less than 1 foot. For example, 0'-6 1/2" becomes
    6 1/2".

0 Inches
:   Suppresses the inches portion of a feet-and-inches dimension when the distance is an integral number of feet. For example,
    1'-0" becomes 1'.

Alternate Unit Tolerance

Formats alternate tolerance units.

Precision
:   Displays and sets the number of decimal places. (DIMALTTD system variable)

Suppress

Controls the suppression of leading and trailing zeros and of feet and inches that have a value of zero. (DIMALTTZ system
variable)

Leading Zeros
:   Suppresses leading zeros in all decimal dimensions. For example, 0.5000 becomes .5000.

Trailing Zeros
:   Suppresses trailing zeros in all decimal dimensions. For example, 12.5000 becomes 12.5, and 30.0000 becomes 30.

0 Feet
:   Suppresses the feet portion of a feet-and-inches dimension when the distance is less than 1 foot. For example, 0'-6 1/2" becomes
    6 1/2".

0 Inches
:   Suppresses the inches portion of a feet-and-inches dimension when the distance is an integral number of feet. For example,
    1'-0" becomes 1'.

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*