# YouTube Videos Manager (SQLite)

## Description  
A simple Python-based CLI application that helps you manage a collection of YouTube videos locally. You can **list**, **add**, **update**, and **delete** videos, all stored in a persistent **SQLite3** database.

---

## Features

- List all saved YouTube videos in a table-like format  
- Add new videos with title and duration  
- Update existing video information using video ID  
- Delete videos using their ID  
- Data stored persistently in a `youtube.db` SQLite database  
- Simple and clean CLI-based UI with smooth transitions

---

## How It Works

- All videos are stored in the `videos` table inside `youtube.db`.
- The app presents a menu-driven interface using the terminal.
- Uses `os`, `time`, and `getpass` for better UX and cleaner console flow.
- Includes duplicate-checking and ID-based validation to ensure reliability.

---

## Run It Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abishbaig/youtube-manager-sqlite3.git
   cd youtube-videos-manager-sqlite
