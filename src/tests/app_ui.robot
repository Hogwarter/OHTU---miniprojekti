*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Testaa Etusivun Elementit
    [Tags]    Etusivu
    Go To  ${HOME_URL}
    Page Should Contain    Latex Lähde App
    Page Should Contain    Tyyppi:

Valitse Tyypin Dropdown
    [Tags]    Dropdown
    Go To  ${HOME_URL}
    Select From List By Label    xpath=//select    Book
    Click Button    xpath=//button[text()="Submit"]


*** Keywords ***
Open And Configure Browser
    
    ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${options}  add_argument  --headless
    Call Method    ${options}  add_argument  --disable-gpu
    Call Method    ${options}  add_argument  --no-sandbox
    Create WebDriver  Chrome  options=${options}
    Maximize Browser Window
