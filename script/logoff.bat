chcp 65001
set y=%date:~3,4%
set m=%date:~8,2%
set d=%date%
set t=%time%
echo Logoff %d% %t% >> C:\script\%y%%m%.log