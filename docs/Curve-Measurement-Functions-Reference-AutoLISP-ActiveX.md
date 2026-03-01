# Curve Measurement Functions Reference (AutoLISP/ActiveX)

NOTE:ActiveX support in AutoLISP is limited to Windows only; not available on Mac OS or Web.

The following table provides summary descriptions of the AutoLISP curve measurement functions.

| Curve measurement functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(vlax-curve-getArea curve-obj)](vlax-curve-getArea-AutoLISP-ActiveX.md) | Returns the area inside the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getClosestPointTo curve-obj givenPnt [extend])](vlax-curve-getClosestPointTo-AutoLISP-ActiveX.md) | Returns the point (in WCS coordinates) on a curve that is nearest to the specified point | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getClosestPointToProjection curve-obj givenPnt normal [extend])](vlax-curve-getClosestPointToProjection-AutoLISP-ActiveX.md) | Returns the closest point (in WCS) on a curve after projecting the curve onto a plane | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getDistAtParam curve-obj param)](vlax-curve-getDistAtParam-AutoLISP-ActiveX.md) | Returns the length of the curve's segment from the curve's beginning to the specified parameter | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getDistAtPoint curve-obj point)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md) | Returns the length of the curve's segment between the curve's start point and the specified point | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getEndParam curve-obj)](vlax-curve-getEndParam-AutoLISP-ActiveX.md) | Returns the parameter of the endpoint of the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getEndPoint curve-obj)](vlax-curve-getEndPoint-AutoLISP-ActiveX.md) | Returns the endpoint (in WCS coordinates) of the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getFirstDeriv curve-obj param)](vlax-curve-getFirstDeriv-AutoLISP-ActiveX.md) | Returns the first derivative (in WCS coordinates) of a curve at the specified location | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getParamAtDist curve-obj point)](vlax-curve-getParamAtDist-AutoLISP-ActiveX.md) | Returns the parameter of a curve at the specified distance from the beginning of the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getParamAtPoint curve-obj dist)](vlax-curve-getParamAtPoint-AutoLISP-ActiveX.md) | Returns the parameter of the curve at the point | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getPointAtDist curve-obj dist)](vlax-curve-getPointAtDist-AutoLISP-ActiveX.md) | Returns the point (in WCS coordinates) along a curve at the distance specified by the user | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getPointAtParam curve-obj param)](vlax-curve-getPointAtParam-AutoLISP-ActiveX.md) | Determines the point on the curve that corresponds to the *param* parameter and returns the point | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getSecondDeriv curve-obj param)](vlax-curve-getSecondDeriv-AutoLISP-ActiveX.md) | Returns the second derivative (in WCS coordinates) of a curve at the specified location | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getStartParam curve-obj)](vlax-curve-getStartParam-AutoLISP-ActiveX.md) | Returns the start parameter on the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-getStartPoint curve-obj)](vlax-curve-getStartPoint-AutoLISP-ActiveX.md) | Returns the start point (in WCS coordinates) of the curve | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-isClosed curve-obj)](vlax-curve-isClosed-AutoLISP-ActiveX.md) | Determines if the specified curve is closed (i.e., start point is same as endpoint) | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-isPeriodic curve-obj)](vlax-curve-isPeriodic-AutoLISP-ActiveX.md) | Determines if the specified curve has an infinite range in both directions and there is a period value  *dT,* such that there is a point on curve at ( *u* +  *dT*) = point on curve ( *u*), for any parameter  *u* | ✓ | ✓ | -- | -- | -- |
| [(vlax-curve-isPlanar curve-obj)](vlax-curve-isPlanar-AutoLISP-ActiveX.md) | Determines if there is a plane that contains the curve | ✓ | ✓ | -- | -- | -- |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

#### Related Concepts

* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*