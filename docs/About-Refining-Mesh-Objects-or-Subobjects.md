# About Refining Mesh Objects or Subobjects

Refine a mesh object or subobject to convert underlying facets to editable faces.

You can refine any mesh that has a level of smoothness of 1 or higher.

## Refine a Mesh Object and Reset the Baseline

Refining an object increases the number of editable faces by converting the underlying facets to faces. The number of resulting
faces depends on the current level of smoothness. Higher smoothness levels result in a higher number of faces after refinement.

![](../images/GUID-52D59BC9-DF94-47E6-9BFD-4C047C690607-low.png)

In addition to increasing the number of faces, refining a mesh object resets its level of smoothness back to the baseline.
Therefore, an object might appear to be smoothed, but its smoothness level can still equal 0 (zero).

## Refine a Mesh Face

You can refine an entire mesh object as shown in the previous illustration, or select a specific face to refine. A refined
face is subdivided into four faces and the surrounding faces are deformed slightly to accommodate the change.

![](../images/GUID-002DF25E-41AC-4586-9602-EA9BE115DB44-low.png)

Refining a mesh face does not affect the overall smoothing level of the mesh object. Unlike a refined mesh object, refined
faces can be refined again immediately. With mesh face refinement, you can target smaller areas for detailed modeling.

## How Refinement Affects Creases

A crease that is set to Always retains its sharpness no matter how much you smooth or refine the object. However, the behavior
is different when you assign a crease value. If you refine an object or edge that has a crease value, the assigned crease
value is lowered by the value of the original level of smoothing. Suppose that you add a crease with a crease value of 4 and
then refine a mesh whose level of smoothness is 2. The new crease value is 2.

![](../images/GUID-E98957ED-A596-48F0-9CF6-990B36C687D5-low.png)

If a crease is applied before an object is smoothed or refined, the effect is not apparent until after the object is smoothed
or refined.

#### Related Tasks

* [To Work With Changing Mesh Object Smoothness](To-Work-With-Changing-Mesh-Object-Smoothness.md)
* [To Work With Setting Mesh Density](To-Work-With-Setting-Mesh-Density.md)
* [To Work With Refining Mesh Faces and Objects](To-Work-With-Refining-Mesh-Faces-and-Objects.md)
* [To Work With Mesh Creases](To-Work-With-Mesh-Creases.md)

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Adding Creases to Meshes](About-Adding-Creases-to-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*