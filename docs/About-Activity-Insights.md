# About Activity Insights

Use Activity Insights to see your teammates' contributions to shared drawing files, view version histories, and collaborate
across AutoCAD products.

Activity Insights records each contributor's updates to a drawing file, streamlining collaboration and helping you pick up
where you left off.

![](../images/GUID-5A3AC27F-DABD-43E5-A9CA-8D369711C7E4-low.png)

NOTE:Activities are logged even when the Activity Insights palette is closed. All activities are displayed the next time the palette
opens.

## Activity Insights Location

Activities are written to the Activity Insights Location specified on the Application tab of the Application Preferences dialog
box. The default location is
/Users/{username}/Library/Application Support/Autodesk/ActivityInsights/Common.

To use Activity Insights for collaboration, change this to
[a shared location](GUID-48FA5C69-37CF-408C-A44C-621E17ABADD7.htm#GUID-C7CA5859-3F99-489F-8ADD-AAAF3F69C04B).

NOTE:AutoCAD LT for Mac allows you to only view Version activities when working with files saved to supported cloud storage providers
such as Google Drive, OneDrive, Box, and Dropbox. However, AutoCAD LT for Mac does support the logging of all drawing activities.
To make sure you capture all drawing activities, your collaborators using AutoCAD LT for Mac should set the
[ACTIVITYINSIGHTSPATH](ACTIVITYINSIGHTSPATH-System-Variable.md) system variable at the Command prompt to the same shared location.

## See Activity Types

Below is a list of some of the activities logged and displayed on the Activity Insights palette:

| Action | Activity Insights tile |
| Saving an unnamed drawing | New drawing created |
| Saving changes to a drawing | Saved |
| Saving a version of the drawing stored within a supported cloud provider | Version (version number) |
| Saving to a different file format | Saved to different format |
| Actions with Xrefs | Partial list of xref activities:  * Referenced a DWG * Referenced by other DWG * Bound a DWG |
| Drawing file cleanup | Partial list of cleanup activities:  * Purged * Audited |

## Activities Outside AutoCAD

There are some activities that occur outside of AutoCAD and AutoCAD LT that are included in the Activity Insights display.
They can include the following:

* Drawing renamed using Finder
* Drawing copied using Finder
* An older release of the product is used to make edits to the drawing

The user for these activities is shown as Unknown user on the Activity Insights palette.

## Collaborating Across AutoCAD Products

All AutoCAD products record drawing activities. However, AutoCAD LT currently only displays Version activities on its palette,
and AutoCAD for mobile does not have an Activity Insights palette. When working with collaborators across different AutoCAD
products, make sure you are all saving to the same Activity Insights location.

AutoCAD, AutoCAD for Mac, and AutoCAD for web displays all activities for the open drawing even if a specific activity isn't
supported within that AutoCAD product. For example, the STANDARDS command is only supported in AutoCAD on Windows. But if
used, the Standards activity will show up in the Activity Insights palette for AutoCAD for Mac and AutoCAD for web.

#### Related References

* [FAQ: Why Am I Not Seeing Activity Insights?](FAQ-Why-Am-I-Not-Seeing-Activity-Insights.md)

#### Related Information

* [Commands for Activity Insights](Commands-for-Activity-Insights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*