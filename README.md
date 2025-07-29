# Imperial College London Santander Cycles Availability Siri Shortcut

## 📖 Introduction

This project is a simple but powerful automation that allows you to ask Siri for the real-time availability of Santander Cycles, specifically for Imperial. It uses a Python script, hosted on an iPhone, to fetch live data from the Transport for London (TfL) feed and provides an immediate, spoken response.

It contains two scripts that are hard-coded to detect the bike availability and empty dock availability at the Huxely, RSM, and main entrance to Imperial College London.


---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Core Libraries:** `requests`, `xml.etree.ElementTree`
* **Platform:** Apple iOS
* **Tools:** a-Shell, Siri Shortcuts
* **API:** Transport for London (TfL) Live Cycle Hire XML Feed

---

## ✨ Key Features

* **Hands-Free Activation:** Get bike availability just by asking Siri.
* **Real-Time Data:** Fetches live data directly from TfL's feed, which updates every minute.
* **Specific & Focused:** Reports the number of available bikes/e-bikes or empty docks for stations near Imperial.
* **Voice Feedback:** Siri reads the results aloud, making it perfect for when you're on the go.

---

## 🚀 The Process

The project started with a desire to get cycle hire information quickly.

1.  **Initial Idea:** The first approach considered using the official TfL API with an API key but shifted towards using the public XML feed for a simpler, key-less implementation.
2.  **Script Development:** A Python script was written to fetch the XML data using the `requests` library and parse it with the built-in `xml.etree.ElementTree` to find the target station's data.
3.  **Mobile Environment:** The `a-Shell` app was chosen to run the Python script on the iPhone.
4.  **Integration Challenges:** The biggest hurdles involved making the Siri Shortcut correctly execute the script.
    * **File Not Found Error:** The script worked in `a-Shell` but not via Shortcuts. This was solved by using the script's full, absolute path in the shortcut command.
    * **Siri Silence:** Siri would run the shortcut but not speak the result. This was fixed by replacing the `Speak Text` action with the more robust `Stop and Output` action.
5.  **Version Control:** After setting up a Git repository, I noticed a huge number of changed files. I learned that the Python virtual environment (`venv`) was being tracked, and fixed this by adding it to a `.gitignore` file.

---

## 🎓 Lessons Learned

* **Siri's Output Mechanism:** For a shortcut to reliably speak a result when activated by voice, `Stop and Output` is the correct action to use. It formally hands the final text back to Siri.
* **The Importance of `.gitignore`:** Virtual environments and cache folders (`venv`, `__pycache__`) should never be committed to a Git repository. They are specific to a local machine and bloat the project.
* **Mobile Scripting is Viable:** With tools like a-Shell, it's entirely possible to build and run powerful automations directly on an iPhone.

---

## 📈 Areas for Improvement

* **Dynamic Station Selection:** Allow the user to ask for any station by name, rather than using a hardcoded one in the script.
* **Robust Error Handling:** Add logic to handle cases where the iPhone is offline or the TfL feed is unavailable.
* **Nearest Station Finder:** Instead of a fixed station, the script could use the phone's location to find the nearest N stations and report their status.

---

## ⚙️ Running the Project

**Prerequisites:**
* An iPhone
* The [a-Shell](https://apps.apple.com/us/app/a-shell/id1473805438) app installed.

There are two files, empty-imperial

**Setup Instructions:**
1.  **Save the Script:** Send the python code to your iPhone (via airdrop or email). Open files on your iPhone and move the python script to the 'a-Shell' folder.
2.  **Find the Full Path:** In a-Shell, run the `pwd` command to get the absolute path to your home directory.
3.  **Create the Shortcut:**
    * Open the **Shortcuts** app and create a new shortcut.
    * Add the **"Run command in a-Shell"** action.
    * In the command field, type `python` followed by the full path to your script (e.g., `python /private/var/mobile/Containers/Data/Application/'some long id'/Documents/;your_script_name'.py`).
    * Add the **"Speak Text"** action. It will automatically receive the script's result and speak the text aloud.
    * Give the shortcut a memorable name that you will say to Siri.
    * You can also add a block that sets the volume 

---

## 🎤 Demo

To run the project, simply activate Siri and say the name of your shortcut.

> "Hey Siri, imperial"

Siri will then execute the script and reply with:

> "Huxley bike station has 1 bikes with 1 being ebikes!"
> "RSM bike station has 1 bikes with 0 being ebikes!"
> "Main entrance bike station has 0 bikes with 0 being ebikes!"

Or checking how empty the bike docks are:

> "Hey Siri, empty imperial"

> "Huxley bike station has 19 empty docks!"
> "RSM bike station has 17 empty docks!"
> "Main entrance bike station has 19 empty docks!"
