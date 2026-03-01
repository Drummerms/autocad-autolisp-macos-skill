# About Entering Commands on the Command Line

Commands are the instructions that tell the program what to do.

There are many ways to initiate a command:

* Make a selection on a tool set, toolbar, or menu.
* Enter a command in a dynamic input tooltip.
* Enter a command on the command line.

The resizable command window accepts commands and system variables and displays prompts that help you complete a command sequence
(including commands that were initiated at another location such as a tool set).

![](../images/GUID-E6FC4728-17EC-4B8F-A42D-595541420CD0-low.png)

NOTE: When Dynamic Input is turned on and is set to display dynamic prompts, you can enter commands and options in tooltips near
the cursor. Dynamic Input can be turned on an off from the status bar.
![](../images/GUID-F76BF07D-4782-4908-8569-5A44A72F1C82-low.png)

## Respond to Command Prompts

After you enter a command, you may see a series of prompts displayed at the command line. For example, after you enter PLINE
and specify the first prompt, the following prompt is displayed:

PLINE Specify next point or [Arc/Halfwidth/Length/Undo/Width]:

![](../images/GUID-462F3ED7-C9A8-49A8-B17F-7886E9AF92BF-low.png)

In this case, the default is to specify the next point. You can either enter
*X,Y* coordinate values or click a location in the drawing area.

To choose a different option, specify the option by entering the capitalized letter. You can enter uppercase or lowercase
letters. For example, to choose the Width option, type
*w* and press Enter.

Sometimes the default option (including the current value) is displayed after the angle-bracketed options:

POLYGON Enter number of sides <4>:

In this case, you can press Enter to retain the current setting (4). If you want to change the setting, type another number
and press Enter.

## Enter Command Aliases

Some commands have abbreviated names, or
*command aliases*, that you can enter at the command line. For example, instead of entering
*circle* to start the CIRCLE command, you can type
*c* and press Enter. The command Suggestion List (if displayed) indicates the alias in front of the command name:

C (CIRCLE)

Custom command aliases are defined in the
*acaduser.pgp* or
*acadltuser.pgp*file. To edit command aliases, click
Tools menu ![](../images/ac.menuaro.gif) Customize ![](../images/ac.menuaro.gif) Edit Command Aliases (PGP).

## Interrupt a Command with Another Command or System Variable

Many commands can be used
*transparently*. That is, they can be entered on the command line while you use another command. Commands that do not select objects, create
new objects, or end the drawing session usually can be used in this way.

To use a command transparently, enter an apostrophe (') before entering the command at any prompt. On the command line, double
angle brackets (>>) precede prompts that are displayed for transparent commands. After you complete the transparent command,
the original command resumes. In the following example, you turn on the grid and set it to one-unit intervals in the middle
of the LINE command.

Command:
*line*

Specify first point:
*'grid*

>>Specify grid spacing (X) or [ON/OFF/Snap/Major/aDaptive/Limits/Follow/Aspect] <0.5000>:
*1*

Resuming LINE command

Specify first point:

Changes made in dialog boxes that you have opened transparently cannot take effect until the interrupted command has been
completed. Similarly, if you reset a system variable transparently, the new value cannot take effect until you start the next
command.

## Aids for Entering Commands

The program offers several ways to remember which commands to use:

* *Automatic completion.* Completes name of a command or system variable as you type it.
* *Command line suggestion list.*Displays a list of commands or system variables that match or contain the letters you have typed. The program offers suggestions
  for misspelled entries.
* *Automatic correction.* Commands that you frequently misspell. The program automatically adds words that you misspell and correct a specified number
  of times to the
  *AutoCorrectUserDB.pgp* file. You can also update this text file manually.
* *Command cycling.* Cycles through commands you have already used in the current session when you press the Arrow keys. An arrow button on the
  left end of the command line also displays recent commands.

You can change the settings for these options from the command line menu.

![](../images/GUID-8D825DD9-F60C-49A8-B819-4DC9D3D3305A-low.png)

#### Related Tasks

* [To Work With Entering Commands](To-Work-With-Entering-Commands.md)
* [To Work With Entering System Variables](To-Work-With-Entering-System-Variables.md)
* [To Use the Command Line Version of a Command](To-Use-the-Command-Line-Version-of-a-Command.md)

#### Related Concepts

* [About Navigating and Editing in the Command Window](About-Navigating-and-Editing-in-the-Command-Window.md)
* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

#### Related Information

* [Enter System Variables on the Command Line](Enter-System-Variables-on-the-Command-Line.md)
* [To Work With the Command Window](To-Work-With-the-Command-Window.md)
* [Switch Between Dialog Boxes and the Command Line](Switch-Between-Dialog-Boxes-and-the-Command-Line.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*