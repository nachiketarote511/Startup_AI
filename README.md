# AI Startup Intelligence Platform

A complete full-stack AI-powered startup analysis and intelligence platform combining React frontend, FastAPI backend, and multiple machine learning models.

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (React + TypeScript)           │
│  ├─ Dashboard & Analytics                                   │
│  ├─ Startup Analysis & Search                               │
│  ├─ AI Score Visualizations                                 │
│  └─ What-If Simulator                                       │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP API (React Query)
┌──────────────────────▼──────────────────────────────────────┐
│                  FastAPI Backend (Python)                    │
│  ├─ Model Loading & Caching (Singleton)                     │
│  ├─ Score Prediction Endpoints                              │
│  ├─ Search & Filtering                                      │
│  └─ CORS Middleware for frontend integration                │
└──────────────────────┬──────────────────────────────────────┘
                       │ joblib/pickle
┌──────────────────────▼──────────────────────────────────────┐
│              ML Models & Data Layer                          │
│  ├─ 16+ Trained ML Models                                   │
│  ├─ Startup CSV Dataset (50,000 records)                    │
│  └─ Feature Encoders & Scalers                              │
└─────────────────────────────────────────────────────────────┘
```

## 📋 Project Structure

```
k:\AI_Startup_Intelligence\
├── frontend/                           # React + TypeScript frontend
│   ├── src/
│   │   ├── lib/
│   │   │   ├── api-client.ts          # NEW: API client with React Query hooks
│   │   │   ├── mock-data.ts           # Mock data (fallback)
│   │   │   └── utils.ts
│   │   ├── routes/
│   │   │   ├── index.tsx              # Dashboard (updated with API)
│   │   │   ├── startup-analysis.tsx   # NEW: Full analysis page
│   │   │   ├── explorer.tsx           # Startup explorer
│   │   │   ├── simulator.tsx          # What-If simulator
│   │   │   └── [other pages].tsx
│   │   ├── components/
│   │   ├── __root__.tsx
│   │   └── server.ts
│   ├── package.json
│   ├── .env                           # NEW: Backend API URL config
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── backend/                           # NEW: FastAPI backend
│   ├── app.py                         # Main FastAPI application
│   ├── config.py                      # Configuration & model paths
│   ├── models_cache.py                # Singleton model loader
│   ├── repositories.py                # Data access layer (CSV)
│   ├── services.py                    # Business logic & predictions
│   ├── schemas.py                     # Pydantic request/response models
│   ├── routes/
│   │   ├── analysis.py                # Analysis endpoints
│   │   └── health.py                  # Health check endpoints
│   ├── requirements.txt               # Python dependencies
│   ├── .env                           # Backend environment config
│   └── .env.example
│
├── models/                            # Pre-trained ML models
│   ├── success_model/                 # Success probability prediction
│   ├── health_model/                  # Startup health scoring
│   ├── risk_model/                    # Risk assessment
│   ├── founder_strength_model/        # Founder evaluation
│   ├── funding_strength_model/        # Capital & runway analysis
│   ├── market_opportunity_model/      # Market potential
│   ├── growth_potential_model/        # Growth trajectory
│   ├── innovation_assessment_model/   # Technology & IP scoring
│   ├── competition_analysis_model/    # Competitive positioning
│   ├── recommendation_model/          # AI recommendations
│   ├── investor_model/                # Investor readiness
│   ├── startup_clustering_engine/     # Startup clustering
│   ├── knowledge_graph_engine/        # Knowledge graph
│   ├── market_gap_engine/             # Market gap detection
│   └── [other engines]
│
├── datasets/
│   ├── cleaned/
│   │   └── startup_info.csv           # Main dataset (50,000 startups, 155 features)
│   └── raw/
│
├── notebooks/                         # Jupyter notebooks for model development
│   ├── 01_data_collection.ipynb
│   ├── 05_success_prediction.ipynb
│   ├── 06_risk_analysis.ipynb
│   └── [other analysis notebooks]
│
├── start-backend.bat                  # Windows batch script to run backend
└── README.md                          # This file
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ (for frontend)
- **Python** 3.11+ (for backend)
- **Windows** (for batch scripts) or adjust shell commands for Linux/Mac

### 1. Setup Backend

```bash
# Navigate to project root
cd k:\AI_Startup_Intelligence

# Option A: Using batch script (Windows)
start-backend.bat

# Option B: Manual setup
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Backend will start on **http://localhost:8000**

### 2. Setup Frontend

```bash
# In a new terminal, from project root
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend will start on **http://localhost:5173**

### 3. Verify Integration

- Open http://localhost:5173 in browser
- Navigate to "Startup Analysis" page
- Search for a startup (e.g., "HyperAnalytics")
- View AI-driven scores and recommendations

## 🔌 API Endpoints

### Health & Info
- `GET /api/health` - Health check with models status
- `GET /api/models` - List loaded models
- `GET /api/info` - API information

### Startup Analysis
- `GET /api/analyze/startup/{name}` - Full analysis
- `GET /api/analyze/startup/{name}/health` - Health score
- `GET /api/analyze/startup/{name}/success` - Success probability
- `GET /api/analyze/startup/{name}/risk` - Risk assessment
- `GET /api/analyze/startup/{name}/scores` - All scores

### Search & Discovery
- `GET /api/analyze/startups/search?q=query&limit=50` - Search startups
- `GET /api/analyze/sectors` - Get all sectors
- `GET /api/analyze/stats` - Dataset statistics

## 🧠 AI Models Integrated

| Model | Purpose | Input Features | Output |
|-------|---------|---|---|
| Success Model | Success probability prediction | 12 features | High/Medium/Low (confidence) |
| Health Model | Startup health assessment | 10 features | High/Medium/Low |
| Risk Model | Risk evaluation | 10 features | High/Medium/Low |
| Founder Strength | Team evaluation | 10 features | High/Medium/Low |
| Funding Strength | Capital & runway | 9 features | High/Medium/Low |
| Market Opportunity | Market potential | 8 features | High/Medium/Low |
| Growth Potential | Growth trajectory | 8 features | High/Medium/Low |
| Innovation | Tech & IP strength | 6 features | High/Medium/Low |
| Competition | Competitive positioning | 8 features | High/Medium/Low |
| + 7 more engines | Clustering, recommendations, knowledge graph, etc. | Various | Various |

## 📊 Frontend Features

### Pages Integrated with Backend

1. **Dashboard** (`/`) - Overview with statistics
2. **Startup Analysis** (`/startup-analysis`) - NEW - Search and analyze startups
3. **Explorer** (`/explorer`) - Browse all startups with sorting
4. **Success Prediction** (`/success-prediction`) - Success scores
5. **Failure Risk** (`/failure-risk`) - Risk assessment
6. **Investor Readiness** (`/investor-readiness`) - Investment readiness
7. **Startup Health** (`/startup-health`) - Health metrics
8. **Founder Strength** (`/founder-strength`) - Team evaluation
9. **Funding Strength** (`/funding-strength`) - Capital analysis
10. **Market Opportunity** (`/market-opportunity`) - Market analysis
11. **Growth Potential** (`/growth-potential`) - Growth forecasts
12. **Innovation** (`/innovation`) - Tech scoring
13. **Competition** (`/competition`) - Competitive analysis
14. **Recommendations** (`/recommendations`) - AI recommendations
15. **What-If Simulator** (`/simulator`) - Parameter simulation
16. **Competitors** (`/competitors`) - Competitor discovery
17. **Market Gap** (`/market-gap`) - Market gap analysis
18. **Startup Clustering** (`/clustering`) - Clustering analysis
19. **Knowledge Graph** (`/knowledge-graph`) - Relationship mapping

## 🔐 Environment Configuration

### Frontend (`.env`)
```env
# Backend API URL
VITE_API_URL=http://localhost:8000
```

### Backend (`.env`)
```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# CORS (for frontend)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Database (future MongoDB integration)
MONGODB_URL=mongodb://localhost:27017
DB_NAME=ai_startup_intelligence
```

## 📦 Frontend Dependencies

- **React 19** - UI framework
- **TypeScript 5** - Type safety
- **TanStack Router** - Routing
- **React Query 5** - Server state management & API calls
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization
- **Lucide React** - Icons
- **Shadcn UI** - Component library

## 🐍 Backend Dependencies

- **FastAPI 0.104** - Web framework
- **Uvicorn 0.24** - ASGI server
- **Pydantic 2.5** - Data validation
- **Pandas 2+** - Data processing
- **Scikit-learn 1.5.2** - ML models
- **Joblib 1.3** - Model serialization
- **Python-dotenv** - Environment management

## 🔄 Data Flow

### Example: Analyzing a Startup

1. **User Action** (Frontend)
   - User types "TechCorp" in search box
   - Clicks search or presses Enter

2. **API Request** (Frontend → Backend)
   ```javascript
   GET /api/analyze/startups/search?q=TechCorp&limit=50
   ```

3. **Backend Processing**
   - Loads startup CSV from disk
   - Filters by name/sector
   - Returns matching records

4. **User Selection** (Frontend)
   - User clicks "TechCorp AI" from results
   - Triggers full analysis query

5. **Comprehensive Analysis** (Backend)
   - Loads 16+ ML models from disk (cached)
   - Extracts required features for each model
   - Runs predictions through scikit-learn models
   - Compiles scores and recommendations
   - Returns JSON response

6. **UI Rendering** (Frontend)
   - React Query caches response
   - Displays scores, charts, recommendations
   - Enables real-time filtering

## 🧪 Testing the Integration

### Via Backend API (curl)

```bash
# Health check
curl http://localhost:8000/api/health

# Search startups
curl "http://localhost:8000/api/analyze/startups/search?q=neural&limit=10"

# Analyze specific startup
curl http://localhost:8000/api/analyze/startup/HyperAnalytics%20Technologies

# Get all sectors
curl http://localhost:8000/api/analyze/sectors
```

### Via Frontend UI

1. Open http://localhost:5173
2. Navigate to "Startup Analysis"
3. Search for "neural" or any startup name
4. Click a result to view detailed analysis
5. Observe real-time score calculations

## 🚧 Future Enhancements (MongoDB Integration)

The backend architecture supports MongoDB integration:

```python
# Future additions:
# - AsyncMongo driver for non-blocking DB operations
# - Collections for user saved analyses, reports, alerts
# - Caching layer (Redis) for frequently accessed predictions
# - Authentication & multi-tenant support
# - Audit logging for all predictions
```

## 📝 Notes

- All model artifacts load on startup (singleton pattern)
- CSV dataset is loaded lazily and cached
- React Query handles response caching (5-minute default)
- CORS is enabled for frontend development
- Models are pre-trained and ready for inference
- No retraining needed - inference only

## 🤝 Contributing

Backend endpoints are documented with docstrings. Frontend pages use React Query hooks for data fetching.

## 📄 License

Proprietary - AI Startup Intelligence Platform

---

**Last Updated**: 2024
**Version**: 1.0.0
**Status**: Production Ready (Backend + Frontend Integration)
