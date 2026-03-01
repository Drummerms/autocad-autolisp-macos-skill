# Modify

Perform operations such as erase, move, and trim on the objects in a drawing.

The most common of these tools are located on the Modify panel of the Drafting tab of the toolsets. Take a minute to look
through them.

![](../images/GUID-8235BECD-0897-458B-9DAA-6A6F3DBD9F2C-low.png)

## Erase

To erase an object, use the ERASE command. You can enter E in the Command window, or click the Erase tool.
![](../images/GUID-342B2C46-0E0A-431A-829D-77901015ED51-low.png) When you see the cursor change to a square
*pickbox*, click each object that you want to erase, and then press Enter or the Spacebar. Alternatively, before you enter any command,
you can select several objects and then press the Delete key.

NOTE:You may need to choose Customize Panel on the Modify panel to include the Erase tool.
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png)

## Select Multiple Objects

Sometimes you need to select a large number of objects. Instead of selecting each object individually, you can select the
objects in an area by clicking an empty location (1), moving your cursor right or left, and then clicking a second time (2).

![](../images/GUID-129C54C8-1473-41CD-A35C-99FAA8CDF91F-low.png)

* With a
  *crossing selection*, any objects within or touching the green area are selected.
* With a
  *window selection*, only the objects completely contained within the blue area are selected.

The result is called the
*selection set*, which is the set of objects that will be processed by a command.

TIP: You can easily remove objects from the selection set. For example, if you select 42 objects, and two of them should not have
been selected, hold down Shift and then select the two that you want to remove. Then, press Enter or the Spacebar, or right
click to end the selection process.

## Move and Copy

Here's how you would use the COPY command to lay out a row of decorative tiles. Starting with a polyline that represents
its shape, you need to make copies that are 1/8" apart.

![](../images/GUID-277E1E94-3142-4BF7-9683-0A3441912379-low.png)

You click the Copy tool or enter CP in the Command window to start the command. From here, you can choose between two methods,
depending on what's more convenient. You will use both these methods frequently.

### The Distance Method

The second tile needs to be a total of 9-7/8" + 1/8" = 10" to the right of the original tile. So, you select the tile, press
Enter or the Spacebar to end your selection, and click anywhere in the drawing area (1). This point does not have to be located
on the tile.

![](../images/GUID-1A8AF248-4552-4077-B46D-B923E4945CAA-low.png)

Next, you move your cursor to the right, relying on the polar tracking angle to keep the direction horizontal, and then enter
10 for the distance. Press Enter or the Spacebar a second time to end the command.

The specified distance and a direction from the point (1) is applied to the tile that you selected.

### The Two Points Method

Another method, one that you will often use when you don't want to add numbers together, requires two steps. You start the
COPY command and select the tile as before, but this time you click the two endpoints as shown. These two points also define
a distance and direction.

![](../images/GUID-5959D5ED-486B-40D4-9DB4-395EDD36F9C5-low.png)

Next, to add the 1/8" space between the tiles, click the Move tool or enter M in the Command window. The MOVE command is similar
to the COPY command. Select the newly copied tile, and press Enter or the Spacebar. As before, click anywhere in the drawing
area and move your cursor to the right. Enter 1/8 or .125 for the distance.

TIP:The two points that define the distance and direction don't need to be located on the object that you want to copy or move.
You can use two points specified anywhere in your model.

For example, enter the MOVE command. Use a selection method to select the objects in the rectangle (1). Specify a base point
(2) and a second point (3) to determine the distance and direction of the move. Press Spacebar or Enter to see the results.

![](../images/GUID-E878DC3A-2171-4249-9BFF-27BD348D1FDF-low.png)

The distance and direction determined by endpoint at 2 and 3 in the illustration are applied to the rectangle.

### Create Multiple Copies

Similarly, you can use the two-points method as a repeating sequence. Let's say that you want to make more copies of the
circle at the same horizontal distance. You start the COPY command and select the circle as shown.

![](../images/GUID-A2B6FA57-DC6F-497D-A530-B30D4E9AE9EF-low.png)

Then, using the Center object snap, click the center of circle 1, followed by the center of circle 2, and so on.

![](../images/GUID-C4A3E29F-7C18-4EB3-AE17-76F1DF118161-low.png)

For larger numbers of copies, try experimenting with the Array option of the COPY command. For example, here's a linear arrangement
of deep foundation piles. From a base point, you specify number of copies and the center-to-center distance.

![](../images/GUID-45498B27-828C-4068-B81C-72E2807244E8-low.png)

## Offset

Most models include a lot of parallel lines and curves. Creating them is easy and efficient with the OFFSET command. Click
the OFFSET tool or enter O in the Command window.

![](../images/GUID-FEECD8F1-401E-4C20-80F1-CC3DECBB3560-low.png)

Select the object (1), specify the offset distance, and click to indicate on which side of the original that you want the
result (2). Here is an example of offsetting a polyline.

![](../images/GUID-9F60E87D-546A-429E-8F20-58D4DB18E32B-low.png)

TIP: A fast way to create concentric circles is to offset them.

## Trim and Extend

A popular technique is to use the OFFSET command in combination with the TRIM and EXTEND commands. In the Command window,
you can enter TR for TRIM or EX for EXTEND. Trimming and extending are some of the most commonly used operations.

![](../images/GUID-79651890-FB6E-4058-8991-DA583157F3FE-low.png)

In the following illustration, let's say you want to extend the lines that represent the steps for this deck. You start the
Extend command, select the boundary, and then press Enter or the Spacebar.

![](../images/GUID-3DBC8560-1290-4E67-9D02-60513822FCB8-low.png)

Pressing Enter or the Spacebar indicates that you've finished selecting the boundaries, and that you're now ready to select
the objects to be extended.

TIP:A faster method is to press Enter or the Spacebar right away instead of selecting any boundary objects. The result is that
all objects are available as possible boundaries.

Next, you select the objects to be extended (near the ends to be extended), and then you press Enter or the Spacebar to end
the command.

![](../images/GUID-924F4C33-AFDB-4E17-BF07-277434C509D9-low.png)

The result is that the lines are extended to the boundary.

![](../images/GUID-8996E053-92F0-4143-A732-622900253496-low.png)

The TRIM command follows the same steps, except that when you select the objects to trim, you select the portions to trim
away.

## Mirror

The following illustration comes from a tile project. The walls in this residential bathroom are flattened out to be able
to lay out the tile pattern and estimate the number of tiles needed.

![](../images/GUID-C00F0FD2-062E-45E7-BC1D-1B5A0B0C9D00-low.png)

You can save a lot of work by taking advantage of the symmetry between the left and right walls. All you need to do is create
the tiles on one wall and then mirror the wall across the center of the room.

In the example below, you start the MIRROR command (![](../images/GUID-D688E1AF-F7AB-4F1D-B29B-93F48BE3CC25-low.png) or enter MI in the Command window), use window selection (1 and 2) to select the geometry on the right wall, press Enter
or the Spacebar, and then specify a mirror line (3 and 4) corresponding to the centerline of the bathroom.

![](../images/GUID-34AEB801-9F42-46AE-BAB2-AD510131DFF6-low.png)

Finally, decline the option to "Erase source objects" by pressing Enter or the Spacebar.

![](../images/GUID-5FF66723-FF0F-48B2-B3EB-5ACE9072A534-low.png)

TIP: Always look for symmetry to save yourself extra work, even if the symmetry is not 100% identical.

## Stretch

You can stretch most geometric objects. This lets you lengthen and shorten parts of your model. For example, this model might
be a gasket or the design for a public park.

![](../images/GUID-5C5588B2-04F5-4D77-9BEE-A24357A8B93A-low.png)

Use the STRETCH command (![](../images/GUID-9C413D4F-E14A-425C-AC00-CAABC1582429-low.png) or enter S in the Command window) and select the objects with a crossing selection as shown below (1 and 2). The crossing
selection is mandatory—only the geometry that is crossed by the crossing selection is stretched. Then click anywhere in the
drawing area (3), move the cursor to the right, and enter 50 as the distance. This distance might represent millimeters or
feet.

![](../images/GUID-59020FD3-F2BB-479B-BCF2-491A19DA4D8A-low.png)

To shorten the model by a specified amount, you'd move your cursor to the left instead.

## Fillet

The FILLET command (![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png) or enter F in the Command window) creates a rounded corner by creating an arc that is tangent to two selected objects. Notice
that the fillet is created relative to where you select the objects.

![](../images/GUID-330B18E1-EF2B-4452-9F18-2043BA472137-low.png)

You can create a fillet between most types of geometric objects, including lines, arcs, and polyline segments.

TIP: If you hold down the Shift key when you select the second object, the result trims or extends the selected objects to a sharp
corner.

## Explode

The EXPLODE command (![](../images/GUID-28962630-A678-4897-B2D0-D4B92429177D-low.png) or enter X in the Command window) disassociates a compound object into its component parts. You can explode objects such
as polylines, hatches, and blocks (symbols).

After you explode a compound object, you can modify each resulting individual object.

## Edit Polylines

You can choose from several useful options when you want to modify a polyline. The PEDIT command (![](../images/GUID-85E48CB9-5547-4B04-91E8-14F9F012AF53-low.png) or enter PE in the Command window) is located on the Modify panel but you may need to select Customize Panel to display it.
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png)

With this command, you can

* Join two polylines into a single polyline if they share a common endpoint
* Convert lines and arcs into a polyline—simply enter PEDIT and select the line or arc
* Change the width of a polyline

TIP: In some cases, the easiest method to modify a polyline is to explode it, make the modifications, and then turn the objects
back into a polyline using the Join option of the PEDIT command.

## Grips

Grips are displayed when you select an object without starting a command. Grips are often handy for light editing. For example,
the line below accidentally snapped to the wrong endpoint. You can select the misaligned line, click on a grip and then click
to specify the correct location.

![](../images/GUID-437D425B-277D-4272-BADD-4AF458CE02C7-low.png)

By default, when you click a grip, you automatically start in \*\*STRETCH\*\* mode as indicated in the Command window. If you
want to explore other ways of editing objects with grips, press Enter or the Spacebar to cycle through several other editing
modes. Some people perform most editing operations using grips.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Properties](GUID-72AC2E5A-4E0E-45B0-B36C-CE8B6C23B2C8.htm "Assign properties such as color and linetype to individual objects, or as default properties assigned to layers.
")

**Next topic:** [Symbols](GUID-66DB43BA-885F-49CB-9D14-DBEB05B7C8FD.htm " Insert symbols and details into your drawings from commercial online sources or from your own designs.
")

#### Related References

* [ALIGN (Command)](ALIGN-Command.md)
* [COPY (Command)](COPY-Command.md)
* [ERASE (Command)](ERASE-Command.md)
* [EXTEND (Command)](EXTEND-Command.md)
* [EXPLODE (Command)](EXPLODE-Command.md)
* [FILLET (Command)](FILLET-Command.md)
* [MIRROR (Command)](MIRROR-Command.md)
* [MOVE (Command)](MOVE-Command.md)
* [OFFSET (Command)](OFFSET-Command.md)
* [PEDIT (Command)](PEDIT-Command.md)
* [ROTATE (Command)](ROTATE-Command.md)
* [STRETCH (Command)](STRETCH-Command.md)
* [TRIM (Command)](TRIM-Command.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*