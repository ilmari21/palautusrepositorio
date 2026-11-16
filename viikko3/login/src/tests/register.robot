*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Registration Username  newuser
    Set Registration Password  password
    Confirm Registration Password  password
    Click  button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Registration Username  ne
    Set Registration Password  password
    Confirm Registration Password  password
    Click  button >> text=Register
    Registration Should Fail

Register With Valid Username And Too Short Password
    Set Registration Username  newuser
    Set Registration Password  passw
    Confirm Registration Password  passw
    Click  button >> text=Register
    Registration Should Fail

Register With Username That Is Already In Use
    Set Registration Username  kalle
    Set Registration Password  password
    Confirm Registration Password  password
    Click  button >> text=Register
    Registration Should Fail

*** Keywords ***
Set Registration Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Registration Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Confirm Registration Password
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Registration Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Registration Should Fail
    Register Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
