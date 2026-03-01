# About ASCII Codes (AutoLISP)

ASCII codes are integer values that represent alphanumeric characters.

Numeric values 0 through 127 represent digits 0 through 9, letters of the alphabet, punctuation marks, and other special
characters. Some AutoLISP functions return or expect an ASCII code for a single character instead of the string equivalent.

For example, the grread function returns the ASCII code of the key pressed when a user provides keyboard input. The ASCII code in the list returned
can then be evaluated or converted for display based on how the program is going to use it.

The following are a few of the AutoLISP functions that are used when working with ASCII codes:

* grread – Reads values from any of the AutoCAD input devices.
* read-char – Returns the ASCII code representing the character read from the keyboard input buffer or an open file.
* write-char – Writes one character to the screen or to an open file.
* ascii – Returns the ASCII code for the first character of a string.
* chr – Converts an integer representing an ASCII character code into a single-character string.

## Converting ASCII Codes and Characters to ASCII Codes

The ascii and chr functions can be used to handle the conversion of ASCII codes. The ascii function returns the ASCII code associated with a character string, and chr returns the character string associated with an ASCII code.

The following code converts an uppercase A to its ASCII code value:

```
(ascii "A")
65
```

The following code converts an ASCII code value to the character string it represents:

```
(chr 65)
"A"
```

The following example code defines a command named ASCII and a function named BASE that is used by the ASCII command. The ASCII command writes characters with their codes in decimal, octal, and hexadecimal form to the screen and a file named *ASCII.txt*.

```
; BASE converts from a decimal integer to a string in another base.
(defun BASE (bas int / ret yyy zot)
  (defun zot (i1 i2 / xxx)
    (if (> (setq xxx (rem i2 i1)) 9)
      (chr (+ 55 xxx))
      (itoa xxx)
    )
  )

  (setq ret (zot bas int)
        yyy (/ int bas)
  )
  (setq ret (strcat (zot bas yyy) ret))
  (setq yyy (/ yyy bas))

  (strcat (zot bas yyy) ret)
)

(defun C:ASCII (/)                      ;chk out ct code dec oct hex )
  (initget "Yes")
  (setq chk (getkword "\
Writing to ASCII.TXT, continue? <Y>: "))
  (if (or (= chk "Yes") (= chk nil))
    (progn
      (setq out  (open "ascii.txt" "w")
            chk  1
            code 0
            ct   0
      )
      (princ "\
 \
 CHAR DEC OCT HEX \
")
      (princ "\
 \
 CHAR DEC OCT HEX \
" out)
      (while chk
        (setq dec (strcat "  " (itoa code))
              oct (base 8 code)
              hex (base 16 code)
        )
        (setq dec (substr dec (- (strlen dec) 2) 3))
        (if (< (strlen oct) 3)
          (setq oct (strcat "0" oct))
        )

        (princ (strcat "\
 " (chr code) " " dec " " oct " " hex))
        (princ (strcat "\
 " (chr code) " " dec " " oct " " hex)
               out
        )

        (cond
          ((= code 255) (setq chk nil))
          ((= ct 20)
           (setq
             xxx (getstring
                   "\
 \
Press 'X' to eXit or any key to continue: "
                 )
           )
           (if (= (strcase xxx) "X")
             (setq chk nil)
             (progn
               (setq ct 0)
               (princ "\
 \
 CHAR DEC OCT HEX \
")
             )
           )
          )
        )
        (setq ct   (1+ ct)
              code (1+ code)
        )
      )
      (close out)
      (setq out nil)
    )
  )
 (princ)
)
```

#### Related Concepts

* [About Integers (AutoLISP)](About-Integers-AutoLISP.md)
* [About Number Handling (AutoLISP)](About-Number-Handling-AutoLISP.md)
* [About String Conversions (AutoLISP)](About-String-Conversions-AutoLISP.md)
* [About Strings and String Handling (AutoLISP)](About-Strings-and-String-Handling-AutoLISP.md)
* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*