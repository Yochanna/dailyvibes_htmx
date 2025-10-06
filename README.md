# Yochanna To-Do App

A beautiful, minimal to-do list application built with Django and HTMX.

## Features

- ✨ Add tasks instantly
- ✅ Mark tasks as done
- 🎨 Clean, modern UI with pink theme
- ⚡ Fast, reactive updates with HTMX (no page reloads!)
- 📱 Fully responsive design

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTMX + Vanilla CSS
- **Database**: PostgreSQL (production) / SQLite (local dev)
- **Deployment**: Render.com ready

## Local Development

### Prerequisites

- Python 3.11+
- pip

### Setup

1. **Clone or extract the project**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## Deploy to Render.com

This app is **turnkey ready** for Render.com deployment!

### Option 1: Deploy via Blueprint (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Go to Render Dashboard**
   - Visit [render.com](https://render.com)
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and set everything up!

3. **Wait for deployment**
   - Render will create both the web service and PostgreSQL database
   - Your app will be live in a few minutes

### Option 2: Manual Deploy

1. **Create a new Web Service**
   - Go to Render Dashboard
   - Click "New" → "Web Service"
   - Connect your repository

2. **Configure the service**
   - **Name**: yochanna-todo-app
   - **Runtime**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn myproject.wsgi:application`

3. **Create a PostgreSQL database**
   - Click "New" → "PostgreSQL"
   - **Name**: yochanna-todo-db
   - Copy the Internal Database URL

4. **Add environment variables**
   - `SECRET_KEY`: (generate a random string)
   - `DEBUG`: False
   - `DATABASE_URL`: (paste the database URL from step 3)

5. **Deploy!**

### Post-Deployment

After deployment, your app will be available at:
```
https://yochanna-todo-app.onrender.com
```

The first deployment may take 5-10 minutes. Subsequent deploys are faster!

## Project Structure

```
myproject/
├── manage.py
├── requirements.txt
├── render.yaml          # Render.com blueprint
├── build.sh            # Build script
├── Procfile            # Process file
├── .gitignore
├── myproject/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── yochanna/           # Main app
    ├── models.py       # Task model
    ├── views.py        # HTMX views
    ├── urls.py
    ├── templates/      # HTML templates
    │   ├── home.html
    │   └── partials/
    │       └── task_list.html
    └── static/
        └── css/
            └── style.css
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Auto-generated on Render |
| `DEBUG` | Debug mode | `False` in production |
| `DATABASE_URL` | PostgreSQL connection string | Auto-set by Render |
| `ALLOWED_HOSTS` | Allowed hostnames | Auto-configured |

## Troubleshooting

### Local Development Issues

**Database errors?**
```bash
python manage.py migrate --run-syncdb
```

**Static files not loading?**
```bash
python manage.py collectstatic
```

### Render Deployment Issues

**Build failing?**
- Check the build logs in Render dashboard
- Ensure `build.sh` has execute permissions

**App not loading?**
- Check environment variables are set correctly
- Verify DATABASE_URL is connected
- Check the service logs

## License

MIT License - feel free to use this project however you'd like!

## Support

For issues or questions, please open an issue on GitHub.

---

Built with ❤️ using Django + HTMX
