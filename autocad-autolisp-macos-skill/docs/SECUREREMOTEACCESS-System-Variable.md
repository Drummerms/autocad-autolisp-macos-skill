# SECUREREMOTEACCESS (System Variable)

Controls whether ObjectARX programs are restricted from accessing internet locations or remote servers.

|  |  |
| --- | --- |
| Type: | Switch |
| Saved in: | Registry |
| Initial value: | 1 |

To help protect against malicious code in an ObjectARX network API call, setting the value to 1 blocks the following operations:

* Copying remote files to the local computer using AcadHostApplicationServices::getRemoteFile().
* Uploading files to a remote location using AcadHostApplicationServices::putRemoteFile().

| Value | Description |
| 0 | Allows access with ObjectARX to any location, including the internet or a remote server. This option maintains legacy behavior. |
| 1 | Blocks access with ObjectARX to the internet or a remote server. Loads files only if they are local. This setting was expanded in the 2020.1 product update and might interfere with some applications. |

Leaving SECUREREMOTEACCESS turned on reduces the possibility of an application or malware loading or copying a file to or
from your local computer using ObjectARX.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*