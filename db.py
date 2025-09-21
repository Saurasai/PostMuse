import sqlite3
import os
from passlib.context import CryptContext
import streamlit as st
import logging

logger = logging.getLogger(__name__)

DB_PATH = "data/users.db"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def init_db():
    logger.info("Initializing database")
    try:
        os.makedirs("data", exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                api_calls INTEGER NOT NULL DEFAULT 0
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS scheduled_posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                platform TEXT NOT NULL,
                content TEXT NOT NULL,
                schedule_time TEXT NOT NULL
            )
        """)
        conn.commit()
        logger.debug("Database tables created successfully")
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        st.error(f"Database initialization error: {e}")
        raise
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def add_user(email: str, password: str, role="user"):
    logger.info(f"Attempting to add user: {email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        hashed = pwd_context.hash(password)
        c.execute("INSERT INTO users (email, password, role) VALUES (?, ?, ?)", (email, hashed, role))
        conn.commit()
        logger.debug(f"User {email} added successfully")
        return True
    except sqlite3.IntegrityError:
        logger.warning(f"User {email} already exists")
        return False
    except sqlite3.Error as e:
        logger.error(f"Database error during user addition: {e}")
        st.error(f"Database error during user addition: {e}")
        return False
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def verify_user(email: str, password: str):
    logger.info(f"Verifying user: {email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE email = ?", (email,))
        row = c.fetchone()
        if row and pwd_context.verify(password, row[0]):
            logger.debug(f"User {email} verified successfully")
            return True
        logger.warning(f"Invalid credentials for user: {email}")
        return False
    except sqlite3.Error as e:
        logger.error(f"Database error during user verification: {e}")
        st.error(f"Database error during user verification: {e}")
        return False
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def get_user_role(email: str):
    logger.info(f"Fetching role for user: {email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE email = ?", (email,))
        row = c.fetchone()
        role = row[0] if row else None
        logger.debug(f"User {email} role: {role}")
        return role
    except sqlite3.Error as e:
        logger.error(f"Database error fetching user role: {e}")
        st.error(f"Database error fetching user role: {e}")
        return None
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def get_api_calls(email: str):
    logger.info(f"Fetching API calls for user: {email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT api_calls FROM users WHERE email = ?", (email,))
        row = c.fetchone()
        calls = row[0] if row else 0
        logger.debug(f"API calls for {email}: {calls}")
        return calls
    except sqlite3.Error as e:
        logger.error(f"Database error fetching API call count: {e}")
        st.error(f"Database error fetching API call count: {e}")
        return 0
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def increment_api_calls(email: str):
    logger.info(f"Incrementing API calls for user: {email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE users SET api_calls = api_calls + 1 WHERE email = ?", (email,))
        conn.commit()
        logger.debug(f"API calls incremented for {email}")
    except sqlite3.Error as e:
        logger.error(f"Database error incrementing API call count: {e}")
        st.error(f"Database error incrementing API call count: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def schedule_post(user_email, platform, content, schedule_time):
    logger.info(f"Scheduling post for user: {user_email}, platform: {platform}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT INTO scheduled_posts (user_email, platform, content, schedule_time) VALUES (?, ?, ?, ?)",
            (user_email, platform, content, schedule_time)
        )
        conn.commit()
        logger.debug(f"Post scheduled successfully for {user_email} on {platform} at {schedule_time}")
    except sqlite3.Error as e:
        logger.error(f"Database error scheduling post: {e}")
        st.error(f"Database error scheduling post: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def get_user_scheduled_posts(user_email):
    logger.info(f"Fetching scheduled posts for user: {user_email}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "SELECT id, platform, content, schedule_time FROM scheduled_posts WHERE user_email = ? ORDER BY schedule_time",
            (user_email,)
        )
        posts = c.fetchall()
        logger.debug(f"Retrieved {len(posts)} scheduled posts for {user_email}")
        return posts
    except sqlite3.Error as e:
        logger.error(f"Database error fetching scheduled posts: {e}")
        st.error(f"Database error fetching scheduled posts: {e}")
        return []
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")

def delete_scheduled_post(post_id):
    logger.info(f"Deleting scheduled post with ID: {post_id}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM scheduled_posts WHERE id = ?", (post_id,))
        conn.commit()
        logger.debug(f"Scheduled post {post_id} deleted successfully")
    except sqlite3.Error as e:
        logger.error(f"Database error deleting scheduled post: {e}")
        st.error(f"Database error deleting scheduled post: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            logger.warning("Failed to close database connection")