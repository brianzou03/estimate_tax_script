# H&R Block Tax Calculator Script
This script accesses H&R Block's tax calculator at https://www.hrblock.com/tax-calculator/.
The script uses Selenium and Selenium's chrome webdriver to click/input values into
the H&R Block tax calculator based on user provided inputs.

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

## Technology Stack
* Python 3
* Selenium

## Potential Expansion
For future expansion, the project can be expanded to take W-2 forms, as well as
calculate potential tax refunds using the same H&R Block calculator.