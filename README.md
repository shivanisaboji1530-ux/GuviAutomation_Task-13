# Drag and Drop Automation Test

## Overview
This project automates the Drag and Drop functionality available on the jQuery UI Droppable page using Selenium WebDriver and Pytest.

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Chrome Browser

## Test Cases

### Positive Test
- Open the Drag and Drop page.
- Drag the source element to the target area.
- Verify the target text changes to "Dropped!".

### Negative Test
- Open the Drag and Drop page.
- Do not perform the drag-and-drop action.
- Verify the target text remains "Drop here".
