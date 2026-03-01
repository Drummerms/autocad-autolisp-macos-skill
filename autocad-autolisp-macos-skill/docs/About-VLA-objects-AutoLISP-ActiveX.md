# About VLA-objects (AutoLISP/ActiveX)

Objects in a drawing can be represented as ActiveX (VLA) objects.

NOTE:ActiveX is not supported on Mac OS and Web.

When working with ActiveX methods and properties, you must refer to VLA-objects, not the ename pointer returned by functions
such as
entlast. VLA-objects can be converted to an ename pointer with
vlax-vla-object->ename. You can also use
vlax-ename->vla-object to convert an ename pointer to a VLA-object.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*