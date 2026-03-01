# AutoLISP Developer's Guide (AutoLISP)

The AutoLISP Developer's Guide provides you with an overview of the main topics and workflows for using the AutoLISP programming
language.

## Sections in this Topic

* [Tutorials](GUID-265AADB3-FB89-4D34-AA9D-6ADF70FF7D4B.htm#SECTION_DDD4EEE0ADAB45A884B4E342A70A1587)
* [AutoLISP Programming](GUID-265AADB3-FB89-4D34-AA9D-6ADF70FF7D4B.htm#SECTION_3D43AF51AB164D678B4D791B47DA2F95)
* [Using Visual Studio (VS) Code with the AutoCAD AutoLISP Extension](GUID-265AADB3-FB89-4D34-AA9D-6ADF70FF7D4B.htm#SECTION_0F0149725D374A68A428B9B5B0ECB2CD)
* [Working with Programmable Dialog Boxes DCL](GUID-265AADB3-FB89-4D34-AA9D-6ADF70FF7D4B.htm#SECTION_64F9F11D99CE4E90B10DCEE5E0D42A91)

## Tutorials

Basic
:   [Getting Started](Tutorial-Getting-Started-AutoLISP.md)

    [Creating a New Command and Working with System Variables](Tutorial-Creating-a-New-Custom-Command-and-Controlling-with-System-Variables-AutoLISP.md)

    [Creating, Loading, and Opening an AutoLISP File](Tutorial-Creating,-Loading,-and-Opening-an-AutoLISP-File-AutoLISP.md)

AutoCAD AutoLISP Extension
:   [Installing and Configuring the AutoLISP Extension](Tutorial-Installing-and-Configuring-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

    [Getting Started with the AutoLISP Extension](Tutorial-Getting-Started-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

    [Debugging LSP Files with the AutoLISP Extension](Tutorial-Debugging-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

    [Formatting LSP Files with the AutoLISP Extension](Tutorial-Formatting-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

## AutoLISP Programming

Getting Started
:   [Getting Organized](About-Getting-Organized-AutoLISP.md)

    [AutoLISP and Visual LISP](AutoLISP-and-Visual-LISP-AutoLISP.md)

    [AutoLISP Documentation](About-AutoLISP-Documentation-AutoLISP.md)

    [Related Developer References](Related-Developer-References-AutoLISP.md)

    [What's New or Changed](What's-New-or-Changed-with-AutoLISP-AutoLISP.md)

Basics
:   [Expressions](About-Expressions-AutoLISP.md)

    [Function Syntax](About-Function-Syntax-AutoLISP.md)

    [Defining Commands](About-Defining-Commands-AutoLISP.md)

    [Variables](About-Variables-AutoLISP.md)

    [Source Code Files](About-Source-Code-Files-AutoLISP.md)

    [Comments in AutoLISP Program Files](About-Comments-in-AutoLISP-Program-Files-AutoLISP.md)

    [Create and Open AutoLISP Source Code Files](To-Create-and-Open-AutoLISP-Source-Code-Files-AutoLISP.md)

Data Types
:   [Integers](About-Integers-AutoLISP.md)

    [Reals](About-Reals-AutoLISP.md)

    [Lists](About-Lists-AutoLISP.md)

    [Point Lists](About-Point-Lists-AutoLISP.md)

    [Dotted Pairs](About-Dotted-Pairs-AutoLISP.md)

    [Strings](About-Strings-and-String-Handling-AutoLISP.md)

    [Entity Names](About-Entity-Names-AutoLISP.md)

    [Nil](About-Nil-Variables-AutoLISP.md)

Converting Data Types and Geometric Utilities
:   [Angular Conversion](About-Angular-Conversion-AutoLISP.md)

    [String Conversions](About-String-Conversions-AutoLISP.md)

    [ASCII Codes](About-ASCII-Codes-AutoLISP.md)

    [Coordinate System Transformations](About-Coordinate-System-Transformations-AutoLISP.md)

    [Geometric Utilities](About-Geometric-Utilities-AutoLISP.md)

    [Unit Conversion](About-Unit-Conversion-AutoLISP.md)

Working with AutoCAD and Using Commands
:   [System and Environment Variables](About-System-and-Environment-Variables-AutoLISP.md)

    [Using AutoCAD Commands](About-Using-AutoCAD-Commands-AutoLISP.md)

    [Undoing Changes Made by a Routine](About-Undoing-Changes-Made-by-a-Routine-AutoLISP.md)

    [Pausing for User Input During an AutoCAD Command](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)

    [Passing Pick Points to AutoCAD Commands](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)

    [Accessing and Assigning Help to a Command](About-Accessing-and-Assigning-Help-to-a-Command-AutoLISP.md)

Prompting for User Input
:   [Accessing and Requesting User Input](About-Accessing-and-Requesting-User-Input-AutoLISP.md)

    [Controlling User-Input Function Conditions](About-Controlling-User-Input-Function-Conditions-AutoLISP.md)

    [Arbitrary Keyboard Input](About-Arbitrary-Keyboard-Input-AutoLISP.md)

Manipulating Drawing Objects
:   [Adding an Entity without Using the Command Function](About-Adding-an-Entity-without-Using-the-Command-Function-AutoLISP.md)

    [Modifying an Entity without the Command Function](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)

    [Obtaining Entity Information](About-Obtaining-Entity-Information-AutoLISP.md)

    [Selecting Objects and Selection Sets](About-Selecting-Objects-and-Selection-Sets-AutoLISP.md)

    [Attaching Extended Data to an Entity](About-Attaching-Extended-Data-to-an-Entity-AutoLISP.md)

    [Symbol Tables](About-Symbol-Tables-AutoLISP.md)

    [Dictionary Objects and Entries](About-Dictionary-Objects-and-Entries-AutoLISP.md)

Interacting with Devices and Operating System
:   [Configuration Files](About-Configuration-Files-AutoLISP.md)

    [Controlling the Graphics and Text Windows](About-Controlling-the-Graphics-and-Text-Windows-AutoLISP.md)

    [Controlling Low-Level Graphics](About-Controlling-Low-Level-Graphics-AutoLISP.md)

    [Controlling Menus](About-Controlling-Menus-AutoLISP.md)

    [Calibrating Tablets](About-Calibrating-Tablets-AutoLISP.md)

    [Searching for Files](About-Searching-for-Files-AutoLISP.md)

    [File Descriptors](About-File-Descriptors-AutoLISP.md)

Handling Errors in AutoLISP Programs
:   [Error Handling](About-Error-Handling-AutoLISP.md)

    [Using the \*error\* Function](About-Using-the-error-Function-AutoLISP.md)

    [Catching Errors and Continuing Program Execution](About-Catching-Errors-and-Continuing-Program-Execution-AutoLISP.md)

    [Exiting a Function Quietly](About-Exiting-a-Function-Quietly-AutoLISP.md)

Debugging AutoLISP Programs
:   [Displaying Messages](About-Displaying-Messages-AutoLISP.md)

## Using Visual Studio (VS) Code with the AutoCAD AutoLISP Extension

Overview
:   [Getting Started with Visual Studio Code](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)

    [What is and Why Visual Studio Code?](What-is-and-Why-Visual-Studio-Code-AutoLISP-VS-Code.md)

    [Configuring Visual Studio Code](Configuring-VS-Code-AutoLISP-VS-Code.md)

Managing, Debugging, and Compiling AutoLISP Files
:   [Creating and Opening AutoLISP Files](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md)

    [Editing AutoLISP Files](Editing-AutoLISP-Files-AutoLISP-VS-Code.md)

    [Formatting AutoLISP Files](Formatting-AutoLISP-Files-AutoLISP-VS-Code.md)

    [Debugging AutoLISP Files (AutoCAD for Windows and Mac OS Only)](Debugging-AutoLISP-Files-AutoLISP-VS-Code.md)

## Working with Programmable Dialog Boxes DCL

Overview
:   [Syntax and Comments in DCL Files](About-Syntax-and-Comments-in-DCL-Files-DCL.md)

    [Example: Quick Overview of Dialog Boxes](Example-Quick-Overview-of-Dialog-Boxes-DCL.md)

Defining a Dialog Box
:   [Designing Dialog Boxes](About-Designing-Dialog-Boxes-DCL.md)

    [Dialog Box Components](About-Dialog-Box-Components-DCL.md)

    [Tile Definitions](About-Tile-Definitions-DCL.md)

    [Tile References](About-Tile-References-DCL.md)

Working with a Dialog Box
:   [Function Sequence to Display and Work with a Dialog](About-the-Function-Sequence-to-Display-and-Work-with-a-Dialog-DCL.md)

    [Initializing Modes and Values](About-Initializing-Modes-and-Values-DCL.md)

    [Action Expressions and Callbacks](About-Action-Expressions-and-Callbacks-DCL.md)

    [Displaying Nested Dialog Boxes](About-Displaying-Nested-Dialog-Boxes-DCL.md)

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*