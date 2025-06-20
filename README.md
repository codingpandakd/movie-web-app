# 🎬 Movie Night Organizer 🍿

Welcome to the **Movie Night Organizer**! This is a simple yet powerful Flask-based web application designed tohelp you and your friends keep track of movies you want to watch. Create user profiles, build personalized movie lists, and easily manage your movie-watching journey.

Say goodbye to scattered notes and forgotten film recommendations!

## ✨ Features

*   👤 **User Profiles:** Create separate profiles for different users.
*   📝 **Personalized Movie Lists:** Each user can maintain their own list of movies.
*   ➕ **Add Movies:** Easily add new movies to your list by title.
*   👀 **View Movies:** See all the movies a user has added.
*   ✏️ **Update Movies:** Correct or change movie titles in your list.
*   🗑️ **Delete Movies:** Remove movies you've watched or no longer want in your list.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.12 or higher
*   `uv` (Python package installer and virtual environment manager)
    *   You can install `uv` by following the official instructions: [https://github.com/astral-sh/uv#installation](https://github.com/astral-sh/uv#installation)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd MovieWebApps
    ```
    *(Replace `<YOUR_REPOSITORY_URL>` with the actual URL of this repository)*

2.  **Create a virtual environment and install dependencies using `uv`:**
    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```
    *(Note: If a `requirements.txt` is not present, you can generate one from `pyproject.toml` or install dependencies directly. For this project, based on `pyproject.toml` and `uv.lock`, using `uv pip install -r requirements.txt` after generating it or `uv pip install flask flask-sqlalchemy python-dotenv requests` should work. For simplicity, we'll assume a `requirements.txt` might be used or generated. If not, the direct install is the way.)*

    Alternatively, to install directly from `pyproject.toml` (if `uv` supports it directly in your version, or by converting `pyproject.toml` to `requirements.txt` first):
    ```bash
    # Ensure your uv version supports this or generate requirements.txt first
    # uv pip install .
    ```

3.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

4.  **Initialize the Database:**
    The application uses Flask-SQLAlchemy. The database will be created automatically when you first run the application, as per the `db.create_all()` command in `app.py`.

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will start on `http://0.0.0.0:5000/` (or `http://localhost:5000/`).

## 📖 Usage

Once the application is running, open your web browser and navigate to `http://localhost:5000/`.

*   **Homepage (`/`):** Displays the list of existing users and a form to create new users.
*   **User Creation:** Enter a username in the form on the homepage and submit to create a new user.
*   **Movie Lists (`/users/<user_id>/movies`):**
    *   Click on a username or navigate directly to see a user's movie list.
    *   Here you can add new movies for that user.
    *   Existing movies will be listed with options to update their titles or delete them.
*   **Adding a Movie:** On a user's movie page, type the movie title in the form and submit.
*   **Updating a Movie:** Click the "Update" button next to a movie, enter the new title, and submit.
*   **Deleting a Movie:** Click the "Delete" button next to a movie to remove it from the list.

## 🛠️ Technology Stack

*   🐍 **Python:** The core programming language.
*   <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original-wordmark.svg" alt="Flask" width="50" height="50"/> **Flask:** A micro web framework for Python.
*   💾 **SQLAlchemy (Flask-SQLAlchemy):** For database interaction (using SQLite).
*   📄 **HTML & CSS:** For structuring and styling the web pages.
*   📦 **uv:** For Python packaging and virtual environment management.
*   📝 **python-dotenv:** For managing environment variables.

## 📸 Screenshots

*(Optional: It's highly recommended to add a few screenshots of the application in action here. For example, the main user page, a user's movie list, etc. This will help users quickly understand what your application looks like.)*

**Example Placeholder:**

<!--
![User List Page](path/to/your/screenshot_user_list.png)
*Caption: Main page showing the list of users.*

![Movie List Page](path/to/your/screenshot_movie_list.png)
*Caption: A user's movie list with options to add, update, or delete movies.*
-->

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to fork the repository and submit a pull request. You can also open an issue if you find a bug or want to propose a new feature.

1.  **Fork the Project**
2.  **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3.  **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4.  **Push to the Branch** (`git push origin feature/AmazingFeature`)
5.  **Open a Pull Request**

## 📜 License

This project is currently unlicensed.

It is recommended to choose an open-source license and add a `LICENSE` file to your project. Common choices include:
*   [MIT License](https://opensource.org/licenses/MIT)
*   [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)
*   [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)

Once you've added a `LICENSE` file, you can update this section to reflect it, for example:

`Distributed under the MIT License. See `LICENSE` for more information.`
