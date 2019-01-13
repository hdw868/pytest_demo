Feature: Outline

  Scenario Outline: Outlined given, when, then
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers

    Examples: Vertical
      | start | 12 | 2 | 3 |
      | eat   | 5  | 1 | 0 |
      | left  | 7  | 1 | 3 |