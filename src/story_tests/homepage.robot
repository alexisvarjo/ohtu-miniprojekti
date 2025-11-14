*** Settings ***

Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
The Homepage Opens
    Go To  ${HOME_URL}