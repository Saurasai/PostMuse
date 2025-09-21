# Pose Muse ✨

**Pose Muse** is a Streamlit-based web application 🚀 for creating and scheduling platform-specific social media posts 📱. It supports Twitter, LinkedIn, and Instagram, with features for user authentication 🔒, draft generation ✍️, post scheduling ⏰, and a powerful admin panel 🛠️ for managing users and posts.

---

## Table of Contents 📑

1. [Features 🌟](#features-)
2. [Installation 🛠️](#installation-)
3. [Usage 📖](#usage-)
4. [Database Structure 🗄️](#database-structure-)
5. [Admin Panel 🔧](#admin-panel-)
6. [File Structure 📂](#file-structure-)
7. [Dependencies 📦](#dependencies-)
8. [Logging 📜](#logging-)
9. [Contributing 🤝](#contributing-)
10. [License 📄](#license-)

---

## Features 🌟

- 🔒 **User Authentication**: Secure login and registration with email and password, using bcrypt for password hashing.
- ✍️ **Draft Generation**: Generate platform-specific posts for Twitter, LinkedIn, and Instagram based on user inputs (topic, hashtags, insight, tone).
- ⏰ **Post Scheduling**: Schedule posts for specific platforms and times (login required).
- 🛠️ **Admin Panel**: Full CRUD operations for managing users and scheduled posts, accessible only to admin users.
- 📊 **API Call Limits**:  
  - Free users: 5 calls per session.  
  - Registered users: 10 calls.  
  - Admins: Unlimited calls.
- 📥 **Download Drafts**: Export generated drafts as a CSV file.
- 📜 **Logging**: Comprehensive logging for debugging and monitoring.

---

## Installation 🛠️

### Clone the Repository 📥

```bash
git clone https://github.com/your-username/pose-muse.git
cd pose-muse
````

### Set Up a Virtual Environment 🐍 (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies 📦

```bash
pip install -r requirements.txt
```

### Run the Application 🚀

```bash
streamlit run app.py
```

Open your browser and navigate to [http://localhost:8501](http://localhost:8501) 🌐.

---

## Usage 📖

### Access the App 🌐

* Open the application in a web browser.
* Use as a free user (limited to 5 API calls per session) or log in/register for more features.

### Login/Register 🔒

* **Login:** Use email and password. 
* **Register:** Create a new account with an email and password.

### Generate Drafts ✍️

* Enter a topic, optional Twitter hashtags, LinkedIn insight/story, and select a tone.
* Click **"Generate All Drafts"** to create platform-specific posts.
* Edit drafts, copy to clipboard, or schedule them for posting.

### Schedule Posts ⏰

* Log in to schedule posts.
* Select a date and time for each draft.
* View and delete scheduled posts in the **Scheduled Posts** tab.

### Admin Panel 🛠️ (Admin Users Only)

* Access the admin panel via the expandable section in the main UI.
* **Create:** Add new users with email, password, and role.
* **Read:** View all users (email, role, API calls) and scheduled posts.
* **Update:** Modify user roles and API call counts.
* **Delete:** Remove users (and their scheduled posts) or individual scheduled posts.

---

## Database Structure 🗄️

The application uses SQLite for data storage in `data/users.db`. Two tables are created:

### users:

| Column     | Type    | Description                              |
| ---------- | ------- | ---------------------------------------- |
| id         | Integer | Primary key, auto-increment              |
| email      | Text    | Unique, not null                         |
| password   | Text    | Hashed with bcrypt, not null             |
| role       | Text    | Either 'user' or 'admin', default 'user' |
| api\_calls | Integer | Tracks API usage, default 0              |

### scheduled\_posts:

| Column         | Type    | Description                                         |
| -------------- | ------- | --------------------------------------------------- |
| id             | Integer | Primary key, auto-increment                         |
| user\_email    | Text    | References user’s email, not null                   |
| platform       | Text    | Target platform (Twitter, LinkedIn, etc.), not null |
| content        | Text    | Post content, not null                              |
| schedule\_time | Text    | ISO format datetime (UTC), not null                 |

A default admin account is created during database initialization.

---

## Admin Panel 🔧

Accessible only to users with the **admin** role:

* ➕ **Create User:** Form to add new users with email, password, and role (user or admin).
* 📋 **Manage Users:**

  * View all users’ email, role, and API call count.
  * Update user roles and API calls via dropdown/input fields.
  * Delete users (except current admin’s own account), which also removes their scheduled posts.
* 📅 **Manage Scheduled Posts:**

  * View all scheduled posts (ID, user email, platform, content, scheduled time).
  * Delete posts by entering their ID.

---

## File Structure 📂

```
app.py               # Main Streamlit app (UI, auth, draft gen, scheduling, admin)
db.py                # SQLite DB management, authentication, CRUD ops
config.py            # Configuration for prompts and tones (referenced)
api.py               # API functions for draft generation (referenced)
data/users.db        # SQLite database (auto-created)
requirements.txt     # Python dependencies
```

---

## Dependencies 📦

* `streamlit` — web interface
* `sqlite3` — database operations (Python stdlib)
* `passlib` — bcrypt password hashing
* `pandas` — CSV export of drafts
* `asyncio` — asynchronous draft generation
* `streamlit-lottie` and `streamlit-components` — UI enhancements
* `logging` — application logging

Install dependencies with:

```bash
pip install streamlit passlib pandas streamlit-lottie streamlit-components
```

---

## Logging 📜

The app uses Python’s `logging` module:

* ℹ️ **Info:** General operations (e.g., UI rendering, login attempts)
* 🐛 **Debug:** Detailed success messages (e.g., user added, drafts generated)
* ⚠️ **Warning:** Non-critical issues (e.g., invalid credentials, user already exists)
* ❌ **Error:** Critical issues (e.g., database errors, generation failures)

Useful for debugging and monitoring application behavior.

---

## Contributing 🤝

1. Fork the repository 🍴.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Make changes and commit:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request 📬.

Please follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines and include appropriate logging.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

```
