*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Delete Robot Sources
Test Teardown  Delete Robot Sources

*** Test Cases ***
Adding An Article With A DOI And Seeing It
    Input Text  name=doi  10.1038/nature11631
    Input Text  name=citekey  doi_article_robot
    Click Button  Add citation
    Page Should Contain  Citation added
    Go To  http://${SERVER}/remove_article/doi_article_robot
    Click Button  Confirm

#Adding A Book With A DOI And Seeing It
#    Input Text  name=doi  10.1007/978-3-031-45468-4
#    Input Text  name=citekey  doi_book_robot
#    Click Button  Add citation
#    Page Should Contain  Citation added
#    Go To  http://${SERVER}/remove_book/doi_book_robot
#    Click Button  Confirm

Adding An Inproceeding With A DOI And Seeing It
    Input Text  name=doi  10.1109/CVPR.2016.90
    Input Text  name=citekey  doi_inproceeding_robot
    Click Button  Add citation
    Page Should Contain  Citation added
    Go To  http://${SERVER}/remove_inproceeding/doi_inproceeding_robot
    Click Button  Confirm
