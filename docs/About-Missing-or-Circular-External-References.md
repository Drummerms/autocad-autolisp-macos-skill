# About Missing or Circular External References

If a referenced drawing cannot be located when you open a drawing, several options available to you. If a referenced drawing
contains a sequence of nested references that refers back to itself, an error message is displayed.

The program stores the folder path of the referenced drawing. Each time you open or plot the drawing, or use the Reload option
in the Reference Manager to update the xref, the program checks the folder path to determine the name and location of the
referenced drawing file.

If the name or location of the drawing file has changed, the program cannot locate or reload the xref, and it displays an
error message that displays the folder path and name of the missing drawing file.

In the drawing, at each insertion of the missing xref, the program displays text that displays the folder path of the missing
xref. You can use the XREF Path option to update or correct the path.

Along with error messages being displayed at the Command prompt, a task dialog box might be displayed that allows you to ignore
all missing xrefs or update their folder locations. You can use the Reference Manager palette to update the locations of the
unresolved references.

To avoid these errors make sure that when you transfer or distribute drawing files that have xrefs attached, you also include
all the referenced files.

## Changing Nested Xref Paths

When a drawing is opened and a nested xref is loaded, the program attempts to find the xref in the original xref path first.
If the xref is not found, the following search is initiated in the order shown:

* Current folder of the host drawing
* Project search paths defined on the Application tab in the Application Preferences dialog box
* Search paths defined in the Support File Search Paths item on the Application tab in the Application Preferences dialog box

This search order helps ensure that revisions made to the xref are reflected in the current drawing, and also makes it possible
for the xref to be found if its folder path has changed.

## Resolving Circular References

A drawing that contains a sequence of nested references that refers back to itself is considered a circular reference. For
example, if drawing A attaches drawing B, which attaches drawing C, which attaches drawing A, the reference sequence A>B>C>A
is a circular reference.

If the program detects a circular reference while attaching an xref, a warning is displayed asking you if you want to continue.
If you respond with yes, the program reads in the xref and any nested xrefs to the point where it detects the circularity.
If you respond with no, the process is halted and the xref is not attached.

If a circular reference is encountered while loading a drawing, an error message is displayed and the circular reference for
the current session is broken. For example, if you have the circular reference A>B>C>A, and you open *a.dwg*, the program detects and breaks the circularity between *c.dwg* and *a.dwg*. The following error message is displayed:

Breaking circular reference from C to current drawing.

#### Related Concepts

* [About Logging External Reference Operations](About-Logging-External-Reference-Operations.md)

#### Related Information

* [About Name Conflicts in External References](About-Name-Conflicts-in-External-References.md)
* [To Bind Xref-dependent Named Objects to the Current Drawing](To-Bind-Xref-dependent-Named-Objects-to-the-Current-Drawing.md)
* [To Rename Named Objects](To-Rename-Named-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*