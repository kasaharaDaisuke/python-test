# -*- coding: utf-8 -*- 

import json
import os
import datetime

assetsdir = "assetsex/"
version = 0
ex_files = set({"project.manifest","version.manifest"})
as_files = {}

# seek dir
def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in fild_all_files(assetsdir):
    print file, os.stat(file).st_mtime
    if os.path.isfile(file):
      f_info = os.stat(file)
      dt = datetime.datetime.fromtimestamp(f_info.st_mtime)
      key_file = file.replace(assetsdir,"")
      if key_file not in ex_files:
          as_files[key_file] = {"md5":f_info.st_mtime, "compressed":False, "update":dt.strftime('%Y-%m-%d %H:%M:%S')}
          if version < f_info.st_mtime:
            version = f_info.st_mtime
  
# 元のversion.manifestファイル読み込み
with open("assetsex/version.manifest","r") as v_file:
    v_data = json.load(v_file)
    v_data["version"] = version

# version.manifestファイル書き込み
with open('assetsex/version.manifest', 'w') as f:
    json.dump(v_data, f, sort_keys=True, indent=4)
  
# 元のproject.manifestファイル読み込み
with open("assetsex/project.manifest", "r") as json_file:
  json_data = json.load(json_file)  
  json_data["version"] = version
  json_data["assets"] = {}
  
  for file in as_files:
    json_data['assets'][file] = as_files[file]


# JSONファイル書き込み
with open('assetsex/project.manifest', 'w') as f:
    json.dump(json_data, f, sort_keys=True, indent=4)


# 内容の確認
print json.dumps(json_data, sort_keys=True, indent=4)