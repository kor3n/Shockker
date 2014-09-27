import subprocess



def shockker(imp):
	shock = imp
	p = subprocess.Popen(shock, shell=True, stderr=subprocess.PIPE)
	out = p.stderr.read(1)
	p.wait()
	return

check1 = '[ ]'
check2 = '[ ]'
check3 = '[ ]'
exit = 0

while exit != 1:
	print (chr(27) + "[2J") #Clear Screen
	print ("  _____ _          _ _  _____ _                _    ")
	print (" / ____| |        | | |/ ____| |              | |   ")
	print ("| (___ | |__   ___| | | (___ | |__   ___   ___| | __")
	print (" \___ \| '_ \ / _ \ | |\___ \| '_ \ / _ \ / __| |/ /")
	print (" ____) | | | |  __/ | |____) | | | | (_) | (__|   < ")
	print ("|_____/|_| |_|\___|_|_|_____/|_| |_|\___/ \___|_|\_\ ")
	print ("[+]A Simple ShellShock Tester		      @kor3n ")

	print ('''

	''')


	print ('''A simple tester for the shellshock vulnerability :).
I would recommend you try all of the exploits before and after 
an update. Just Choose from the menu below on what exploit to
try. When you use the tester a * will be in the blank boxes
to mark what are vulnerable.
	''')

	print ('''Menu:

%s[1] Exploit 1

%s[2] Exploit 2

%s[3] Exploit 3

[4] Exit

	''' % (check1, check2, check3))


	choice = input("Enter Exploit Number: ")

	if choice == '1':
		shockker("env x='() { :;}; echo [+]Vulnerable.' bash -c 'echo [+] CVE-2014-6271 Exploit 1'")
		print ()
		y1 = input("Do you see Vulnerable? (Y/n): ")
		if y1 == 'y' or y1 == 'Y':
			check1 = '[*]'
		elif y1 == '':
			check1 = '[*]'
	elif choice == '2':
		shockker("env X='() { (ionsec.co.uk)=>\x5C' bash -c 'echo date'; cat echo ; rm -f echo")
		print ()
		y1 = input("Do you see the date? (Y/n): ")
		if y1 == 'y' or y1 == 'Y':
			check2 = '[*]'
		elif y1 == '':
			check2 = '[*]'
	elif choice == '3':
		shockker("env -i X=' () { }; echo [+]Vulnerable.' bash -c 'date'")
		print ()
		y1 = input("Do you see Vulnerable? (Y/n): ")
		if y1 == 'y' or y1 == 'Y':
			check3 = '[*]'
		elif y1 == '':
			check3 = '[*]'
	elif choice == '4':
		exit = 1

