# Working With Markup Import and Markup Assist

Use Markup Import to overlay a marked-up PDF, JPG, or PNG file on top of a drawing in the Trace workspace, and use Markup
Assist to insert any detected markups into the drawing.

NOTE:Markup Import and Markup Assist are not available for AutoCAD LT or AutoCAD LT for Mac.

## Import a Markup

1. Click
   Collaborate Tab ![](../images/ac.menuaro.gif) Traces Panel ![](../images/ac.menuaro.gif) Markup Import.
2. Select a PDF, JPG, or PNG markup file to import.

   The imported markup file can include hand-drawn or digitally drawn markups. The markup file can be a digital copy, a photograph,
   or a scanned version of the original drawing.
3. Move, align, rotate, or scale the markup if the imported markup file isn't automatically aligned to the drawing correctly.

## Modify or Align the Imported Markup File

Imported markups are automatically aligned with the existing drawing. However, sometimes the imported markup doesn't align
correctly and requires manual alignment.

To align the imported file:

1. Specify a source point and then the corresponding destination point. To rotate the imported markup, specify a second source
   point followed by a second destination point.
2. Press Enter to end the command.
3. The selected objects are moved from the source point to the destination point. Second and third points, if you specify them,
   rotate, and tilt the selected objects.

## Use Markup Assist To Insert Text

Markup Assist identifies text in the imported markup that can be inserted into the drawing file as multiline text or as a
multileader object, or used to append or replace existing text in the drawing.

1. After importing a markup, with the trace open, turn on TRACEBACK and MARKUPASSISTMODE.

   ![](../images/GUID-F3555BF1-7508-401F-B32E-1E2A903FE8D2-low.png)
2. Click the blue highlighted border of an identified text markup. When hovering over an identified markup, you'll see the Markup
   Assist icon.
   ![](../images/GUID-1ACB4267-9A16-4939-99D5-65B573048A0A-low.png)

   The Markup Assist dialog box opens.

   ![](../images/GUID-1BB8E43E-6929-4876-A5FE-750F26C1D20F-low.png)
3. Select one of the following:
   * *Insert as Mleader.* Starts the MLEADER command and inserts the markup text into the drawing. After inserting as an mleader, the markup switches
     to faded.
   * *Insert as Mtext.* Starts the MTEXT command and inserts the markup text into the drawing. After inserting as mtext, the markup switches to faded.
   * *Update Existing Text.* Use the markup text to append or replace existing drawing text. After appending or replacing text, the markup switches to
     faded.
   * *Fade Markup.* Fade the markup so it is less visible on the trace.
   * *Copy to Clipboard.* Copy the text to the Clipboard.

Often, Markup Assist doesn't perfectly identify the characters in the markup text. This is especially true with hand-written
markups. Fortunately, you can edit the text using the Markup Assist dialog box before inserting it. To add more complex changes
or formatting changes, it's recommended to copy to the text to Clipboard and edit text outside the Markup Assist dialog box,
or insert the text into the drawing, then edit it using the MTEDIT command.

## Use Markup Assist to Insert a Revision Cloud

Markup Assist identifies boundaries (for instance, a hand drawn circle) that can be inserted into the drawing as revision
clouds.

1. After importing a markup, with the trace open, turn on TRACEBACK and MARKUPASSISTMODE.
2. Click the blue highlighted border of the boundary markup. When hovering over an identified markup, you'll see the Markup
   Assist icon.
   ![](../images/GUID-1ACB4267-9A16-4939-99D5-65B573048A0A-low.png)

The Markup Assist dialog box opens.

3. Select one of the following:
   * *Insert as Rectangular Revcloud.* Insert a rectangular revision cloud into the drawing, using the highlighted border as the defined size and shape of the revcloud.
     The markup switches to faded.
   * *Insert as Polygonal Revcloud.* Insert a polygonal revision cloud into the drawing, using the approximate shape of the detected markup as the defined size
     and shape of the revcloud. The markup switches to faded.
   * *Fade Markup.* Fade the markup so it is less visible on the trace.

## Use Markup Assist to Update Existing Text

You can use the markup text to append or replace existing text in the drawing.

1. After importing a markup, with the trace open, turn on TRACEBACK and MARKUPASSISTMODE.
2. Click the blue highlighted border of an identified text markup. When hovering over an identified markup, you'll see the Markup
   Assist icon.
   ![](../images/GUID-1ACB4267-9A16-4939-99D5-65B573048A0A-low.png)

The Markup Assist dialog box opens.

3. Select Update Existing Text.
4. Select the text in the drawing that you want to update.
5. Choose one of the following:

   * *Append.* Opens the text editor and adds the text to the end of the existing text.
   * *Replace.* Opens the text editor and adds the text to the end of the existing text. Make changes in the text editor, and close the text
     editor when complete.
   * *Select a strikethrough.* Select a strikethrough markup, which opens the text editor and adds the text in place of the crossed out text.
6. Make changes in the text editor, and close the text editor when complete.

## Use Strikethrough Text

Markup Assist recognizes text that has been crossed out, and allows you to erase the text or replace the text with text from
a markup.

To replace existing text:

1. Click a strikethrough markup. The Markup Assist dialog box opens.
2. Click Replace Existing Text.
3. Click the text in the drawing to replace.
4. Click the text in the markup to replace the existing text with.

To erase existing text:

1. Click a strikethrough markup. The Markup Assist dialog box opens.
2. Click Erase Existing Text.
3. Select the text in the drawing to erase.

## Fade and Unfade Markups

1. With TRACEBACK on, click Fade Markup on the Trace toolbar. Alternatively, at the Command Prompt, enter FADEMARKUP.
2. Select markups. To unfade, enter N at the Command Prompt and then select markups.

You can also fade and unfade individual markups by clicking the markup while in Markup Assist mode, and then selecting Fade
Markup or Unfade Markup from the Markup Assist dialog box.

## Selecting Markups Within a Boundary

When you use any command that prompts to "Select Objects," you can click the blue highlighted border of a Markup Assist boundary
to select all the AutoCAD objects within it. When you click the highlighted border, all objects entirely within the border
are added to the selection set.

NOTE:Set the MARKUPSELECTIONMODE to 0 to turn off, 1 to enable selection using boundary markup assist boxes as criteria, or 2 to
enable selection using any markup assist box as criteria.

## Markups With Associated PDF Text Comments

Text comments that are added to a PDF using Adobe software will display and can be inserted into the drawing as an Mleader
or Mtext, or used to update existing text.

![](../images/GUID-D03D6413-07A7-4A63-8A9E-F73E4DDF4CA3-low.png)

To insert text from a PDF text comment:

1. Click the markup that contains a PDF text comment.

The Markup Assist dialog box opens.

2. Insert the text as an Mleader, Mtext, or Update Existing Text.

## Instruction Text on a Markup

Markup Assist detects certain instructions in markup text that are linked to commands such as "MOVE," "COPY," or "DELETE."
When Markup Assist identifies an instruction, you can click that instruction to start the associated command.

![](../images/GUID-1C5FD0C7-7C5B-46D4-B7A0-7B857424ED24-low.png)

## To Import Markup Directly from Your Camera on a Mobile Device

You can use the AutoCAD mobile app to import a photograph into the drawing as markup.

1. In the AutoCAD mobile app, tap
   Annotate ![](../images/ac.menuaro.gif) Import Markup ![](../images/ac.menuaro.gif) Camera.
2. Using the device's camera, take a photo and confirm the image.

#### Related Concepts

* [About Trace](About-Trace.md)

#### Related Information

* [About Docs Markup Import](About-Docs-Markup-Import.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*