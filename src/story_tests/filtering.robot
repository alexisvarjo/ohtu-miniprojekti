*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Author Keyword Filtering
    Add Article With Key    author_filtering_robot
    Sleep    ${DELAY}

    Select From List By Value    id=keyword    author
    Sleep    ${DELAY}

    Input Text    search    robot
    Sleep    ${DELAY}

    Click Button    Search
    Sleep    ${DELAY}

    Page Should Contain    author_filtering_robot
