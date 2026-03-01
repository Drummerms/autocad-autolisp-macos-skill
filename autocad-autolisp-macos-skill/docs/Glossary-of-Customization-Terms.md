# Glossary of Customization Terms

## Common

Customization (CUI/CUIx) file
:   A package file that contains multiple XML-based files and custom image files. Each one of the XML-based files contains data
    for a different type of user interface element that can be customized.

    NOTE:On Windows only, CUIx files replaced the CUI, MNU, MNS, and MNC files that were used to define user interface elements in
    earlier releases.

Interface element
:   An object that makes up the user interface and can be customized.

    On Windows, this might be a ribbon panel and tab, Quick Access toolbar, and so on. It is a node in the Customizations In
    *<file name>* pane that contains user interface items. On Mac OS, this is a menu or tool set.

Interface item
:   The individual components of a user interface element.

    On Windows, this might be a button on a ribbon panel, drop-down list on the Quick Access toolbar, command that is started
    by a shortcut key, and so on. On Mac OS, this might be a menu item or tool on a tool set.

Macro
:   A series of commands and input that are ran in a defined sequence to accomplish a drawing task.

Palette
:   A modeless interface element that can be docked to or set to float separately from the application window.

    On Windows, this includes the Properties, Layer Properties Manager, Command Line, and so on. On Mac OS, this includes Properties
    Inspector and Layers among others.

## Windows Only

Customization group
:   A name that is assigned to a CUIx file to identify the customization content between different loaded CUIx files. Prior to
    the introduction of the AutoCAD 2006-based products, a customization group was referred to as a
    *menu group*.

Element ID
:   A unique identifier of a user interface element. In earlier releases, an element ID was referred to as a
    *tag*.

Dashboard panel
:   An organizational structure used to lay out commands and controls for display on the dashboard, which was used in releases
    prior to AutoCAD 2009-based products. Starting with AutoCAD 2010-based products, the dashboard was replaced by the ribbon.

Enterprise customization file
:   A CUIx file that is typically controlled by a CAD administrator or manager. It is often accessed by many users and is stored
    in a shared network location. The file is read-only to users to prevent the contents in the file from being changed. Often,
    a CAD administrator or manager creates an enterprise CUIx file by modifying the program's default main CUIx file, and saving
    the file to a shared network location. Users then specify this file in the Options dialog box.

Legacy Customization (CUI) file
:   An XML-based file that stores customization data for products starting with AutoCAD 2006-based products and ending with AutoCAD
    2009-based products. The CUI file was replaced by the introduction of the CUIx file. A CUI file can be converted to a CUIx
    file using the Transfer tab of the CUI Editor (CUI command).

Legacy Menu (MNS) file
:   An ASCII based file that stores menu customization data for AutoCAD 2005-based products and earlier releases. Use the Transfer
    tab of the CUI Editor (CUI command) to convert a MNS file to a CUIx file.

Legacy Menu Template (MNU) file
:   An ASCII based file that is used as a template to define the contents of the MNS file for AutoCAD 2005-based products and
    earlier releases. Use the Transfer tab of the CUI Editor (CUI command) to convert a MNU file to a CUIx file.

Main customization file
:   A CUIx file that defines most of the user interface elements (including the standard ribbon panels and tabs, Quick Access
    toolbars, keyboard shortcuts, and so on) and is automatically loaded when the program starts.

Ribbon
:   An interface element that displays tabs made up of panels which contain commands and controls, and can be docked horizontally
    or vertically along the program’s application window.

Ribbon panel
:   An organizational structure used to lay out commands and controls for display on the ribbon or as a floating user interface.

Partial customization file
:   A CUIx file that is not defined as the main or enterprise CUIx file. You can load and unload partial CUIx files as you need
    them during a drawing session.

Quick Access toolbar
:   An interface element that is located above the ribbon, by default, and provides access to common drawing file management
    tools.

Workspace
:   A collection of user interface elements, including their contents, properties, display states, and locations.

## Mac OS Only

Tool set
:   An interface element that displays tool groups made up of commands and flyouts (or drop-downs) that are displayed vertically
    outside the drawing area.

Tool group
:   An organizational structure used to lay out commands and flyouts (or drop-downs) for display on the Tool Sets palette.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Command Customization](About-Command-Customization.md)
* [About Creating and Managing Pull-down Menus](About-Creating-and-Managing-Pull-down-Menus.md)
* [About Managing Tool Sets](About-Managing-Tool-Sets.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*