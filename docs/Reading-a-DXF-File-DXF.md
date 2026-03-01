# Reading a DXF File (DXF)

The following example is a simple Visual Basic program that reads a DXF file and extracts specific codes and values from
a given object in a given section.

```
' ReadDXF extracts specified code/value pairs from a DXF file.
' This function requires four string parameters, a valid DXF
' file name, a DXF section name, the name of an object in that
' section, and a comma delimited list of codes.
'
Function ReadDXF( _
        ByVal dxfFile As String, ByVal strSection As String, _
        ByVal strObject As String, ByVal strCodeList As String)
    Dim tmpCode, lastObj As String
    Open dxfFile For Input As #1
    ' Get the first code/value pair
    codes = ReadCodes
    ' Loop through the whole file until the "EOF" line
    While codes(1) <> "EOF"
        ' If the group code is '0' and the value is 'SECTION' ..
        If codes(0) = "0" And codes(1) = "SECTION" Then
            ' This must be a new section, so get the next
            ' code/value pair.
            codes = ReadCodes()
            ' If this section is the right one ..
            If codes(1) = strSection Then
                ' Get the next code/value pair and ..
                codes = ReadCodes
                ' Loop through this section until the 'ENDSEC'
                While codes(1) <> "ENDSEC"
                    ' While in a section, all '0' codes indicate
                    ' an object. If you find a '0' store the
                    ' object name for future use.
                    If codes(0) = "0" Then lastObj = codes(1)
                    ' If this object is one you're interested in
                    If lastObj = strObject Then
                        ' Surround the code with commas
                        tmpCode = "," & codes(0) & ","
                        ' If this code is in the list of codes ..
                        If InStr(strCodeList, tmpCode) Then
                            ' Append the return value.
                            ReadDXF = ReadDXF & _
                                codes(0) & "=" & codes(1) & vbCrLf
                        End If
                    End If
                    ' Read another code/value pair
                    codes = ReadCodes
                Wend
            End If
        Else
            codes = ReadCodes
        End If
    Wend
    Close #1
End Function

' ReadCodes reads two lines from an open file and returns a two item
' array, a group code and its value. As long as a DXF file is read
' two lines at a time, all should be fine. However, to make your
' code more reliable, you should add some additional error and
' other checking.
'
Function ReadCodes() As Variant
    Dim codeStr, valStr As String
    Line Input #1, codeStr
    Line Input #1, valStr
    ' Trim the leading and trailing space from the code
    ReadCodes = Array(Trim(codeStr), valStr)
End Function
```

#### Related References

* [About Writing a DXF Interface Program](About-Writing-a-DXF-Interface-Program.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*