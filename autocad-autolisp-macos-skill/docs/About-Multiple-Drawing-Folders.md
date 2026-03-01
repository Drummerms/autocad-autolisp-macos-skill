# About Multiple Drawing Folders

Keeping your drawing and other associated files in separate directories makes it easier to perform basic file maintenance.

The scenario described in this topic is based on the sample directory structure described in About File Organization, but
you can expand or alter it to meet your needs.

You can set up the
*/AcadJobs* or
*/AcltJobs* directory to contain your drawing subdirectories. The drawing subdirectories can contain other subdirectories that hold related
support files for a particular drawing type or job. The
*/AcadJobs/Job1/Support* directory can contain blocks and customized files specific to the drawing files in
*/AcadJobs/Job1*. Specifying
*support* (with no path prefix) in the Support path adds the
*support* directory within the current directory to the Support path.

To make sure that the required drawing directory is the current directory when you start, and that all files and subdirectories
in that directory are easily accessible, you can create a program icon or a desktop shortcut that specifies the correct working
directory for each job. This functionality works only if you set the REMEMBERFOLDERS system variable to 0.

You can use a batch program to create new job directories automatically. The following batch program verifies that a specified
directory exists, sets that directory to be current, and then runs the application.

Windows
:   NOTE:This script can also be used with AutoCAD LT by substituting
    *Acad* for
    *Acaclt* below. Before running the script, make sure to replace the text
    *<product name>* in the path to the executable on your workstation with the name of the installed product.

    ```
    @echo off
    C:
    if exist \AcadJobs\Jobs\%1 goto RUNACAD
    echo.
    echo *** Creating \AcadJobs\Jobs\%1
    echo *** Press Ctrl+C to cancel.
    echo.
    pause
    mkdir \AcadJobs\Jobs\%1
    :RUNACAD
    cd \AcadJobs\Jobs\%1
    start “C:\Program Files\Autodesk\<product name>\acad.exe”
    ```

    Using an ASCII text editor (such as Notepad), save the batch program to a file named
    *acad.bat* or
    *acadlt.bat* as appropriate. Be sure to change the drive and directory names to match those on your system.

    Place this file in a directory that is on your system search path (for example,
    *C:\winnt*). You can run this batch program using the Run command from Windows, or by double-clicking the file in File Explorer. If
    you saved the file as
    *acad.bat*, use the following syntax:

    *acad
    *jobname**

    where
    *jobname* is the name of the job directory to make current.

Mac OS
:   NOTE:This script can also be used with AutoCAD LT by substituting
    *Acad* for
    *Acaclt* below. For the last line, verify the path to the executable. Before running the script, make sure to replace the text
    *<product name>* in the path to the executable on your workstation with the name of the installed product.

    ```
    #!/bin/sh
    prj="$1"
    #Switch to the project folder and start the application
    function startApp() {
      cd /AcadJobs/Jobs/$prj
      echo "Starting the Application"
      "/Applications/Autodesk/<product name>/<product name>.app/Contents/MacOS/<product name>"
    }
    #Clear Terminal and check for the existence of the folder
    clear
    cd .
    if [ -d /AcadJobs/Jobs/$prj ]
    then
      startApp
    fi
    #Prompt to create folder
    echo .
    echo Creating /AcadJobs/Jobs/$prj
    echo 'Press Y to continue (or A to abort)'
    echo .
    cont="True"
    answer=""while [ "$cont" = "True" ]
    do
      read -n1 -t10 answer
      echo
      if [ "$answer" = "y" ] || [ "$answer" = "Y" ] || [ "$answer" = "a" ] || [ "$answer" = "A" ]
      then
        cont="False"
      fi
    done
    #Check to see if the user requested to abort or continue
    if [ "$answer" = "a" ] || [ "$answer" = "A" ]
    then
      exit 1
    else
      mkdir -p /AcadJobs/Jobs/$prj
    fi
    #Switch to the project folder and start the application
    startApp
    ```

    Using an ASCII text editor (such as TextEdit), save the batch program to a file named
    *acad.sh* or
    *acadlt.sh*. Be sure to change the drive and directory names to match those on your system.

    Place this file in your home directory or a shared location that is on your system. You can run this shell script program
    using the Terminal window in /Applications/Utilities on the drive the operating system is installed. If you saved the file
    as
    *acad.sh* or
    *acadlt.sh*, use the following syntax:

    *./acad.sh
    *jobname** or
    *./acadlt.sh
    *jobname**

    where
    *jobname* is the name of the job directory to make current.

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About File Organization](About-File-Organization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*