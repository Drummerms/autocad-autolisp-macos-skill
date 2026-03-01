# Shade and Color Faces

Shading and color effects control the display of faces in a model.

## Face Styles

The face style defines the shading on a face. Realistic (below left) is meant to produce the effect of realism. Gooch (below
right) can show details better by softening the contrast between lit areas and shadowed areas. Lit areas use warm tones and
shadowed areas use cool tones.

![](../images/GUID-FC24BD88-60E3-4FFA-9F0E-77257937D4F7-low.png)

The None face style produces no shading, and displays only edges. Customize edge settings to control whether facet edges or
isolines are displayed.

## Lighting Quality

Lighting quality determines the smoothness of shaded objects.

Faceted lighting computes a single color for each face. Individual faces appear flat. Smooth lighting smooths the edges between
polygon faces by computing the colors as a gradient between the faces’ vertices. This gives objects a smooth appearance.

For the Smoothest option, the Per-Pixel Lighting setting must be enabled under the Hardware acceleration option of 3DCONFIG.
The colors are computed for individual pixels, giving a smoother appearance. If not, the Smooth setting is used instead.

![](../images/GUID-71E169B9-96DE-4F62-A31A-86C03CB72087-low.png)

## Highlights

The size of an object’s highlights affect the perception of shininess. A smaller, more intense highlight makes objects appear
shinier. The highlight intensity that is set in a visual style does not apply to objects with attached materials.

![](../images/GUID-4E221259-B635-485D-B8B2-DA3B78018E4E-low.png)

## Opacity

The opacity property controls the transparency of objects.

![](../images/GUID-71A7922B-7BFA-4A39-9369-546C1062437E-low.png)

## Face Color Modes

Display face colors in the normal way, or specify a face color mode. Monochrome displays faces in the varying shades of a
specified color. Tint shades faces by changing the hue and saturation values based on a specified color. Desaturate softens
colors.

![](../images/GUID-A6DDD443-8501-495B-A5CC-D01FEEC49776-low.png)

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)

#### Related Information

* [About Using Visual Styles](About-Using-Visual-Styles.md)
* [About Backgrounds and Shadows](About-Backgrounds-and-Shadows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*