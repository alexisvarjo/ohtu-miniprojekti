*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Delete Robot Sources

*** Test Cases ***
Adding And Modifying An Article
    Add Article With Key  modifying_robot
    Page Should Contain   modifying_robot

    Modify Article With Key
    ...    modifying_robot
    ...    robot
    ...    1995
    ...    new_title
    ...    new_journal
    ...    new_volume
    ...    new_number
    ...    new_urldate
    ...    new_url

    Page Should Contain   robot
    Page Should Contain   1995
    Page Should Contain   new_title
    Page Should Contain   new_journal
    Page Should Contain   new_volume
    Page Should Contain   new_number
    Page Should Contain   new_urldate
    Page Should Contain   new_url
