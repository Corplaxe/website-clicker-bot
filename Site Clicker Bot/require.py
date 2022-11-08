from selenium import webdriver
options = webdriver.FirefoxOptions()
#options.headless = True
profile = webdriver.FirefoxProfile(r"C:\Users\TunaH\AppData\Roaming\Mozilla\Firefox\Profiles\eep1xh0v.default-release")
browser = webdriver.Firefox(executable_path=r"C:\Users\TunaH\OneDrive\Masaüstü\geckodriver.exe",firefox_profile=profile,options=options,firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")