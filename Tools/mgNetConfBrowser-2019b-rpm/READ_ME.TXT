This is the "READ_ME.TXT" file distributed with
MG-SOFT NetConf Browser 2019 Professional Edition.

Copyright (C) 2010-2018  MG-SOFT Corporation.
All rights reserved.

============================================================================
Table of Contents
-----------------

1. About the Software
2. What's New in this Version
3. Installing and Starting the Software
  3.1. Installing and Starting the Software on Windows
  3.2. Installing and Starting the Software on Linux
  3.3. Installing and Starting the Software on Mac OS X
4. Uninstalling the Software
  4.1. Uninstalling the Software on Windows
  4.2. Uninstalling the Software on Linux
  4.3. Uninstalling the Software on Mac OS X  
5. MG-SOFT Corporation on the Internet
6. Ordering the Software
7. Licensing Agreement
8. Contacting MG-SOFT Corporation


============================================================================
1. About the Software
---------------------

MG-SOFT NetConf Browser Professional Edition is a powerful and user-
friendly NETCONF and RESTCONF client application that lets you retrieve, 
modify, install and delete the configuration of any NETCONF or RESTCONF 
server device in the network. 

The software can load any set of standard or vendor-specific YANG 1.1 
(RFC 7950) or YANG 1 (RFC 6020) modules (and corresponding YIN modules) 
and display their contents in a visual manner, where module elements are 
represented in a hierarchical tree structure, containing nodes on which 
NETCONF or RESTCONF operations can be invoked.

NetConf Browser offers an intuitive user interface that lets you easily 
retrieve the device configuration and state data, as well as modify the 
device configuration via the NETCONF v1.1 (RFC 6241) or NETCONF v1.0 
(RFC 4741) protocol operations (get, get-config, lock, unlock, edit-
config, copy-config, delete-config, commit, etc.). The software supports 
establishing NETCONF sessions over SSH2 and TLS v1.2 secure transport 
protocols. MG-SOFT NetConf Browser also supports NETCONF Call Home over 
SSH and TLS (RFC 8071). 

Besides the NETCONF protocol, MG-SOFT NetConf Browser fully supports 
also the RESTCONF protocol with both, XML and JSON encoding of data (RFC 
8040). NetConf Browser lets you use all standard RESTCONF HTTP methods 
like GET, POST, PUT, PATCH, DELETE etc., invoke proprietary operations 
and actions, and allows receiving RESTCONF event notifications. The 
software incorporates YANG-based auto-complete mechanism for composing 
the RESTCONF URIs, as well as fully fledged auto-completion feature when 
writing RESTCONF message payloads in XML and JSON format. NetConf 
Browser supports regular RESTCONF over HTTPS sessions, as well as 
RESTCONF Call Home sessions.

In addition to providing quick access to common NETCONF and RESTCONF 
operations, the software also implements advanced tools, like the 
RFC 6110-compliant NETCONF Content Editor and Validator that has been 
extended by MG-SOFT to support also RESTCONF protocol and allows you to 
easily compose any type of NETCONF XML or RESTCONF XML or JSON document 
and validate it using the DSDL schemas, which are automatically 
generated from selected YANG modules. Furthermore, the software supports 
subscribing to and receiving event notifications via NETCONF and RESTCONF
(RFC 5277, RFC 8040). In addition, NetConf Browser also supports the YANG 
Module Library mechanism (RFC 7895) and the NETCONF get-schema operation 
(RFC 6022). The software can download schema definitions (e.g., YANG and 
YIN modules) from remote NETCONF and RESTCONF servers automatically.

MG-SOFT NetConf Browser is a Java(TM) application that can be installed 
and used on Windows, Linux and Mac OS X operating systems with Java 
Runtime Environment version 7.0 (a.k.a. JRE 1.7) or later installed. 


This product includes software developed by the
 Visigoth Software Society (http://www.visigoths.org/).
For detailed third-party licenses information, please 
refer to the /doc/3rdPartyLicenses/ subfolder.

========================================================================
2. What's New in this Version 
-----------------------------

Here is a brief description of the major new functions and features in
MG-SOFT NetConf Browser Professional Edition V7.x release:

* Complete support for RESTCONF protocol.
  MG-SOFT NetConf Browser now implements full support for the RESTCONF 
  protocol (RFC 8040) with both, XML and JSON data encoding. The 
  application user interface, data validation procedures and message 
  payload composition feature have all been extended to transparently 
  support also RESTCONF in addition to the NETCONF protocol. NetConf 
  Browser lets you use all standard RESTCONF HTTP methods, like GET, 
  POST, PUT, PATCH, DELETE, etc., invoke proprietary operations 
  and actions, and enable receiving event notifications via RESTCONF.
  The software incorporates YANG-based auto-complete mechanism for 
  composing the RESTCONF URIs, as well as fully fledged auto-completion
  feature when writing RESTCONF message payloads in XML and JSON format. 
 
* Support for RESTCONF and RESTCONF Call Home connections over HTTPS.
  The NetConf Browser connecting capabilities have been extended to 
  enable connecting to RESTCONF devices via the HTTP over TLS (HTTPS), 
  using the TLS public key infrastructure (X.509 certificates) for 
  authenticating both server and client. In addition to TLS 
  authentication, the HTTP client authentication is also available, 
  featuring the basic and digest authentication methods. Besides the 
  regular RESTCONF connections, RESTCONF Call Home connections that are 
  initiated by servers are also supported. All device connection details 
  (inc. user credentials) and data model can be saved to user-configured 
  device profiles for later use and effortless management of RESTCONF 
  (and NETCONF) devices. After establishing a RESTCONF session with a 
  server, NetConf Browser automatically discovers the server RESTCONF 
  root resource, server capabilities, data-model-specific RPC 
  operations, event streams, and yang-library data. The software can 
  automatically download YANG files from the RESTCONF server and load 
  them so one can immediately start managing the given device.
  
* Extended NETCONF Content Editor supporting RESTCONF.
  The RFC6110-based DSDL schema generation and validation in the NETCONF 
  Content Editor has been extended by MG-SOFT to support also RESTCONF 
  protocol. It now allows you to easily compose any type of NETCONF XML 
  or RESTCONF XML or JSON document and validate it using the DSDL 
  schemas, which are automatically generated from the selected YANG 
  modules. The integrated RESTCONF toolbar provides an easy way to 
  select the desired operation (GET, POST, PATCH, etc.) and to create 
  a target resource URI using the resource auto-completion feature. 
  All this lets you create an arbitrary RESTCONF message and send it to
  the server to manipulate or retrieve the desired resource in no time. 
  
* Generating configuration from YANG model (NETCONF and RESTCONF).
  MG-SOFT NetConf Browser now lets you select, e.g., a subtree node in 
  the YANG tree and generate a NETCONF XML instance document or RESTCONF 
  XML or JSON document for an <edit-config> or PUT/PATCH request, 
  respectively. The generated content contains at least one instance of 
  all config=true data nodes (leaf, leaf-list, list, container, anyxml, 
  etc.) from the given subtree. The generated leaf and leaf-list elements
  have valid, yet dummy values that can be easily edited before sending 
  the content to the server. This powerful feature allows you to quickly
  and easily create a (part of) configuration that does not exist on 
  the server yet. 

* Generating content for custom RPC/actions to invoke proprietary 
  operations.
  The software lets you select an arbitrary "rpc" or "action" type of 
  node in the YANG tree and generate the corresponding RPC (NETCONF) or 
  POST (RESTCONF) request with all required input elements as defined in 
  YANG. After reviewing or editing the auto-generated RPC or action 
  content, you can send it to a server to invoke the respective 
  operation or action.

* Support for Java version 9, 10, 11 and HiDPI.
  NetConf Browser has been tested to successfully run on Oracle Java 
  version 9, 10 and 11 on all supported platforms: Windows, Linux and Mac. 
  Starting with Java version 11, both Oracle JDK (commercial version) and 
  OpenJDK (open source build) are preliminary supported. Using Java 9 or 
  later also adds proper support for HiDPI displays (e.g., UHD/4K). The 
  latter means that the application windows, graphics, and text are scaled 
  automatically according to the system settings, which makes NetConf 
  Browser perfectly usable also with modern high pixel density displays.

* Enhanced documentation.
  Significantly updated and enhanced user manual and product documentation
  with numerous hints and usage examples will help you get the most from 
  MG-SOFT NetConf Browser Pro. 
  
Besides the above listed features, a number of minor improvements have 
been implemented and all known problems occurring in older versions have 
been fixed for this release.


============================================================================
3. Installing and Starting the Software
---------------------------------------

MG-SOFT NetConf Browser is a Java(TM) application that can be installed 
and used on 32-bit and 64-bit Windows, Linux and Mac OS X operating 
systems with Oracle Java Runtime Environment version 7.0 (a.k.a. JRE 1.7) 
or newer installed. Using the latest version of Oracle Java is recommended. 
If you have a large data model (YANG or YIN), it is recommended to use a 
64-bit OS and 64-bit version of Java, which can allocate much more memory 
than 32-bit version.

Make sure to install the latest version of the software as available
from http://www.mg-soft.com/download.html


3.1. Installing and Starting the Software on Windows
----------------------------------------------------
Installing the Software
-----------------------
You need administrative user privileges to install the software.

To install the MG-SOFT NetConf Browser, unzip the distribution zip 
file and run the setup.exe. Follow the on-screen guidelines. You must 
reboot the computer if the setup procedure prompts you to do so.

Starting the Software
---------------------
To start the software, open the Start menu, navigate to and click the
NetConf Browser menu entry (MG-SOFT NetConf Browser/NetConf Browser). 


3.2. Installing and Starting the Software on Linux
---------------------------------------------------
Installing the Software
-----------------------
The root user privileges are required to install the software.

Before installing the software, please close all running MG-SOFT 
applications and uninstall any previous version of MG-SOFT NetConf 
Browser from the system. For uninstalling instructions, please
refer to the "Uninstalling the Software" section below.

On Linux, download the appropriate package (.rpm, .deb or .tgz) and use 
the corresponding package manager to install the software, as follows:

a) Linux distributions with the RPM package manager (RHEL, CentOS, Fedora, 
   SUSE, etc): 
   
   - On a 32-bit (i386) Linux distribution with the RPM package manager, 
     install the 32-bit RPM package by executing the following command 
     in a Terminal window: 
     # rpm -ivh mgNetConfBrowser_2019-X.X-X.i386.rpm

   - On a 64-bit (x86_64) Linux distribution with the RPM package manager, 
     install the 64-bit RPM package, as follows:
     # rpm -ivh mgNetConfBrowser_2019-X.X-X.x86_64.rpm

b) Linux distributions with the DPKG package manager (Debian, Ubuntu, etc.):
   
   - On a 32-bit (i386) Linux distribution with the DPKG package manager, 
     install the 32-bit DEB package:
     # dpkg -i mgNetConfBrowser-2019_X.X-X_i386.deb

   - On a 64-bit (x86_64/amd64) Linux distribution with the DPKG package 
     manager, install the 64-bit DEB package, as follows:
     # dpkg -i mgNetConfBrowser-2019_X.X-X_x86_64.deb

c) Linux distributions with the installpkg tool (e.g., Slackware):
   
   - On a 32-bit (i386) Linux distribution with the installpkg tool, 
     install the 32-bit TGZ package:
     # installpkg mgNetConfBrowser_2019-X.X-i386-X.tgz

   - On a 64-bit (x86_64) Linux distribution with the installpkg tool, 
     install the 64-bit TGZ package:
     # installpkg mgNetConfBrowser_2019-X.X-x86_64-X.tgz
     
     
In case you have KDE or GNOME Environments installed on your machine, the
installation will add an entry to the K Menu or Gnome Menu, respectively.

Starting the Software
---------------------
The first and the easiest way is to run the application from the 
K menu|MG-SOFT NetConf Browser|NetConf Browser (KDE environment), or 
Gnome menu|MG-SOFT NetConf Browser|NetConf Browser (GNOME environment).

To start the software from the command prompt, open the Terminal 
window, and run the following script:

  # /usr/local/mg-soft/mgnetconfbrowser/bin/mgnetconfbrowser.sh
  
  
3.3. Installing and Starting the Software on Mac OS X (Intel)
-------------------------------------------------------------
Installing the Software
-----------------------
You need to have admin user privileges to install the software. Before 
installing the software, please close all running MG-SOFT applications 
and remove any previous version of MG-SOFT NetConf Browser from the 
system (please refer to the "Uninstalling the Software" section below).

Note: MG-SOFT NetConf Browser no longer supports Apple Java 6. To
      install and use the software on Mac OS X 10.7.3 or later, please 
      download and install Oracle Java 7u26 (a.k.a. 1.7u26) or later from 
      www.java.com.

To install the software double-click the MG-SOFT NetConf Browser .dmg 
file. MG-SOFT NetConf Browser virtual drive appears on the desktop. 
Drag&drop the "MG-SOFT NetConf Browser.app" from the MG-SOFT NetConf 
Browser virtual drive to the system "Applications" folder.

The software has been successfully installed and tested by MG-SOFT on 
the following Mac OS X versions running on Intel-based Mac platforms:

- Mac OS X v10.7.3+ Lion
- Mac OS X v10.8.x Mountain Lion
- Mac OS X v10.9.x Mavericks
- Mac OS X v10.10.x Yosemite
- Mac OS X v10.11.x El Capitan
- Mac OS X v10.12.x Sierra
- Mac OS X v10.13.x High Sierra
- Mac OS X v10.14.x Mojave

Starting the Software
---------------------
To start the software, open a Finder window, navigate to the Applications 
folder and double-click the "MG-SOFT NetConf Browser.app" icon in it.


============================================================================
4. Uninstalling the Software
----------------------------
To uninstall the software, you need the administrative user 
privileges.


4.1. Uninstalling the Software on Windows
-----------------------------------------
To uninstall the software on Windows, select the "Start/Programs/
MG-SOFT NetConf Browser/Uninstall MG-SOFT NetConf Browser" command from 
the Windows taskbar. 

Follow the instructions displayed on the screen.


4.2. Uninstalling the Software on Linux
---------------------------------------
If the software has been installed by the RPM package manager, 
run the following command in a terminal window to uninstall 
MG-SOFT NetConf Browser from your computer:
 
  # rpm -e mgNetConfBrowser_VVVV


If the software has been installed by the DPKG package manager,
use the following command to uninstall MG-SOFT NetConf Browser 
from your computer:
 
  # dpkg -r mgNetConfBrowser-VVVV


On Slackware Linux distribution use the following command to 
uninstall MG-SOFT NetConf Browser from your computer:
 
  # removepkg mgNetConfBrowser_VVVV
 
Where VVVV is the version of the software installed (e.g., 
2016, 2017, 2018, etc.) 


4.3. Uninstalling the Software on Mac OS X 
-------------------------------------------
To uninstall the software on Mac OS X, open a Finder window, navigate 
to the Applications folder and move the "MG-SOFT NetConf Browser.app" 
icon to the Trash in the Dock (or right-click the app icon and choose the 
"Move to Trash" command from the context menu).


============================================================================
5. MG-SOFT Corporation on the Internet
--------------------------------------

* MG-SOFT Web Site              http://www.mg-soft.si/
* MG-SOFT Products & Services   http://www.mg-soft.si/products.html
* MG-SOFT Sales Page            http://www.mg-soft.si/sales.html
* MG-SOFT Support Page          http://www.mg-soft.si/support.html
* MG-SOFT Corp. Profile         http://www.mg-soft.si/profile.html

* MIB Browser Professional      http://www.mg-soft.si/mgMibBrowserPE.html
* Trap Ringer Professional      http://www.mg-soft.si/tringer.html
* Net Inspector                 http://www.mg-soft.si/netinsp.html
* NETCONF Browser Professional  http://www.mg-soft.si/mgNetConfBrowser.html
* Visual YANG Designer Pro.     http://www.mg-soft.si/mgYangDesigner.html
* YANG Explorer Professional    http://www.mg-soft.si/mgYangExplorer.html
* NETCONF/YANG Python Scripting http://www.mg-soft.si/mgNetConfScripting.html
* Visual MIB Builder            http://www.mg-soft.si/builder.html
* MIB Explorer                  http://www.mg-soft.si/mgMibExplorer.html
* SNMP Master Agent             http://www.mg-soft.si/agent.html
* SNMP Agent Simulator          http://www.mg-soft.si/mgSnmpAgentSimulator.html
* SNMP Proxy Agent              http://www.mg-soft.si/mgSnmpProxyAgent.html

Latest News
-----------
Visit http://www.mg-soft.si/news.html for the latest news and 
information about the software releases and updates.

Evaluation Software
-------------------
Evaluation software is available for downloading from MG-SOFT's web
site at http://www.mg-soft.si/download.html

To apply for a 30-day evaluation license key, fill in and submit the
on-line order form at http://www.mg-soft.si/evalKeyReq.html

For immediate software release notifications, subscribe to our mailing
list at http://www.mg-soft.si/maillist.html


============================================================================
6. Ordering the Software
------------------------

Visit http://www.mg-soft.com/sales.html or contact <sales@mg-soft.com>
to obtain the latest ordering and licensing information. Prior to
ordering the software, visit http://www.mg-soft.com/licenseTypes.html
for details on various licensing arrangements for licensing MG-SOFT's
software products.


============================================================================
7. Licensing Agreement
----------------------

Check the 'LICENSE AGREEMENT.TXT' file that was installed with the
software. Also, check the 'LICENSE TYPES.TXT' file or visit
http://www.mg-soft.com/licenseTypes.html for details on various
licensing arrangements for licensing MG-SOFT's software products.
Contact <sales@mg-soft.com> for additional information.


============================================================================
8. Contacting MG-SOFT Corporation
----------------------------------

For the latest information about our products, check our WEB
site at http://www.mg-soft.com/ or contact us directly.

You can subscribe to our mailing lists on-line by submitting the
application form at http://www.mg-soft.com/maillist.html

For additional information about MG-SOFT Corporation, please
contact the following address:

MG-SOFT Corporation          Phone:    +386 2 2506565
Strma ulica 8                Fax:      +386 2 2506566
2000 Maribor                 E-mail:   info@mg-soft.com
Slovenia                     Internet: http://www.mg-soft.com/


============================================================================
