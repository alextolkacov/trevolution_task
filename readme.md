Hey!

Before you start make sure that Python 3.9 or newer is installed.

If so, from the root run the command `pip3 install requirements.txt` to install
all necessary dependencies.

How to run tests:
1. in your terminal type `pytest test` to run all tests that are located in tests/ directory
2. if you want to run a particular test - type 
```
pytest test/path_to_the_test_file.py
```
3. if you're an experienced user in your terminal type 
```
pytest test -n $THREADS --reruns $RERUNS --alluredir=allure_report --screenshot=on --screenshot_path=on
```
where:
* `$THREADS` is the thread count
* `$RERUNS` is a rerun count
* `allure_report` is a directory where allure reports will be saved
* `--screenshot=on --screenshot_path=on` allows to sve screenshots in case of failure

After tests are finished just run `allure serve allure_report` from your root
to see a full report of a test run.

But make sure that allure is installed on your laptop. If it's not
-> `brew install allure`
