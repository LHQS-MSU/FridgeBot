![Python](https://img.shields.io/badge/python-v3.9.12-brightgreen.svg)
![Static Badge](https://img.shields.io/badge/Fridge-BlueFors-orange)
![GitHub file size in bytes](https://img.shields.io/github/size/LHQS-MSU/FridgeBot/src/tester.py?color=pink)
[![pylint](https://img.shields.io/badge/PyLint-7.74-orange?logo=python&logoColor=white)
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

Niyaz created a telegram fridge bot a few years ago that was based request/response behavior. Users would message the bot and get details back. The difference in this project is a frequent eye on the fridge and a bot that will *initiate* alerts. It's still in development[^1].

[^1]: Contact Abby Peterson at pete1328@msu.edu or agirlpete01@gmail.com with any questions as she is the project developer.
