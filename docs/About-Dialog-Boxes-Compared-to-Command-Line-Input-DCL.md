# About Dialog Boxes Compared to Command Line Input (DCL)

Give users some control over how they access the dialog box to enter input.

One advantage of using dialog boxes instead of a command line interface is that boxes do not confine users to a strict sequence
of prompts. In a dialog box, users should be able to enter input in any sequence. Some constraints are necessary—when selecting
one option causes another to be unavailable, for example—but build in only constraints that have underlying reasons in the
way your application works.

For example, the following figure shows the Object Grouping dialog box. This dialog box contains a Group Name field, where
users may enter a name for a new group they are creating. If the Unnamed option is selected, a Group Name cannot be specified.

![](../images/GUID-6E77BE3C-AFB7-4286-9CDB-E9030AE0416E-low.png)

Nested dialog boxes should appear on top of one another rather than require the user to exit the current box before calling
another. Always let users return to the dialog box that was initially displayed. This design does not commit users to a choice
before they are ready to leave the dialog box. Because the current dialog box appears on top of the previous one, it reminds
users of the context: where they have come from and where they will return to.

Whenever users do something to change the current status or options, provide them with immediate feedback. If users select
something, show it or describe it immediately. If one choice excludes other choices, be sure to make the invalid choices unavailable
immediately.

In the AutoCAD Color Selection dialog box, for example, an image tile shows the color immediately after the user selects its
number. In the sample Block Definition dialog box, the number of selected objects is always displayed in a message below the
Select Objects button:

![](../images/GUID-964921C0-F0F9-4C1D-BCB3-592D2E4DD695-low.png)

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Nested Dialog Boxes (DCL)](About-Nested-Dialog-Boxes-DCL.md)
* [About Handling Keyboard Input (DCL)](About-Handling-Keyboard-Input-DCL.md)
* [About Users With Disabilities (DCL)](About-Users-With-Disabilities-DCL.md)
* [About International Language Considerations (DCL)](About-International-Language-Considerations-DCL.md)
* [About Using Capitalization with Tiles (DCL)](About-Using-Capitalization-with-Tiles-DCL.md)
* [Decorative Tiles (DCL)](Decorative-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*