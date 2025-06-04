# Music Management System

This project is a Django-based Music Management System that allows users to upload, view, play, and delete songs. 

## Project Structure

```
music_management/
├── manage.py
├── music_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── music_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── song_list.html
│   │   └── add_song.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
│   └── songs/
└── README.md
```

## Features

- Upload and manage songs with title, artist, and audio file.
- View a list of all uploaded songs.
- Play audio files directly in the browser.
- Delete songs from the list.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd music_management
   ```

2. **Install dependencies:**
   Make sure you have Python and Django installed. You can install Django using pip:
   ```
   pip install django
   ```

3. **Run migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/` to start using the Music Management System.

## Usage

- To add a new song, navigate to the "Add New Song" link.
- Uploaded songs will be displayed in a list with playback controls.
- You can delete songs from the list as needed.

## License

This project is open-source and available under the MIT License.