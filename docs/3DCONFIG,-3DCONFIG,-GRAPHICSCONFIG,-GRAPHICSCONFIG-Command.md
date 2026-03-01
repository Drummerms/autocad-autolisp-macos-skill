# 3DCONFIG, -3DCONFIG, GRAPHICSCONFIG, -GRAPHICSCONFIG (Command)

Sets options that affect 3D display performance.

The following prompts are displayed.

Acceleration
:   Specifies whether to use software or hardware acceleration in 3D.

    Hardware
    :   Specifies hardware acceleration. The hardware graphics card performs the drawing tasks to increase performance.

        * *Per-pixel lighting.* Enables the computation of colors for individual pixels. With this option turned on, the 3D objects and lighting effects
          appear smoother in the viewport.
        * *Advanced material effects.* Controls the status of the advanced materials effect on-screen.
        * *Full shadow display.* Enables the display of full shadows.
        * *Uncompressed textures.* Increases the amount of video memory to display better quality textures in drawings that contain materials with images or
          have attached images.

          NOTE: With this option on, the time it takes to load the images may increase the first time that they are accessed and there is
          a reduction in the quality of the images when they are displayed in the viewport or plotted.
        * *Exit.* Ends the command.

    Software
    :   Software acceleration is not supported and is provided for scripting compatibility only.

    Exit
    :   Ends the command.

Adaptive Degradation
:   Turns off or minimizes display effects when performance drops below the minimum acceptable speed (frames per second) that
    you specify. Wireframe visual styles will reduce the number of vectors displayed; other visual styles will degrade to the
    Shaded visual style.

General Options
:   Sets performance-related options that are not hardware dependent.

    Smooth Faces
    :   Smooths the facets in a polyface mesh object when displayed in the viewport and in a rendering. This is useful when using
        objects that were imported through 3DSIN or when using PFACE objects. Note that when enabled, all objects in the drawing are
        made smooth. If you do not want all objects to be smooth, recreate the model using a different object type.

    Dynamic Tesselation
    :   Sets the options that determine the smoothness of the objects in a drawing. Objects are drawn using many short lines (or triangles
        when drawing spheres). These lines are called
        *tessellation lines*. Objects in your drawing appear smoother when you use more tessellation lines. If Dynamic Tesselation is on, you can set
        the following values:

        * *Surface tesselation.* Determines the amount of detail for surfaces in your drawing. A higher setting provides more detail but uses more tessellation
          lines and more memory.
        * *Curve tesselation.* Determines the amount of detail for curves in your drawing. A higher setting provides more detail but uses more tessellation
          lines and more memory.
        * *Tesselations to cache.* Configures your system according to memory and performance requirements. The 3D cache always stores at least one tessellation.
          When this option is set to 1, the tessellation for all viewports is the same; some objects in the drawing may be regenerated
          as you zoom in and out. Setting this option to 2 or more is useful when you have more than one viewport with different views.
          Increasing the number requires more memory.

    Discard Backfaces
    :   Discards back faces when drawing objects. You cannot see the effect of discarding back faces on some objects, such as spheres,
        because you cannot see the back face even when it is present. The effect of discarding back faces is visible on objects such
        as those that don't have a top. Discarding back faces enhances performance.

    Transparency Quality
    :   Adjusts the transparency quality. At the Low setting, a screen-door effect achieves transparency without sacrificing speed.
        At the Medium setting, the default in software mode, blending improves image quality. The High setting, the default in hardware
        mode, produces an image free of visual artifacts at the cost of drawing speed. Materials must also be turned on for transparency
        to be visible.

        NOTE:Materials must also be turned on for transparency to be visible.

    Plot Emulation
    :   Plot emulation is not supported and is provided for scripting compatibility only.

    Exit
    :   Ends the command.

#### Related Concepts

* [About Memory Tuning](About-Memory-Tuning.md)
* [Performance Tuning](Performance-Tuning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*