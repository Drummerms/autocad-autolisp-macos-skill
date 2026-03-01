# Unit Definition File Reference (AutoLISP)

The AutoCAD unit definition file, *acad.unt*, allows you to define the factors to convert data one set of units to another set of units.

The *acad.unt* file is a plain ASCII text format file and is used by the unit-conversion function cvunit. You can add new and modify the unit definitions available by using a text editor. A definition consists of two lines in
the file—the unit name and the unit definition. The first line must have an asterisk (\*) in the first column, followed by
the name of the unit. A unit name can have several abbreviations or alternate spellings, separated by commas. If a unit name
has singular and plural forms, you can specify these using the following format:

```
*[ [common] [ ( [singular.] plural) ] ]...
```

You can specify multiple expressions (singular and plural). They do not have to be located at the end of the word, and a
plural form is not required. The following are examples of valid unit name definitions:

```
*inch(es)
*milleni(um.a)
*f(oot.eet) or (foot.feet)
```

The line following the \*unit name line defines the unit as either fundamental or derived.

## Fundamental Units

A fundamental unit is an expression in constants. If the line following the \*unit name line begins with something other than an equal sign (=), it defines fundamental units. Fundamental units consist of five
integers and two real numbers in the following form:

```
c, e, h, k, m, r1, r2
```

The five integers correspond to the exponents of these five constants:

*c* Velocity of light in a vacuum

*e* Electron charge

*h* Planck's constant

*k* Boltzman's constant

*m* Electron rest mass

As a group, these exponents define the dimensionality of the unit: length, mass, time, volume, and so on.

The first real number (r1) is a multiplier, and the second (r2) is an additive offset (used only for temperature conversions).
The fundamental unit definition allows for different spellings of the unit (for example, meter and metre); the case of the unit is ignored. An example of a fundamental unit definition is as follows:

```
*meter(s),metre(s),m
-1,0,1,0,-1,4.1214856408e11,0
```

In this example, the constants that make one meter are as follows:

![](../images/GUID-D1CEC7F1-1E34-46B9-AB8F-CABCCA8CE1AD-low.png)

## Derived Units

A derived unit is defined in terms of other units. If the line following the \*unit name line begins with an equal sign ( *=* ), it defines derived units. Valid operators in these definitions are  *\**  (multiplication),  */*  (division),  *+*  (addition),  *-*  (subtraction), and  *^*  (exponentiation).

You can specify a predefined unit by naming it, and you can use abbreviations (if provided). The items in a formula are multiplied
together unless some other arithmetic operator is specified. For example, the units database defines the dimensionless multiple
and submultiple names, so you can specify a unit such as micro-inches by entering micro inch.

The following are examples of derived unit definitions.

```
; Units of area
*township(s)
=93239571.456 meter^2
```

The definition of a township is given as 93,239,571.456 square meters.

```
; Electromagnetic units
*volt(s),v
=watt/ampere
```

In this example, a volt is defined as a watt divided by an ampere. In the *acad.unt*, both watts and amperes are defined in terms of fundamental units.

## User Comments

Comments can be added to the file by placing a semicolon at the beginning of a line. The comment continues to the end of
the line.

```
; This entire line is a comment.
```

#### Related Concepts

* [About Unit Conversion (AutoLISP)](About-Unit-Conversion-AutoLISP.md)
* [Example: Convert Inches to Meters (AutoLISP)](Example-Convert-Inches-to-Meters-AutoLISP.md)
* [Conversion Functions Reference (AutoLISP)](Conversion-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*