import os
print("start upload...")

cmd='python /home/esir/Arduino/piupdue/piupdue.py -f /home/esir/Arduino/DueCtrl_V4_EADC.cpp.bin'
return_code=os.system(cmd)
cmd='sudo /home/esir/Arduino/bossac -e -w -v -b /home/esir/Arduino/DueCtrl_V4_EADC.cpp.bin -R'
return_code=os.system(cmd)
print(return_code)

print("end upload.")
