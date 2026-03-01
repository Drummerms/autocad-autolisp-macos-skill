# To Work With Revision Clouds

How to create and edit revision clouds for highlighting parts of a drawing.

## Create a Rectangular Revision Cloud

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Rev-Cloud drop-down ![](../images/ac.menuaro.gif) Rectangular.
   ![](../images/GUID-0B452EB5-92EF-4067-8975-D5E37FA6B515-low.png)
2. Specify the first corner of the revision cloud.
3. Specify the other corner of the revision cloud.

## Create a Polygonal Revision Cloud

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Rev-Cloud drop-down ![](../images/ac.menuaro.gif) Polygonal.
   ![](../images/GUID-AED9A9A0-B6B6-446C-877A-2B82130417D6-low.png)
2. Specify the start point of the revision cloud.
3. Click to specify additional vertices of the revision cloud.

## Create a Freehand Revision Cloud

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Rev-Cloud drop-down ![](../images/ac.menuaro.gif) Freehand.
   ![](../images/GUID-D89B6B5D-B3EF-41D0-B1CE-E350C57B8922-low.png)
2. Guide the crosshairs along the cloud path. You can click pick points along the path if you want to vary the size of the arcs.
3. Press Enter at any time to stop drawing the revision cloud.

   To close the revision cloud, return to its starting point.
4. To reverse the direction of the arcs, enter
   *yes* at the Command prompt and press Enter.

## Create a Revision Cloud with Calligraphy Pen Style

1. At the Command prompt, enter REVCLOUD.
2. In the drawing area, right-click and choose Style.
3. Select Calligraphy.
4. Press Enter to save the calligraphy setting and to continue with the command, or press Esc to end the command.

## Create Revision Clouds with Uniform Chord Length

1. At the Command prompt, enter REVCLOUDARCVARIANCE.
2. Enter
   *off* or
   *0* to change the default to uniform chord length.
3. Insert revision clouds as needed.

NOTE:This system variable does not affect existing revision clouds.

## Convert an Object to a Revision Cloud

1. At the Command prompt, enter REVCLOUD.
2. In the drawing area, right-click and choose Object.
3. Select a circle, ellipse, polyline, or spline that you want to convert to a revision cloud.
4. Press Enter to keep the current direction of the arcs. Otherwise, enter
   *yes* to reverse the direction of the arcs.
5. Press Enter.

## Change the Default Value for Arc Lengths in a Revision Cloud

1. At the Command prompt, enter REVCLOUD.
2. In the drawing area, right-click and choose the Arc length option.
3. Enter a new approximate chord length for the revision cloud arcs.
4. Continue the REVCLOUD command or press Esc to accept the new value and exit the command.

## Modify Revision Cloud Vertices Using Grips

NOTE:By default, REVCLOUDGRIPS system variable is on and revision clouds display the minimal number of grips required to perform
typical modifications.

1. At the Command prompt, enter REVCLOUDGRIPS.
2. Enter
   *off* or
   *0* to display a grip for each arc segment on the revision cloud.
3. Select a revision cloud.
4. Select a grip and depending on the grip location, stretch the revision cloud or add, remove, or stretch a vertex.

   NOTE:Hover over the grip to display the menu options to stretch, add, or remove a vertex.

## Modify the Lengths of Arcs in a Revision Cloud Using Grips

1. At the Command prompt, enter REVCLOUDGRIPS.
2. Enter
   *off* or
   *0* to display a grip for each arc segment on the revision cloud.
3. Select the revision cloud you want to edit.
4. Move the pick points along the path of the revision cloud to change the individual arc lengths and chords.

## Modify the Arc Length in a Revision Cloud Using Property Palette

1. Select the revision clouds you want to change.
2. Right-click over the drawing window. Click Properties.
3. On the Properties palette, change the Arc Length value.

#### Related References

* [REVCLOUD (Command)](REVCLOUD-Command.md)

#### Related Information

* [About Revision Clouds](About-Revision-Clouds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*