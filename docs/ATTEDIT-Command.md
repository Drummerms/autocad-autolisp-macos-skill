# -ATTEDIT (Command)

## List of Prompts

If you enter *-attedit* at the Command prompt, the following prompts are displayed.

Edit attributes one at a time? [[Yes](ATTEDIT-Command.md)/[No](ATTEDIT-Command.md)] <Y>:  *Enter* *y* *or press* Enter *to edit attributes one at a time, or enter* *n* *to edit attributes globally*

The following prompts filter the attributes to be changed based on attribute tag, current value, or object selection.

Yes

Edits attributes one at a time. Attributes to be edited one at a time must be visible and parallel to the current UCS.

Attribute values are case sensitive.

![](../images/GUID-9E89EBE4-F767-490A-B72F-AC1856E41926-low.png)

The first attribute in the selection set is marked with an *X*. You can change any properties of the attribute you select.

Enter an option [Value/Position/Height/Angle/Style/Layer/Color/Next] <N>: *Enter the property to change, or p**ress* Enter *for the next* *attribute*

If the original attribute was defined with aligned or fit text, the prompt does not include Angle. The Height option is omitted
for aligned text. For each of the options except Next, ATTEDIT prompts for a new value. The *X* remains on the current attribute until you move to the next attribute.

![](../images/GUID-98D583BB-79AF-4EB9-9E20-9D8A15BDF1E0-low.png)

![](../images/GUID-FA4BA91A-D3B5-4769-9578-43382F2C74A4-low.png)

Value

Changes or replaces an attribute value.

Enter type of value modification [Change/Replace]: *Enter* *c* *or* *r* *or press* Enter

Change
:   Modifies a few characters of the attribute value.

    Either string can be null. The ? and \* characters are interpreted literally, not as wild-card characters.

Replace
:   Substitutes a new attribute value for the entire attribute value.

    If you press Enter, the attribute value is empty (null).

Position

Changes the text insertion point.

![](../images/GUID-A469541F-038D-4B3C-B3F0-72CF2C6C5FC3-low.png)

If the attribute is aligned, ATTEDIT prompts for both ends of a new text baseline.

Height

Changes the text height.

![](../images/GUID-90E37E5B-2441-4084-A100-4564D391CE9B-low.png)

When you specify a point, the height becomes the distance between the specified point and the start point of the text.

Angle

Changes the rotation angle.

![](../images/GUID-0CD3A3C5-779B-42C9-8449-365E0B18909A-low.png)

If you specify a point, the text is rotated along an imaginary line between the specified point and the start point of the
text.

Style

Changes the style setting.

![](../images/GUID-31076597-5ED8-47CF-87F8-16070AD27BE5-low.png)

Layer

Changes the layer.

Color

Changes the color.

You can enter a color from the AutoCAD Color Index (a color name or number), a true color, or a color from a color book.

You can enter a color name, a color number between 1 and 255, or *bylayer* or *byblock*.

True Color
:   Specifies a true color to be used for the selected object.

Color Book
:   Specifies a color from a loaded color book to be used for the selected object.

    If you enter a color book name, you are prompted to enter the color name in the color book, such as PANTONE® 573.

Next

Moves to the next attribute in the selection set. If there are no more attributes, ATTEDIT ends.

No

Edits more than one attribute at a time. Global editing applies to both visible and invisible attributes.

Editing attributes globally limits you to replacing a single text string with another text string. If you edit attributes
one at a time, you can edit any or all of the attributes.

Yes
:   Edits only visible attributes.

    Attribute values are case sensitive. To select empty (null) attributes, which normally are not visible and cannot be selected,
    enter a backslash (\).

    Select the attribute you want to change.

    Either string can be empty (null). The ? and \* characters are interpreted literally, not as wild-card characters.

No
:   Edits attributes whether they are visible or not. Changes to attributes are not reflected immediately. The drawing is regenerated
    at the end of the command unless [REGENAUTO](REGENAUTO-Command.md), which controls automatic regeneration, is off.

    Attribute values are case sensitive. To select empty (null) attributes, which normally are not visible, enter a backslash
    (\).

    The attributes that match the specified block name, attribute tag, and attribute value are selected.

    Either string can be empty (null). The ? and \* characters are interpreted literally, not as wild-card characters.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*