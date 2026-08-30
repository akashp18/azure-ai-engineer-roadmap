# Module 01: Python for AI Engineering

This module covers the core Python programming skills necessary to build and troubleshoot AI applications using the Azure SDK. It is split into **Part 1 (Basics)** and **Part 2 (Advanced)**.

---

## Part 1: The Basics (Completed)

*The foundation of Python programming.*

**Skills learned:** Variables, Data Structures (Lists/Dicts), Loops, Control Flow, Basic Functions, and JSON/REST APIs via the `requests` library.

**Milestone Project:** Expense Tracker CLI (Completed)

---

## Part 2: Advanced Python for Azure SDKs

*These concepts are required to write robust, production-level code using Microsoft's Azure SDKs and OpenAI client libraries.*

### 📚 Learning Resources

- **Object-Oriented Programming (OOP):** [Python Classes and Objects (Corey Schafer)](https://www.youtube.com/watch?v=ZDa-Z5JzLm)
- **Error Handling:** [Python Try Except (W3Schools)](https://www.w3schools.com/python/python_try_except.asp)
- **Environment Variables:** [python-dotenv documentation](https://pypi.org/project/python-dotenv/)
- **Asynchronous Programming:** [Asyncio in Python - A Complete Tutorial (Real Python)](https://realpython.com/async-io-python/)

### 💻 Practice Exercises

*Complete these exercises in your local repository under `01-python/exercises/`*

1. **OOP Basics:** Create a Python class that acts as a blueprint for a user profile. Give it methods to update data.
2. **Environment Variables:** Install `python-dotenv`, create a `.env` file, and write a script that securely reads a mock API key from the environment.
3. **Async / Await:** Write an asynchronous function that uses `asyncio.sleep` to simulate a network call to the Azure OpenAI service.
4. **Error Handling:** Wrap a piece of API calling code in a `try/except` block that specifically catches network timeout errors.

### 🛠️ Advanced Milestone Project: Async Weather & API Client

Build a command-line application that:
- Uses `python-dotenv` to securely load a mock API key from a `.env` file.
- Uses `asyncio` and `aiohttp` to make 3 concurrent (parallel) API requests to a mock endpoint.
- Uses a `WeatherClient` **Class** to manage the state and requests.
- Implements robust `try/except` error handling if the API is down.
