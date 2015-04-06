:: Joseph DeVictoria - ECEn 493 Mars Rover - 2015
:: This script will run a full udp broadcast of the controller data
:: from the xbox controller.
@ECHO off
set PATH=%PATH%;C:\Program Files\Java\jdk1.8.0_40\bin
rmdir /s /q "bin/mars"

javac -cp -Xlint:unchecked -sourcepath src/mars/ -d bin/ src/mars/*.java

IF [%1]==[] ( 
	SET hostnameone=localhost
) ELSE (
	SET hostnameone=%1
)
IF [%2]==[] ( 
	SET hostnametwo=localhost
) ELSE (
	SET hostnametwo=%2
)
IF [%3]==[] (
	SET port=27015 
) ELSE (
	SET port=%3
)
echo src\python\xbox.py
start "Mars Rover Xbox Controller Parser" src\python\xbox.py
pushd bin
echo java mars.Mars -S localhost %port%
start "Mars Rover Base Station Client" java mars.Mars -C %hostnameone% %hostnametwo% %port% 
echo java mars.Mars -C %hostnameone% %hostnametwo% %port%
start "Mars Rover Base Station Server" java mars.Mars -S localhost %port%
cd ..