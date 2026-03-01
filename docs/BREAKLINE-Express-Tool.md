# BREAKLINE (Express Tool)

Creates a breakline, a polyline that includes the breakline symbol.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Break-Line Symbol.
![](../images/GUID-7B69B6A9-6651-4A2B-9DAB-B35DB3CDADE6-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Express Tools ![](../images/ac.menuaro.gif) Break-Line Symbol.

You specify two points and the location of the breakline symbol between them. You can control the relative size and appearance
of the breakline symbol and the extension of the polyline beyond the selected start and end points.

NOTE: The current setting of the DIMSCALE System Variable controls the ultimate size of the breakline elements. For example, using
the default breakline block, BRKLINE.DWG, with a distance of 1.00 between defpoints, and assuming a BREAKLINE Size option
of 0.5, with DIMSCALE set to 48 the resultant distance between defpoints is (1 \* 0.5 \* 48) or 24 units. This relationship
between the BREAKLINE elements and the current DIMSCALE setting is consistent with the behavior of standard AutoCAD dimension
scaling.

## Options

| Block | Determines the block to be used as the breakline symbol. The default block is defined by *brkline.dwg*. |
| Size | Determines the size of the breakline symbol. |
| Extension | Determines the length of the line extension beyond selected points. |

## Customize the Breakline Symbol

You can create your own block for the breakline symbol by creating a drawing in the resources support folder. Make sure that
the drawing contains two point objects that have been created on the Defpoints layer. Those point objects determine the placement
of the symbol and how the line will be broken. Here are the steps:

1. Start a new drawing.
2. Draw the breakline symbol:

   ![](../images/GUID-799F283C-FDBF-4F32-95B7-36A9F8056784-low.gif)
3. Make the Defpoints layer current. If it does not exist, create it and make it the current layer:

   ![](../images/GUID-011C529C-AB42-4093-BB25-35193EBD0AF1-low.gif)
4. Use the POINT command to create a point object at each location where the line will connect with the breakline symbol. Use
   only two points.

   ![](../images/GUID-1BAEA439-58D4-4FFF-B8BC-8424967A035D-low.gif)
5. Save the drawing file in
   Applications/Autodesk/AutoCAD {release}/AutoCAD {release}.app/Contents/Resources/Support.

When you start the BREAKLINE command, use the Block option to specify the drawing file for the new breakline block.

![](../images/GUID-9C75FB35-41AE-411B-A2C5-42B91D1DB883-low.gif)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*