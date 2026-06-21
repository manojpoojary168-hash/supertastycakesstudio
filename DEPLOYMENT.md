# Deployment Guide — Super Tasty Cakes Studio on Render

Deploy the Django app with Postgres, WhiteNoise (static files), and Cloudinary (media uploads).

---

## Prerequisites

- [Render](https://render.com) account (free tier works)
- [Cloudinary](https://cloudinary.com) account (free tier works)
- Git repository pushed to GitHub/GitLab

---

## 1. Cloudinary setup

1. Sign in at [cloudinary.com](https://cloudinary.com).
2. Open the **Dashboard**.
3. Copy:
   - **Cloud name** → `CLOUDINARY_CLOUD_NAME`
   - **API Key** → `CLOUDINARY_API_KEY`
   - **API Secret** → `CLOUDINARY_API_SECRET`

These are required in production — the app will not start without them.

---

## 2. Deploy with Render Blueprint (recommended)

1. Push this repo to GitHub/GitLab.
2. In Render: **New → Blueprint**.
3. Connect the repository — Render reads `render.yaml`.
4. After the blueprint is created, open the **Web Service → Environment** and set:

   | Variable | Example |
   |----------|---------|
   | `ALLOWED_HOSTS` | `super-tasty-cakes.onrender.com` |
   | `CSRF_TRUSTED_ORIGINS` | `https://super-tasty-cakes.onrender.com` |
   | `CLOUDINARY_CLOUD_NAME` | your cloud name |
   | `CLOUDINARY_API_KEY` | your API key |
   | `CLOUDINARY_API_SECRET` | your API secret |

   `SECRET_KEY`, `DATABASE_URL`, and `DJANGO_SETTINGS_MODULE` are set by the blueprint.

5. Click **Manual Deploy → Deploy latest commit** (or wait for auto-deploy).

---

## 3. Manual Render setup (alternative)

### Web Service

| Setting | Value |
|---------|-------|
| Runtime | Python 3 |
| Build Command | `./build.sh` |
| Start Command | `gunicorn config.wsgi --log-file -` |

### Postgres

1. **New → PostgreSQL** (free plan).
2. Copy the **Internal Database URL**.
3. Add it as `DATABASE_URL` on the Web Service.

### Environment variables (Web Service)

Set every variable from `.env.example`:

```
DJANGO_SETTINGS_MODULE=config.settings.production
SECRET_KEY=<generate-a-strong-random-key>
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com
DATABASE_URL=<from Render Postgres>
CLOUDINARY_CLOUD_NAME=<from Cloudinary>
CLOUDINARY_API_KEY=<from Cloudinary>
CLOUDINARY_API_SECRET=<from Cloudinary>
DEFAULT_WHATSAPP_NUMBER=919075075993
```

**Important:** `CSRF_TRUSTED_ORIGINS` must include the `https://` prefix.

---

## 4. What `build.sh` does

With `DJANGO_SETTINGS_MODULE=config.settings.production`:

1. Installs dependencies from `requirements.txt`
2. Runs `collectstatic` → WhiteNoise serves CSS/JS from `staticfiles/`
3. Runs `migrate` → applies migrations to Postgres

---

## 5. Post-deploy setup

Open the Render **Shell** for your web service:

```bash
# Create admin user for Smita
python manage.py createsuperuser

# Optional: load sample catalogue data
python manage.py load_sample_data --flush
```

Then in the browser:

1. Visit `https://your-app.onrender.com/admin/`
2. Log in and upload real cake/gallery/hero images (stored on Cloudinary)
3. Submit a test **Custom Cake Request** on the live site to confirm CSRF works

---

## 6. Configuration reference

### WhiteNoise (static files)

- Middleware: `WhiteNoiseMiddleware` (after `SecurityMiddleware`)
- Storage: `whitenoise.storage.CompressedManifestStaticFilesStorage`
- Build step: `collectstatic` in `build.sh`

### Cloudinary (media uploads)

- Storage: `cloudinary_storage.storage.MediaCloudinaryStorage`
- Config: `CLOUDINARY_STORAGE` in `config/settings/base.py`
- Used for: cake images, gallery images, hero image, custom cake reference uploads

### Security (production)

- `DEBUG=False`
- HTTPS redirect enabled
- HSTS enabled
- Secure session and CSRF cookies
- `CSRF_TRUSTED_ORIGINS` for HTTPS form POSTs

---

## 7. Troubleshooting

| Problem | Fix |
|---------|-----|
| `DisallowedHost` | Add Render URL to `ALLOWED_HOSTS` |
| 403 on custom cake form | Set `CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com` |
| Static CSS/JS 404 | Check build logs — `collectstatic` must succeed |
| Admin upload fails | Verify all three Cloudinary env vars |
| Database errors | Confirm `DATABASE_URL` is linked and migrations ran |
| `ImproperlyConfigured` Cloudinary | Set `CLOUDINARY_*` env vars on Render |

---

## 8. Custom domain (optional)

1. Add custom domain in Render → Web Service → Settings.
2. Update environment variables:
   ```
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-app.onrender.com
   CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com,https://your-app.onrender.com
   ```
3. Redeploy.
