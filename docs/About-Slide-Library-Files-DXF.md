# About Slide Library Files (DXF)

This section describes the format of slide libraries (AutoCAD Release 9 and later) for the benefit of developers who wish
to incorporate support for slide libraries into their programs.

The general format of a slide library is as follows:

```
"AutoCAD Slide Library 1.0" CR LF ^Z NUL NUL NUL NUL

```
 Header (32 bytes)
```

```
 One or more slide directory entries (36 bytes each)
```

```
 One or more slides (variable length)
```
```

Slide directory entries have the following format:

```
```
 Slide name (NUL terminated) (32 bytes)
```

```
 Address of slide within library file (4 bytes)
```
```

The slide address is always written with the low-order byte first. Each slide to which the directory points is a complete
slide file as described in the previous section. The end of the slide directory is signified by an entry with a null slide
name (first byte is NUL). A slide library can contain a mixture of old-format and new-format slides.

#### Related References

* [About Drawing Interchange File Formats (DXF)](About-Drawing-Interchange-File-Formats-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*