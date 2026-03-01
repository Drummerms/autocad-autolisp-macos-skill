# About Migrating Custom Files and Settings

Seamlessly migrate your custom files and settings from a previous release to the current release. The migration utility starts
automatically when you first open AutoCAD.

NOTE:Settings are migrated from an AutoCAD for Mac 2017 or later release only.

![](../images/GUID-98A352B3-A9CA-49E9-9AB4-150435877CD6-low.png)

The custom settings and files that can be migrated fall under the following categories:

## Interface

CUI
:   Customization (CUI/CUIx) files define user interface elements such as commands, tool sets, and pull-down menus. Based on the
    previous release from which you are migrating, the utility looks for the CUI or CUIx file specified by the Main Customization
    File setting.

    ![](../images/GUID-78D54EAE-49F2-4220-887A-A532C065748E-low.png)

## Settings

Command Alias
:   Command aliases are shortened names that are used to start commands. Custom command aliases are stored in the
    *acaduser.pgp* (or
    *acadltuser.pgp* in AutoCAD LT) file. The migration utility migrates custom command aliases from the previous release to the current release.

Plot Files
:   Plot files store various settings that control the output of a drawing file, including those for plotters and printers and
    that control the appearance of the linework in the output.

    * *Plotter Configuration (PC3) Files*. Identifies the electronic formats and devices available to output a drawing. The PC3 files from a previous release are migrated
      to a subfolder named after the release in which they were migrated; the naming convention of the subfolder is
      *Product Name* PC3 Files. The subfolder is created to maintain compatibility with both the previous and current product release. The
      *Product Name* PC3 Files subfolder is created under the location defined by the Printer Configuration Search Path setting.
    * *Plotter Model Parameters (PMP) Files*. Store user-defined paper sizes and calibration settings for a configured output device defined in a PC3 file. The PMP files
      from the previous release are migrated to the location defined under the Printer Description File Search Path setting.
    * *Plot Style Table (CTB/STB) Files*. Control the color, linetype, lineweight and other settings in a drawing during output. The program supports two types of
      plot styles: color-dependent (CTB) and named (STB) plot styles. The CTB and STB files from the previous release are migrated
      to the location defined under the Plot Style Table Search Path setting.

    ![](../images/GUID-57814809-5F7D-4D3F-A453-CF0B9DD62E69-low.png)

Templates
:   Drawing template (DWT) files are used to create new drawings. The drawings created using a DWT file contain all of the styles
    and drawing objects defined in the DWT file. The custom DWT files from the previous release are migrated into the template
    folder directly. If a file with the same name already exists in the template folder, the file is not migrated.

    ![](../images/GUID-EACE2B78-0491-4DD4-9A4E-223E2CA4AC2F-low.png)

My Properties
:   Customized properties of selected entities to show in the My Properties tab of the Properties Inspector.

## Content

Hatch Patterns
:   Hatch pattern definitions are used to define the line patterns of a hatch object in a drawing and are stored in hatch pattern
    (PAT) files.

    * *User-defined Hatch Pattern Files*. Hatch pattern definitions defined in their own PAT files or .PAT.LNK files are copied from the support folders of the previous
      release to the support folders of the current release.
    * *Standard Hatch Pattern Files*. Hatch pattern definitions that ship with the program and are defined in the
      *acad.pat* and
      *acadiso.pat* (or
      *acadlt.pat* and
      *acadltiso.pat* in AutoCAD LT) files. The Migrate Custom Settings utility can migrate only the hatch pattern definitions in the user-defined
      section of the standard PAT files. The pattern definitions are copied from the previous release to the file with the same
      name in the current release.

Linetypes
:   Linetype definitions are used to define the line patterns of drawing objects and are stored in linetype (LIN) files.

    * *User-defined Linetype Files*. Linetype definitions defined in custom LIN files are copied from the support folders of the previous release to the support
      folders of the current release.
    * *Standard Linetype Files*. Linetype definitions that ship with the program and are defined in the
      *acad.lin* and
      *acadiso.lin* (or
      *acadlt.lin* and
      *acadltiso.lin* in AutoCAD LT) files. The Migrate Custom Settings utility can migrate only the linetype definitions in the user-defined section
      of the standard LIN files. The linetype definitions are copied from the previous release to the file with the same name in
      the current release.

Shapes
:   Shape definitions are used to define text fonts, and insert special characters in a linetype definition or drawing. The source
    for shape definitions is stored in a SHP file. Shape definitions must be compiled into a SHX file prior to them being available
    for used in a linetype or drawing; the COMPILE command is used to compile a SHP file into a SHX file. The Migrate Custom Settings
    utility migrates SHX files from the support folders of the previous release to the support folders of the current release.

#### Topics in this section

* [To Locate and View the Migration Report File](To-Locate-and-View-the-Migration-Report-File.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*