*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Adding And Modifying An Article
    Add Article With Key    article_modifying_robot
    Sleep    ${DELAY}
    Page Should Contain     article_modifying_robot

    Modify Article With Key
    ...    article_modifying_robot
    ...    robot
    ...    1995
    ...    new_title
    ...    new_journal
    ...    10
    ...    2
    ...    new_urldate
    ...    new_url
    ...    new_tag
    Sleep    ${DELAY}

    Page Should Contain    robot
    Page Should Contain    1995
    Page Should Contain    new_title
    Page Should Contain    new_tag

Adding And Modifying A Book
    Add Book With Key    book_modifying_robot
    Sleep    ${DELAY}
    Page Should Contain    book_modifying_robot

    Modify Book With Key
    ...    book_modifying_robot
    ...    robot
    ...    new_editor
    ...    new_title
    ...    new_publisher
    ...    1995
    ...    10
    ...    2
    ...    new_urldate
    ...    new_url
    ...    new_tag
    Sleep    ${DELAY}

    Page Should Contain    robot
    Page Should Contain    new_title
    Page Should Contain    1995
    Page Should Contain    new_tag

Adding And Modifying An Inproceeding
    Add Inproceeding With Key    inproceeding_modifying_robot
    Sleep    ${DELAY}
    Page Should Contain    inproceeding_modifying_robot

    Modify Inproceeding With Key
    ...    inproceeding_modifying_robot
    ...    robot
    ...    new_editor
    ...    new_title
    ...    new_booktitle
    ...    1995
    ...    new_publisher
    ...    new_pages
    ...    10
    ...    2
    ...    new_urldate
    ...    new_url
    ...    new_tag
    Sleep    ${DELAY}

    Page Should Contain    robot
    Page Should Contain    new_title
    Page Should Contain    1995
    Page Should Contain    new_tag
