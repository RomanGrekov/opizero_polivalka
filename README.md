# opizero_polivalka

# Ansible
# Check target host
ansible target -a "uptime" -c paramiko<br />

# Userfull links

http://opi-gpio.readthedocs.io/en/latest/api-documentation.html<br />
http://pillow.readthedocs.io/en/3.4.x/reference/ImageDraw.html<br />
https://nayon.fr/blog/ssd1306-monochrome-oled-display-on-orangepi-in-python/<br />
https://www.14core.com/wiring_the_i2c__spi_oled_monochrome_display_with_raspberrypi/<br />

# Network settings
/etc/wpa_supplicant/wpa_supplicant.conf<br />    
<br />
network={<br />
   ssid="Visonic"<br />
   proto=WPA2<br />
   psk="*******"<br />
   id_str="mywifi"<br />
}<br />
<br />
##############################################<br />
<br />
/etc/network/interfaces<br />
auto lo<br />
iface lo inet loopback<br />
<br />
allow-hotplug wlan0<br />
iface wlan0 inet manual<br />
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf <br />
iface mywifi inet dhcp<br />

or use nmcli<br />
iwconfig wlan0<br />
nmcli dev wifi list<br />
nmcli device wifi connect MYHOME password 'p@55w0rd'<br />
nmcli radio wifi<br />
nmcli radio wifi <on|off><br />
nmcli device wifi rescan<br />

#############################################<br />

