*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources

*** Test Cases ***
Bib Browser View
    Add Article With Key  bib_browser_robot
    Page Should Contain  bib_browser_robot
    Click Link  View bib in browser
    Page Should Contain  bib_browser_robot

Bib File Download
    Add Article With Key  bib_file_robot
    Page Should Contain  bib_file_robot
    Click Link  Download a .bib file