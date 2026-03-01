# About Lighting

## Default Lighting

When there are no lights in a scene, the scene is rendered with default lighting. Default lighting is derived from one or
two distant light sources that follow the viewpoint as you orbit around the model. All faces in the model are illuminated
so that they are visually discernible. You can adjust the exposure of the rendered image, but you do not need to create or
place lights yourself.

When you place user-defined lights or enable sunlight, you can optionally disable default lighting. Default lighting is set
per viewport, and it is recommended to disable default lighting when user-defined lights are placed in a scene.

## Photometric Lighting

You add lights to give a scene a natural and realistic appearance. Lighting enhances the clarity and three-dimensionality
of a scene. Photometric lights use photometric (light energy) values that enable you to define lights more accurately as they
would be in the real world. You can create lights with various distribution and color characteristics, or import specific
photometric files available from lighting manufacturers.

Photometric lights can use an Illuminating Engineering Society (IES) photometric data file format published by lighting manufacturers.
By using the IES data files published by a manufacturer, you can visualize commercially available lighting in your model.
Then you can experiment with different fixtures, and by varying the light intensity and color temperature, you can design
a lighting system that produces the results you want.

![](../images/GUID-99083F95-4B68-474C-B889-CAF05DDDFB63-low.png)

## Sun and Sky

The sun is a special light available as part of the photometric workflow and is similar to a distant light. The angle of
the sun is defined by the geographic location that you specify for the model and by the date and time of day that you specify.
The intensity and color emitted by the sun can be adjusted to reflect different times of day and atmospheric conditions. The
sun and sky are the primary sources of natural illumination. With sun and sky simulation, you can adjust their properties
and enable sky illumination (through the sky background feature). The sky background feature adds soft, subtle lighting effects
caused by the lighting interactions between the sun and the atmosphere.

## Standard Lighting

For more creative control over lighting, you can use standard lights to illuminate your model. You can create point lights,
spotlights, and distant lights to achieve the effects you want. You can move or rotate lights with grip editing, turn them
on or off, and change properties such as color and intensity. The effects of changes are visible in the viewport in real-time.

Spotlights and point lights are each represented by glyphs (symbols used to indicate the position and direction of the light).
Distant lights are not represented by glyphs in the drawing because they do not have a discrete position and affect the entire
scene. You can turn the display of light glyphs on or off while you work, and specify whether light glyphs should be plotted.
By default, light glyphs are not plotted.

NOTE:Starting with AutoCAD 2016-based products, all standard lights are calculated as photometric lights. It is recommended to
update all standard lights in a scene to photometric lights.

## Luminary Assemblies

Light fixtures can be represented by luminary assemblies. A luminary assembly is created by embedding photometric lights
in blocks that also contain geometry. Self-illuminating materials are often assigned to the geometry of a luminary assembly
to give the appearance that the objects in the assembly are glowing.

![](../images/GUID-68527A55-A7CA-4365-A4B4-F265CDD2EFAF-low.png)

#### Related Concepts

* [About Choosing Natural or Artificial Light](About-Choosing-Natural-or-Artificial-Light.md)

#### Related Information

* [To Work With Lighting Settings](To-Work-With-Lighting-Settings.md)
* [About Point Lights](About-Point-Lights.md)
* [To Create a Point Light in Standard Lighting Workflow](To-Create-a-Point-Light-in-Standard-Lighting-Workflow.md)
* [To Create a Point Light in Photometric Workflow](To-Create-a-Point-Light-in-Photometric-Workflow.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*