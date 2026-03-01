# About Docs Markup Import

Import and sync published markups from Autodesk Docs to AutoCAD so that drafters can more easily view and incorporate revisions.

NOTE:Access the online
[AutoCAD help](https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-0CD6B2CE-EAF0-478B-B39B-F4821F9DC91D) to see the latest information for Markup Import and Markup Assist.

In Autodesk Docs, add markups to a PDF file, then share the PDF from Autodesk Docs with collaborators who can view the markups
in the AutoCAD Trace environment. The PDF is continually connected to the AutoCAD drawing, meaning as updates and revisions
are made to the PDF markup file in Autodesk Docs, collaborators can see those changes in AutoCAD.

NOTE:

* Markup Import and Markup Assist are not available for AutoCAD LT or AutoCAD LT for Mac.
* AutoCAD for Mac doesn't support the ability to import markups from Autodesk Docs but can display markups from Autodesk Docs
  in a drawing created with AutoCAD on Windows. See the
  [Opening Markups in AutoCAD (as a recipient)](GUID-09B13612-17BF-41B0-ADAD-693975006B6B.htm#SECTION_14710F23956F4201A13FAA3C40D8E377) section for more information.

## Sending Markups from Autodesk Docs (as a sender)

1. In Autodesk Docs, in the Files tool, open a PDF with published markups.
2. Select Sync markups to AutoCAD.

![](../images/GUID-ED120DC7-4112-47C7-B11A-45622674B9A9-low.png)

3. Choose who will receive the markups and add any comments.
4. Click Send.

![](../images/GUID-5E4ED576-EDCE-4593-AD65-F1440271561A-low.png)

Recipients will receive an email from Autodesk Construction Cloud with a link to the AutoCAD drawing.

## Opening Markups in AutoCAD (as a recipient)

NOTE:Opening and importing markups from Autodesk Docs is not available on AutoCAD for Mac. However, once markups are imported by
a recipient in Windows, the synced markups will be available on AutoCAD for Mac. When the markups from Autodesk Docs changes,
a notification pops up the next time the drawing or trace is opened. The notification contains a link to open the PDF (with
markups) from Docs in your Web browser.

1. In the email received from Autodesk Construction Cloud, click Import and Sync Markups to AutoCAD. The default version of AutoCAD
   opens.

Alternatively, a recipient can use MARKUPIMPORT and select the PDF that contains published markups.

NOTE:Autodesk Desktop Connector must be installed.
[Click here to install Autodesk Desktop Connector](https://www.autodesk.com/markup-import-desktop-connector-install) (Windows only).

2. Once AutoCAD opens, you're prompted to import the markup to a drawing layout (or model).

*If AutoCAD is able to detect the drawing and layout associated with the PDF:*

3. The layout opens. Choose Import markup to import the markup onto a new trace. Or, if the currently displayed layout is incorrect,
   select a different layout onto which to import the PDF.

*If AutoCAD is unable to detect the drawing and layout associated with the PDF:*

You'll need to manually select the drawing and layout on which to import the markup.

4. Open the drawing and layout onto which you would like to import the markup.
5. Once the correct layout is displayed, click the link in the notification to import the markup onto a new trace.

![](../images/GUID-7A7A5472-BC08-45A1-ACA0-1423AE2BDBC0-low.png)

Once the PDF has been imported to AutoCAD and associated with a drawing, any changes made to the PDF in Autodesk Docs will
be reflected in AutoCAD the next time the trace is opened in AutoCAD. This means that as a reviewer updates the PDF markup
file in Autodesk Docs, any drafter who has the drawing open in AutoCAD will see those updates every time they re-open the
trace.

## Automatically Associating PDFs with Drawings

When opening and importing markups, some PDF markups will automatically associate with the related drawing and layout. Drawings
and markups will automatically associate if:

* The drawing is saved to Autodesk Docs.
* The PDF was created using Plot to PDF in AutoCAD (Windows) 2025 or later, and was plotted from an Autodesk DWG to PDF driver.
* Desktop Connector is installed.

Any other type of PDF needs to be manually associated. This includes:

* PDFs created from AutoCAD 2024 or earlier.
* PDFs created from AutoCAD for Mac.
* PDFs that were created from drawings not saved to Autodesk Docs.
* PDFs plotted from third party drivers (non-Autodesk DWG to PDF drivers).

## Additional Notes:

* Any project members with permission to view the drawing and PDF will be able to open the link that is generated in the email
  from Autodesk Construction Cloud. This means the link can be forwarded, but only project members who have been granted access
  to the file(s) can successfully open them. Administrators can add or remove project members and set permissions in Autodesk
  Docs.

#### Related Concepts

* [About Trace](About-Trace.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*