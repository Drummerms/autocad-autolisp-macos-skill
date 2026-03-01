# vlax-import-type-library (AutoLISP/ActiveX)

Imports information from a type library

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(vlax-import-type-library :tlb-filename filename [:methods-prefix mprefix  :properties-prefix pprefix :constants-prefix cprefix])
```

*filename*
:   *Type:* String

    Name of the type library. A file can be one of the following types:

    * A type library (TLB) or object library (OLB) file
    * An executable (EXE) file
    * A library (DLL) file containing a type library resource
    * A compound document holding a type library
    * Any other file format that can be understood by the LoadTypeLib API

    If you omit the path from
    *tlb-filename*, AutoCAD looks for the file in the support file search path.

*mprefix*
:   *Type:* String

    Prefix to be used for method wrapper functions. For example, if the type library contains a Calculate method and the
    *mprefix* parameter is set to “cc-”, Visual LISP generates a wrapper function named
    cc-Calculate. This parameter defaults to “”.

*pprefix*
:   *Type:* String

    Prefix to be used for property wrapper functions. For example, if the type library contains a Width property with both read
    and write permissions, and
    *pprefix* is set to “cc-”, then Visual LISP generates wrapper functions named
    cc-get-Width and
    cc-put-Width. This parameter defaults to “”.

*cprefix*
:   *Type:* String

    Prefix to be used for constants contained in the type library. For example, if the type library contains a
    ccMaxCountOfRecords property with both read and write permissions, and
    *cprefix* is set to “cc-”, Visual LISP generates a constant named
    cc-ccMaxCountOfRecords. This parameter defaults to “”.

NOTE:Keywords are required when passing arguments to
vlax-import-type-library.

## Return Values

*Type:* T or nil

T, if successful; otherwise,
nil if the library could not be imported.

## Remarks

Function wrappers created by
vlax-import-type-library are available only in the context of the document
vlax-import-type-library was issued from.

In the current release,
vlax-import-type-library is executed at runtime, rather than at compile time. In future releases, this may change. The following practices are recommended
when using
vlax-import-type-library:

* If you want your code to run on different machines, avoid specifying an absolute path in the
  *tlb-file-name* parameter.
* If possible, avoid using
  vlax-import-type-library from inside any AutoLISP expression (that is, always call it from a top-level position).
* In your AutoLISP source file, code the
  vlax-import-type-library call before any code that uses method or property wrappers or constants defined in the type library.

## Examples

Import a Microsoft Word type library, assigning the prefix “msw-” to methods and properties, and “mswc-” to constants:

```
(vlax-import-type-library
  :tlb-filename "C:/Program Files (x86)/Microsoft Office/root/Office16/msword.olb"
  :methods-prefix "msw-"
  :properties-prefix "msw-"
  :constants-prefix "mswc-")
T
```

#### Related References

* [vlax-create-object (AutoLISP/ActiveX)](vlax-create-object-AutoLISP-ActiveX.md)
* [vlax-get-object (AutoLISP/ActiveX)](vlax-get-object-AutoLISP-ActiveX.md)
* [vlax-get-or-create-object (AutoLISP/ActiveX)](vlax-get-or-create-object-AutoLISP-ActiveX.md)
* [vlax-typeinfo-available-p (AutoLISP/ActiveX)](vlax-typeinfo-available-p-AutoLISP-ActiveX.md)

#### Related Concepts

* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*