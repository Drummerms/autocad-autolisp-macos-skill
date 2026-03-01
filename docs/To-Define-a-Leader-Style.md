# To Define a Leader Style

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Leader panel ![](../images/ac.menuaro.gif) Multileader Style Manager.
   ![](../images/GUID-35FD07B0-ECA0-4396-A6F4-B3DC82B3998C-low.png)
2. In the Multileader Style Manager, click New.
3. In the Create New Multileader Style dialog, specify a name for the new multileader style.
4. In the Modify Multileader Style dialog, Leader Format tab, select or clear the following options:
   * *Type*. Determines the type of landing. You can choose a straight landing, spline landing, or no landing.
   * *Color*. Determines the color of the landing.
   * *Linetype*. Determines the linetype of the landing.
   * *Lineweight*. Determines the lineweight of the landing.
5. *Arrow head*. Specify a symbol and size for the multileader arrowhead.
6. *Leader Break*. Controls the settings used when adding a dimension break to a multileader.
   * *Break Size*. Displays and sets the break size used for the DIMBREAK command when the multileader is selected.
7. On the Leader Structure tab, select or clear the following options:
   * *Maximum Leader Points*. Specifies a maximum number of points for the multileader landing line.
   * *First and Second Segment Angles*. Specifies the angle of the first and second points in the landing.
   * *Landing*. Controls the landing settings of the multileader.
     + *Automatically include*. Attaches a horizontal landing to the multileader content.
     + *Set Distance*. Determines the fixed distance for the multileader landing line.
   * *Scale*. Controls the scaling of the multileader.
     + *Annotative*. Specifies that the multileader is annotative.
     + *Scale to Layout*. Determines a scaling factor for the multileader based on the scaling in the model space and paper space viewports.
     + *Specify Scale*. Specifies the scale for the multileader.
8. On the Content tab, specify either text or block content for the multileader. If the multileader object will contain text
   content, then select or clear the following options:
   * *Default Text*. Sets default text for the multileader content. A field can be inserted here. The [...] button launches the MTEXT In Place
     Editor.
   * *Text Style*. Specifies a predefined text style for the attribute text. Currently loaded text styles are displayed.
   * *Text Angle*. Specifies the rotation angle of the multileader text.
   * *Text Color*. Specifies the color of the multileader text.
   * *Text Height*. Sets the height of the multileader text as it will display in paper space.
   * *Frame Text*. Frames the multileader text content with a text box.
   * *Attachment*. Controls the attachment of the landing to the multileader text.
     + *Horizontal*. Inserts the leader to the left or right of the text content. A horizontal attachment includes a landing line between the
       text and the leader.
       - *Left*.Controls the attachment of the landing line to the multileader text when the text is to the right of the leader.
       - *Right*.Controls the attachment of the landing line to the multileader text when the text is to the left of the leader.
       - *Landing Gap*.Specifies the distance between the landing line and the multileader text
       - *Extend Leader to Text*. Extends the landing line to end at the edge of the text line where the leader is attached, not at the edge of the multiline
         text box.

         The length of the multiline text box is determined by the length of the longest line of text, not the length of the bounding
         box.
     + *Vertical*. Inserts the leader at the top or bottom of the text content. A vertical attachment does not include a landing line between
       the text and the leader.
       - *Top*. Attaches the leader to the top center of the text content. Click the drop-down to insert an overline between the leader
         attachment and the text content.
       - *Bottom*. Attaches the leader to the bottom of the text content. Click the drop-down to insert an underline between the leader attachment
         and the text content.
       - *Landing Gap*.Specifies the distance between the landing and the multileader text.

   If block content is specified, then select or clear the following options:

   * *Source Block*. Specifies the block used for multileader content.
   * *Attachment*. Specifies the way the block is attached to the multileader object. You can attach the block by specifying the extents, the
     insertion point, or the center point of the block.
   * *Color*. Specifies the color of the multileader block content. The Block color control in the MLEADERSTYLE Content tab only takes
     effect if the object color included in the block is set to ByBlock.
   * *Scale*. Specifies the scale of the block upon insertion. For example, if the block is a 1 inch square and the scale specified is
     0.5000, then the block is inserted as a 1/2 inch square.
9. Click OK.

#### Related Concepts

* [About Leader Styles](About-Leader-Styles.md)
* [About Adding Content to a Leader](About-Adding-Content-to-a-Leader.md)

#### Related Information

* [To Collect Multiple Notes to be Attached to a Single Landing](To-Collect-Multiple-Notes-to-be-Attached-to-a-Single-Landing.md)
* [To Create a Landing Line With Multiple Segments](To-Create-a-Landing-Line-With-Multiple-Segments.md)
* [To Apply a Leader Style to an Existing Leader](To-Apply-a-Leader-Style-to-an-Existing-Leader.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*