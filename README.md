# Mazie AI Assistant

> A Python-based voice assistant that listens, understands, and responds through speech.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Speech Recognition](https://img.shields.io/badge/Speech%20Recognition-Enabled-blue)](https://pypi.org/project/SpeechRecognition/)
[![Text to Speech](https://img.shields.io/badge/Text%20to%20Speech-pyttsx3-orange)](https://pypi.org/project/pyttsx3/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## What is Mazie?

**Mazie** is a Python-based voice assistant project built to explore how speech recognition and voice-controlled automation can be combined into a simple desktop assistant.

The project works around four basic capabilities:

```text
🎙️ Listen
   ↓
🧠 Understand
   ↓
⚙️ Perform an action
   ↓
🔊 Respond
```

It is a hands-on project for learning how voice interfaces, speech recognition, text-to-speech, and automation can work together.

## Key Features

### 🎙️ Speech Recognition

Mazie can process spoken input using Python speech-recognition capabilities.

### 🔊 Text to Speech

The assistant can respond using generated speech through `pyttsx3`.

### 👂 Wake-Word Based Interaction

The project explores wake-word based interaction so that the assistant can be activated through voice.

### ⚙️ Voice-Controlled Automation

The assistant can connect spoken commands with programmed actions.

## Technology Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| 🐍 Python             | Main programming language |
| 🎙️ SpeechRecognition | Speech input              |
| 🔊 pyttsx3            | Text-to-speech            |
| 🖥️ Desktop Python    | Local assistant execution |

## How It Works

The basic interaction flow is:

```text
User speaks
     ↓
Microphone input
     ↓
Speech recognition
     ↓
Command interpretation
     ↓
Action
     ↓
Text-to-speech response
     ↓
User hears the response
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/akshatas28/Mazie_Ai_Assistant.git
```

### 2. Move into the project

```bash
cd Mazie_Ai_Assistant
```

### 3. Install dependencies

Install the required Python packages used by the project:

```bash
pip install SpeechRecognition pyttsx3
```

If additional dependencies are required by the current implementation, install them before running the assistant.

### 4. Run the assistant

```bash
python <main-file>.py
```

Replace `<main-file>.py` with the project's main Python file.

## Project Architecture

At a high level:

```text
                 ┌─────────────────┐
                 │      User       │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Microphone    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Speech          │
                 │ Recognition     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Command         │
                 │ Processing      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Action / Task   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Text to Speech  │
                 └────────┬────────┘
                          │
                          ▼
                       User
```

## What I Learned

This project helped explore practical concepts around:

* Python application development
* Speech recognition
* Text-to-speech systems
* Event-driven interaction
* Voice-based commands
* Desktop automation
* Connecting multiple Python libraries into one application

## Future Improvements

Possible areas for further development include:

* More reliable wake-word detection
* Better command classification
* More automation capabilities
* Improved error handling
* Configurable commands
* External API integrations
* More natural conversational interaction
* LLM-based command understanding

## Why I Built It

Mazie started as a hands-on way to understand how a voice-controlled application can be built using Python.

Rather than treating each library separately, the project brings them together into one working application.

## Related Work

I also work on Python, DSA, cloud, automation, and AI systems.(Along with multiple enterprise intergration platforms)

* [Advance Python](https://github.com/akshatas28/Advance_Python)
* [Java Problem Solving](https://github.com/akshatas28/java-problem-solving)
* [LeetCode Solutions](https://github.com/akshatas28/Leetcode_Solutions)
* [GitHub Profile](https://github.com/akshatas28)

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.

---

> Build something small. Understand how it works. Then make it better.
