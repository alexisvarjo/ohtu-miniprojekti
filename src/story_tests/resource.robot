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

Delete Robot Sources
    Go To  ${DELETE_ROBOT_SOURCES_URL}

Add Article With Key
    [Arguments]  ${citekey}
    Go To  ${HOME_URL}
    Select From List By Value  id=add_type  article
    Click Button  Add
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

Add Book With Key
    [Arguments]  ${citekey}
    Go To  ${HOME_URL}
    Select From List By Value  id=add_type  book
    Click Button  Add
    Input Text  name=citekey    ${citekey}
    Input Text  name=author     robot
    Input Text  name=editor     robots
    Input Text  name=title      Robot takeover
    Input Text  name=publisher  Robots inc
    Input Text  name=year       2077
    Input Text  name=volume     6
    Input Text  name=number     7
    Input Text  name=urldate    2077-01-01
    Input Text  name=url        https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Input Text  name=tag        tag
    Click Button  Create
    Go To  ${HOME_URL}

Add Inproceeding With Key
    [Arguments]  ${citekey}
    Go To  ${HOME_URL}
    Select From List By Value  id=add_type  inproceeding
    Click Button  Add
    Input Text  name=citekey    ${citekey}
    Input Text  name=author     robot
    Input Text  name=editor     robots
    Input Text  name=title      Robot takeover
    Input Text  name=booktitle  Examples of robot takeovers
    Input Text  name=year       2077
    Input Text  name=publisher  Robots inc
    Input Text  name=pages      12-21
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

Modify Book With Key
    [Arguments]    ${citekey}    ${new_author}    ${new_editor}    ${new_title}
    ...            ${new_publisher}    ${new_year}    ${new_volume}    ${new_number}
    ...            ${new_urldate}   ${new_url}   ${new_tag}

    Go To  ${HOME_URL}

    Click Link  xpath=//tr[td[normalize-space()='${citekey}']]//a[normalize-space()='Modify']

    Input Text  name=citekey    ${citekey}
    Input Text  name=author     ${new_author}
    Input Text  name=editor     ${new_editor}
    Input Text  name=title      ${new_title}
    Input Text  name=publisher  ${new_publisher}
    Input Text  name=year       ${new_year}
    Input Text  name=volume     ${new_volume}
    Input Text  name=number     ${new_number}
    Input Text  name=urldate    ${new_urldate}
    Input Text  name=url        ${new_url}
    Input Text  name=tag        ${new_tag}

    Click Button  Edit

Modify Inproceeding With Key
    [Arguments]    ${citekey}    ${new_author}    ${new_editor}    ${new_title}
    ...            ${new_booktitle}    ${new_year}    ${new_publisher}
    ...            ${new_pages}    ${new_volume}    ${new_number}
    ...            ${new_urldate}   ${new_url}   ${new_tag}

    Go To  ${HOME_URL}

    Click Link  xpath=//tr[td[normalize-space()='${citekey}']]//a[normalize-space()='Modify']

    Input Text  name=citekey    ${citekey}
    Input Text  name=author     ${new_author}
    Input Text  name=editor     ${new_editor}
    Input Text  name=title      ${new_title}
    Input Text  name=booktitle  ${new_booktitle}
    Input Text  name=year       ${new_year}
    Input Text  name=publisher  ${new_publisher}
    Input Text  name=pages      ${new_pages}
    Input Text  name=volume     ${new_volume}
    Input Text  name=number     ${new_number}
    Input Text  name=urldate    ${new_urldate}
    Input Text  name=url        ${new_url}
    Input Text  name=tag        ${new_tag}

    Click Button  Edit
