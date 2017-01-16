# -*- coding: utf-8 -*- 

import json

with open("assetsex/project.manifest.json", "r") as json_file:
  obj = json.load(json_file)
  
  obj["assets"]["res/addfile.gif"] = {"md5":"xxxx","compressed":False}
  obj["assets"]["res/ui/test.gif"] = {"md5":"xxxx_testgif","compressed":False}
  
  print json.dumps(obj, sort_keys=True, indent=4)

