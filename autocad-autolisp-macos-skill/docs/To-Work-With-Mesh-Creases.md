# To Work With Mesh Creases

## Add a Crease to a Mesh Object

1. (Optional) Specify the type of subobject to crease: right-click in the drawing area and click Subobject Selection Filter ![](../images/ac.menuaro.gif) Face, Vertex, or Edge.
2. Click
   Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Mesh Crease drop-down ![](../images/ac.menuaro.gif) Add Crease.
   ![](../images/GUID-F13194E5-3E58-4DB6-BC93-BE1026424C25-low.png)
3. Select the mesh edges, faces, or vertices to crease. (If you have set a subobject selection filter, only one type of subobject
   can be selected.)

   To remove a subobject from the selection set, Shift+click the subobject.
4. Specify the crease value:
   * *Always* retains the crease at all levels of smoothness.
   * *Values of 1 or higher*sets the level of smoothness that starts to affect the crease.

   The specified subobjects are creased. A crease is not visible on objects that have not been smoothed (the level of smoothness
   = 0).

## Change the Crease Value of an Existing Mesh Crease (Properties window)

1. If the Properties window is not displayed, select any object. Right-click the object and select Properties.
2. Press Ctrl+click the mesh subobject that you want to modify.

   NOTE: If you cannot select a specific subobject, verify whether subobject selection filtering is turned on for a different subobject
   type. (Right-click in the drawing area and click Subobject Selection Filter.)
3. In the Properties window, Crease area, Type box, change the crease value:
   * *None* removes the crease and sets the subobject to the current level of smoothness.
   * *Always* retains the crease at all levels of smoothness.
   * *By Level*sets the level of smoothness that starts to affect the crease. When this setting is selected, you can specify the crease level
     in the Level box.

## Remove a Mesh Crease

1. (Optional) Specify the type of subobject to modify: right-click in the drawing area and click Subobject Selection Filter ![](../images/ac.menuaro.gif) Face, Vertex, or Edge.
2. Click
   Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Mesh Crease drop-down ![](../images/ac.menuaro.gif) Remove Crease.
   ![](../images/GUID-8225CFF1-841A-4ECA-8A93-820278413F29-low.png)
3. Press Ctrl+click the mesh subobjects to be modified and press Enter.

   You can also use window selection to specify multiple subobjects.

#### Related Tasks

* [To Work With Changing Mesh Object Smoothness](To-Work-With-Changing-Mesh-Object-Smoothness.md)
* [To Work With Setting Mesh Density](To-Work-With-Setting-Mesh-Density.md)
* [To Work With Refining Mesh Faces and Objects](To-Work-With-Refining-Mesh-Faces-and-Objects.md)

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Refining Mesh Objects or Subobjects](About-Refining-Mesh-Objects-or-Subobjects.md)
* [About Adding Creases to Meshes](About-Adding-Creases-to-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*