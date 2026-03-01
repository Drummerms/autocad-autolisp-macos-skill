# To Create a Point Light in Standard Lighting Workflow

Creates a point light that radiates light in all directions from its location.

1. At the command prompt, enter
    *lightingunits* and set the value to 1 (American units) or 2 (International SI units) for photometric lighting.
2. Click
   Modeling tab ![](../images/ac.menuaro.gif) Render panel ![](../images/ac.menuaro.gif) Light drop-down ![](../images/ac.menuaro.gif) New Point Light.
   ![](../images/GUID-B12DEAEE-5ABC-4685-B80D-AAA31F2E0B6F-low.png)
3. Click in the drawing to specify a location for the light. Enter coordinate values or use the pointing device.
4. If the LIGHTINGUNITS system variable is set to 0, the following prompt is displayed: Enter an option to change [ Name/ Intensity/
   Status/ shadoW/ Attenuation/ Color/ eXit] <eXit>:
5. If the LIGHTINGUNITS system variable is set to 1 or 2, the following prompt is displayed: Enter an option to change [ Name/
   Intensity factor/ Status/ Photometry/ shadoW/ Attenuation/ filterColor/ eXit] <eXit>:

NOTE:When the LIGHTINGUNITS system variable is set to 1 or 2, the Attenuation option has no affect on the creation of the light.
It is only maintained for scripting compatibility.

6. At the Command prompt, enter
   *n* and enter a name. This name will appear in the properties and in the Lights in Model window.

   You can continue to specify properties by entering options, or you can exit and set properties interactively. When you use
   the interactive method, you can see the results of your changes as you work.
7. Press Enter twice to exit the command.

   Select the light and use grip tools to change the light. You can also right-click the light and then click Properties.

#### Related Concepts

* [About Lighting](About-Lighting.md)
* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)

#### Related Information

* [To Work With Lighting Settings](To-Work-With-Lighting-Settings.md)
* [About Point Lights](About-Point-Lights.md)
* [To Create a Point Light in Photometric Workflow](To-Create-a-Point-Light-in-Photometric-Workflow.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*