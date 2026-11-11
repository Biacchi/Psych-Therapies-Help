# Psych Therapies Help

A small Flask website that explains a handful of psychotherapy approaches (CBT, DBT, ACT, psychodynamic, ABA, systemic, humanistic and MBCT) and has a quick quiz that suggests which one might fit you. It is a learning project, so please do not treat it as medical advice.

## Why it exists

A web-dev practice project from my CS50x days. I wanted something with real pages, templates, a form and a bit of logic, and picked a topic I find interesting. The site text is in Brazilian Portuguese, the code is in English.

## How it works

- `/` shows the home page with one card per therapy.
- `/<therapy>` shows a page for each therapy (for example `/CBT`).
- `/survey` is a 10-question quiz (anxiety, depression, stress, trauma, relationships, self-esteem, anger, mood swings, grief, obsessions).
- `/submit` adds up the answers using a hand-made mapping from symptoms to therapies and shows the therapy with the highest score.

Answers are only used to compute the result in that request. Nothing is stored.

## How to run it

```bash
pip install -r requirements.txt
flask --debug run
```

Then open http://127.0.0.1:5000. There is also a `Procfile` (`gunicorn app:app`) for hosting platforms and a `.devcontainer` for GitHub Codespaces.

## What is in here

- `app.py`: the Flask app and the scoring logic
- `templates/`: Jinja templates, one per therapy plus home, survey and result
- `static/`: CSS and images
- `requirements.txt`, `Procfile`, `.devcontainer/`: setup and deploy files

## What I learned

Flask routing and Jinja templates, building a form-to-result flow, and that deciding which therapy is "best" with a few sums and a `max()` is very fun and also very much not how real clinicians do it.

## Heads-up

- The recommendation logic is a toy. For real mental health questions, talk to a licensed professional.
- No license file yet, so by default all rights are reserved.
- I have not run the app again after tidying the repo.
