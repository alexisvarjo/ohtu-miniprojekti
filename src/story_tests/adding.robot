*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources
Test Teardown  Delete Robot Sources

*** Test Cases ***
Adding And Seeing An Article
    Add Article With Key  adding_and_seeing_robot
    Page Should Contain  adding_and_seeing_robot