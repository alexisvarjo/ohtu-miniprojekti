*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Adding and seeing an article
    Add Article With Key  adding_and_seeing_robot
    Page Should Contain  adding_and_seeing_robot