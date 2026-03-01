# paragraph Tile (DCL)

A paragraph is a cluster of
text\_part or
concatenation tiles that are arranged vertically.

*Supported Platforms:* Windows, Mac OS, and Web

```
: paragraph { }
```

![](../images/GUID-36C61767-BB51-4E5C-8E53-790729107C37-low.png)

You can construct paragraphs of running text either statically or at runtime. There is a margin around the
paragraph as a whole.

The
paragraph tile is defined in the
*base.dcl* file.

The illustration above was generated with the following DCL:

```
: paragraph
{
  : concatenation
  {
    : text_part
    {
      label = "One";
    }
    : text_part
    {
      label = "good turn";
    }
  }
  : text_part {
    label = "Deserves another";
  }
}
```

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

#### Related Concepts

* [concatenation Tile (DCL)](concatenation-Tile-DCL.md)
* [text Tile (DCL)](text-Tile-DCL.md)
* [Text Cluster Tiles (DCL)](Text-Cluster-Tiles-DCL.md)
* [text\_part Tile (DCL)](text_part-Tile-DCL.md)
* [Dialog Box Exit Buttons and Error Tiles (DCL)](Dialog-Box-Exit-Buttons-and-Error-Tiles-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*