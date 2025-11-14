*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Adding and seeing an article
    Go To  ${HOME_URL}
    Click Link  Add article
    Input Text  citekey  robot
    Input Text  author  John Doe
    Input Text  year  2011
    Input Text  name  Tehostettu kisällioppiminen
    Input Text  journal  Journal of Programming
    Input Text  volume  12
    Input Text  number  1
    Input Text  urldate  2025-11-13
    Input Text  url  http://example.com/vpl11
    Click Button  Create
    Page Should Contain  Source added successfully
    Page Should Contain  robot