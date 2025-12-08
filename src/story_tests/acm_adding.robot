*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Adding An Article With An ACM Link And Seeing It
    Input Text    id=acm_url       https://dl.acm.org/doi/10.1145/3710912
    Input Text    id=acm_citekey   acm_article_robot
    Sleep    ${DELAY}

    Click Button    id=acm_add
    Sleep    ${DELAY}
    Page Should Contain    Citation added

    Go To    http://${SERVER}/remove_article/acm_article_robot
    Sleep    ${DELAY}
    Click Button    Confirm
    Sleep    ${DELAY}

Adding An Inproceeding With An ACM Link And Seeing It
    Input Text    id=acm_url       https://dl.acm.org/doi/10.1145/2380552.2380613
    Input Text    id=acm_citekey   acm_inproceeding_robot
    Sleep    ${DELAY}

    Click Button    id=acm_add
    Sleep    ${DELAY}
    Page Should Contain    Citation added

    Go To    http://${SERVER}/remove_inproceeding/acm_inproceeding_robot
    Sleep    ${DELAY}
    Click Button    Confirm
    Sleep    ${DELAY}
