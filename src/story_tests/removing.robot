*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources

*** Test Cases ***
Adding And Removing An Article
    Add Article With Key  removing_robot
    Page Should Contain  removing_robot
    Click Link  Remove
    Click Button  Confirm
    Page Should Not Contain  removing_robot
