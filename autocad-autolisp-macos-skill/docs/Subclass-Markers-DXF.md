# Subclass Markers (DXF)

When filing a stream of group data, a single object may be composed of several filer members, one for each level of inheritance
where filing is done. Since derived classes and levels of inheritance can evolve separately, the data of each class filer
member must be segregated from other members. This is achieved using subclass markers.

All class filer members are expected to precede their class-specific portion of instance data with a “subclass” marker—a 100
group code followed by a string with the actual name of the class. This does not affect the state needed to define the object's
state, but it provides a means for the DXF file parsers to direct the group codes to the corresponding application software.

For example, an object that has data from different derived classes would be represented as follows:

```
999
FOOGRANDCHILD, defined by class AcDbSonOfSonOfFoo, which
999
 is derived from AcDbSonOfFoo
  0
FOOGRANDCHILD
  5
C2
100
AcDbFoo
999
Uses 10/20/30 group codes
 10
1.1
 20
2.3
 30
7.3
100
AcDbSonOfFoo
999
Also uses 10/20/30 group codes, for a different purpose
 10
1.1
 20
2.3
 30
7.3
100
AcDbSonOfSonOfFoo
999
Also uses 10/20/30 group codes, for yet another purpose
 10
13.2
 20
23.1
 30
31.2
999
Now for the Xdata
1001
APP_1
1070
45
1001
APP_2
1004
18A5B3EF2C199A
```

#### Related References

* [About Advanced DXF Issues (DXF)](About-Advanced-DXF-Issues-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*