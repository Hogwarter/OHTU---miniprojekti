*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${DELAY}       0.5 seconds
${HOME_URL}    http://localhost:5001
${BROWSER}     Chrome  
${CHROME_OPTS}    --headless --disable-gpu --no-sandbox  
