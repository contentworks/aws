yum install httpd wget git -y
systemctl restart httpd
curl -O https://www.tooplate.com/zip-templates/2121_wave_cafe.zip
tar -C /var/www/html --strip-components=1 -zxvf 2121_wave_cafe.zip && rm -f 2121_wave_cafe.zip
