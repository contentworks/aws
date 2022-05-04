yum install httpd wget git
systemctl restart httpd
cat << 'EOF' >> /var/www/html/index.html
<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>AWSome Website</title>
</head>
<body>
  <h1>Hello! From Target Group 01 / VM 02</h1>
</body>
</html>
EOF
