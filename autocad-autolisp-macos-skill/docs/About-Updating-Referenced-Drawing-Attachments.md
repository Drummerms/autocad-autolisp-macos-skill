# About Updating Referenced Drawing Attachments

When you open a drawing, all drawing references (xrefs) update automatically. You can also update xrefs whenever you want
to ensure that the most current versions are displayed in your drawing.

When you open a drawing, all xrefs update automatically. Use the Refresh Content (Reload) option from the Reference Manager
to update xrefs whenever you want to ensure that the most current versions are displayed in your drawing.

![](../images/GUID-6CD555D3-4C0D-4758-805F-2EFF242CB16B-low.png)

Whenever you modify and save an externally referenced drawing in a network environment, other people can access your changes
immediately by reloading the xrefs in their open drawings.

## Receive Notification of Changed Xrefs

When you attach xrefs to a drawing, the program periodically checks whether the referenced files have changed since the last
time the xrefs were loaded or reloaded. The XREFNOTIFY system variable controls xref notification.

By default, if a referenced file has changed, a balloon message is displayed near the lower-left corner of the drawing window.
Click the link in the balloon to reload all changed xrefs.

If Compare Changes is checked, the xref is compared to its reference drawing and the comparison results display in the current
drawing. When you close the comparison, the xref is reloaded.

![](../images/GUID-900B6F6C-7A7C-4AF4-965A-C2BAAE0100CB-low.png)

By default, the program checks for changed xrefs every five minutes. You can change the number of minutes between checks by
setting the XNOTIFYTIME system registry variable using
*(setenv "XNOTIFYTIME" "* **n** *")* where
*n* is a number of minutes between 1 and 10080 (seven days).

NOTE:When changing the value of XNOTIFYTIME, you must enter the XNOTIFYTIME with the capitalization as shown.

## Compare an Xref

You can compare an xref with the reference drawing file at any time. Right-click an xref in the Reference Manager and select
one of the compare options. Differences are highlighted with color and revision clouds in the current drawing.

## Update Xrefs with Demand Loading Turned On

If demand loading is turned on when you load or reload an xref

* With the XLOADCTL system variable set to 1, the referenced drawing is kept open and locked. No one else can modify the referenced
  drawing.
* With XLOADCTL set to 2, a temporary copy of the most recently saved version of the referenced file is opened and locked. Others
  can open and modify the referenced drawing.

#### Related Tasks

* [To Compare Xrefs](To-Compare-Xrefs.md)

#### Related References

* [Reference Manager Palette](Reference-Manager-Palette.md)

#### Related Concepts

* [About Nesting and Overlaying Referenced Drawings](About-Nesting-and-Overlaying-Referenced-Drawings.md)
* [About Archiving Drawings with Xrefs (Binding)](About-Archiving-Drawings-with-Xrefs-Binding.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Update an Attached Xref](To-Update-an-Attached-Xref.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*