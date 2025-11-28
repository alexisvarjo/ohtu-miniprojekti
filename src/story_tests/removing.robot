*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources
Test Teardown  Delete Robot Sources

*** Test Cases ***
Adding And Removing An Article
    Add Article With Key  article_removing_robot
    Page Should Contain  article_removing_robot
    Click Link  Remove
    Click Button  Confirm
    Page Should Not Contain  article_removing_robot

# Adding And Removing An Inproceeding
#    Add Article With Key  inproceeding_removing_robot
#    Page Should Contain  inproceeding_removing_robot
#    Click Link  Remove
#    Click Button  Confirm
#    Page Should Not Contain  inprocedding_removing_robot