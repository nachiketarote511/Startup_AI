from pathlib import Path
import joblib

print("Loading Models...")

BASE_DIR = Path(__file__).resolve().parents[2]

MODELS_DIR = BASE_DIR / "models"

print("Models Directory:", MODELS_DIR)

# =====================================================
# PREDICTION MODELS
# =====================================================

success_model = joblib.load(
    MODELS_DIR /
    "success_model" /
    "random_forest_success.pkl"
)

risk_model = joblib.load(
    MODELS_DIR /
    "risk_model" /
    "risk_model.pkl"
)

investor_model = joblib.load(
    MODELS_DIR /
    "investor_model" /
    "investor_readiness.pkl"
)

health_model = joblib.load(
    MODELS_DIR /
    "startup_health_model" /
    "startup_health_model.pkl"
)

founder_model = joblib.load(
    MODELS_DIR /
    "founder_strength_model" /
    "founder_strength_model.pkl"
)

funding_model = joblib.load(
    MODELS_DIR /
    "funding_strength_model" /
    "funding_strength_model.pkl"
)

market_model = joblib.load(
    MODELS_DIR /
    "market_opportunity_model" /
    "market_opportunity_model.pkl"
)

growth_model = joblib.load(
    MODELS_DIR /
    "growth_potential_model" /
    "growth_potential_model.pkl"
)

innovation_model = joblib.load(
    MODELS_DIR /
    "innovation_assessment_model" /
    "innovation_assessment_model.pkl"
)

competition_model = joblib.load(
    MODELS_DIR /
    "competition_analysis_model" /
    "competition_analysis_model.pkl"
)

# =====================================================
# LABEL ENCODERS
# =====================================================

success_encoder = joblib.load(
    MODELS_DIR /
    "success_model" /
    "label_encoder.pkl"
)

risk_encoder = joblib.load(
    MODELS_DIR /
    "risk_model" /
    "label_encoder.pkl"
)

investor_encoder = joblib.load(
    MODELS_DIR /
    "investor_model" /
    "label_encoder.pkl"
)

health_encoder = joblib.load(
    MODELS_DIR /
    "startup_health_model" /
    "label_encoder.pkl"
)

founder_encoder = joblib.load(
    MODELS_DIR /
    "founder_strength_model" /
    "label_encoder.pkl"
)

funding_encoder = joblib.load(
    MODELS_DIR /
    "funding_strength_model" /
    "label_encoder.pkl"
)

market_encoder = joblib.load(
    MODELS_DIR /
    "market_opportunity_model" /
    "label_encoder.pkl"
)

growth_encoder = joblib.load(
    MODELS_DIR /
    "growth_potential_model" /
    "label_encoder.pkl"
)

innovation_encoder = joblib.load(
    MODELS_DIR /
    "innovation_assessment_model" /
    "label_encoder.pkl"
)

competition_encoder = joblib.load(
    MODELS_DIR /
    "competition_analysis_model" /
    "label_encoder.pkl"
)

# =====================================================
# ENGINES
# =====================================================

competitor_engine = joblib.load(
    MODELS_DIR /
    "competitor_discovery_engine" /
    "competitor_discovery_engine.pkl"
)

market_gap_engine = joblib.load(
    MODELS_DIR /
    "market_gap_detection_engine" /
    "market_gap_detection_engine.pkl"
)

clustering_engine = joblib.load(
    MODELS_DIR /
    "startup_clustering_engine" /
    "startup_clustering_engine.pkl"
)

what_if_engine = joblib.load(
    MODELS_DIR /
    "what_if_simulator_model" /
    "what_if_simulator.pkl"
)

weakness_engine = joblib.load(
    MODELS_DIR /
    "weakness_detection_model" /
    "weakness_detection_engine.pkl"
)

recommendation_engine = joblib.load(
    MODELS_DIR /
    "recommendation_model" /
    "advanced_recommendation_engine.pkl"
)

knowledge_graph = joblib.load(
    MODELS_DIR /
    "startup_knowledge_graph_engine" /
    "startup_knowledge_graph.pkl"
)

# =====================================================
# clustering 
# =====================================================

clustering_scaler = joblib.load(
    MODELS_DIR /
    "startup_clustering_engine" /
    "scaler.pkl"
)


print("All Models, Encoders & Engines Loaded Successfully ✅")