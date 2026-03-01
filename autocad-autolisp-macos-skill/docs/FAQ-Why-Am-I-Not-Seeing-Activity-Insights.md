# FAQ: Why Am I Not Seeing Activity Insights?

This topic covers the most common reasons why you might not be seeing any Activity Insights.

## Not Signed In

Be sure to sign into your Autodesk account from within your product. If you are not signed in, activities are not being collected
within Activity Insights.

## Not the Right Product

Not all Autodesk products support Activity Insights. Currently, AutoCAD, AutoCAD for Mac, AutoCAD Web, and the AutoCAD-based
specialized toolsets support viewing all activities. AutoCAD mobile app can log activities, but does not show activities on
a palette. We are working to include more products in the future.

NOTE:Currently, AutoCAD LT displays only Version activity on the Activity Insights palette. All activities are logged for drawings
saved to OneDrive, Box, Dropbox, and Google Drive. Activities outside of Version activity are not logged for drawings saved
to Autodesk Docs.

## Account and License Type

Activity Insights is only available if:

* You are on the
  [named user plan](https://knowledge.autodesk.com/customer-service/account-management/users-software/user-management/named-users).
* You have a commercial license; not a Not for Resale (NFR), trial, or educational license.

## Activity Insights Location is Not Valid

Activities are written to the Activity Insights Location specified on the Files tab of the Options dialog box (or Application
tab of the Application Preferences dialog box on Mac OS). If that location is not valid or accessible, activities can't be
displayed on the Activity Insights palette.

NOTE:AutoCAD Web includes the Activity Insights feature only for drawings stored in Autodesk Docs.

## Only Seeing My Own Events

Events are being written to a local location. The default locations for the Activity Insights Location are:

* *Windows* -
  C:\Users\{username}\AppData\Local\Autodesk\ActivityInsights\Common
* *Mac OS* -
  /Users/{username}/Library/Application Support/Autodesk/ActivityInsights/Common

Change these to a shared location so that any drawing activity is logged in a single, shared location regardless of who works
on a drawing.

## Activities Processing

It can take a minute or so to process existing activities and refresh the palette after the Activity Insights location is
updated to point to the shared folder.

#### Related Tasks

* [To Work with Activity Insights](To-Work-with-Activity-Insights.md)

#### Related Concepts

* [About Activity Insights](About-Activity-Insights.md)

#### Related Information

* [Commands for Activity Insights](Commands-for-Activity-Insights.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*