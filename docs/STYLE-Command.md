# -STYLE (Command)

Creates, modifies, or specifies text styles.

## List of Prompts

The following prompts are displayed.

Enter [name of text style](STYLE-Command.md) or [[?](STYLE-Command.md)] <*current*>: *Enter a style name, enter* *?**, or press* Enter

Text Style Name
:   Specifies the text style name. To define a style that uses Big Fonts, you can use long file names that do not contain commas.
    Commas are used to separate SHX files and Big Font files for defining a Big Font file.

    Enter a TrueType font family name or an SHX font file name. If you do not enter a file name extension, this program searches
    for an SHX file. If the file is not located, Windows substitutes the first located registered TrueType font.

    All long file names except those containing commas are accepted at the prompt. The comma is reserved for the Big Font naming
    convention: an SHX file followed by a comma (,), followed by the Big Font file name. A space is interpreted as part of the
    font name, not as a carriage return.

    If you enter *annotative*, you are prompted to create an annotative text style.

Tilde (~)
:   Displays the Select Font File dialog box.

    In the Select Font File dialog box, valid types include SHX and TTF. The character definitions of the selected font file are
    loaded automatically unless the file is already in use by another text style. You can define several styles that use the same
    font file.

Match Text Orientation to Layout
:   If you enter *yes* the current text style orientation in paper space viewports matches the layout.

Height of Text
:   If you enter a height of *0.0*, you are prompted for the text height each time you enter text using this style. Entering a height greater than *0.0* sets the Text Height (Non annotative), entering a height greater than *0.0* sets the Paper Text Height (Annotative), for this style.

Width Factor
:   Entering a value less than *1.0* condenses the text. Entering a value greater than *1.0* expands it.

Obliquing Angle
:   Entering a value between *-85* and *85* obliques the text.

Vertical
:   Vertical is available only if the selected font supports dual orientation.

?—List Text Styles
:   Lists the text styles available in the drawing.

    At the Enter Text Style(s) to List prompt, entering the name of a style displays the name, font file, height, width factor,
    obliquing angle, and generation of the style and exits the command. Entering an asterisk (*\**) or pressing Enter displays the height, width factor, obliquing angle, and generation (whether text is drawn backwards, upside-down,
    vertically, or normally) of each style, and then exits the command.

#### Related Tasks

* [To Set the Current Text Style](To-Set-the-Current-Text-Style.md)
* [To Create Text](To-Create-Text.md)

#### Related References

* [STYLE (Command)](STYLE-Command-2.md)

#### Related Concepts

* [Text Style Dialog Box](Text-Style-Dialog-Box.md)
* [About Text Styles](About-Text-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*