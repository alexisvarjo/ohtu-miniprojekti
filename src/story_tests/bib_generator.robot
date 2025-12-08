*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Bib Browser View
    Add Article With Key    bib_browser_robot
    Sleep    ${DELAY}
    Page Should Contain     bib_browser_robot

    Click Link    View bib in browser
    Sleep    ${DELAY}
    Page Should Contain     bib_browser_robot

Bib File Download
    Add Article With Key    bib_file_robot
    Sleep    ${DELAY}
    Page Should Contain     bib_file_robot

    Click Link    Download a .bib file
    Sleep    ${DELAY}
