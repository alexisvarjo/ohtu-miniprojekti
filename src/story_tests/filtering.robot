*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources
Test Teardown  Delete Robot Sources

*** Test Cases ***
Author Keyword Filtering
    Add Article With Key  author_filtering_robot
    Select From List By Label  id:keyword  Author
    Input Text  search  robot
    Click Button  Search
    Page Should Contain  author_filtering_robot