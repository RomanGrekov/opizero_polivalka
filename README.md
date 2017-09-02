# opizero_polivalka

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

#############################################<br />

