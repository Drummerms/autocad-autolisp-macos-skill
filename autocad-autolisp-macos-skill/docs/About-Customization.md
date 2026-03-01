# About Customization

AutoCAD and AutoCAD-based products, including AutoCAD LT, can be customized to improve your productivity with the product
and help enforce CAD standards.

The following is a list of the available customization options:

* *Organize files.* You can organize program, support, and drawing files. For example, you can make a separate folder for each project that includes
  only the support files that the project needs. (OPTIONS command)
* *Create custom drawing template files.* You can create custom drawing template (DWT) files to use when creating a new drawing. Drawing template files can store commonly
  used layers, blocks, and styles that you might use in specific projects or across all your drawings. (SAVEAS command)
* *Define command aliases.* You can define simple aliases, or abbreviations, for frequently used commands by modifying the AutoCAD PGP file
  *acad.pgp* or, in AutoCAD LT,
  *acadlt.pgp*. For example, you might want to start the
  *BLOCK* command by entering
  *b* at the Command prompt.

  NOTE:AutoCAD for Mac stores user-defined command aliases in
  *acaduser.pgp* and
  *acadltuser.pgp*.
* *Define AutoCorrect entries and synonyms.* You can define AutoCorrect entries (*AutoCorrectUserDB.pgp*) and synonyms (*acadSynonymsGlobalDB.pgp*) for commands that you might commonly misspell or forget the standard name of.
* *Create custom linetypes, hatch patterns, shapes, and text fonts.* You can create linetypes (LIN files), hatch patterns (HAT files), shapes (SHP files), and text fonts (SHX files) that conform
  to your company standards. Shape and text fonts cannot be compiled for use in AutoCAD LT.
* *Customize the user interface.* You can create and modify customization (CUI/CUIx) files to control many aspects of the user interface. (CUI command)
* *Automate repetitive tasks by writing scripts.* You can create a script (SCR) file that defines and executes a sequential set of commands with predetermined input. For example,
  you can create a script that creates layers and inserts a title block. You can also use a script to plot a set of drawings
  in a certain way: you can write a script that opens each drawing, hides and displays various layers, and starts the PLOT command.
  (SCRIPT command)

The following is a list of additional customization and programming options that are not available in AutoCAD LT.

* *Run external programs and utilities from within AutoCAD.* You can create an alias that starts an application that is installed outside of the program. For example, you can copy or
  delete a file from within AutoCAD by adding the appropriate external command to the program parameters (PGP) file,
  *acad.pgp*. Not available in AutoCAD for Mac.
* *Record action macros.* You can record commands and input, and save them to an action macro (ACTMX) file to automate repetitive tasks. Not available
  in AutoCAD for Mac. (ACTRECORD command)

  NOTE:ACTM files created in AutoCAD 2024 and earlier releases must be migrated to the ACTMX file format before they can be played
  back.
* *Redefine AutoCAD commands.* You can redefine commands to issue supplementary messages and instructions, or replace the standard behavior of a command.
  For example, to create a drawing management system in which the QUIT command is redefined to write billing information to
  a log file before ending the AutoCAD session. (REDEFINE command)

The following is a list of additional customization and programming options that are available in AutoCAD and AutoCAD LT
on Windows only.

* *Customize Tool Palettes.* You can create tools by dragging objects from your drawing onto a tool palette or a command from the Customize User Interface
  (CUI) Editor. New tool palettes can be created to organize the tools you create. (CUSTOMIZE command)
* *Customize the status bar.* You can use the DIESEL string expression language and the MODEMACRO system variable to provide additional information on
  the status bar, such as the date and time, system variable settings, or retrievable information using AutoLISP.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About File Organization](About-File-Organization.md)
* [About Multiple Configurations](About-Multiple-Configurations.md)
* [About Multiple Drawing Folders](About-Multiple-Drawing-Folders.md)
* [About Customized File Locations](About-Customized-File-Locations.md)
* [About Creating Command Aliases](About-Creating-Command-Aliases.md)
* [About Supported Programming Interfaces](About-Supported-Programming-Interfaces.md)
* [About Simple Custom Linetypes](About-Simple-Custom-Linetypes.md)
* [About Custom Hatch Patterns and Hatch Pattern Definitions](About-Custom-Hatch-Patterns-and-Hatch-Pattern-Definitions.md)
* [About DIESEL and Status Bar Customization](About-DIESEL-and-Status-Bar-Customization.md)
* [About Command Scripts](About-Command-Scripts.md)
* [AutoLISP and Visual LISP (AutoLISP)](AutoLISP-and-Visual-LISP-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*