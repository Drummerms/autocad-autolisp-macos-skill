# menucmd (AutoLISP)

Issues menu commands, or sets and retrieves menu item status

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(menucmd str)
```

*str*
:   *Type:* String

    Menu area and the value to assign to that menu area. The
    *string* argument has the following syntax:

    "menu\_area=value"

    The allowed values of
    *menu\_area*, shown in the following list, are the same as they are in menu file submenu references.

    *B1-B4* -- BUTTONS menus 1 through 4

    *A1-A4* -- AUX menus 1 through 4

    *P0-P16* -- Pull-down (POP) menus 0 through 16

    *I* -- Image tile menus

    *S* -- SCREEN menu (Obsolete)

    *T1-T4* -- TABLET menus 1 through 4

    *M* -- DIESEL string expressions

    **Gmenugroup.nametag**  -- A menugroup and name tag.

    NOTE:

    * Only Pull-down (POP) menus and DIESEL string expressions are supported on Mac OS.
    * Only DIESEL string expressions are supported on Web.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

The
menucmd function can switch between subpages in an AutoCAD menu. This function can also force the display of menus. This allows AutoLISP
programs to use image tile menus and to display other menus from which the user can make selections. AutoLISP programs can
also enable, disable, and place marks in menu or ribbon items.

## Examples

The following code displays the image tile menu
MOREICONS:

```
(menucmd "I=moreicons") Loads the MOREICONS image tile menu (menucmd "I=*") Displays the menu
```

The following code checks the status of the third menu item in the pull-down menu
POP11. If the menu item is currently enabled, the
 *menucmd*  function disables it.

```
(setq s (menucmd "P11.3=?")) Gets the status of the menu item (if (= s "") If the status is an empty string,   (menucmd "P11.3=~") disable the menu item )
```

The previous code is not foolproof. In addition to being enabled or disabled, menu items can also receive marks. The code
(menucmd "P11.3=?") could return
"!.", indicating that the menu item is currently checked. This code would assume that the menu item is disabled and continue without
disabling it. If the code included a call to the
wcmatch function, it could check the status for an occurrence of the tilde (~) character and then take appropriate action.

The
menucmd function also allows AutoLISP programs to take advantage of the DIESEL string expression language. Some things can be done
more easily with DIESEL than with the equivalent AutoLISP code. The following code returns a string containing the current
day and date:

```
(menucmd "M=$(edtime,$(getvar,date),DDDD\",\" D MONTH YYYY)")
"Sunday, 16 July 1995"
```

#### Related References

* [menugroup (AutoLISP)](menugroup-AutoLISP.md)

#### Related Concepts

* [Display Control Functions Reference (AutoLISP)](Display-Control-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*