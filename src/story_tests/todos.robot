THIS FILE ONLY INCLUDES ROBOT.TEST EXAMPLES
DON'T REMOVE THE COMMENTS!

#*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos
# reset todos is in resource.robot with the python function being in app.py

#*** Test Cases ***
At start there are no todos
    Go To  ${HOME_URL}
    Title Should Be  Todo app
    Page Should Contain  things still unfinished: 0

After adding a todo, there is one
    Go To  ${HOME_URL}
    Click Link  Create new todo
    Input Text  content  Buy milk
    Click Button  Create
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk

After adding two todos and marking one done, there is one unfinished
    Go To  ${HOME_URL}
    Click Link  Create new todo
    Input Text  content  Buy milk
    Click Button  Create
    Click Link  Create new todo
    Input Text  content  Clean house
    Click Button  Create
    Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk, done