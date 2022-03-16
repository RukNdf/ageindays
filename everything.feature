Feature: age in days
  Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

  Scenario Outline: Extract years, months, and days from days
    Given the person is <dayIn> days old
    When we calculate the date
    Then the result is <years> years <months> months <days> days
	Examples:
	| dayIn | years | months | days |
	|  400  | 	1 	|  	1    |	 5	|