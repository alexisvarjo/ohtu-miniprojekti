*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Delete Robot Sources
Test Teardown    Delete Robot Sources

*** Test Cases ***
Adding And Modifying An Article
    Add Article With Key  article_modifying_robot
    Page Should Contain   article_modifying_robot

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

    Page Should Contain   robot
    Page Should Contain   1995
    Page Should Contain   new_title
    Page Should Contain   new_urldate
    Page Should Contain   new_url
    Page Should Contain   new_tag

Adding And Modifying An Inproceeding
    Add Inproceeding With Key  inproceeding_modifying_robot
    Page Should Contain   inproceeding_modifying_robot

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

    Page Should Contain   robot
    Page Should Contain   new_title
    Page Should Contain   1995
    Page Should Contain   new_urldate
    Page Should Contain   new_url
    Page Should Contain   new_tag