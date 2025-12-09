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

Search By Material
    Go To    ${HOME_URL}

    Select From List By Value    id=material_type    article
    Select From List By Value    id=keyword          ${EMPTY}
    Input Text    name=minYear   ${EMPTY}
    Input Text    name=maxYear   ${EMPTY}
    Input Text    name=search    ${EMPTY}
    Click Button    Filter

    Page Should Contain  article
    Page Should Not Contain  book
    Page Should Not Contain  inproceeding


Search By Author
    Go To    ${HOME_URL}

    Select From List By Value    id=material_type    ${EMPTY}
    Select From List By Value    id=keyword          author
    Input Text    name=minYear   ${EMPTY}
    Input Text    name=maxYear   ${EMPTY}
    Input Text    name=search    Shoshichi Kobayashi
    Click Button    Filter

    Page Should Contain  Shoshichi Kobayashi
    Page Should Not Contain  Ölk
    Page Should Not Contain  joku

Search By Year
    Go To    ${HOME_URL}

    Select From List By Value    id=material_type    ${EMPTY}
    Select From List By Value    id=keyword          ${EMPTY}
    Input Text    name=minYear    1995
    Input Text    name=maxYear    2000
    Input Text    name=search     ${EMPTY}
    Click Button    Filter

    Page Should Contain  1995
    Page Should Contain  1996
    Page Should Contain  1997
    Page Should Contain  1998
    Page Should Contain  1999
    Page Should Contain  2000

    Page Should Not Contain  1994
    Page Should Not Contain  2001


Search By Keyword
    Go To    ${HOME_URL}

    Select From List By Value    id=material_type    ${EMPTY}
    Select From List By Value    id=keyword          ${EMPTY}
    Input Text    name=minYear   ${EMPTY}
    Input Text    name=maxYear   ${EMPTY}
    Input Text    name=search    Robotics
    Click Button    Filter

    Page Should Contain  Robotics
    Page Should Not Contain  joku
    Page Should Not Contain  lök
