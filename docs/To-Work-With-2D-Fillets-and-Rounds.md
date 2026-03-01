# To Work With 2D Fillets and Rounds

## Set the Fillet Radius

The fillet radius determines the size of the arc created by the FILLET command, which connects two selected objects or the
segments in a 2D polyline. Until you change it, the fillet radius applies to all subsequently created fillets.

![](../images/GUID-22BF8A20-6B16-4959-96E9-5B340A2CC035-low.png)

NOTE:If the fillet radius is set to 0, the selected objects are trimmed or extended until they intersect; no arc is created. When
the fillet radius is set to 0, you can remove the arc segment between two straight line segments or all arc segments from
a 2D polyline.

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Fillet drop-down ![](../images/ac.menuaro.gif) Fillet.
   ![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png)
2. At the Command prompt, enter
   *r* (Radius).
3. Enter a new fillet radius value.

   Once the fillet radius has been set, select the objects or line segments that define the points of tangency for the resulting
   arc or press Enter to end the command.

   TIP:Press and hold Shift while selecting objects or line segments to override the current fillet radius with a value of 0.

## Add A Fillet Between Two Objects or Line Segments of a 2D Polyline

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Fillet drop-down ![](../images/ac.menuaro.gif) Fillet.
   ![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png)
2. In the drawing area, select the first object or line segment that will define the points of tangency for the resulting arc.
3. Select the second object or line segment.

TIP:At the main prompt of the FILLET command, use the Multiple option to continue adding fillets after selecting the first two
objects or line segments. When the Multiple option is not used, the command ends after selecting the second object or line
segment.

## Add A Fillet Without Trimming the Selected Objects or Line Segments

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Fillet drop-down ![](../images/ac.menuaro.gif) Fillet.
   ![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png)
2. At the Command prompt, enter
   *t* (Trim).
3. Enter
   *n* (No Trim).
4. In the drawing area, select the objects or line segments that define the points of tangency for the resulting arc.

## Insert Arcs At Each Vertex of A 2D Polyline

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Fillet drop-down ![](../images/ac.menuaro.gif) Fillet.
   ![](../images/GUID-96B6BF37-E721-4F8B-BDC9-22D1F1036AC4-low.png)
2. At the Command prompt, enter
   *p* (Polyline).
3. In the drawing area, select a polyline.

#### Related Concepts

* [About Fillets and Rounds](About-Fillets-and-Rounds.md)
* [About Chamfers and Bevels](About-Chamfers-and-Bevels.md)

#### Related Information

* [To Work With 2D Chamfers and Bevels](To-Work-With-2D-Chamfers-and-Bevels.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*