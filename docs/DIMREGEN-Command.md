# DIMREGEN (Command)

Updates the locations of all associative dimensions.

## Summary

The locations of all associative dimensions in the current drawing are updated.

Associative dimensions need to be updated manually with DIMREGEN in the following cases:

* After panning or zooming with a wheel mouse in a layout with model space active; update associative dimensions created in
  paper space.
* After opening a drawing containing external references that are dimensioned in the current drawing; update associative dimensions
  if the associated external reference geometry has been modified.

NOTE:After opening a drawing that has been modified with a previous version, the association between dimensions and objects or
points may need to be updated. You can use the [DIMREASSOCIATE](DIMREASSOCIATE-Command.md) command to reassociate modified dimensions with the objects or points that they dimension.

#### Related Concepts

* [About Associative Dimensions](About-Associative-Dimensions.md)
* [About Setting the Scale for Dimensions](About-Setting-the-Scale-for-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*