
#!/bin/sh
# start.sh

# install crontab (already in base image, but ensure)
service cron start || true

# install crontab file (copy cron/2fa-cron into crontab)
if [ -f /app/cron/2fa-cron ]; then
  crontab /app/cron/2fa-cron || true
fi

# start uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
