# DIESEL Error Message Reference

Generally, if you make a mistake in a DIESEL expression, what went wrong may not be obvious. Depending on the nature of the
error, DIESEL embeds an error indication in the output stream.

| DIESEL error messages | |
| Error message | Description |
| $? | Syntax error (usually a missing right parenthesis or a runaway string) |
| $*(func,??)* | Incorrect arguments to *func* |
| $*(func)??* | Unknown function *func* |
| $(++) | Output string too long—evaluation truncated |

#### Related References

* [DIESEL Functions Reference](DIESEL-Functions-Reference.md)
* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Responding to AutoLISP with DIESEL Expressions in Macros](About-Responding-to-AutoLISP-with-DIESEL-Expressions-in-Macros.md)
* [About DIESEL Expressions in Macros](About-DIESEL-Expressions-in-Macros.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*