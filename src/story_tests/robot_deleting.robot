*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Robot Article Source Deleting
    Add Article With Key  robot_article_deleting_robot
    Page Should Contain  robot_article_deleting_robot
    Delete Robot Sources
    Page Should Contain  Robot sources deleted

Robot Book Source Deleting
    Add Article With Key  robot_book_deleting_robot
    Page Should Contain  robot_book_deleting_robot
    Delete Robot Sources
    Page Should Contain  Robot sources deleted

Robot Inproceeding Source Deleting
    Add Article With Key  robot_inproceeding_deleting_robot
    Page Should Contain  robot_inproceeding_deleting_robot
    Delete Robot Sources
    Page Should Contain  Robot sources deleted