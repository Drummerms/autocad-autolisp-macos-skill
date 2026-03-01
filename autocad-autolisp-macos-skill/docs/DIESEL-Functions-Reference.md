# DIESEL Functions Reference

Status retrieval, computation, and display are performed by DIESEL functions.

All functions have a limit of 10 parameters, including the function name itself.

| Function | Description/Example |
| + (addition) | Returns the sum of the numbers  *val1* ,  *val2* , …,  *val9* .  ``` $(+, val1 [, val2, …, val9]) ```  If the current thickness is set to 5, the following DIESEL string returns 15.  ``` $(+, $(getvar, thickness), 10) ``` |
| - (subtraction) | Returns the result of subtracting the numbers  *val2*  through  *val9*  from  *val1* .  ``` $(-, val1 [, val2 , …, val9]) ``` |
| \* (multiplication) | Returns the result of multiplying the numbers  *val1* ,  *val2* , …,  *val9* .  ``` $(*, val1 [, val2, …, val9]) ``` |
| / (division) | Returns the result of dividing the number  *val1*  by  *val2* , …,  *val9* .  ``` $(/, val1 [, val2, …, val9]) ``` |
| = (equal to) | If the numbers  *val1*  and  *val2*  are equal, the string returns 1; otherwise, it returns 0.  ``` $(=, val1, val2) ``` |
| < (less Than) | If the number  *val1*  is less than  *val2* , the string returns 1; otherwise, it returns 0.  ``` $(<, val1, val2) ```  The following expression gets the current value of HPANG; if the value is less than the value stored in the system variable USERR1, it returns 1. If the value 10.0 is stored in USERR1 and the current setting of HPANG is 15.5, the following string returns 0.  ``` $(<, $(getvar, hpang), $(getvar, userr1)) ``` |
| > (greater Than) | If the number  *val1*  is greater than  *val2* , the string returns 1; otherwise, it returns 0.  ``` $(>, val1, val2) ``` |
| != (not Equal to) | If the numbers  *val1*  and  *val2*  are not equal, the string returns 1; otherwise, it returns 0.  ``` $(!=, val1, val2) ``` |
| <= (less Than or Equal to) | If the number  *val1*  is less than or equal to  *val2*  , the string returns 1; otherwise, it returns 0.  ``` $(<=, val1, val2) ``` |
| >= (greater Than or Equal to) | If the number  *val1*  is greater than or equal to  *val2* , the string returns 1; otherwise, it returns 0.  ``` $(>=, val1, val2) ``` |
| and | Returns the bitwise logical AND of the integers  *val1*  through  *val9* .  ``` $(and, val1 [, val2,…, val9]) ``` |
| angtos | Returns the angular value in the format and precision specified.  ``` $(angtos, value [, mode, precision]) ```  Edits the given  *value*  as an angle in the format specified by the  *mode*  and  *precision*  as defined for the analogous AutoLISP function. If  *mode*  and  *precision*  are omitted, it uses the current values chosen by the UNITS command.  NOTE:AutoLISP is not available in AutoCAD LT for Mac OS.  The following *mode* values can be applied:  * 0, for Degrees * 1, for Degrees/Minutes/Seconds * 2, for Grads * 3, for Radians * 4, for Surveyor's Units |
| Edtime | Returns a formatted date and time based on a given picture.  ``` $(edtime, time, picture) ```  Edits the Julian date given by  *time*  (obtained, for example, from  *$(getvar,date)*  according to the given  *picture* ). The  *picture*  consists of format phrases replaced by specific representations of the date and time. Characters not interpretable as format phrases are copied literally into the result of  *$(edtime)* . Format phrases are defined as shown in the following table.  For example, assume that the date and time are Saturday, 5 September 1998 4:53:17.506 the corresponding format phrases and output examples for *edtime* are as follows:  * D - 5 * DD - 05 * DDD - Sat * DDDD - Saturday * M - 9 * MO - 09 * MON - Sep * MONTH - September * YY - 98 * YYYY - 1998 * H - 4 * HH - 04 * MM - 53 * SS - 17 * MSEC - 506 * AM/PM - AM * am/pm - am * A/P - A * a/p - a  Enter the entire AM/PM phrase as shown in the preceding table; if AM is used alone, the A will be read literally and the M will return the current month.  If any AM/PM phrases appear in the picture, the H and HH phrases edit the time according to the 12-hour civil clock (12:00-12:59 1:00-11:59) instead of the 24-hour clock (00:00-23:59).  The following example uses the date and time from the preceding table. Notice that the comma must be enclosed in quotation marks because it is read as an argument separator.  ``` $(edtime, $(getvar,date), DDD"," DD MON YYYY - H:MMam/pm) ```  It returns the following:  Sat, 5 Sep 1998 - 4:53am  If  *time*  is 0, the time and date at the moment that the outermost macro was executed is used. This avoids lengthy and time-consuming multiple calls on $(getvar,date) and guarantees that strings composed with multiple $(edtime) macros all use the same time. |
| eq | If the strings  *val1*  and  *val2*  are identical, the string returns 1; otherwise, it returns 0.  ``` $(eq, val1, val2) ```  The following expression gets the name of the current layer; if the name matches the string value stored in the USERS1 (USERS1-5) system variable, it returns 1. Assume the string "PART12" is stored in USERS1 and the current layer is the same.  NOTE:The USERS1-5 system variables are not available in AutoCAD LT for Mac OS.  ``` $(eq, $(getvar, users1), $(getvar, clayer)) ```  It returns the following:  1 |
| Eval | Passes the string  *str*  to the DIESEL evaluator and returns the result of evaluating it.  ``` $(eval, str) ``` |
| fix | Truncates the real number  *value*  to an integer by discarding any fractional part.  ``` $(fix, value) ``` |
| Getenv | Returns the value of the environment variable  *varname* .  ``` $(getenv, varname) ```  If no variable with that name is defined, it returns the null string. |
| Getvar | Returns the value of the system variable with the given  *varname* .  ``` $(getvar, varname) ``` |
| if | Conditionally evaluates expressions.  ``` $(if, expr, dotrue [, dofalse]) ```  If  *expr*  is nonzero, it evaluates and returns  *dotrue* . Otherwise, it evaluates and returns  *dofalse* . Note that the branch not chosen by  *expr*  is not evaluated. |
| Index | Returns the specified member of a comma-delimited string.  ``` $(index, which, string) ```  Assumes that the  *string*  argument contains one or more values delimited by the macro argument separator character, the comma. The  *which*  argument selects one of these values to be extracted, with the first item numbered 0. This function is most frequently used to extract *X*, *Y*, or *Z* coordinate values from point coordinates returned by $(getvar).  Applications can use this function to retrieve values stored as comma-delimited strings from the USERS1-5 system variables.  NOTE:The USERS1-5 system variables are not available in AutoCAD LT for Mac OS. |
| nth | Evaluates and returns the argument selected by  *which* .  ``` $(nth, which, arg0 [, arg1,…, arg7]) ```  If  *which*  is 0, nth returns  *arg0* , and so on. Note the difference between  *$(nth)*  and  *$(index)* ;  *$(nth)* returns one of a series of arguments to the function, while  *$(index)*  extracts a value from a comma-delimited string passed as a single argument. Arguments not selected by  *which*  are not evaluated. |
| or | Returns the bitwise logical OR of the integers  *val1*  through  *val9* .  ``` $(or, val1 [, val2,…, val9]) ``` |
| Rtos | Returns the real value in the format and precision specified.  ``` $(rtos, value [, mode, precision]) ```  Edits the given  *value*  as a real number in the format specified by  *mode*  and  *precision.*  If  *mode*  and  *precision*  are omitted, it uses the current values selected with the UNITS command. |
| Strlen | Returns the length of  *string*  in characters.  ``` $(strlen, string) ``` |
| Substr | Returns the substring of  *string* , starting at character  *start*  and extending for  *length*  characters.  ``` $(substr, string, start [, length]) ```  Characters in the string are numbered from 1. If  *length*  is omitted, it returns the entire remaining length of the string. |
| Upper | Returns the  *string*  converted to uppercase according to the rules of the current locale.  ``` $(upper, string) ``` |
| xor | Returns the bitwise logical XOR of the integers  *val1*  through  *val9* .  ``` $(xor, val1 [, val2,…, val9]) ``` |

#### Related References

* [DIESEL Error Message Reference](DIESEL-Error-Message-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Responding to AutoLISP with DIESEL Expressions in Macros](About-Responding-to-AutoLISP-with-DIESEL-Expressions-in-Macros.md)
* [About DIESEL Expressions in Macros](About-DIESEL-Expressions-in-Macros.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*