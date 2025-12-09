*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser

*** Test Cases ***
The Homepage Opens
    Sleep    ${DELAY}
    Go To    ${HOME_URL}
    Sleep    ${DELAY}
