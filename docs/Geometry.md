# Geometry

Create basic geometric objects such as lines, circles, and hatched areas.

You can create a lot of different types of geometric objects in AutoCAD, but you only need to know a few of them for most
2D drawings.

TIP:If you want to simplify the display while you create geometric objects, press F12 or
![](../images/GUID-598052FD-166B-48E0-9A64-DBB598CD8039-low.png) on the touch bar, to turn off dynamic input at the cursor.

## Lines

The line is the most basic and common object in AutoCAD drawings. To draw a line, click the Line tool.

![](../images/GUID-BD9FB4D0-49B4-450C-854D-2EAF0E2F6593-low.png)

Alternatively, you can type LINE or just L in the Command window, and then press Enter or the Spacebar.

Notice the prompt in the Command window for a point location.

![](../images/GUID-B61C97E1-5670-490C-9973-0880F22A6072-low.png)

To specify the starting point for this line, you would type in the Cartesian coordinates 0,0. It's generally a good idea
to locate one corner of your model at 0,0, which is called the origin point. To locate additional points, you could specify
additional X,Y coordinate locations in the drawing area, however more efficient methods for specifying points are available,
and will be presented in the Precision topic.

![](../images/GUID-98EF7FE6-EE10-4DFE-BBBC-536F257C8E52-low.png)

After you specify the next point, the LINE command keeps prompting you for additional points. Press Enter or the Spacebar
to end the sequence.

## Grid Display

Some people like working with grid lines as a reference, while others prefer working in a blank area. To turn off the grid
display, press F7 or
![](../images/GUID-CD7987DD-AB67-4027-AD87-149DA630BFFB-low.png) on the touch bar. Even with the grid turned off, you can force your cursor to snap to grid increments by pressing F9 or
![](../images/GUID-BEBC9838-A4E4-4AEC-8612-5FE13E3058BC-low.png) on the touch bar.

## Lines as Construction Aids

Lines can serve as reference and construction geometry such as

* Property line setbacks
* The mirror line of a symmetrical mechanical part
* Clearance lines to avoid interferences
* Traversal path lines

## Circles

The default option of the CIRCLE command requires you to specify a center point and a radius.

![](../images/GUID-857BBE41-F4A1-4ACD-87AD-821C7E595548-low.png)

Additional circle options are available from the drop-down:

![](../images/GUID-79A53F82-5FCB-4DE2-A76D-F231687B5660-low.png)

Alternatively, you can also enter CIRCLE or just C in the Command window and specify an option.

![](../images/GUID-AD2FC14E-8C2F-4AC4-8B30-C47EB799F7CE-low.png)

Circles can be useful as reference geometry. For example, you can see that the two doors in the illustration can interfere
with each other.

![](../images/GUID-FD6C9554-E95B-42E4-AA7F-6EC6B09CA289-low.png)

## Polylines and Rectangles

A polyline is a connected sequence of line or arc segments that is created as a single object.

![](../images/GUID-677845B0-ACF7-4C7E-A19A-F65FDA82DA34-low.png)

Use the PLINE command to create open or closed polylines for

* Geometry that needs to have fixed-width segments
* Continuous paths for which you need to know the total length
* Contour lines for topographic maps and isobaric data
* Wiring diagrams and traces on printed circuit boards
* Process and piping diagrams

Polylines can have a constant width or they can have different starting and ending widths. After you specify the first point
of the polyline, you can use the Width option to specify the width of all subsequently created segments. You can change the
width value at any time, even as you create new segments.

![](../images/GUID-A42F2D0C-04E0-466C-9811-9C8D73DB3D54-low.png)

Polylines can have different starting and ending widths for each segment as shown here:

![](../images/GUID-5C8210DF-5E8D-4E9F-A34B-9D0A2DEE83DC-low.png)

Here is an example of a printed circuit board in which the traces were created with wide polylines. The landing pads were
created with the DONUT command.

![](../images/GUID-AB9BA7D2-FBF0-49AA-B4AC-33B3075FA048-low.png)

A fast way to create closed rectangular polylines is to use the RECTANG command (enter REC in the Command window).

![](../images/GUID-80594EDF-50A5-4818-806A-C6348422A73E-low.png)

Simply click two diagonal points for the rectangle as illustrated.

![](../images/GUID-3F9A5613-290C-4C62-890D-87C2A605DD4D-low.png)

## Hatches and Fills

In AutoCAD, a hatch is a single, compound object that covers a specified area with a pattern of lines, dots, shapes, a solid
fill color, or a gradient fill.

![](../images/GUID-92D4CFA0-0F04-429A-9D1B-DE1602FC1BD7-low.png)

When you start the HATCH command, the Hatch visor temporarily displays. On this visor, you can choose from industry-standard
imperial and ISO hatch patterns, along with many specialized options.

![](../images/GUID-0EAAC2FE-72AA-475E-86CB-C49898787392-low.png)

The simplest procedure is to choose a hatch pattern and scale from the visor, and click within any area that is completely
enclosed by objects. You need to specify the scale factor for the hatch to control its size and spacing.

NOTE:If an area is not completely enclosed, red circles display to indicate places to check for gaps. Enter REDRAW in the Command
window to dismiss the red circles.

After you create a hatch, you can move the bounding objects to adjust the hatch area, or you can delete one or more of the
bounding objects to create partially bounded hatches:

![](../images/GUID-C7E04D88-C75B-411A-B5B9-9B0D31B694D2-low.png)

If you set a hatch pattern to be a solid or gradient fill, also consider setting a transparency level for interesting overlap
effects. To set the transparency, select the hatch object and adjust the slider on the Properties Inspector.

![](../images/GUID-736CBF20-C416-4E44-A5A4-2DCBE9D529A9-low.png)

NOTE:The Properties Inspector is covered in the Properties topic.

Here are some examples of how you can use solid-fill hatches:

![](../images/GUID-3778A099-ECA6-42CE-B924-6DDD61FD97D2-low.png)

If you need to align the pattern in a hatch, which might be the case with the decking boards above, hover over the hatch's
origin grip, and select Origin Point to specify an alignment point.

![](../images/GUID-2116E100-3396-4E17-9F00-0D99BA23292B-low.png)

## The User Coordinate System (Optional)

The user coordinate system (UCS) icon indicates the direction of the positive X and Y axis for any coordinates that you enter,
and it also defines the horizontal and vertical directions in a drawing. In some 2D drawings, it can be convenient to click
and place the UCS to change the origin point and the X or Y axis.

For example, by reorienting the UCS, you can create rectangles that are automatically aligned with the X axis as shown.

![](../images/GUID-5DBA3948-70E1-444A-A012-DD16A77B4856-low.png)

To restore the user coordinate system to its original location, enter UCS in the Command window and press Enter to specify
the default <World> option.

## Overlapping Objects

For overlapping hatches, fills, wide polylines, and text objects, use the DRAWORDER command to determine which objects are
on top or below the others. For example, you probably want the yellow highway to cross the blue river rather than the other
way around.

![](../images/GUID-AE066C5D-5663-46B2-A726-2724E7AF804E-low.png)

You can access several draw order options from the Modify panel on the tool set. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) on the Modify panel and select to display the Draw Order drop-down.

![](../images/GUID-4226F890-430F-4057-86FE-FB2CB8438E7D-low.png)

Expand the drop-down to see draw order options including sending all hatches to the back, selected objects to the front, and
so on.

![](../images/GUID-1363E896-21D2-4EE0-868F-9A0F36111A1B-low.png)

The drop-down list displays options for selected objects plus options that apply to all objects of a certain type, such as
text.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [View](GUID-9AC70B3B-57DD-4AA3-8F6C-9D096886040F.htm " Pan and zoom to different views in a drawing.
")

**Next topic:** [Precision](GUID-85D8C41C-9C3E-440F-BD60-61848DD27219.htm " Ensure the precision required for your models.
")

#### Related References

* [LINE (Command)](LINE-Command.md)
* [CIRCLE (Command)](CIRCLE-Command.md)
* [PLINE (Command)](PLINE-Command.md)
* [RECTANG (Command)](RECTANG-Command.md)
* [HATCH (Command)](HATCH-Command.md)
* [UCS (Command)](UCS-Command.md)
* [DRAWORDER (Command)](DRAWORDER-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*