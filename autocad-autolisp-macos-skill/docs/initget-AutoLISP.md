# initget (AutoLISP)

Establishes keywords for use by the next user-input function call

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(initget [bits] [keywords])
```

*bits*
:   *Type:* Integer

    A bit-coded that allows or disallows certain types of user input. The bits can be added together in any combination to form
    a value between 0 and 255. If no
    *bits* argument is supplied, zero (no conditions) is assumed. The bit values are as follows:

    *1* (bit 0) -- Prevents the user from responding to the request by entering only Enter.

    *2* (bit 1) -- Prevents the user from responding to the request by entering zero.

    *4* (bit 2) -- Prevents the user from responding to the request by entering a negative value.

    *8* (bit 3) -- Allows the user to enter a point outside the current drawing limits. This condition applies to the next user-input
    function even if the AutoCAD LIMCHECK system variable is currently set.

    *16* (bit 4) -- (Not currently used.)

    *32* (bit 5) -- Uses dashed lines when drawing a rubber-band line or box. For those functions with which the user can specify
    a point by selecting a location in the drawing area, this bit value causes the rubber-band line or box to be dashed instead
    of solid. (Some display drivers use a distinctive color instead of dashed lines.) If the AutoCAD POPUPS system variable is
    0, AutoCAD ignores this bit.

    *64* (bit 6) -- Prohibits input of a
    *Z* coordinate to the
    getdist function; lets an application ensure that this function returns a 2D distance.

    *128* (bit 7) -- Allows arbitrary input as if it is a keyword, first honoring any other control bits and listed keywords. This
    bit takes precedence over bit 0; if bits 7 and 0 are set and the user presses Enter, a null string is returned.

    *256* (bit 8) -- Give direct distance input precedence over arbitrary input. For external applications, arbitrary input is given
    precedence over direct distance input by default. Set this bit if you wish to force AutoCAD to evaluate user input as direct
    distance input. Note that legal point input from the keyboard always takes precedence over either direct distance or arbitrary
    input.

    *512* (bit 9) -- If set before a call to
    getpoint or
    getcorner, a temporary UCS will be established when the cursor crosses over the edge of a planar face of a solid. The temporary UCS
    is reset when the cursor moves off of a face. It is dynamically re-established when the cursor moves over a different face.
    After the point is acquired, the dynamic UCS is reset to the current UCS. This functionality is not enabled for non-planar
    faces such as the side of a cylinder.

    *1024* (bit 10) -- When calling
    getdist,
    getangle,
    getorient,
    getpoint, or
    getcorner, you may not want the distance, angle, orient, point, or corner to be influenced by ortho, polar, or otracking in the
    *Z* direction. Setting this bit before calls to any of these functions will temporarily disable ortho, polar, and otracking in
    the
    *Z* direction. This is useful when you create 2D entities such as a polyline, arc, or circle, or when you use the AutoCAD ARRAY
    command, which creates only a 2D array. In 2D-only commands it can be confusing and error-prone to allow 3D points to be entered
    using ortho
    *Z*, polar
    *Z*, or otrack
    *Z*.

    NOTE:Future versions of AutoLISP may use additional
    initget control bits, so avoid setting bits that are not listed here.

*keywords*
:   *Type:* String

    Series of keywords.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

The functions that honor keywords are
getint,
getreal,
getdist,
getangle,
getorient,
getpoint,
getcorner,
getkword,
entsel,
nentsel, and
nentselp. The
getstring function is the only user-input function that does not honor keywords.

The keywords are checked by the next user-input function call when the user does not enter the expected type of input (for
example, a point to
getpoint). If the user input matches a keyword from the list, the function returns that keyword as a string result. The application
can test for the keywords and perform the action associated with each one. If the user input is not an expected type and does
not match a keyword, AutoCAD asks the user to try again. The
initget bit values and keywords apply only to the next user-input function call.

If
initget sets a control bit and the application calls a user-input function for which the bit has no meaning, the bit is ignored.

If the user input fails one or more of the specified conditions (as in a zero value when zero values are not allowed), AutoCAD
displays a message and asks the user to try again.

Function Applicable Control Bits
:   The special control values are honored only by those
    get*XXX* functions for which they make sense, as indicated in the following table:

    | User-input functions and applicable control bits | | | | | | |
    |  |  | Control bits values | | | | |
    | Function | Honors  key  words | No  null  (1) | No  zero  (2) | No  negative  (4) | No  limits  (8) | Uses  dashes  (32) |
    | getint | X | X | X | X |  |  |
    | getreal | X | X | X | X |  |  |
    | getdist | X | X | X | X |  | X |
    | getangle | X | X | X |  |  | X |
    | getorient | X | X | X |  |  | X |
    | getpoint | X | X |  |  | X | X |
    | getcorner | X | X |  |  | X | X |
    | getkword | X | X |  |  |  |  |
    | entsel | X |  |  |  |  |  |
    | nentsel | X |  |  |  |  |  |
    | nentselp | X |  |  |  |  |  |

    | User-input functions and applicable control bits (continued) | | | | | |
    |  | Control bits values | | | | |
    | Function | 2D  distance  (64) | Arbitrary  input  (128) | Direct  distance  (256) | UCS face  tracking  (512) | Disable  Z-tracking  (1024) |
    | getint |  | X |  |  |  |
    | getreal |  | X |  |  |  |
    | getdist | X | X | X |  | X |
    | getangle |  | X | X |  | X |
    | getorient |  | X | X |  | X |
    | getpoint |  | X | X | X | X |
    | getcorner |  | X | X | X | X |
    | getkword |  | X |  |  |  |
    | entsel |  |  |  |  |  |
    | nentsel |  |  |  |  |  |
    | nentselp |  |  |  |  |  |

Keyword Specifications
:   The
    *string* argument is interpreted according to the following rules:

    1. Each keyword is separated from the following keyword by one or more spaces. For example,
       "Width Height Depth" defines three keywords.
    2. Each keyword can contain only letters, numbers, and hyphens (-).

    There are two methods for abbreviating keywords:

    * The required portion of the keyword is specified in uppercase characters, and the remainder of the keyword is specified in
      lowercase characters. The uppercase abbreviation can be anywhere in the keyword (for example,
      "LType",
      "eXit", or
      "toP").
    * The
      *entire* keyword is specified in uppercase characters, and it is followed immediately by a comma, which is followed by the required
      characters (for example,
      "LTYPE,LT"). The keyword characters in this case must include the first letter of the keyword, which means that
      "EXIT,X" is not valid.

    The two brief examples,
    "LType" and
    "LTYPE,LT", are equivalent: if the user types
    *LT* (in either uppercase or lowercase letters), this is sufficient to identify the keyword. The user can enter characters that
    *follow* the required portion of the keyword, provided they don't conflict with the specification. In the example, the user could
    also enter
    *LTY* or
    *LTYP*, but
    *L* would not be sufficient.

    If
    *string* shows the keyword entirely in uppercase
    *or* lowercase characters with no comma followed by a required part, AutoCAD recognizes the keyword only if the user enters all
    of it.

    The
    initget function provides support for localized keywords. The following syntax for the keyword string allows input of the localized
    keyword while it returns the language independent keyword:

    ```
    "local1 local2 localn _indep1 indep2 indepn"
    ```

    where
    *local1* through
    *localn* are the localized keywords, and
    *indep1* through
    *indepn* are the language-independent keywords.

    There must always be the same number of localized keywords as language-independent keywords, and the first language-independent
    keyword is prefixed by an underscore as shown in the following example:

    ```
    (initget "Abc Def _Ghi Jkl")
    (getkword "\
    Enter an option (Abc/Def): ")
    ```

    Entering
    *A* returns Ghi and entering
    *\_J* returns Jkl.

## Examples

None

#### Related References

* [getkword (AutoLISP)](getkword-AutoLISP.md)

#### Related Concepts

* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*