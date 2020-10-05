# _*_ coding:utf-8 _*_

import os
import json
import platform

from bpb.lib.controller import Controller

BASE_DIR = os.path.abspath(os.getcwd())

def initConfig():
  config_init = {}

  config_init["NAVER_ID"] = input("NAVER_ID: ")
  config_init["NAVER_PASSWORD"] = input("NAVER_PASSWORD: ")

  if config_init:
    with open('config.json', 'w') as f:
      json.dump(config_init, f)

    print("\n\nconfig.json 파일이 생성되었습니다.")
    print("\n\n=============== 계정정보 ================")
    with open('config.json', 'r') as f:
      content = json.load(f)

    print(content)
    print("=========================================")

def configuration():
  print("\n\nconfig.json 파일 확인 중..")
  if os.path.isfile("config.json"):
    print("\n\n확인완료")
    print("\n\n파일 내의 계정정보 확인 중..")
    with open("config.json", "r") as f:
      config_json = json.load(f)

    isAuth = True
    isAuth = True if config_json["NAVER_ID"] else False
    isAuth = True if config_json["NAVER_PASSWORD"] else False

    print(config_json)
    if isAuth is False:
      print("\n\n계정정보가 없습니다. 새롭게 입력하겠습니다.")
      initConfig()
    
  else:
    print("\n\n파일이 없습니다 생성하겠습니다.")
    initConfig()
  return BASE_DIR + '/config.json'

if __name__ == "__main__":
  account_set_path = configuration()
  current_driver = ""
  current_driver = "chromedriver_mac" if platform.system() == "Darwin" else "chromedriver.exe"
  web_driver = BASE_DIR + "/lib/" + current_driver
  resource_dir = BASE_DIR + "/data"
  target = resource_dir + "/test.md"

  controller = Controller(target, account_set_path, web_driver, resource_dir, debug=True)
  controller()