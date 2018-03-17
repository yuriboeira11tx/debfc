#coding: utf-8
# Developer: Derxs
# Version: 1.0
import os

def main():
	print("\033[01;34m[*]\033[00;00m Aguarde...")
	
	arquivo = open('fonts.conf', 'w')
	
	arquivo.write('''<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <match target="font">
    <edit name="antialias" mode="assign"><bool>true</bool></edit>
  </match>
  <match target="font">
    <edit name="hintstyle" mode="assign"><const>hintnone</const></edit>
  </match>
  <match target="font">
   <edit mode="assign" name="hinting"><bool>false</bool></edit>
  </match>
</fontconfig>''')
	
	arquivo.close()

	os.system("mv fonts.conf ~/.fonts.conf")
	
	print("\033[01;32m[*]\033[0;0m Sucesso!")

try:
	main()
except:
	print("\033[01;31m[!]\033[0;0m Houve algum erro! Tente executar com root")
