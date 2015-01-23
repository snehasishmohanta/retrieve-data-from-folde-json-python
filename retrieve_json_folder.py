
#it will print all the data 

import re
import os
import json
auto_prefix = u'\u200B'
path = "/home/snehasish/log/search1/"

for path, dirs, files in os.walk(path):
        for data in files:
                with open("/home/snehasish/log/search1/"+data) as text:
                        for line in text:
                                 file1 = json.loads(line)
                                 try:
                                        query = (file1["appData"]["_request_params"]["params"]["q"])[0]

                                        query = query.replace(auto_prefix, "")
                                        print file1["requestDate"],"-",query.encode('utf-8')
                                 except KeyError:
                                        pass

#below code will print all the value which contain unicode infront of query.

import re
import json
import sys
file1 = sys.argv[1]
auto_prefix = u'\u200B'


with open(file1) as text:
        for line in text:
                file2 = json.loads(line)
                query = (file2["appData"]["_request_params"]["params"]["q"])[0]
                #if query.startswith(auto_prefix):
                if auto_prefix in query:
                        query = query.replace(auto_prefix, "")
                        print file2["requestDate"],"-",query.encode('utf-8')



#below code will print all the require data and print if TRUE if it contain the UNICODE and print False if it doesn't contain


import re
import os
import json
auto_prefix = u'\u200B'
path1 = "/home/snehasish/log/search1"
path2 = "/home/snehasish/log/search2"
for path, dirs, files in os.walk(path1):
        for data in files:
                with open("/home/snehasish/log/search1/"+data) as text:
                        for line in text:
                                file1 = json.loads(line)
                                try:
                                        query = (file1["appData"]["_request_params"]["params"]["q"])[0]
                                        if auto_prefix in query:
                                                query = query.replace(auto_prefix, "")
                                                print file1["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                        else:
                                                print file1["requestDate"],",",query.encode('utf-8'), ", FALSE"
                                except KeyError:
                                        pass
for path, dirs, files in os.walk(path2):
        for data in files:
                with open("/home/snehasish/log/search2/"+data) as text:
                        for line in text:
                                file1 = json.loads(line)
                                try:
                                        query = (file1["appData"]["_request_params"]["params"]["q"])[0]
                                        if auto_prefix in query:
                                                query = query.replace(auto_prefix, "")
                                                print file1["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                        else:
                                                print file1["requestDate"],",",query.encode('utf-8'), ", FALSE"
                                except KeyError:
                                        pass
# remove if page having value more than 1

import re
import os
import json
auto_prefix = u'\u200B'
path1 = "/home/snehasish/new-log/1-search-logs-01-20/"
path2 = "/home/snehasish/new-log/2-search-logs-01-20/"
for path, dirs, files in os.walk(path1):
	for file1 in files:
        	with open("/home/snehasish/new-log/1-search-logs-01-20/"+file1) as text:
                	for line in text:
				data = json.loads(line)
                		if data["appData"]["_request_params"]["params"].has_key("page"):
                        		page = (data["appData"]["_request_params"]["params"]["page"])[0]
                        		if page == "1":
                                		try:
                                        		query = (data["appData"]["_request_params"]["params"]["q"])[0]                                          
                                        		if auto_prefix in query:
                                                		query = query.replace(auto_prefix, "")
                                                		print data["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                        		else:
                                                		print data["requestDate"],",",query.encode('utf-8'), ", FALSE"
                                		except KeyError:
                                        		pass

                        		else:
                                		pass
                		else:
                        		try:
                                		query = (data["appData"]["_request_params"]["params"]["q"])[0]
                                		if auto_prefix in query:
                                	        	query = query.replace(auto_prefix, "")
                                        		print data["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                		else:
                                        		print data["requestDate"],",",query.encode('utf-8'), ", FALSE"
                        		except KeyError:
                                		pass
for path, dirs, files in os.walk(path2):
        for file1 in files:
                with open("/home/snehasish/new-log/2-search-logs-01-20/"+file1) as text:
                        for line in text:
                                data = json.loads(line)
                                if data["appData"]["_request_params"]["params"].has_key("page"):
                                        page = (data["appData"]["_request_params"]["params"]["page"])[0]
                                        if page == "1":
                                                try:
                                                        query = (data["appData"]["_request_params"]["params"]["q"])[0]                          
                                                        if auto_prefix in query:
                                                                query = query.replace(auto_prefix, "")
                                                                print data["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                                        else:
                                                                print data["requestDate"],",",query.encode('utf-8'), ", FALSE"
                                                except KeyError:
                                                        pass

                                        else:
                                                pass
                                else:
                                        try:
                                                query = (data["appData"]["_request_params"]["params"]["q"])[0]
                                                if auto_prefix in query:
                                                        query = query.replace(auto_prefix, "")
                                                        print data["requestDate"],",",query.encode('utf-8'), ", TRUE"
                                                else:
                                                        print data["requestDate"],",",query.encode('utf-8'), ", FALSE"
                                        except KeyError:
                                                pass
