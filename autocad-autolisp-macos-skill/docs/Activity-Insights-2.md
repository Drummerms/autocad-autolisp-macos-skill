# Activity Insights

Activity Insights provides an understanding of the past actions that you or others have performed with regard to your drawings.

Activity Insights tracks activities whenever a drawing file is opened and being worked on. It can also track some events
outside the program such as a drawing being renamed or copied in Finder. When a drawing is opened, past activities performed
in the drawing are read from the Activity Insights database and displayed chronologically in the Activity Insights palette.
Activities displayed are limited to the product you are using, for example AutoCAD LT only shows Version activities which
are created from working with drawings stored on a supported cloud storage provider. At the same time, activities are being
written to the database as you work in the drawing, which keeps the contents of the palette current.

NOTE:Activities are logged even when the Activity Insights palette is closed. All activities are displayed the next time the palette
opens.

Activities are written to the Activity Insights Location specified on the Application tab of the Application Preferences dialog
box. The default location for the Activity Insights Location is
/Users/{username}/Library/Application Support/Autodesk/ActivityInsights/Common. Change this to a shared location so that all activities are logged in one location regardless of which drawings are worked
on and who works on them.

![](../images/GUID-5753D71E-D790-426F-BEA5-E27A8F736B64-low.png)

You can also view a drawing's activities without having to opening the file. From the Start tab, click Recent, and select
your drawing. Then, click the vertical ellipsis and select View Activity Insights in AutoCAD or View Drawing History in AutoCAD
LT to see the drawing's activities in the palette.

![](../images/GUID-CF91490A-203B-4CFE-AC67-945489C80A54-low.png)

With this information, meaningful insights can be surfaced about your workflows and practices.

## *New Commands*

[ACTIVITYINSIGHTSCLOSE](ACTIVITYINSIGHTSCLOSE-Command.md) - Closes the Activity Insights palette.

[ACTIVITYINSIGHTSOPEN](ACTIVITYINSIGHTSOPEN-Command.md) - Opens the Activity Insights palette.

## *New System Variables*

[ACTIVITYINSIGHTSPATH](ACTIVITYINSIGHTSPATH-System-Variable.md) - Specifies the path where Activity Insights event log files are written (or copied to).

[ACTIVITYINSIGHTSSUPPORT](ACTIVITYINSIGHTSSUPPORT-System-Variable.md) - Enables or disables the Activity Insights feature.

[ACTIVITYINSIGHTSVIEWEDLOGGING](ACTIVITYINSIGHTSVIEWEDLOGGING-System-Variable.md) - Turns on\off the logging of "Viewed" events.

#### Related Concepts

* [What's New in AutoCAD for Mac 2025](What's-New-in-AutoCAD-for-Mac-2025.md)
* [About Activity Insights](About-Activity-Insights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*