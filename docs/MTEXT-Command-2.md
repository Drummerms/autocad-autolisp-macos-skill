# -MTEXT (Command)

Creates a multiline text object.

## List of Prompts

The following prompts are displayed.

Specify first corner.

Specify opposite corner or [Height/Justify/Line spacing/Rotation/Style/Width/Columns].

Opposite Corner

As you drag the pointing device to specify the opposite corner, a rectangle is displayed to show the location and size of
the multiline text object. Arrows within the rectangle indicate the direction of the paragraph's text flow.

Height

Specifies the text height to use for multiline text characters.

* *Specify Height.*

The Specify Height prompt is displayed only if the current text style is not annotative.

* *Specify Paper Text Height.*

The Specify Paper Text Height prompt is displayed only if the current text style is annotative.

The default height, if nonzero, is the height of the current style; otherwise, it is the height stored in the
[TEXTSIZE](TEXTSIZE-System-Variable.md) system variable. Character height is calculated in drawing units. Changing the height updates the value stored in TEXTSIZE.

Justify

Determines both text justification and text flow, for new or selected text, in relation to the text boundary. The current
justification is applied to new text. The text is justified within the specified rectangle based on the justification setting
and one of nine justification points on the rectangle. The justification point is based on the first point used to specify
the rectangle. Text is center-, left-, or right-justified with respect to the left and right text boundaries. Spaces entered
at the end of a line are included as part of the text and affect the justification of the line. Text flow controls whether
text is aligned from the middle, the top, or the bottom of the paragraph with respect to the top and bottom text boundaries.

Enter justification [TL/TC/TR/ML/MC/MR/BL/BC/BR] <TL>.

| Justify Options | |
| Option | Meaning |
| TL | Top Left |
| TC | Top Center |
| TR | Top Right |
| ML | Middle Left |
| MC | Middle Center |
| MR | Middle Right |
| BL | Bottom Left |
| BC | Bottom Center |
| BR | Bottom Right |

The following illustrations show each justification option.

![](../images/GUID-108BEB66-F6F8-456E-BB83-9B17F903E7EB-low.png)

Line Spacing

Specifies line spacing for the multiline text object. Line spacing is the vertical distance between the bottom (or baseline)
of one line of text and the bottom of the next line of text.

NOTE:Exact spacing is recommended when you use MTEXT to create a table. Use a smaller text height than the specified line spacing
to ensure that text does not overlap.

At Least
:   Adjusts lines of text automatically based on the height of the largest character in the line. When At Least is selected, lines
    of text with taller characters have added space between lines.

Distance
:   Sets the line spacing to an absolute value measured in drawing units. Valid values must be between 0.0833 (0.25x) and 1.3333
    (4x).

Exactly
:   Forces the line spacing to be the same for all lines of text in the multiline text object. Spacing is based on the text height
    of the object or text style.

Spacing Factor
:   Sets the line spacing to a multiple of single-line spacing.

    Single spacing is 1.66 times the height of the text characters. You can enter a spacing factor as a number followed by
    *x* to indicate a multiple of single spacing. For example, specify single spacing by entering
    *1x*, or specify double spacing by entering
    *2x*.

Rotation

Specifies the rotation angle of the text boundary.

* *Specify rotation angle.*

If you use the pointing device to specify a point, the rotation angle is determined by the angle between the
*X* axis and the line defined by the most recently entered point (default 0,0,0) and the specified point.

The previous prompt is redisplayed until you specify the opposite corner of the text boundary.

Style

Specifies the text style to use for multiline text.

Style Name
:   Specifies a text style name. Text styles can be defined and saved using the
    [STYLE](STYLE-Command-2.md) command.

?—List Styles
:   Lists text style names and characteristics.

The previous prompt is redisplayed until you specify the opposite corner of the text boundary.

Width

Specifies the width of the text boundary.

If you use the pointing device to specify a point, the width is calculated as the distance between the start point and the
specified point. Words within each line of the multiline text object wrap to fit the width of the text boundary. If you specify
a width of 0, word wrap is turned off and the width of the multiline text object is as wide as the longest line of text. You
can end a line of text at a specific point by typing the text and pressing Enter. To end the command, press Enter at the MTEXT
prompt.

Columns

Specifies the column options for an mtext object.

Static
:   Specifies the total column width, the number of columns, the gutter width (the space between the columns), and the height
    of columns.

Dynamic
:   Specifies column width, gutter width and column height. Dynamic columns are text driven. Adjusting columns affect text flow
    and text flow causes columns to be added or removed.

No columns
:   Sets no column mode to current mtext object.

The default column setting is stored in the
[MTEXTCOLUMN](MTEXTCOLUMN-System-Variable.md) system variable.

#### Related Concepts

* [About Text Styles](About-Text-Styles.md)
* [About Creating Notes Using Text](About-Creating-Notes-Using-Text.md)

#### Related Information

* [MTEXT (Command)](MTEXT-Command.md)
* [In-Place Text Editor](In-Place-Text-Editor.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*