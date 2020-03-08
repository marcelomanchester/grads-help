import datetime
import os

def format(number):
    if number < 10:
        number = '0' + str(number)
    return str(number)

print('Requesting files ...')
try:
    now = datetime.datetime.now()
    os.system("curl http://ftp.cptec.inpe.br/modelos/io/produtos/MERGE/GPM/HOURLY/MERGE_GPM_EARLY/"+ str(now.year) + format(now.month) + "/MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.ctl -o MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.ctl")
    os.system("curl http://ftp.cptec.inpe.br/modelos/io/produtos/MERGE/GPM/HOURLY/MERGE_GPM_EARLY/"+ str(now.year) + format(now.month) + "/MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.grib2 -o MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.grib2")
    os.system("curl http://ftp.cptec.inpe.br/modelos/io/produtos/MERGE/GPM/HOURLY/MERGE_GPM_EARLY/"+ str(now.year) + format(now.month) + "/MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.idx -o MERGE_GPM_early_"+ str(now.year) + format(now.month) + format(now.day-2) +"00.idx")
    print("Finished. Your data is available in this directory!")
except:
    print("Error!!!")


