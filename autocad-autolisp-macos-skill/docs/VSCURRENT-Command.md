# VSCURRENT (Command)

Sets the visual style in the current viewport.

## List of Prompts

The following prompts are displayed.

Enter an option [[2dwireframe](VSCURRENT-Command.md)/[Wireframe](VSCURRENT-Command.md)/[Hidden](VSCURRENT-Command.md)/[Realistic](VSCURRENT-Command.md)/[Conceptual](VSCURRENT-Command.md)/[Shaded](VSCURRENT-Command.md)/[shaded with Edges](VSCURRENT-Command.md)/[shades of Gray](VSCURRENT-Command.md)/[SKetchy](VSCURRENT-Command.md)/[X-ray](VSCURRENT-Command.md)/[Other](VSCURRENT-Command.md)] <*2dwireframe*>:

NOTE:To display lighting from point lights, distant lights, spotlights, or the sun, set the visual style to Realistic, Conceptual,
or a custom visual style with shaded objects.

2D Wireframe
:   Displays the objects using lines and curves to represent the boundaries. Raster images, linetypes, and lineweights are visible.
    Even if the value for the [COMPASS](COMPASS-System-Variable.md) system variable is set to 1, it does not appear in the 2D Wireframe view.

Wireframe
:   Displays the objects using lines and curves to represent the boundaries. Displays a shaded 3D UCS icon. You can set the COMPASS
    system variable to 1 to view the compass.

Hidden
:   Displays the objects using 3D wireframe representation and hides lines representing back faces.

Realistic
:   Shades the objects and smooths the edges between polygon faces. Materials that you have attached to the objects are displayed.

Conceptual
:   Shades the objects and smooths the edges between polygon faces. Shading uses a transition between cool and warm colors. The
    effect is less realistic, but it can make the details of the model easier to see.

Shaded
:   Produces a smooth shaded model.

Shaded with Edges
:   Produces a smooth shaded model with visible edges.

Shades of Gray
:   Produces a gray color effect by using the monocolor face color mode.

Sketchy
:   Produces a hand-sketched effect by using the overhang and jitter.

X-ray
:   Changes the opacity of faces to make the whole scene partially transparent.

Other
:   Displays the following prompt:

    Enter a visual style name [?]: *Enter the name of a visual style in the current drawing, or enter* *?* *to display a list of names and repeat the prompt*

#### Related Concepts

* [About Using Visual Styles](About-Using-Visual-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*