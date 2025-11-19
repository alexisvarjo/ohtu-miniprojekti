*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${DELETE_ROBOT_SOURCES_URL}  http://${SERVER}/delete_robot_sources_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.01 seconds
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Todos
    Go To  ${RESET_URL}

Add Article With Key
    [Arguments]  ${citekey}
    Go To  ${HOME_URL}
    Click Link  Add article
    Input Text  citekey  ${citekey}
    Input Text  author  robot
    Input Text  year  2077
    Input Text  name  Robot takeover
    Input Text  journal  Robots today
    Input Text  volume  6
    Input Text  number  7
    Input Text  urldate  2077-01-01
    Input Text  url  https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Click Button  Create
    Go To  ${HOME_URL}

Modify Article With Key
    [Arguments]  ${citekey} ${new_author} ${new_year} ${new_title} ${new_journal} ${new_volume} ${new_number} ${new_urldate} ${new_url}
    Go To  ${HOME_URL}
    Click Link  Modify article
    Input Text  citekey  ${citekey}
    Input Text  author  ${new_author}
    Input Text  year  ${new_year}
    Input Text  name  ${new_title}
    Input Text  journal  ${new_journal}
    Input Text  volume  ${new_volume}
    Input Text  number  ${new_number}
    Input Text  urldate  ${new_urldate}
    Input Text  url  ${new_url}
    Click Button  Modify
    Go To  ${HOME_URL}

Delete Robot Sources
    Go To  ${DELETE_ROBOT_SOURCES_URL}
