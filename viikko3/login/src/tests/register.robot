*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Registration Username  newuser
    Set Registration Password  kalle123
    Confirm Registration Password  kalle123
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

Register With Password Containing Numbers
    Set Registration Username  numberpassword
    Set Registration Password  kalle123
    Confirm Registration Password  kalle123
    Click  button >> text=Register
    Registration Should Succeed

Register With Password Containing Special Characters
    Set Registration Username  specialpassword
    Set Registration Password  kalle#abc
    Confirm Registration Password  kalle#abc
    Click  button >> text=Register
    Registration Should Succeed

Reject Password Containing Only Lowercase Letters
    Set Registration Username  lowercasepassword
    Set Registration Password  kallekalle
    Confirm Registration Password  kallekalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain a non-letter character

Reject Password Containing Only Uppercase And Lowercase Letters
    Set Registration Username  mixedcasepassword
    Set Registration Password  KalleKalle
    Confirm Registration Password  KalleKalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain a non-letter character

Register With Matching Password Confirmation
    Set Registration Username  matchingconfirmation
    Set Registration Password  kalle123
    Confirm Registration Password  kalle123
    Click  button >> text=Register
    Registration Should Succeed

Reject Registration With Mismatching Password Confirmation
    Set Registration Username  mismatchingconfirmation
    Set Registration Password  kalle123
    Confirm Registration Password  kalle124
    Click  button >> text=Register
    Registration Should Fail With Message  Passwords do not match

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

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
