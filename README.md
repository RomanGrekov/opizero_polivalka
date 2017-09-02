# opizero_polivalka

# Network settings
/etc/wpa_supplicant/wpa_supplicant.conf

network={
   ssid="Visonic"
   proto=WPA2
   psk="*******"
   id_str="mywifi"
}

##############################################

/etc/network/interfaces
auto lo
iface lo inet loopback

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface mywifi inet dhcp

#############################################

