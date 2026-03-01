# About Strings and String Handling (AutoLISP)

A string is a group of characters surrounded by quotation marks. Within quoted strings the backslash (\) character allows
control characters (or escape codes) to be included.

When you explicitly use a quoted string in AutoLISP, that value is known as a literal string or a string constant.

Examples of valid strings are “string 1” and “\
Enter first point:”.

AutoLISP provides many functions for working with string values. The following are some of the most commonly used functions:

* strcat – Returns a string that is the concatenation of multiple strings.
* strcase – Returns a string where all alphabetic characters have been converted to uppercase or lowercase.
* strlen – Returns an integer that is the number of characters in a string.
* substr – Returns a substring of a string.
* vl-string-search – Searches for the specified pattern in a string.
* vl-string-subst – Substitutes one string for another, within a string.

## Convert the Case of a String

The alphabetic characters of a string can be converted to uppercase or lowercase with the strcase function. It accepts two arguments: a string and an optional argument that specifies the case in which the characters are
returned. If the optional second argument is omitted, it evaluates to nil and strcase returns the characters converted to uppercase.

```
(strcase "This is a TEST.")
"THIS IS A TEST."
```

If you provide a second argument of T, the characters are returned as lowercase.

```
(strcase "This is a TEST." T)
"this is a test."
```

NOTE:The predefined variable T is often used to represent a True value when a function returns or excepts a True/False value. A nil value is used to represent a False value in these conditions.

## Combine Multiple Strings

You can combine multiple strings into a single string value with the strcat function. This is useful for placing a variable string within a constant string, such as an error message or note in a drawing.
The following code example sets a variable to a string value and then uses strcat to insert that string between two other strings.

```
(setq str "BIG")
(setq bigstr (strcat "This is a " str " test."))
"This is a BIG test."
```

## Return a Substring of a String

The substr function allows you to return a portion of a string. This function requires two arguments and has one optional argument.
The first argument is a string and the second argument is an integer that represents the start character of the string that
you want to return as the substring. If the third argument is not provided, substr returns all characters including and following the specified start character.

```
(substr "Welcome to AutoLISP" 12)
"AutoLISP"
```

If want to return a substring that is at the beginning or middle of the string provided to the substr function, you can specify an integer for the third argument that represents the number of characters that should be returned.
For example, the following example code returns the first 7 characters of the provided string:

```
(substr "Welcome to AutoLISP" 1 7)
"Welcome"
```

Often, when working with a string you might not know how long it is but might know the start position of the substring you
want to return. The strlen function returns the number of characters (including spaces) in a string.

```
(setq filnam "bigfile.txt")
(strlen filnam)
11
```

The following example code returns all the characters in a filename except the last four (the period and the three-letter
extension). This is done by using strlen to get the length of the string and subtract 4 from that value. Then substr is used to specify the first character of the substring and its length.

```
(setq newlen (- (strlen filnam) 4))
7

(substr filnam 1 newlen)
"bigfile"
```

You can combine the two previous lines of code into one if you do not need the length of the string stored in the newlen variable for other functions.

```
(substr filnam 1 (- (strlen filnam) 4))
"bigfile"
```

## Find and Replace Text in a String

Finding and replacing text can be helpful in updating notes or part numbers. The vl-string-search function allows you to locate a pattern within a string, and return the start position as an integer of the first instance
of the specified pattern. If the function returns an integer, you can then use that as the starting position for another search
to make sure there is not more than one instance of the pattern in the string.

The vl-string-subst function can be used to replace text within a string. Similar to the vl-string-search function, it can only identify the first instance of a specified pattern. You can use the vl-string-search function after replacing a text string to see if another instance of a pattern is contained in the string returned by vl-string-subst.

The following code examples find and replace the text [WIDTH] in a string.

```
(setq note "All door openings are [WIDTH] unless otherwise noted.")
"All door openings are [WIDTH] unless otherwise noted."

(setq position (vl-string-search "[WIDTH]" note))
22

(setq revised-note (vl-string-subst "36\"" "[WIDTH]" note position))
"All door openings are 36\" unless otherwise noted."

(prompt revised-note)(princ)
All door openings are 36" unless otherwise noted.
```

#### Related Concepts

* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [About Control Characters in Strings (AutoLISP)](About-Control-Characters-in-Strings-AutoLISP.md)
* [About String Conversions (AutoLISP)](About-String-Conversions-AutoLISP.md)
* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*