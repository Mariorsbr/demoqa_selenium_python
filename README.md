# Selenium Test Automation Framework with Python, Behave, and Page Object Model (POM)

This project demonstrates a basic structure for automating web tests using:
- **Selenium WebDriver**
- **Python 3**
- **Behave (BDD)**
- **Page Object Model (POM)** design pattern

---

## 📁 Project Structure

<pre>
├── features/
│ ├── steps/
│ │ └── step_example.py
├── ui/
│ │ └── example.feature
├── pages/
│ └── home_page.py
└── README.md  
</pre>

##🧪 Running Tests

To run all tests using Behave:

<pre>behave</pre>

To run a specific scenario by name:

<pre>behave -n "Scenario Name"</pre>

## 📄 Sample Feature File

<pre>
Feature: Open the home page

  Scenario: Validate the page title
    Given I am on the home page
    Then the page title should be "My Website"
</pre>

## 🔗 References  
<ul>
  <li><a href="https://selenium-python.readthedocs.io/">Selenium with Python Docs</a></li>
  <li><a href="https://behave.readthedocs.io/en/latest/tutorial/#features">Behave Documentation</a></li>
  <li><a href="https://cucumber.io/docs/gherkin/" >Gherkin Syntax Guide</a></li>
</ul>
