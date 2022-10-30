# H&R Block Tax Calculator Script
This script accesses H&R Block's tax calculator at https://www.hrblock.com/tax-calculator/

## Installations
```
$ pip install selenium
$ pip install webdriver_manager
```

## Possibly required installation
```
$ pip3 install packaging
```

## Known Issues
The executable_path for the chromedriver is deprecated, will potentially update in the future.

```
DeprecationWarning: executable_path has been deprecated, please pass in a Service object
driver = webdriver.Chrome(executable_path='chromedriver.exe')
```
