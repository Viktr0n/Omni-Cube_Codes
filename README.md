# Omni-Cube

## Project Overview

The Omni-Cube is a gaming console with an omnidirectional Andotrope display. It is a final thesis project for upper secondary school that addresses the challenge of restricted viewing angles in traditional multiplayer gaming by providing a 360-degree display experience.

This repository contains the codes used in this project. For the 3D models, please go to this repo:
https://github.com/Kingfisk/Omni-Cube_3DModels 

## Hardware Components

- **Main Console**: Raspberry Pi 3 Model B running CircuitPython
- **Display**: RA8875 omnidirectional display with 360-degree image capability
- **Controllers**: Two handheld wireless controllers built with ESP32/ESP32-S3 using Bluetooth Low Energy (BLE)
- **Motor Control**: H-bridge controlled DC motor for display rotation
- **Chassis**: Custom 3D-printed PLA housing designed in Fusion 360

## Software Structure

- **OC_splashscreen.py** - Splash screen with project title and creator credits
- **OC_main_menu.py** - Main menu system with game selection and power control
- **OC_pong.py** - Pong game implementation with BLE controller support
- **OC_motorCode.py** - Motor control via PWM and GPIO
- **OC_controller_plr1.ino & OC_controller_plr2.ino** - Wireless controller firmware with BLE communication

## Features

- **Dual Wireless Controllers** - D-pad and A/B button inputs for two players
- **BLE Connectivity** - Seamless Bluetooth Low Energy communication between controllers and console
- **Power Management** - Automatic deep sleep modes after 2 minutes of inactivity
- **Expandable Game Architecture** - Easy-to-extend system for adding new games beyond Pong
- **Omnidirectional Display** - 360-degree viewing experience for multiplayer gaming

## Getting Started

The User_manual describes how to start the project, how to maneuver the main menu and the controlls for the Pong game. If you want to add more of your own games to the project, step-by-step instructions are also included in the User_manual

## Authors

- Oscar Bodenäs
- Victor Ekberg

## Technologies

- CircuitPython
- C++ (Arduino)
- Bluetooth Low Energy (BLE)
- RA8875 Display Controller
- Raspberry Pi GPIO Control
