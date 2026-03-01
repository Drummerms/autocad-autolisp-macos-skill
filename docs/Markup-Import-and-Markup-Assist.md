# Markup Import and Markup Assist

Markup Import and Markup Assist use machine learning to identify markups and provide a way to view and insert drawing revisions
with less manual effort.

Markups can be imported as a PDF, PNG, or JPG and are overlaid on top of your drawing in the Trace workspace. Markups in
the imported file are automatically identified as mtext, mleaders, and revision clouds. Markup Assist lets you insert those
identified markups into the drawing as geometry.

## Markup Import

Use Markup Import to place a marked-up version of your drawing on top of the original file to make it easier to view and
incorporate changes to your drawing. For example, if you have a PDF version of your drawing that has text and revision notes
added, use Markup Import to overlay the revised drawing on top of the original. Or, if you have a printed version of your
drawing that contains hand-written revision notes, you can take a photograph of the printed version and then import it as
a JPG or PNG.

The imported file is automatically placed and aligned on top the drawing file in a new trace.

If the imported file is not aligned correctly, you can manually align, move, scale, or rotate the imported file.

![](../images/GUID-67D39258-F18F-42AD-8B47-B05EC43EFA3D-low.png)

## Markup Assist

Markup Assist automatically identifies markups as text, leaders, and revision clouds. Click an identified markup, then insert
it as an mtext, mleader, or revcloud object. You can edit the text before inserting it, or choose to copy the text to the
clipboard.

## To Import a Markup

1. Click Markup Import.
   ![](../images/GUID-ADD13904-5945-4437-97D8-5AED3D753676-low.png) Find

   You can also enter MARKUPIMPORT at the Command prompt.
2. Select a PDF, PNG, or JPG markup file to import.

   The markup file can be a digital copy, a photograph, or a scanned version of the original drawing.
3. Move, align, rotate, or scale the markup if the imported markup file isn't automatically aligned to the drawing correctly.

## To Use Markup Assist

1. After importing a markup, make sure TRACEBACK is on and Markup Assist is on. You can toggle between Trace Front and Trace
   Back in the Trace Settings toolbar. While TRACEBACK is on, you can toggle Markup Assist on or off.

   ![](../images/GUID-FAB9F185-ECB4-4598-B467-91A4E5CBECCC-low.png)
2. Click the border on an identified markup.

   ![](../images/GUID-5BF2894A-CE1F-4CE8-9E20-225B6351B5BB-low.png)
3. If the identified markup is text, choose to insert the object as mtext, as an mleader, or update existing text using the
   text string. You can edit the text before inserting it.

   ![](../images/GUID-374F4ABA-C116-4405-908E-825C2061F046-low.png)

   Inserting the object adds it to the drawing as geometry.
4. To Update Existing Text:
   1. Select existing text in the drawing that you want to replace.
   2. Choose one of the following:
      * *Append.* Adds the text that was selected from the markup to the end of the text field and keeps the existing text.
      * *Replace.* Adds the text that was selected from the markup and removes the existing text.
      * *Select a strikethrough.* Select a strikethrough markup (text that has been crossed out with a markup), and the text that was selected from the markup
        will replace the drawing text and fade the strikethrough markup.
5. If the markup object is identified as a revision cloud, you can insert it as a revcloud.

   ![](../images/GUID-8050438E-D4FA-4598-8EAC-B9B182DAAB41-low.png)

## *Strikethrough Text*

Markup Assist recognizes text that has been crossed out, and allows you to erase the text or replace the text with text from
a markup.

To replace existing text:

1. Click a strikethrough. The Markup Assist dialog box opens.
2. Click Replace Existing Text.
3. Click the text in the drawing to replace.
4. Click the text in the markup to replace the existing text with.

To erase existing text:

1. Click a strikethrough. The Markup Assist dialog box opens.
2. Click Erase Existing Text.
3. Select the text in the drawing to erase.

## Markups With Associated PDF Text Comments

Text comments that are added to a PDF using Adobe software will display and can be inserted into the drawing as an Mleader
or Mtext, or used to update existing text.

![](../images/GUID-E3419C6E-6CCC-4F5F-95A1-054DD3E512E0-low.png)

To insert text from a PDF text comment:

1. Click the markup that contains a PDF text comment.

The Markup Assist dialog box opens.

2. Insert the text as an Mleader, Mtext, or Update Existing Text.

## Fade Markup

Use Fade Markup to control the transparency of individual markups. Fade Markup is useful for hiding any markups that you've
already inserted, or if there is a markup you want to ignore. Access the FADEMARKUP command from the Trace visor, or from
the Markup Assist dialog box. Control the transparency of faded markups in Trace Settings on the Trace visor, or with the
TRACEMARKUPFADECTRL system variable.

To unfade a markup that was previously faded, use one of the following methods:

* Select the markup and click Unfade Markup from the Markup Assist dialog box.
* Select FADEMARKUP from the Trace visor, enter N at the Command Prompt, and select the markup's boundary.

## Selecting Markups Within a Boundary

When you use any command that prompts to "Select Objects," you can click the blue highlighted border of a Markup Assist boundary
to select all the AutoCAD objects within it. When you click the highlighted border, all objects entirely within the border
are added to the selection set.

NOTE:Set the MARKUPSELECTIONMODE to 0 to turn off, 1 to enable selection using boundary markup assist boxes as criteria, or 2 to
enable selection using any markup assist box as criteria.

## Instruction Text on a Markup

Markup Assist detects certain instructions in markup text that are linked to commands such as "MOVE," "COPY," or "DELETE."
When Markup Assist identifies an instruction, you can click that instruction to start the associated command.

![](../images/GUID-98CCB313-9BCC-4ADD-9F55-7A75A1B4CD8C-low.png)

## *New Commands*

[FADEMARKUP](FADEMARKUP-Command.md) - Fades individual markups so they are less visible on a trace.

[MARKUPASSIST](MARKUPASSIST-Command.md) - Analyzes an imported markup and can help place text callouts and revision clouds faster and with less manual effort.

[-MARKUPASSIST](MARKUPASSIST-Command-2.md) - At the Command prompt, analyzes an imported markup and can help place text callouts and revision clouds faster and with
less manual effort.

[MARKUPIMPORT](MARKUPIMPORT-Command-2.md) - Imports a marked up drawing (image/pdf) in-place into your DWG as a new trace.

[-MARKUPIMPORT](MARKUPIMPORT-Command.md) - At the command prompt, imports a marked up drawing (image/pdf) in-place into your DWG as a new trace.

## *New System Variables*

[COMMENTHIGHLIGHT](COMMENTHIGHLIGHT-System-Variable.md) - Controls the display of the indicator badge on PDF text comments.

[MARKUPASSISTMODE](MARKUPASSISTMODE-System-Variable.md) - Controls whether identified markups are highlighted.

[MARKUPPAPERDISPLAY](MARKUPPAPERDISPLAY-System-Variable.md) - Indicates whether or not a digital markup is currently active.

[MARKUPPAPERTRANSPARENCY](MARKUPPAPERTRANSPARENCY-System-Variable.md) - Controls the level of transparency when a digital markup is active.

[MARKUPSELECTIONMODE](MARKUPSELECTIONMODE-System-Variable.md) - Enables selection using boundary markup assist boxes as criteria.

[TRACEMARKUPFADECTL](TRACEMARKUPFADECTL-System-Variable.md) - Controls the transparency of faded markups. The lower the number, the more visible the markup is.

[TRACEVPSUPPORT](TRACEVPSUPPORT-System-Variable.md) - Controls whether markup boxes are actionable within a currently active model space viewport.

#### Related Tasks

* [Working With Markup Import and Markup Assist](Working-With-Markup-Import-and-Markup-Assist.md)

#### Related References

* [Commands for Markup Import and Markup Assist](Commands-for-Markup-Import-and-Markup-Assist.md)

#### Related Concepts

* [What's New in AutoCAD for Mac 2024](What's-New-in-AutoCAD-for-Mac-2024.md)
* [About Markup Import and Markup Assist](About-Markup-Import-and-Markup-Assist.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*