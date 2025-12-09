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

Title Keyword Filtering
    Add Article With Key    title_filtering_robot
    Sleep    ${DELAY}

    Select From List By Value    id=keyword    title
    Sleep    ${DELAY}

    Input Text    search    title_filtering_robot
    Sleep    ${DELAY}

    Click Button    Search
    Sleep    ${DELAY}

    Page Should Contain    title_filtering_robot

Tag Keyword Filtering
    Add Article With Key    tag_filtering_robot
    Sleep    ${DELAY}

    Select From List By Value    id=keyword    tag
    Sleep    ${DELAY}

    Input Text    search    tag
    Sleep    ${DELAY}

    Click Button    Search
    Sleep    ${DELAY}

    Page Should Contain    tag

Year Filtering
    Add Article With Key    year_filtering_robot
    Sleep    ${DELAY}

    Input Text    id=minYear    2066
    Sleep    ${DELAY}
    Input Text    id=maxYear    2068
    Sleep    ${DELAY}
    Click Button  Search
    Sleep    ${DELAY}

    Page Should Contain  year_filtering_robot