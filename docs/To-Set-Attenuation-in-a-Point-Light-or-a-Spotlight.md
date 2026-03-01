# To Set Attenuation in a Point Light or a Spotlight

1. In the drawing, click the light glyph.
2. In the Attenuation panel under the Lighting Properties Tab of Properties Inspector:
   * Select a type of attenuation.
     + *Inverse Linear (Standard lights only).* sets attenuation to be the inverse of the linear distance from the light.

       For example, at a distance of 2 units, light is half as strong as at the point light; at a distance of 4 units, light is one
       quarter as strong. The default value for inverse linear is half the maximum intensity.
     + *Inverse Square (Photometric lights).* sets attenuation to be the inverse of the square of the distance from the light. For example, at a distance of 2 units, light
       is one quarter as strong as at the spotlight; at a distance of 4 units, light is one sixteenth as strong.
     + *None (Standard lights only)*. sets no attenuation. Objects far from the point light are as bright as objects close to the light.
3. Check the Use Limits checkbox. The default is no. (Standard Lights only)
4. Enter *Start Limit Offset* to specifies the point where light starts as an offset from the center of the light. The default is 0.
5. Enter *End Limit Offset* to specifies the point where light ends as an offset from the center of the light. No light is cast beyond this point.

#### Related Concepts

* [About Light Properties](About-Light-Properties.md)

#### Related Information

* [To Work With the Adjustment of Lights](To-Work-With-the-Adjustment-of-Lights.md)
* [To Work With the Display of Light Glyphs](To-Work-With-the-Display-of-Light-Glyphs.md)
* [About the Shape Property of a Light](About-the-Shape-Property-of-a-Light.md)
* [To Specify a Source Vector for a Distant Light](To-Specify-a-Source-Vector-for-a-Distant-Light.md)
* [To Change the Color of a Light](To-Change-the-Color-of-a-Light.md)
* [To Assign a Shape to a Light](To-Assign-a-Shape-to-a-Light.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*