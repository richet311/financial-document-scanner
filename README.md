# Financial Document Scanner

A privacy-first web app that reads financial documents (pay stubs, bank
statements, budget sheets) and turns them into plain-language budgeting
insights, without ever touching a real bank account.

> **Disclaimer:** This is an independent personal project. It is not
> affiliated with, endorsed by, or connected to any bank, credit union, or
> financial institution, and it does not connect to real accounts or real
> financial data. All sample documents used for development and demos are
> synthetic.

## Why this exists

Built as a portfolio project ahead of a fintech-focused, social-impact
hackathon application. It's meant to show secure full-stack development and
applied ML skills (OCR, model training, API security, real authentication
and per-account data), on a problem that's actually useful to nonprofits and
individuals working on financial literacy.

## What it does

1. A user uploads a sample financial document (image or PDF), signed in or
   not.
2. The backend extracts the text. Born-digital PDFs get their embedded text
   pulled directly; scanned PDFs and images fall back to OCR (EasyOCR).
3. A classifier (trained on a synthetic, self-generated dataset) labels the
   document type (pay stub, bank statement, budget sheet), and a rules-based
   engine pulls out key fields (income, expenses) and turns them into
   plain-language insights: withholding rate, savings rate, overspending
   warnings.
4. If the user is signed in, the result (document type, extracted fields,
   insights) is saved to their account. The original file itself is never
   stored, whether signed in or not.
5. Signed-in users get a Dashboard with a filterable scan history (by date
   range and document type) and two charts: scans over time and a breakdown
   by document type.

## Architecture

```
frontend/  Vue 3 + Vite SPA
   |
   |--- HTTPS, rate-limited, CORS-locked ---> backend/  FastAPI service
   |                                             - OCR + document classification
   |                                             - Insight engine
   |                                             - Verifies Supabase session tokens
   |                                             - Writes scan results on behalf of the user
   |
   `--- direct client queries (RLS-enforced) ---> Supabase
                                                     - Auth (email + password)
                                                     - Postgres (scan history)
```

FastAPI owns the document-processing pipeline and writes new scan rows.
The frontend talks to Supabase directly for sign-in/sign-up and for reading
and filtering scan history, since Postgres row-level security already
guarantees a user can only ever see their own rows.

## Tech stack

| Layer      | Choice                                      |
|------------|----------------------------------------------|
| Frontend   | Vue 3, Vite, plain JavaScript (no TypeScript) |
| Backend    | Python, FastAPI                               |
| Auth + database | Supabase (Postgres + email/password auth) |
| Rate limiting | `slowapi`                                   |
| OCR        | EasyOCR, PyMuPDF (for born-digital PDF text)  |
| Classifier | scikit-learn (TF-IDF + logistic regression)   |
| Synthetic data | Faker                                     |
| Hosting    | Render.com free tier, Supabase free tier      |

No paid or credit-card-gated cloud services are used anywhere in this
project.

## Security & privacy

- Rate limiting on every API route, keyed by client IP.
- CORS locked to an explicit allow list of origins.
- Uploaded files are validated by size and actual file signature, not just
  extension, and read in bounded chunks rather than all at once.
- The original file is never stored; only derived insights are kept, and
  only for signed-in users, scoped to their account by Postgres row-level
  security.
- Sign-in is handled entirely by Supabase; this app never sees or stores a
  password.
- Centralized error handling and structured logging.

See the in-app **Privacy** and **Terms** pages for the full, plain-language
policy.

## Getting started

### Prerequisites

- Python 3.13
- Node.js 20+
- A free [Supabase](https://supabase.com) project (for sign-in and scan
  history; the app still runs and scanning still works without one, just
  without accounts)

### Supabase setup (one-time)

1. Create a free project at [supabase.com](https://supabase.com).
2. In the SQL Editor, run `backend/supabase/schema.sql` once to create the
   `scans` table and its row-level security policies.
3. In **Settings -> API**, copy the Project URL and the `anon` public key.
   You'll need these for both `backend/.env` and `frontend/.env` below.

### Backend

```bash
cd backend
python -m venv .venv
./.venv/Scripts/activate      # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
cp .env.example .env           # then fill in SUPABASE_URL / SUPABASE_ANON_KEY
python -m app.ml.generate_dataset      # one-time: builds a synthetic training set
python -m app.ml.train_classifier      # one-time: trains and saves the classifier
python -m app.ml.generate_sample_pdfs  # one-time: writes sample PDFs for the frontend's Sample Documents page
uvicorn app.main:app --reload --port 8000
```

The API is now at `http://localhost:8000`, with a health check at
`GET /api/health`. On first startup it downloads the EasyOCR model weights
(a one-time download, needs internet access); after that they're cached
locally and startup is fast. If you skip the two `app.ml` commands, the API
still runs; document classification is just skipped (uploads still get text
extraction and field-based insights). If `SUPABASE_URL` / `SUPABASE_ANON_KEY`
are left blank, uploads still work anonymously; nothing is persisted.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env           # then fill in VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY
npm run dev
```

The app is now at the URL Vite prints (default `http://localhost:5173`).

## Testing

```bash
cd backend
pip install -r requirements-dev.txt
pytest -v
```

The suite mocks out OCR, the classifier, and Supabase at the route level, so
it runs in a couple of seconds with no network access, no EasyOCR model
download, and no live Supabase project required. It covers file validation,
the insight engine's field extraction and math, and the upload route's
happy path, its untrained-classifier fallback, and scan persistence for
signed-in users (including graceful degradation if the save itself fails).

A GitHub Actions workflow (`.github/workflows/ci.yml`) runs this test suite
and a frontend production build on every push and pull request against
`main`.

## Project structure

```
financial-document-scanner/
├── .github/workflows/ci.yml   test + build on every push/PR
├── backend/
│   ├── app/
│   │   ├── main.py           FastAPI app, middleware, error handlers
│   │   ├── core/              config, logging, security, deps (Supabase-verified auth)
│   │   ├── api/routes/        route handlers (health, documents)
│   │   ├── services/          OCR, classifier, insight engine, Supabase client, scan persistence
│   │   └── ml/                dataset generation, classifier training, sample PDFs
│   ├── supabase/schema.sql    one-time table + row-level security setup
│   ├── tests/                 pytest suite
│   ├── requirements.txt
│   └── requirements-dev.txt
├── frontend/
│   ├── public/samples/         generated sample PDFs (see backend/app/ml/generate_sample_pdfs.py)
│   ├── src/
│   │   ├── App.vue            top nav shell + router outlet
│   │   ├── router.js          vue-router routes, dashboard gated behind sign-in
│   │   ├── lib/supabaseClient.js  Supabase client init
│   │   ├── store/auth.js      shared Supabase session state
│   │   ├── pages/              Landing, Scan, Dashboard, Samples, Login, Privacy, Terms
│   │   └── components/        TopNav, UploadDropzone, ResultsPanel, ApiStatus
│   └── package.json
├── render.yaml                deployment blueprint
└── README.md
```

## Known limitations

- The classifier is trained entirely on synthetic, template-generated text,
  so it reports near-perfect accuracy on held-out synthetic data, which is
  easier than real-world documents; it hasn't been validated against
  real-world formatting variety.
- The insight engine matches a small, fixed set of field labels via keyword
  search (e.g. "gross income", "net pay"). Documents that phrase these
  differently won't have those fields extracted.
- Scanning without an account works, but nothing is saved; only signed-in
  scans are persisted.

## Roadmap

- [x] **Phase 1:** repo scaffold. FastAPI + Vue skeletons wired together,
      security middleware, README.
- [x] **Phase 2:** document upload endpoint with file validation and text
      extraction (direct text-layer extraction for born-digital PDFs, OCR
      fallback for scans and images).
- [x] **Phase 3:** synthetic dataset generation (Faker-based templates for
      pay stubs, bank statements, budget sheets) and a trained document-type
      classifier (TF-IDF + logistic regression, scikit-learn).
- [x] **Phase 4:** rules-based budgeting insight engine, upload results view.
- [x] **Phase 5:** pytest suite, GitHub Actions CI, and a Render deployment
      blueprint.
- [x] **Phase 6:** real accounts via Supabase auth, per-account scan history,
      and a filterable reports dashboard with charts.

## Deployment

`render.yaml` is a Render Blueprint defining both services (the FastAPI
backend and the static Vue frontend) on the free plan.

1. Push this repo to GitHub.
2. Set up a Supabase project as described above.
3. In Render, choose **New +** -> **Blueprint** and point it at the repo.
4. Deploy, then fill in `SUPABASE_URL` / `SUPABASE_ANON_KEY` (backend) and
   `VITE_SUPABASE_URL` / `VITE_SUPABASE_ANON_KEY` (frontend) from your
   Supabase project's API settings.
5. Once both services have their `onrender.com` URLs, set `ALLOWED_ORIGINS`
   on the backend to the frontend's URL, and `VITE_API_BASE_URL` on the
   frontend to the backend's URL, then redeploy both. Neither is known
   before the first deploy.

This hasn't been run against a live Render account, so treat it as a
starting point rather than a guaranteed one-shot deploy. EasyOCR pulls in
PyTorch, which has a real memory footprint that's untested against Render's
free-tier limit; the app is built to keep running (born-digital PDFs still
work) even if OCR itself can't load there.

## Emulating this project

Everything above is enough to clone this repo, install dependencies, create
your own free Supabase project, and run both services locally. Copy
`.env.example` to `.env` in both `backend/` and `frontend/` and fill in your
own Supabase project's URL and anon key. No paid services are required.

## License

MIT, see [LICENSE](LICENSE).
