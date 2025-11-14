*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Author keyword filtering
    Add Article With Key  author_filtering_robot
    Select From List By Label  id:keyword  Author
    Input Text  search  robots
    Click Button  Search
    Page Should Contain  author_filtering_robot