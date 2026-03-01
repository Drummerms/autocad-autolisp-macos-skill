# TEXTEVAL (System Variable)

Controls how text strings entered with TEXT (using scripts or AutoLISP) or with -TEXT are evaluated.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

| 0 | All responses to prompts for text strings and attribute values are taken literally. |
| 1 | All text starting from an opening parenthesis [(] or an exclamation mark [!] is evaluated as an AutoLISP expression, as for nontextual input. |

The TEXT command takes all input literally regardless of the setting of TEXTEVAL unless it is executed completely with a script
or AutoLISP expression. The -TEXT command honors the setting of TEXTEVAL.

#### Related References

* [TEXT (Command)](TEXT-Command.md)

#### Related Concepts

* [About Creating Notes Using Text](About-Creating-Notes-Using-Text.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*