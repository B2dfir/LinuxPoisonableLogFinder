# LinuxPoisonableLogFinder
Security Testing Tool to identify whether a list of common log files, which may be used for log poisoning, can be accessed from an known local file inclusion vulnerability.

You must identify a LFI vulnerability first, as well as the complete path that provides access to the root directory.

Usage: PoisonableLogFinder.py <root LFI URI>
E.g. PoisonableLogFinder.py hxxp://192.168.1.10/vuln/index.php?path=../../../../../../
