#!/bin/bash
yum install httpd wget git -y
systemctl restart httpd
cat << 'EOF' >> /var/www/html/index.html
<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>AWSome Website</title>
</head>
<body>
  <h1>Hello! From Target Group 02 / VM 01</h1>
</body>
</html>
EOF
