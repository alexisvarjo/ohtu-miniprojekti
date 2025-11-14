*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Adding And Seeing An Article
    Add Article With Key  robot_deleting_robot
    Page Should Contain  robot_deleting_robot
    Delete Robot Sources
    Page Should Contain  Robot sources deleted