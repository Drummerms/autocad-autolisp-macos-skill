# Text Tab (Dimension Style Manager)

Sets the format, placement, and alignment of dimension text.

DIMSTYLE (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Dimension panel ![](../images/ac.menuaro.gif) Dimension Style
![](../images/GUID-89D5BC05-30EE-4627-B80B-8680F08A01A9-low.png) :
![](../images/GUID-370B208A-7720-44F1-9172-CE646CB91807-low.png) ![](../images/ac.menuaro.gif) Modify.

![](../images/GUID-D1ED4D24-DD4C-415C-947A-48A8D4152310-low.png)

## List of Options

The following options are displayed.

Text Appearance

Controls the dimension text format and size.

Text Style
:   Lists the available text styles.

Text Style Button
:   Displays the
    [Text Style Dialog Box](Text-Style-Dialog-Box.md) where you can create or modify text styles. (DIMTXSTY system variable)

Text Color
:   Sets the color for the dimension text. If you click Select Color (at the bottom of the Color list), the
    [Color Palette dialog box](Color-Palette-Dialog-Box.md) is displayed. You can also enter color name or number. (DIMCLRT system variable)

Fill Color
:   Sets the color for the text background in dimensions. If you click Select Color (at the bottom of the Color list), the
    [Color Palette dialog box](Color-Palette-Dialog-Box.md) is displayed. You can also enter color name or number. (DIMTFILL and DIMTFILLCLR system variables)

Text Height
:   Sets the height of the current dimension text style. Enter a value in the text box. If a fixed text height is set in the Text
    Style (that is, the text style height is greater than 0), that height overrides the text height set here. If you want to use
    the height set on the Text tab, make sure the text height in the Text Style is set to 0. (DIMTXT system variable)

Fraction Height Scale
:   Sets the scale of fractions relative to dimension text. This option is available only when Fractional is selected as the Unit
    Format on the Primary Units tab. The value entered here is multiplied by the text height to determine the height of dimension
    fractions relative to dimension text. (DIMTFAC system variable)

Show Text Frame
:   When selected, draws a frame around dimension text. Selecting this option changes the value stored in the
     [DIMGAP](DIMGAP-System-Variable.md) system variable to a negative value.

Placement

Controls the placement of dimension text.

Vertical
:   Controls the vertical placement of dimension text in relation to the dimension line. (DIMTAD system variable)

    Vertical position options include the following:

    * *Centered:* Centers the dimension text between the two parts of the dimension line.
    * *Above:* Places the dimension text above the dimension line. The distance from the dimension line to the baseline of the lowest line
      of text is the current text gap. See the Offset from Dim Line option.
    * *Outside:* Places the dimension text on the side of the dimension line farthest away from the first defining point.
    * *JIS:* Places the dimension text to conform to a Japanese Industrial Standards (JIS) representation.
    * *Below:* Places the dimension text under the dimension line. The distance from the dimension line to the baseline of the lowest line
      of text is the current text gap. See the Offset from Dim Line option.

    ![](../images/GUID-2DF261A8-7EA4-4271-A281-1669A08A8F6C-low.png)

Horizontal
:   Controls the horizontal placement of dimension text along the dimension line, in relation to the extension lines. (DIMJUST
    system variable)

    Horizontal position options include the following:

    * *Centered:* Centers the dimension text along the dimension line between the extension lines.
    * *At Ext Line 1:* Left-justifies the text with the first extension line along the dimension line. The distance between the extension line and
      the text is twice the arrowhead size plus the text gap value. See Arrowheads and Offset from Dim Line.
    * *At Ext Line 2:* Right-justifies the text with the second extension line along the dimension line. The distance between the extension line
      and the text is twice the arrowhead size plus the text gap value. See Arrowheads and Offset from Dim Line.

    ![](../images/GUID-C2706CF8-F53B-471B-9FB4-52237D286840-low.png)

    * *Over Ext Line 1:* Positions the text over or along the first extension line.
    * *Over Ext Line 2:* Positions the text over or along the second extension line.

    ![](../images/GUID-C6D08AE5-3F77-4A7B-B30B-CCCBB4E2EE89-low.png)

View Direction
:   Controls the dimension text viewing direction. (DIMTXTDIRECTION system variable)

    View Direction includes the following options:

    * *Left-to-Right:* Places the text to enable reading from left to right.
    * *Right-to-Left:* Places the text to enable reading from right to left.

Offset from Dim Line
:   Sets the current text gap, which is the distance around the dimension text when the dimension line is broken to accommodate
    the dimension text.

    This value is also used as the minimum length required for dimension line segments.

    Text is positioned inside the extension lines only if the resulting segments are at least as long as the text gap. Text above
    or below the dimension line is placed inside only if the arrowheads, dimension text, and a margin leave enough room for the
    text gap. (DIMGAP system variable)

    ![](../images/GUID-E702CE46-32B4-41CD-A977-DF9DFA712B2F-low.png)

Alignment

Controls the orientation (horizontal or aligned) of dimension text whether it is inside or outside the extension lines. (DIMTIH
and DIMTOH system variables)

Horizontal
:   Places text in a horizontal position.

    ![](../images/GUID-57D5A180-CDE0-4BBE-913C-ADF074E8B4F2-low.png)

Aligned with Dimension Line
:   Aligns text with the dimension line.

ISO Standard
:   Aligns text with the dimension line when text is inside the extension lines, but aligns it horizontally when text is outside
    the extension lines.

    ![](../images/GUID-72593946-2C09-48F2-91E8-E457B3DA43D6-low.png)

Preview

Displays sample dimension images that show the effects of changes you make to dimension style settings.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*