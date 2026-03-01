# Basics

Review the basic AutoCAD for Mac controls.

After you launch AutoCAD, on the Start tab, click New or click the New drop-down menu to begin a new drawing.

![](../images/GUID-255C8A26-D356-43CD-A7BF-4B6B24F0D81A-low.png)

### Drawing Tabs

The new drawing,
*Drawing1*, starts on a new tab that's just above the drawing area. You can click the tabs to switch between several open drawing files.
Click the plus sign to start a new drawing using the default template.

![](../images/GUID-20AA2E65-BCD7-4CB6-96C5-9BB7B1B337FE-low.png)

NOTE:An asterisk (\*) next to the drawing name indicates that the drawing needs to be saved.

Go ahead and experiment with starting and opening drawings, and switching between the tabs. You can also drag the drawing
tabs to reorder them.

### Tool Sets

AutoCAD includes a tool set to the left of the drawing area. You can access nearly all the commands presented in this guide
from the Drafting tab. In addition, the toolbar above the drawing area includes familiar commands such as New, Open, Save,
Print, Undo, and so on.

![](../images/GUID-CFBC0EF7-A46F-4864-8705-FD524AC4FFD2-low.png)

NOTE:If the Drafting tab is not the current tab, go ahead and click it.

## The Command Window

At the heart of AutoCAD is the Command window, which is docked at the bottom of the drawing area. The Command window displays
prompts, options, and messages.

![](../images/GUID-AA6C2735-EF64-4D57-9981-AB817158EA38-low.png)

You can enter commands directly in the Command window instead of using the tool sets, toolbars, and menus.

Notice that as you start to type a command, it completes automatically. When several possibilities are available such as in
the example below, you can make your choice by clicking it or using the arrow keys and then pressing Enter or the Spacebar.

![](../images/GUID-ADC952F8-91FC-4339-9712-BC590C83931C-low.png)

## New Drawings

You can easily conform to industry or company standards by specifying settings for text, dimensions, linetypes, and several
other features. For example, this backyard deck design displays two different dimension styles.

![](../images/GUID-8752B779-91AF-4BE2-8197-EB7C2F6C8BC8-low.png)

All these settings can be saved in a
*drawing template* file. Click New to choose from several drawing template files:

![](../images/GUID-0BD9C76A-57B2-4E43-88E7-EA69DE69AD1D-low.png)

* For imperial drawings that assume your units are inches, use
  *acad.dwt* or
  *acadlt.dwt*.
* For metric units that assume your units are millimeters, use
  *acadiso.dwt* or
  *acadltiso.dwt*.

![](../images/GUID-6D410264-7D08-41C4-8E51-6C881DA742A4-low.png)

The "Tutorial" template files in the list are simple examples for the architectural or mechanical design disciplines with
both imperial (i) and metric (m) versions. You might want to experiment with them when you start creating dimensions.

Most companies use drawing template files that conform to company standards. They will often use different drawing template
files depending on the project or the client.

## Create Your Own Drawing Template File

You can save any drawing (*.dwg*) file as a drawing template (*.dwt*) file. To create a drawing template file based on an existing one, open the existing drawing template file, modify it, and
then save it with a different filename.

![](../images/GUID-EBF4A9EA-2893-48CA-88F4-9BFDA49D7E03-low.png)

If you work independently, you can develop your drawing template files to suit your working preferences, adding settings
for additional features as you become familiar with them. To modify an existing drawing template file, click Open, specify
Drawing Template (\*.dwt) in the dialog box, and choose the template file.

![](../images/GUID-5DDD042D-31CB-4969-8A8A-B7AB711591EC-low.png)

IMPORTANT: If your company has already established a set of drawing template files, check with your CAD manager before modifying any
of them.

## Units

After you start a new drawing, you'll first decide what the length of one unit represents-an inch, a foot, a centimeter,
a kilometer, or some other unit of length. For example, the objects below could represent two buildings that are each 125
feet long, or they could represent a section from a mechanical part that is measured in millimeters.

![](../images/GUID-A8707F52-007C-4DB3-BF88-7EA0530C8787-low.png)

## Unit Display Settings

After you decide what unit of length that you want to use, the UNITS command lets you control several unit display settings
including the following:

* Format (or Type). For example a decimal length of 6.5 can be set to display as a fractional length of 6-1/2 instead.
* Precision. For example, a decimal length of 6.5 can be set to display as 6.50, 6.500, or 6.5000.

If you plan to work in feet and inches, use the UNITS command to set the unit type to Architectural, and then when you create
objects, specify their lengths in inches. If you plan to use metric units, leave the unit type set to Decimal. Changing the
unit format and precision does not affect the internal precision of your drawing. It affects only how lengths, angles, and
coordinates are displayed in the user interface.

TIP:If you need to change the UNITS settings, make sure that you save the drawing as a drawing template file. Otherwise, you will
need to change the UNITS settings for each new drawing.

## Model Scale

Always create your models at full size (1:1 scale). The term
*model* refers to the geometry of your design. A
*drawing* includes the model geometry along with the views, notes, dimensions, callouts, tables, and the title block displayed in the *layout*.

You'll specify the scale for printing a drawing on a standard-sized sheet later, when you create the layout.

## Recommendations

* To open Help with information about the command in progress, simply press F1.
* To repeat the previous command, press Enter or the Spacebar.
* To see various options, select an object and right-click, or right-click a user interface element.
* To cancel a command in progress or if you ever feel stuck, press Esc. For example, if you click in the drawing area before
  entering a command, you will see something like the following:

![](../images/GUID-EA104C58-B25B-4647-9931-9518CC2040EC-low.png)

Press Esc to cancel this preselection operation.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Next topic:** [View](GUID-9AC70B3B-57DD-4AA3-8F6C-9D096886040F.htm " Pan and zoom to different views in a drawing.
")

#### Related References

* [UNITS (Command)](UNITS-Command-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*