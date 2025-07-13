# ROTMG Daily Login Automation

Automate your daily login process for [Realm of the Mad God](https://www.realmofthemadgod.com/) to ensure you never miss your rewards.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project automates the daily login process for Realm of the Mad God using Python and GUI automation tools.

## Features

- Automates login to ROTMG
- Simulates user input for login credentials
- Optionally collects daily rewards
- Customizable timing and delays

## Requirements

- Python 3.x
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- (Optional) Other dependencies as needed

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/ROTMGDailyLoginAutomation.git
    ```
2. Install dependencies:
    ```sh
    pip install pyautogui
    ```

## Usage

1. Edit the script to add your login credentials and adjust screen coordinates if necessary.
2. Run the script:
    ```sh
    python main.py
    ```

## Configuration

- Update any hardcoded credentials or coordinates in [`main.py`](ROTMGDailyLoginAutomation/main.py).
- Adjust delays and timing as needed for your system.

## Troubleshooting

- Make sure ROTMG is installed and accessible.
- Ensure your screen resolution matches the script’s coordinates.
- Run the script with administrator privileges if needed.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

##