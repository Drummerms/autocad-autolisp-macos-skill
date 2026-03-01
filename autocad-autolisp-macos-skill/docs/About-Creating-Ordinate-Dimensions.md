# About Creating Ordinate Dimensions

Ordinate dimensions measure the perpendicular distance from an origin point called the *datum* to a feature, such as a hole in a part. These dimensions prevent escalating errors by maintaining accurate offsets of the
features from the datum.

![](../images/GUID-7CD94721-71B5-47D2-A5A9-F26A918C5DFE-low.png)

Ordinate dimensions consist of an *X* or *Y* value with a leader line. *X*-datum ordinate dimensions measure the distance of a feature from the datum along the *X* axis. *Y*-datum ordinate dimensions measure the distance along the *Y* axis.

![](../images/GUID-B871CB53-4DA9-4725-978B-C612E78792D3-low.png)

## Locate the Datum

The location and orientation of the current UCS determines the ordinate values. Before creating ordinate dimensions, you typically
set the UCS origin to coincide with the datum.

![](../images/GUID-4E300956-2CDC-4428-969A-A765E0BD3CEE-low.png)

## Locate the Leader

After you specify the feature location, you are prompted for the leader endpoint. By default, the leader endpoint that you
specify automatically determines whether an *X*- or a *Y*-datum ordinate dimension is created. For example, you can create an *X*-datum ordinate dimension by specifying a location for the leader endpoint that is closer to vertical than horizontal.

![](../images/GUID-E30051B1-EFA9-4C69-9A04-9368E7AC7EAF-low.png)

After creating an ordinate dimension, you can easily relocate the dimension leader and text using grip editing. The dimension
text is always aligned with the ordinate leader line.

#### Related Tasks

* [To Create an Ordinate Dimension](To-Create-an-Ordinate-Dimension.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*