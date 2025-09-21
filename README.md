Pose Muse ✨
Pose Muse is a Streamlit-based web application 🚀 for creating and scheduling platform-specific social media posts 📱. It supports Twitter, LinkedIn, and Instagram, with features for user authentication 🔒, draft generation ✍️, post scheduling ⏰, and a powerful admin panel 🛠️ for managing users and posts.
Table of Contents 📑

Features 🌟
Installation 🛠️
Usage 📖
Database Structure 🗄️
Admin Panel 🔧
File Structure 📂
Dependencies 📦
Logging 📜
Contributing 🤝
License 📄

Features 🌟

🔒 User Authentication: Secure login and registration with email and password, using bcrypt for password hashing.
✍️ Draft Generation: Generate platform-specific posts for Twitter, LinkedIn, and Instagram based on user inputs (topic, hashtags, insight, tone).
⏰ Post Scheduling: Schedule posts for specific platforms and times (login required).
🛠️ Admin Panel: Full CRUD operations for managing users and scheduled posts, accessible only to admin users.
📊 API Call Limits: 
Free users: 5 calls per session.
Registered users: 10 calls.
Admins: Unlimited calls.


📥 Download Drafts: Export generated drafts as a CSV file.
📜 Logging: Comprehensive logging for debugging and monitoring.

Installation 🛠️

Clone the Repository 📥:
git clone https://github.com/your-username/pose-muse.git
cd pose-muse


Set Up a Virtual Environment 🐍 (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies 📦:
pip install -r requirements.txt


Run the Application 🚀:
streamlit run app.py

The app will be available at http://localhost:8501 🌐.


Usage 📖

Access the App 🌐:

Open the application in a web browser.
Use as a free user (limited to 5 API calls per session) or log in/register for more features.


Login/Register 🔒:

Login: Use email and password.
Register: Create a new account with an email and password.


Generate Drafts ✍️:

Enter a topic, optional Twitter hashtags, LinkedIn insight/story, and select a tone.
Click "Generate All Drafts" to create platform-specific posts.
Edit drafts, copy to clipboard, or schedule them for posting.


Schedule Posts ⏰:

Log in to schedule posts.
Select a date and time for each draft.
View and delete scheduled posts in the "Scheduled Posts" tab.


Admin Panel 🛠️ (Admin Users Only):

Access the admin panel via the expandable section in the main UI.
Create: Add new users with email, password, and role.
Read: View all users (email, role, API calls) and scheduled posts.
Update: Modify user roles and API call counts.
Delete: Remove users (and their scheduled posts) or individual scheduled posts.



Database Structure 🗄️
The application uses SQLite for data storage in data/users.db. Two tables are created:

users:

id: Integer, primary key, auto-increment.
email: Text, unique, not null.
password: Text, hashed with bcrypt, not null.
role: Text, either 'user' or 'admin', default 'user'.
api_calls: Integer, tracks API usage, default 0.


scheduled_posts:

id: Integer, primary key, auto-increment.
user_email: Text, references user’s email, not null.
platform: Text, target platform (e.g., Twitter, LinkedIn), not null.
content: Text, post content, not null.
schedule_time: Text, ISO format datetime (UTC), not null.



A default admin account (email: admin, password: pass99()) is created during database initialization.
Admin Panel 🔧
The admin panel is accessible only to users with the 'admin' role. It provides:

➕ Create User:
Form to add new users with email, password, and role (user or admin).


📋 Manage Users:
Table displaying all users’ email, role, and API call count.
Update user role or API calls via a dropdown and input field.
Delete users (except the current admin’s own account), which also removes their scheduled posts.


📅 Manage Scheduled Posts:
Table showing all scheduled posts with post ID, user email, platform, content, and scheduled time.
Delete any scheduled post by entering its ID.



File Structure 📂

app.py: Main Streamlit application handling UI, authentication, draft generation, scheduling, and admin panel.
db.py: Database management with SQLite, including user authentication, post scheduling, and CRUD operations.
config.py: Configuration file for prompt templates and tone options (not included in this doc but referenced).
api.py: API functions for generating platform-specific drafts (not included in this doc but referenced).
data/users.db: SQLite database file (created automatically).
requirements.txt: List of Python dependencies.

Dependencies 📦

streamlit: For the web interface.
sqlite3: For database operations (included in Python standard library).
passlib: For bcrypt password hashing.
pandas: For CSV export of drafts.
asyncio: For asynchronous draft generation.
streamlit-lottie and streamlit-components: For UI enhancements.
logging: For application logging.

Install dependencies with:
pip install streamlit passlib pandas streamlit-lottie streamlit-components

Logging 📜
The application uses Python’s logging module to log events:

ℹ️ Info: General operations (e.g., rendering UI, login attempts).
🐛 Debug: Detailed success messages (e.g., user added, drafts generated).
⚠️ Warning: Non-critical issues (e.g., invalid credentials, user already exists).
❌ Error: Critical issues (e.g., database errors, generation failures).

Logs are useful for debugging and monitoring application behavior.
Contributing 🤝

Fork the repository 🍴.
Create a new branch (git checkout -b feature/your-feature).
Make changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request 📬.

Please ensure code follows PEP 8 style guidelines and includes appropriate logging.
License 📄
This project is licensed under the MIT License. See the LICENSE file for details.
