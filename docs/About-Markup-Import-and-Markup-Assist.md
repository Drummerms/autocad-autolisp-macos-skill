# About Markup Import and Markup Assist

Markup Import and Markup Assist use machine learning to identify markups and provide a way to view and insert drawing revisions
with less manual effort.

NOTE:Access the online
[AutoCAD for Mac help](https://help.autodesk.com/view/ACDMAC/2026/ENU/?guid=GUID-0CD6B2CE-EAF0-478B-B39B-F4821F9DC91D) to see the latest information for Markup Import and Markup Assist.

NOTE:Markup Import and Markup Assist are not available for AutoCAD LT or AutoCAD LT for Mac.

Markups can be imported as a PDF, JPG, or PNG and are overlaid on top of your drawing in the Trace environment. Markups in
the imported file are automatically identified as text, revision clouds, strikethroughs, and instructions (such as "move"
or "rotate"). Markup Assist lets you insert those identified markups into the drawing as text or revision clouds, or use the
markups to revise existing text and geometry.

NOTE:Because markups are processed in the cloud, an internet connection is required to use Markup Import and Markup Assist.

## Markup Import

Use Markup Import to place a marked-up version of your drawing on top of the original file to make it easier to view and
incorporate changes to your drawing. For example, if you have a PDF version of your drawing that has text and revision notes
added, use Markup Import to overlay the revised drawing on top of the original. Or, if you have a printed version of your
drawing that contains hand-written revision notes, you can take a photograph of the printed version and then import it as
a JPG or PNG.

![](../images/GUID-5D25BFC7-C136-43FE-8968-F4CCC6F5CF9B-low.png)

Imported markups are added as a new trace in the Trace environment. Use TRACEPALETTEOPEN to open the Traces palette and view
a list of traces in the drawing.

The imported file is automatically placed and aligned on top of the drawing file in a new trace. The imported file can be
a representation of the entire drawing or only a part of the drawing. If the imported file is not aligned correctly, you can
manually align, move, scale, or rotate the imported file.

When viewing imported markups, you can change the background transparency to adjust the visibility of the imported markup.

![](../images/GUID-BC1EFAC7-9915-4DDA-A0C1-466EF7D0B11D-low.png)

## Markup Assist

Markup Assist automatically identifies markups as text and revision clouds. After importing a markup, turn on TRACEBACK to
activate the trace mode that lets you modify the drawing itself.

![](../images/GUID-F3555BF1-7508-401F-B32E-1E2A903FE8D2-low.png)

Click a text markup, then insert it as mtext or an mleader, or use it to update existing text in the drawing. Click a boundary
markup (for instance, a hand-drawn circle), and insert it as a revision cloud. You can edit text before inserting it, copy
the text to the clipboard, or use Update Existing Text to replace or amend existing text in the drawing. Inserted text, leaders,
and revclouds take on the properties of the current layer and current text style.

Use Fade Markup to control the transparency of individual markups. Fade Markup is useful for hiding any markups that you've
already inserted, or if there is a markup you want to ignore. Access the FADEMARKUP command from the Trace toolbar, or from
the Markup Assist dialog box. Control the transparency of faded markups in Trace Settings on the Trace toolbar, or with the
TRACEMARKUPFADECTL system variable.

![](../images/GUID-87FE244A-B510-4707-8566-D16C57157E8A-low.png)

## Best Practices for using Markup Import

* *Trace and Markup Import work best with 2D drawings.* Markups are not easily identified in drawings that are 3D or have non-wireframe visual styles.
* *Imported images are reduced to 4k resolution.* It's recommended that imported markups do not exceed 4k monitor resolution or 144 dpi.
* *When taking photographs of physical paper, ensure that the paper is brightly and evenly lit.* Avoid shadows falling onto the paper, including folds and creases, and avoid taking photographs where the lighting is uneven
  across the extents of the paper. Shadowy or unevenly lit photographs will decrease the likelihood that the markup is successfully
  identified as being separate from the underlying drawing.
* *When taking photographs of physical paper, do not include objects in the background other than the drawing page.* If needed, crop the image to the physical page after the photograph has been taken. If the markup is only in a small area
  of the drawing, it isn't necessary to include the entire drawing in the photograph, but AutoCAD will generally do a better
  job of automatically aligning the photograph to the drawing when more of the paper is included in the image.
* *When taking photographs of physical paper, avoid taking photographs of the page from an acute angle.* As much as possible, take photographs from directly above the paper, with the camera pointed directly at the page. Photographs
  taken from acute angles will introduce distortion into the image after it is imported into AutoCAD, and AutoCAD will be less
  likely to automatically align these images to the drawing. Unlike distortions, rotation of the page in the image should not
  cause distortion and generally will not cause AutoCAD to be less successful aligning the image to the drawing. For example,
  it is not necessary for the "top" of the page to be the "top" of the image.

## Best Practices for using Markup Assist

* *Markup Import works best when the non-markup part of the imported file is monochrome or grayscale.* For best performance, use imported drawings that don't contain colored lines or regions.
* *Markup Import works best when the markup is made in a solid, opaque color, such as red, and not black or dark blue.* Markup in black or dark blue colors, or markup that is light in color or not opaque (such as a colored pencil or a highlighter)
  will decrease the likelihood that the markup is successfully identified as being separate from the underlying drawing.
* *Use high-resolution scans and photographs.* Imported images with scaled-down resolution may reduce markup assist's effectiveness.

## Web and Mobile

All Markup Import features are available in the AutoCAD web and mobile apps. The AutoCAD mobile app also allows you to import
a photo directly from the device's camera. Go to
Annotate ![](../images/ac.menuaro.gif) Import Markup ![](../images/ac.menuaro.gif) Camera and follow the steps on your mobile device to import a photograph of your markup.

NOTE:Markup Assist is not available for the AutoCAD web or mobile apps.

#### Topics in this section

* [Working With Markup Import and Markup Assist](Working-With-Markup-Import-and-Markup-Assist.md)

  Use Markup Import to overlay a marked-up PDF, JPG, or PNG file on top of a drawing in the Trace workspace, and use Markup
  Assist to insert any detected markups into the drawing.
* [Data Processing for Markup Import and Markup Assist](Data-Processing-for-Markup-Import-and-Markup-Assist.md)
* [About Docs Markup Import](About-Docs-Markup-Import.md)

  Import and sync published markups from Autodesk Docs to AutoCAD so that drafters can more easily view and incorporate revisions.

#### Related References

* [Data Processing for Markup Import and Markup Assist](Data-Processing-for-Markup-Import-and-Markup-Assist.md)

#### Related Concepts

* [About Trace](About-Trace.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*