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
