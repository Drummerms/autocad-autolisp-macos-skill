# FAQ: Why can't I use my custom hatch pattern (PAT) files?

If you have problems using custom hatch pattern (PAT) files, you want to ensure the following conditions are met:

* Custom hatch pattern names don't exceed 31 characters in length.
* A blank line is added after the last hatch pattern definition line in a PAT file.
* The PAT files that contain custom hatch patterns are located in one of the folders specified by the Support File Search Path
  setting of the program.
* Each custom hatch pattern is stored in a separate PAT file that has the same name as the custom hatch pattern. For example,
  the custom hatch pattern "WATER" must be stored in a PAT file named
  *water.pat*.

  NOTE:Alternatively, custom hatch patterns can be added under the User Defined Hatch Patterns section to one of the standard PAT
  files;
  *acad.pat*/*acadiso.pat* used by AutoCAD and AutoCAD-based programs and
  *acadlt.pat*/*acadltiso.pat* files used by the AutoCAD LT program. By adding custom hatch patterns to one of the standard PAT files, the custom hatch
  patterns are available to the program without storing each one in a separate PAT file and without needing to list the locates
  of the PAT files as part of the Support File Search Path setting.

#### Related Concepts

* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [About Hatch Patterns With Multiple Lines](About-Hatch-Patterns-With-Multiple-Lines.md)
* [About Hatch Patterns with Dashed Lines](About-Hatch-Patterns-with-Dashed-Lines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*