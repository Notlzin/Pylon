# pylon2d - Notlzin's guide to the lightweight engine

welecome to **pylon2D**, a lightweight python-based 2D game engine (ofcourse its python)
This guide will help you set up and run pylon2d from scratch.
and note: this was copy pasted from GPT-5mini

---

## why pylon2d vro

- **Python-first:** Easy to use, no compilation needed.
- **2D engine:** Focused on simple games and experiments.
- **Lightweight:** Minimal dependencies, runs almost anywhere.

> the name comes from **“py” for python** + **“2d”**, since the original name was taken (bruh).

---

## prerequisites

before starting, make sure you have these:

- **Python 3.10+** installed: [Download Python here](https://www.python.org/downloads/)
- **pip** (comes with Python)

optional but recommended:

- **Virtual environment (venv)** for isolating dependencies
- **Git** if you want to clone the github repository

---

## schtep 1: clone the repo

open a terminal (whether its powershell or what) and run:

```bash
# do this first #
git clone https://github.com/Notlzin/Pylon
cd pylon2d
```

or install the zip from github and extract it via windows or WinRAR or whatever else

## schetp num 2: setup venv (optional... but why not)

reccomended (highly) to avoid any conflicts with your current python version

```bash
python -m venv venv
# activation: #
# windows #
venv\Scripts\activate
# macOS/linux #
source venv/bin/activate
```

## step-steps-stepss 3 (this is getting outta hand): dependencies

install any required python dependencies (aka packages):

```bash
pip install -r requirements.txt
```

if you dont have that, dont worry, pylon2d has barely any dependencies (pygame-only, well there is threading and pickle but uhhh who cares)

## step 4: running it

you can run the inbuilt demo in test folders (aka test/main.py) heres the tutorial:

```bash
python main.py
# or you can just do this #
python test/main.py
```

## step 5: start creating something

now since you have this, start making some stuff, you can fork this, or contribute some examples folder into this repository to show your games
