# To Work with Activity Insights

View all collaboration in your drawing files by setting up a shared Activity Insights location.

## Workflow

1. [Establish a common location to store all logged activities.](GUID-48FA5C69-37CF-408C-A44C-621E17ABADD7.htm#SECTION_A11367BF2A5E4193AC7F633F650C443C)
2. Open the Activity Insights palette to view activities for:
   * [The current drawing](GUID-48FA5C69-37CF-408C-A44C-621E17ABADD7.htm#SECTION_7D889E4355634672B537672B1E457B01)
   * [A recently opened drawing](GUID-48FA5C69-37CF-408C-A44C-621E17ABADD7.htm#SECTION_8B503C0EA1804C57AF8BEEAECB7D051A)
3. [Filter listed activities.](GUID-48FA5C69-37CF-408C-A44C-621E17ABADD7.htm#SECTION_C0F9B2AA3C10468BB3CCF6865DDCD3A3)

## Set Activity Insights File Location

The default location for Activity Insights is
/Users/{username}/Library/Application Support/Autodesk/ActivityInsights/Common. Without changing this to a shared location, only your events will be logged and displayed in the Activity Insights palette.

To leverage Activity Insights for collaboration, update this to a shared location so that everyone's drawing activities are
logged and displayed in the palette.

1. Click
   AutoCAD 2026 ![](../images/ac.menuaro.gif) Preferences.
2. On the Application tab, expand the Activity Insights Location node.
3. Select the current file path, click
   ![](../images/GUID-4AC4C87F-0D68-4B11-AD8D-D11171DD08B0-low.png) and select Change Path.
4. Browse to and select the desired shared location, and click Open.

NOTE:AutoCAD LT records all drawing activities, but currently shows only Version activities within its palette.

## View Activity Insights For The Current Drawing

1. Click Activity Insights on the toolbar.
   ![](../images/GUID-9B46E37A-20F4-4690-85EE-031FE503F1A9-low.png) Find

   The Activity Insights palette opens, displaying activities for the current drawing.

   NOTE:Activities are logged even when the Activity Insights palette is closed. All activities are displayed the next time the palette
   opens.
2. Click an activity to see more detail in the Activity Properties panel.

   ![](../images/GUID-5A3AC27F-DABD-43E5-A9CA-8D369711C7E4-low.png)

   NOTE:The list of activities updates each time the drawing is saved.

## View Activity Insights For A Drawing On App Home

1. Click the Start tab.
2. On the Start tab, click the Recent tab.
3. On the Recent tab, hover over a drawing in the List or Grid view.
4. Click the vertical ellipsis, and select View Activity Insights in AutoCAD or View Drawing History in AutoCAD LT.

   The Activity Insights palette opens, displaying activities for the current drawing.
5. Click an activity to see more detail in the Activity Insights panel.

   ![](../images/GUID-65F4F995-619F-4C6F-8B10-646F7F920902-low.png)

   NOTE:The list of activities updates each time the drawing is saved.

## Filter Activity Insights

![](../images/GUID-FEBD59C9-5B5B-4E0B-AA6C-116CA778EA4D-low.png)

To filter the list of activities by:

1. * *Date:* Select a date or range of dates from the calendar.
   * *User:* Select the user whose activities you'd like to see. Only users who have activities are included in the list.

     NOTE:AU stands for anonymous user for activities outside the product.
   * *Activity:* Select from the list of activity types for the current drawing.

   NOTE:You can select multiple options from the User and Activity filters.

   ![](../images/GUID-88DC2873-7998-44D5-83ED-BE9B122E0066-low.png)
2. Enter text in the Search field to filter the list of activities based on path and file name.

   Path and file name can apply to any Xref events.

   NOTE:Search can be used on its own or with the Date, User, and Event filters.
3. To clear any filter, select the All, All users, or All activities option from the filter drop-down menu.

#### Related References

* [FAQ: Why Am I Not Seeing Activity Insights?](FAQ-Why-Am-I-Not-Seeing-Activity-Insights.md)

#### Related Information

* [Commands for Activity Insights](Commands-for-Activity-Insights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*