::====== Chrome browser 
pytest -s -v -m "sanity" --html='D:\Classes\Framework_Practice\Reports\sanity_tests.html' --browser chrome .\TestCase\
:: pytest -s -v -m "regression" --html='D:\Classes\Framework_Practice\Reports\regression_tests.html' --browser chrome .\TestCase\
:: pytest -s -v -m "sanity and regression" --html='D:\Classes\Framework_Practice\Reports\sanity_regression_tests.html' --browser chrome .\TestCase\


:: ====== Firefox browser 
:: pytest -s -v -m "sanity" --html='D:\Classes\Framework_Practice\Reports\sanity_tests.html' --browser firefox .\TestCase\
:: pytest -s -v -m "regression" --html='D:\Classes\Framework_Practice\Reports\regression_tests.html' --browser firefox .\TestCase\
:: pytest -s -v -m "sanity and regression" --html='D:\Classes\Framework_Practice\Reports\sanity_regression_tests.html' --browser firefox .\TestCase\


:: ====== edge browser 
:: pytest -s -v -m "sanity" --html='D:\Classes\Framework_Practice\Reports\sanity_tests.html' --browser edge .\TestCase\
:: pytest -s -v -m "regression" --html='D:\Classes\Framework_Practice\Reports\regression_tests.html' --browser edge .\TestCase\
:: pytest -s -v -m "sanity and regression" --html='D:\Classes\Framework_Practice\Reports\sanity_regression_tests.html' --browser edge .\TestCase\


:: ====== Headless browser 
:: pytest -s -v -m "sanity" --html='D:\Classes\Framework_Practice\Reports\sanity_tests.html' .\TestCase\
:: pytest -s -v -m "regression" --html='D:\Classes\Framework_Practice\Reports\regression_tests.html' .\TestCase\
:: pytest -s -v -m "sanity and regression" --html='D:\Classes\Framework_Practice\Reports\sanity_regression_tests.html' .\TestCase\
