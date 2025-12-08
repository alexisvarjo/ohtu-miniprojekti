*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Delete Robot Sources
Test Teardown     Delete Robot Sources

*** Test Cases ***
Adding And Seeing An Article
    Add Article With Key    article_adding_and_seeing_robot
    Sleep    ${DELAY}
    Page Should Contain     article_adding_and_seeing_robot

Adding And Seeing A Book
    Add Book With Key    book_adding_and_seeing_robot
    Sleep    ${DELAY}
    Page Should Contain     book_adding_and_seeing_robot

Adding And Seeing An Inproceeding
    Add Inproceeding With Key    inproceeding_adding_and_seeing_robot
    Sleep    ${DELAY}
    Page Should Contain     inproceeding_adding_and_seeing_robot
