# Obtain a Point by Cursor (CAL Command)

To enter a point using the pointing device, use the
*cur* function. The program prompts you to specify a point and uses the coordinate values of the point in the expression. The point
coordinate values are expressed in terms of the current UCS. The
*cur* function sets the value of the [LASTPOINT](LASTPOINT-System-Variable.md) system variable.

The following example adds the vector [3.6,2.4,0]—the result of 1.2\*[3,2]—to the point you select. This expression produces
a point that is offset from the selected point.

*cur+1.2\*[3,2]*

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*