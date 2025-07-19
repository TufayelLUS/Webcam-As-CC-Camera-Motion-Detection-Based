# Webcam As CC Camera Motion Detection Based
This piece of code is based on opencv that detects human movement within the camera frame, just like a CC camera, and to save memory, it records only the movement situation. Make your webcam a cc camera in no time with this!

# Intro
This simple tool watches your webcam and **automatically records when it detects human movement**. It captures:

- **5 seconds before movement**
- **Until movement stops**
- **Plus 10 seconds after the last movement**

All recordings are saved in a folder named **videos**. You can customize the time inside the code base settings.

---

## ✅ Installation (Windows, Mac, Linux)

### 1. Install Python
If you don't have Python yet, download it from:  
👉 https://www.python.org/downloads/

Make sure to select **"Add Python to PATH"** during installation.

### 2. Download the Project
- Click the **"Code"** button on this page and select **Download ZIP**
- Extract the ZIP file

### 3. Install Requirements
Open your terminal or command prompt inside the project folder, then run:

```
pip install opencv-python
```

### 4. Run the Program
In the terminal, run:

```
python camera.py
```

---

## 🎥 Output
- Videos will be saved automatically in a folder named **videos** in the same location.

---

## ❌ Stop Anytime
- Press **`q`** on the window to stop the program.

---

## ℹ️ Notes
- Works with your laptop webcam or any connected camera.
- No technical knowledge needed.
