# TEXT (Command)

Creates a single-line text object.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Text panel ![](../images/ac.menuaro.gif) Single Line Text.
![](../images/GUID-21420186-1EEC-4CDF-AD22-AEC4A6B190C6-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Text ![](../images/ac.menuaro.gif) Single Line Text.

## Summary

You can use single-line text to create one or more lines of text, where each text line is an independent object that you
can move, format, or otherwise modify. Right-click in the text box to select options on the shortcut menu.

If TEXT was the last command entered, pressing Enter at the Specify Start Point of Text prompt skips the prompts for paper
height and rotation angle. The text that you enter in the text box is placed directly beneath the previous line of text. The
point that you specified at the prompt is also stored as the insertion point of the text.

When creating text, you can click anywhere in a drawing to create a new text block. You can also use the keyboard to move
among text blocks (for example: for new text created using the TEXT command, you can navigate through text groups by pressing
Tab or Shift+Tab, or edit a group of text lines by pressing Alt and clicking each text object.)

NOTE:Text that would otherwise be difficult to read (if it is very small, very large, or is rotated) is displayed at a legible
size and is oriented horizontally so that you can easily read and edit it.

You can enter special characters and format text by entering Unicode strings and control codes.

Use -TEXT to honor the TEXTEVAL system variable.

## List of Prompts

The following prompts are displayed.

Current text style:
*<current>* Current text height:
*<current>*Annotative:
*<current>*

Specify start point of text or [Justify/Style]:
*Specify a point or enter an option*

Start Point

Specifies a start point for the text object. Enter text in the In-Place Text Editor for single-line text.

The SpecifyHeight prompt is displayed only if the current text style is not annotative and does not have a fixed height.

The Specify Paper Text Height prompt is displayed only if the current text style is annotative.

![](../images/GUID-F3859A35-BC17-4D52-9070-5FF2181398DC-low.png)

Justify

Controls justification of the text.

You can also enter any of these options at the Specify Start Point of Text prompt.

Align
:   Specifies both text height and text orientation by designating the endpoints of the baseline.

    The size of the characters adjusts in proportion to their height. The longer the text string, the shorter the characters.

    ![](../images/GUID-B137AD8B-2508-4F2F-A68E-88C005B030E3-low.png)

Fit
:   Specifies that text fits within an area and at an orientation defined with two points and a height. Available for horizontally
    oriented text only.

    ![](../images/GUID-1A15DF56-42F9-4178-A57D-F00F6F608795-low.png)

    The height is the distance in drawing units that the uppercase letters extend from the baseline. Designated text height is
    the distance between the start point and a point you specify. The longer the text string, the narrower the characters. The
    height of the characters remains constant.

Center
:   Aligns text from the horizontal center of the baseline, which you specify with a point.

    The rotation angle specifies the orientation of the text baseline with respect to the center point. You can designate the
    angle by specifying a point. The text baseline runs from the start point toward the specified point. If you specify a point
    to the left of the center point, the text is drawn upside down.

    ![](../images/GUID-DC6018C8-4768-4E0F-9D33-B45A81A85829-low.png)

Middle
:   Aligns text at the horizontal center of the baseline and the vertical center of the height you specify. Middle-aligned text
    does not rest on the baseline.

    The Middle option differs from the MC option in that it uses the midpoint of all text, including descenders. The MC option
    uses the midpoint of the height of uppercase letters.

    ![](../images/GUID-F9480DA0-D149-44EC-9083-9823F50806C8-low.png)

Right
:   Right-justifies the text at the baseline, which you specify with a point.

    ![](../images/GUID-1A805062-1090-4F1F-A8A0-5D544662B287-low.png)

TL (Top Left)
:   Left-justifies text at a point specified for the top of the text. Available for horizontally oriented text only.

    ![](../images/GUID-1C50AC97-8190-4A18-92EC-90E9BBD54A14-low.png)

TC (Top Center)
:   Centers text at a point specified for the top of the text. Available for horizontally oriented text only.

    ![](../images/GUID-8668ED0F-4A28-4563-8F64-9FBEC8E3329C-low.png)

TR (Top Right)
:   Right-justifies text at a point specified for the top of the text. Available for horizontally oriented text only.

    ![](../images/GUID-150CAB44-8C1E-4164-9135-B798D5F0C3FE-low.png)

ML (Middle Left)
:   Left-justifies text at a point specified for the middle of the text. Available for horizontally oriented text only.

    ![](../images/GUID-8EB80367-7C80-4E36-895A-DC04ABF1B3A6-low.png)

MC (Middle Center)
:   Centers the text both horizontally and vertically at the middle of the text. Available for horizontally oriented text only.

    The MC option differs from the Middle option in that it uses the midpoint of the height of uppercase letters. The Middle option
    uses the midpoint of all text, including descenders.

    ![](../images/GUID-BB4A8579-3144-4569-AAF2-543A4F5F5F29-low.png)

MR (Middle Right)
:   Right-justifies text at a point specified for the middle of the text. Available for horizontally oriented text only.

    ![](../images/GUID-0E03DE1D-6820-4BFB-8EB9-68F4ADB6ECB1-low.png)

BL (Bottom Left)
:   Left-justifies text at a point specified for the baseline. Available for horizontally oriented text only.

    ![](../images/GUID-FDB2CF82-4334-4C92-A8ED-2CB17DD76A6B-low.png)

BC (Bottom Center)
:   Centers text at a point specified for the baseline. Available for horizontally oriented text only.

    ![](../images/GUID-66222CE6-B642-4C33-8784-F2617E80CB91-low.png)

BR (Bottom Right)
:   Right-justifies text at a point specified for the baseline. Available for horizontally oriented text only.

    ![](../images/GUID-E7FDA3DB-451E-4239-965D-1E0BAEA5C17F-low.png)

Style

Specifies the text style, which determines the appearance of the text characters. Text you create uses the current text style.

Entering
*?* lists the current text styles, associated font files, height, and other parameters.

![](../images/GUID-7492C91B-C771-4BA4-9135-90843DC5DCBF-low.png)

#### Related References

* [Control Codes and Special Characters](Control-Codes-and-Special-Characters.md)
* [Special Unicode Characters](Special-Unicode-Characters.md)
* [Text Shortcut Menu](Text-Shortcut-Menu.md)
* [TEXTEVAL (System Variable)](TEXTEVAL-System-Variable.md)

#### Related Information

* [About Creating Notes Using Text](About-Creating-Notes-Using-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*