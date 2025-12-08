*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Adding And Removing An Article
    Add Article With Key    article_removing_robot
    Sleep    ${DELAY}
    Page Should Contain     article_removing_robot

    Go To    ${VIEW_URL}/article_removing_robot
    Sleep    ${DELAY}

    Click Button    Delete
    Sleep    ${DELAY}

    Click Button    Confirm
    Sleep    ${DELAY}

    Page Should Not Contain    article_removing_robot

Adding And Removing A Book
    Add Book With Key    book_removing_robot
    Sleep    ${DELAY}
    Page Should Contain     book_removing_robot

    Go To    ${VIEW_URL}/book_removing_robot
    Sleep    ${DELAY}

    Click Button    Delete
    Sleep    ${DELAY}

    Click Button    Confirm
    Sleep    ${DELAY}

    Page Should Not Contain    book_removing_robot

Adding And Removing An Inproceeding
    Add Inproceeding With Key    inproceeding_removing_robot
    Sleep    ${DELAY}
    Page Should Contain     inproceeding_removing_robot

    Go To    ${VIEW_URL}/inproceeding_removing_robot
    Sleep    ${DELAY}

    Click Button    Delete
    Sleep    ${DELAY}

    Click Button    Confirm
    Sleep    ${DELAY}

    Page Should Not Contain    inproceeding_removing_robot
