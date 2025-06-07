# 🚗 Concurrent Drive-Thru Simulation

A Python-based concurrent programming project that simulates cars going through a fast food drive-thru. It uses `ThreadPoolExecutor` to model multiple lanes operating in parallel.

## 🎯 Features

- 🚘 Simulates 10 cars arriving at a drive-thru
- 🍔 Randomized food orders (e.g., Burger, Fries, Nuggets)
- ⏱ Real-time logs with timestamps
- 🧠 Demonstrates concurrent programming using `concurrent.futures.ThreadPoolExecutor`
- 💡 Object-Oriented Design with a `Car` class

## 🧪 How It Works

Each car:
1. Arrives at the drive-thru
2. Orders food (random)
3. Pays
4. Picks up the order and leaves

Three drive-thru lanes are open concurrently, allowing multiple cars to be processed at once.

## 🔧 Requirements

- Python 3.6+
- No external libraries needed (uses only the standard library)

## 🚀 Running the Simulation

python drive_thru.py

## 📝 Example Output

[12:01:23] CAR-1 - arrived and ordering Burger
[12:01:23] CAR-2 - arrived and ordering Nuggets
[12:01:23] CAR-3 - arrived and ordering Salad
...

## 📚 Learning Purpose

This project demonstrates how to use concurrency in Python to simulate real-world systems like multi-lane drive-thrus. Great for understanding how tasks can run in parallel using threads.

## 📁 File Overview

File	Description
drive_thru.py	Main simulation script
README.md	This documentation file

Made with ☕ and Python by Ashley
