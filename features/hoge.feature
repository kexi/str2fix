Feature: convert_with_x
  Scenario: 全て半角
    Given I initialize a values with "hoge",10.
    Then It returns "hoge      ".
  Scenario: 全て全角
    Given I initialize a values with "ホゲ",10.
    Then It returns "ﾎｹﾞ       ".
  Scenario: オーバーフロー
    Given I initialize a values with "hogehogehogehoge",10.
    Then It returns "hogehogeho".
  Scenario: オーバーフロー
    Given I initialize a values with "hogehogehogehoge",10.
    Then It returns "hogehogeho".