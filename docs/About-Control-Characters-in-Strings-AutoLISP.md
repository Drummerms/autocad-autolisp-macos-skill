# About Control Characters in Strings (AutoLISP)

Within quoted string values, the backslash (\) character allows control characters (or escape codes) to be included.

The following lists the currently recognized control characters:

| AutoLISP control characters | |
| Code | Description |
| \\ | \ character |
| \" | " character |
| \e | Escape character |
| \ | Newline character |
| \r | Return character |
| \t | Tab character |
| \ *nnn* | Character whose octal code is *nnn* |

The prompt, princ, and get*XXX* functions expand the control characters in a string and display the expanded string at the AutoCAD Command prompt.

The following example shows displaying a backslash character (*\*) and quotation mark (*"*) within a quoted string:

```
(princ "The \"filename\" is: D:\\ACAD\\TEST.TXT.")
The "filename" is: D:\ACAD\TEST.TXT
```

Text can be forced across multiple lines with the newline character (\
).

```
(prompt "An example of the \
newline character. ")
An example of the
newline character.
```

You can also use the terpri function to cause a line break.

The Return character (\r) returns to the beginning of the current line. This is useful for displaying incremental information (for example, a counter
showing the number of objects processed during a loop).

A Tab character (\t) can be used in strings to indent or to provide alignment with other tabbed text strings. In this example, note the use of
the princ function to suppress the ending nil.

```
(prompt "\
Name\tOffice\
- - - - -\t- - - - -
(_> \
Sue\t101\
Joe\t102\
Sam\t103\
")(princ)

Name Office
- - - - - - - - - -
Sue 101
Joe 102
Sam 103
```

#### Related Concepts

* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)
* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)
* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*