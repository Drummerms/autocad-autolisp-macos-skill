# Fit Tab (Dimension Style Manager)

Controls the placement of dimension text, arrowheads, leader lines, and the dimension line.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-B89B6624-7079-4A75-9183-CDB7637C060A-low.png)

## List of Options

The following options are displayed.

Fit Options

Controls the placement of text and arrowheads based on the space available between the extension lines.

![](../images/GUID-875D11F9-C9F8-494D-8877-E268CB574534-low.png)

When space is available, text and arrowheads are placed between the extension lines. Otherwise, text and arrowheads are placed
according to the Fit options. (DIMATFIT, DIMTIX, and DIMSOXD system variables)

Either Text or Arrows (Best Fit)
:   Moves either the text or the arrowheads outside the extension lines based on the best fit (DIMATFIT system variable).

    * When enough space is available for text and arrowheads, places both between the extension lines. Otherwise, either the text
      or the arrowheads are moved based on the best fit.
    * When enough space is available for text only, places text between the extension lines and places arrowheads outside the extension
      lines.
    * When enough space is available for arrowheads only, places them between the extension lines and places text outside the extension
      lines.
    * When space is available for neither text nor arrowheads, places them both outside the extension lines.

Arrows
:   Moves arrowheads outside the extension lines first, then text (DIMATFIT system variable).

    * When enough space is available for text and arrowheads, places both between the extension lines.
    * When space is available for arrowheads only, places them between the extension lines and places text outside them.
    * When not enough space is available for arrowheads, places both text and arrowheads outside the extension lines.

Text
:   Moves text outside the extension lines first, then arrowheads (DIMATFIT system variable).

    * When space is available for text and arrowheads, places both between the extension lines.
    * When space is available for text only, places the text between the extension lines and places arrowheads outside them.
    * When not enough space is available for text, places both text and arrowheads outside the extension lines.

Both Text and Arrows
:   When not enough space is available for text and arrowheads, moves both outside the extension lines (DIMATFIT system variable).

    ![](../images/GUID-1F93BA82-4A68-420D-81F8-E8AC12DFB76A-low.png)

Always Keep Text Between Ext Lines
:   Always places text between extension lines. (DIMTIX system variable)

    ![](../images/GUID-2AA80F16-0378-419C-857E-92869361DF2B-low.png)

Suppress Arrows If They Don't Fit Inside Extension Lines
:   Suppresses arrowheads if not enough space is available inside the extension lines. (DIMSOXD system variable)

Text Placement

Sets the placement of dimension text when it is moved from the default position, that is, the position defined by the dimension
style. (DIMTMOVE system variable)

![](../images/GUID-32F4B4C7-F15D-4FF6-BACA-A5955611304F-low.png)

Beside the Dimension Line
:   If selected, moves the dimension line whenever dimension text is moved. (DIMTMOVE system variable)

    ![](../images/GUID-E4BCA028-3DDA-4A53-8506-C86F556EAEDE-low.png)

Over the Dimension Line, with Leader
:   If selected, dimension lines are not moved when text is moved. If text is moved away from the dimension line, a leader line
    is created connecting the text to the dimension line. The leader line is omitted when text is too close to the dimension line.
    (DIMTMOVE system variable)

    ![](../images/GUID-0BED32B3-2CB9-4427-B7A5-D1A0414BE6E5-low.png)

Over the Dimension Line, Without Leader
:   If selected, dimension lines are not moved when text is moved. Text that is moved away from the dimension line is not connected
    to the dimension line with a leader. (DIMTMOVE system variable)

    ![](../images/GUID-EC00515C-E23A-443B-BED0-781704D81D69-low.png)

Scale for Dimension Features

Sets the overall dimension scale value or the paper space scaling.

Annotative
:   Specifies that the dimension is annotative. Click the information icon to learn more about annotative objects.

Scale Dimensions To Layout
:   Determines a scale factor based on the scaling between the current model space viewport and paper space. (DIMSCALE system
    variable)

    When you work in paper space, but not in a model space viewport, or when TILEMODE is set to 1, the default scale factor of
    1.0 is used or the DIMSCALE system variable.

Use Overall Scale Of
:   Sets a scale for all dimension style settings that specify size, distance, or spacing, including text and arrowhead sizes.
    This scale does not change dimension measurement values. (DIMSCALE system variable)

Fine Tuning

Provides additional options for placing dimension text.

Place Text Manually
:   Ignores any horizontal justification settings and places the text at the position you specify at the Dimension Line Location
    prompt. (DIMUPT system variable)

Draw Dim Line Between Ext Lines
:   Draws dimension lines between the measured points even when the arrowheads are placed outside the measured points. (DIMTOFL
    system variable)

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*