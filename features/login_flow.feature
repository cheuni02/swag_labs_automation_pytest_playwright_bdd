Feature: As a registered user
  I should be able to log on to the product browse
  Otherwise I'll be informed that I'm not

Scenario: Access granted as Legit user with correct password
  Given I am on the login page
  When I log on as "standard_user" with pw "secret_sauce"
  Then I should be taken to my product browse page
  And Be shown normal products

Scenario: Access Denied as Legit user with incorrect password
  Given I am on the login page
  When I log on as "standard_user" with pw "12345"
  Then I should see error "Username and password do not match any user in this service"

Scenario: Access Denied as Locked out user
  Given I am on the login page
  When I log on as "locked_out_user" with pw "secret_sauce"
  Then I should see error "Sorry, this user has been locked out."

