*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.2 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${DELETE_ROBOT_SOURCES_URL}  http://${SERVER}/delete_robot_sources_db
${BROWSER}    chrome
${HEADLESS}   true

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
    # Open directly on home page
    Open Browser  ${HOME_URL}  browser=${BROWSER}  options=${options}

Reset Todos
    Go To  ${RESET_URL}

Delete Robot Sources
    Go To  ${DELETE_ROBOT_SOURCES_URL}

Add Article With Key
    [Arguments]  ${citekey}
    Go To  ${HOME_URL}
    Click Link  Add article
    Input Text  name=citekey    ${citekey}
    Input Text  name=author     robot
    Input Text  name=year       2077
    Input Text  name=name       Robot takeover
    Input Text  name=journal    Robots today
    Input Text  name=volume     6
    Input Text  name=number     7
    Input Text  name=urldate    2077-01-01
    Input Text  name=url        https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Input Text  name=tag        tag
    Click Button  Create
    Go To  ${HOME_URL}

Modify Article With Key
    [Arguments]    ${citekey}    ${new_author}    ${new_year}    ${new_title}
    ...            ${new_journal}    ${new_volume}    ${new_number}
    ...            ${new_urldate}    ${new_url}    ${new_tag}

    Go To  ${HOME_URL}

    Click Link  xpath=//tr[td[normalize-space()='${citekey}']]//a[normalize-space()='Modify']

    Input Text  name=citekey    ${citekey}
    Input Text  name=author     ${new_author}
    Input Text  name=year       ${new_year}
    Input Text  name=name       ${new_title}
    Input Text  name=journal    ${new_journal}
    Input Text  name=volume     ${new_volume}
    Input Text  name=number     ${new_number}
    Input Text  name=urldate    ${new_urldate}
    Input Text  name=url        ${new_url}
    Input Text  name=tag        ${new_tag}

    Click Button  Edit
