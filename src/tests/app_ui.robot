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


Valitse Article Ja Tarkista Sisältö
    [Tags]     Article
    Go To  ${HOME_URL}
    Select From List By Label     xpath=//select    Article
    Click Button     xpath=//button[text()="Submit"]
    Page Should Contain     Create a LaTeX @article Reference
    Page Should Contain     Citekey:
    Page Should Contain     Author:
    Page Should Contain     Title:
    Page Should Contain     Publisher:
    Page Should Contain     Address:
    Page Should Contain     Year

Valitse Article, Täytä Lomake Ja Generoi
    [Tags]    Article Form
    Go To  ${HOME_URL}
    Select From List By Label    xpath=//select    Article
    Click Button    xpath=//button[text()="Submit"]

    Input Text    name=citekey    Artti
    Input Text    name=author    Arttu
    Input Text    name=title    Artin elämä
    Input Text    name=publisher    Otava
    Input Text    name=address    Jump Street 21
    Input Text    name=year    2003
    Click Button    xpath=//button[text()="Generate"]
    Location Should Be  ${HOME_URL}/

    Page Should Contain   @article{ Artti,
    Page Should Contain   author = { Arttu },
    Page Should Contain   title = { Artin elämä },
    Page Should Contain   publisher = { Otava },
    Page Should Contain   address = { Jump Street 21 },
    Page Should Contain   year = { 2003 }
    Page Should Contain   }

*** Keywords ***
Open And Configure Browser
    
    ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${options}  add_argument  --headless
    Call Method    ${options}  add_argument  --disable-gpu
    Call Method    ${options}  add_argument  --no-sandbox
    Create WebDriver  Chrome  options=${options}
    Maximize Browser Window
