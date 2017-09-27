# LinuxPoisonableLogFinder
Security testing tool to identify whether a list of common log files, which may be used for log poisoning, can be accessed from an known local file inclusion vulnerability.

You must identify a LFI vulnerability first, as well as the complete path that provides access to the root directory.

Usage: PoisonableLogFinder.py "root LFI URI" "optional terminator"

E.g. PoisonableLogFinder.py "hxxp://192.168.1.10/vuln/index.php?path=../../../../../../" "%00"

## Change Log
##### 26 Sep 2017 - V1.1 

Updated to take an optional termination string parameter (such as %00), and added two log file locations: `var/log/httpd-access.log` `var/log/httpd-error.log`
  
##### 24 Aug 2017 - V1.0 

Initial release
