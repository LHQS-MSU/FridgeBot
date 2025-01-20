![Python](https://img.shields.io/badge/python-v3.9.12-brightgreen.svg)
![Static Badge](https://img.shields.io/badge/Fridge-BlueFors-orange)
![GitHub file size in bytes](https://img.shields.io/github/size/LHQS-MSU/FridgeBot/src/fridge_bot.py?color=pink)
[![pylint](https://img.shields.io/badge/PyLint-9.25-brightgreen?logo=python&logoColor=white)
[![GitHub Workflow Status](https://github.com/LHQS-MSU/FridgeBot/actions/workflows/pylint.yml/badge.svg)](https://github.com/LHQS-MSU/FridgeBot/actions/workflows/pylint.yml)
![GitHub watchers](https://img.shields.io/github/watchers/LHQS-MSU/FridgeBot)


# Research Project: Fridge Alert System

## Telegram Bot for Blue Fors Fridge - LHQS Member Sign-up

The purpose of this research project is to figure out a secure way for our team members to know the status of the fridge. There have been multiple occurences where the experiment environment gets harmed due to fridge malfunctions, and we don't discover the issue until it's too late.

Thus the goal of a live alert system came to mind. The plan is to check 5 main values and communicate any crucial indicators.
1. Channel 6 - the mixing chamber, temperature
2. Pressure 1 - the vacuum can, for a potential leak
3. Pressure 3&4 - check points, to show any blocakge
4. Pressure 5 - if fridge turns off, to check on helium
5. Variables `cptempwi` & `cptempwo` - if compressor is on/off

### Set-up & Running

#### Telegram Bot

A telegram bot has already been created for this alert system. Username **@blueforsfridgebot** and the bot token (needed to run the program) can be obtained by asking the BotFather (on telegram) or [here](https://t.me/BotFather).

**Start the program** by running the `fridge_bot.py` file. On the Telegram app, the bot should then be responsive. 

#### Code Base

`.env` variables needed:
- BOT_TOKEN: the unique id for our telegram bot so the dispather can start accordingly
- MEMBER_KEY: the passcode users are prompted for when signing up for LHQS telebot access

The **current project status** includes a barebones functioning telebot for all basic and some unique commands (lined out in the [dev guide](https://docs.google.com/document/d/1Dpi2zN4I3fCP5sHKVMMZyGR-yxJY5q_uH7FWfOeb3ZE/edit?usp=sharing)) when chatting with it. The primary feature of `/startalerts` `/stopalerts` bot commands is fleshed out in theory. It is presently connected to the `CH6 T 23-12-05.log` file as a mock test of what live alerts will do.

**Future endeavors** should include getting this repo onto the local PC that the BlueFors Fridge log files are hosted on and redirecting the `main` function in `fridge_bot.py` to call `start_live_testing`. The `bluefors_comm.py` file is also barebones as there are 5 values to track and parsing all the related log files is not a completed process yet.

### Helpful Documents

The primary (past) developer has a few documents noting decisions, discovered tips and tool, as well as (wip) mapped out logic (like how to track the live logs, parse each file, etc.). This [master doc](https://docs.google.com/document/d/1Tnvajhkc5exuQpR9JwZRn7729LXOWxu3sriA_uIe6iQ/edit?usp=sharing) will connect users to all related files and priorly used tools.

## Background
Niyaz created a telegram fridge bot a few years ago that was based request/response behavior. Users would message the bot and get details back. The difference in this project is a frequent eye on the fridge and a bot that will *initiate* alerts. It has not gotten to the point of being deployed [^1].

[^1]: Contact Abby Peterson at pete1328@msu.edu or agirlpete01@gmail.com with any questions as she was the project developer.
