import pandas as pd

from services.model_loader import (
    founder_model,
    funding_model,
    market_model,
    growth_model,
    innovation_model,
    health_model,
    investor_model,
    success_model,
    risk_model,
    competition_model,

    founder_encoder,
    funding_encoder,
    market_encoder,
    growth_encoder,
    innovation_encoder,
    health_encoder,
    investor_encoder,
    success_encoder,
    risk_encoder,
    competition_encoder,

    recommendation_engine,
    clustering_engine,
    clustering_scaler
)


def run_prediction_pipeline(data):

    results = {}

    # =====================================================
    # FOUNDER STRENGTH
    # =====================================================

    founder_df = pd.DataFrame([{
        "founder_count": data.founder_count,
        "max_founder_experience": data.max_founder_experience,
        "female_founder_count": data.female_founder_count,
        "iit_founder": data.iit_founder,
        "iim_founder": data.iim_founder,
        "foreign_university_founder": data.foreign_university_founder,
        "patent_count": data.patent_count,
        "trademark_count": data.trademark_count,
        "dpiit_registered": data.dpiit_registered,
        "gst_registered": data.gst_registered
    }])

    founder_pred = founder_model.predict(founder_df)[0]

    founder_label = founder_encoder.inverse_transform(
        [founder_pred]
    )[0]

    results["founder_strength"] = founder_label
    results["founder_strength_score"] = int(founder_pred)

    # =====================================================
    # FUNDING STRENGTH
    # =====================================================

    funding_df = pd.DataFrame([{
        "total_funding": data.total_funding,
        "latest_funding": data.latest_funding,
        "funding_round_count": data.funding_round_count,
        "investor_count": data.investor_count,
        "top_tier_investor_count": data.top_tier_investor_count,
        "average_round_size": data.average_round_size,
        "valuation": data.valuation,
        "burn_rate": data.burn_rate,
        "runway_months": data.runway_months
    }])

    funding_pred = funding_model.predict(
        funding_df
    )[0]

    funding_label = funding_encoder.inverse_transform(
        [funding_pred]
    )[0]

    results["funding_strength"] = funding_label
    results["funding_strength_score"] = int(funding_pred)

    # =====================================================
    # MARKET OPPORTUNITY
    # =====================================================

    market_df = pd.DataFrame([{
        "market_size": data.market_size,
        "market_growth_rate": data.market_growth_rate,
        "tam": data.tam,
        "sam": data.sam,
        "som": data.som,
        "customer_segment_count": data.customer_segment_count,
        "international_market_access": data.international_market_access,
        "industry_growth_rate": data.industry_growth_rate
    }])

    market_pred = market_model.predict(
        market_df
    )[0]

    market_label = market_encoder.inverse_transform(
        [market_pred]
    )[0]

    results["market_opportunity"] = market_label
    results["market_opportunity_score"] = int(market_pred)

    # =====================================================
    # GROWTH POTENTIAL
    # =====================================================

    growth_df = pd.DataFrame([{
        "employee_growth_rate": data.employee_growth_rate,
        "customer_growth_rate": data.customer_growth_rate,
        "revenue_growth_rate": data.revenue_growth_rate,
        "monthly_active_users": data.monthly_active_users,
        "retention_rate": data.retention_rate,
        "customer_count": data.customer_count,
        "revenue": data.revenue,
        "employee_count": data.employee_count
    }])

    growth_pred = growth_model.predict(
        growth_df
    )[0]

    growth_label = growth_encoder.inverse_transform(
        [growth_pred]
    )[0]

    results["growth_potential"] = growth_label
    results["growth_score"] = int(growth_pred)

    # =====================================================
    # INNOVATION
    # =====================================================

    innovation_df = pd.DataFrame([{
        "patent_count": data.patent_count,
        "trademark_count": data.trademark_count,
        "api_available": data.api_available,
        "mobile_app_available": data.mobile_app_available,
        "web_platform_available": data.web_platform_available,
        "technology_score": data.technology_score
    }])

    innovation_pred = innovation_model.predict(
        innovation_df
    )[0]

    innovation_label = innovation_encoder.inverse_transform(
        [innovation_pred]
    )[0]

    results["innovation"] = innovation_label
    results["innovation_score"] = int(innovation_pred)

        # =====================================================
    # SCORE MAPPING
    # =====================================================

    score_map = {
    "High": 90,
    "Medium": 60,
    "Low": 30
    }

    risk_score_map = {
    "High Risk": 90,
    "Medium Risk": 60,
    "Low Risk": 30
    }

    founder_score = score_map[founder_label]
    funding_score = score_map[funding_label]
    market_score = score_map[market_label]
    growth_score = score_map[growth_label]
    innovation_score = score_map[innovation_label]

    results["founder_strength_score"] = founder_score
    results["funding_strength_score"] = funding_score
    results["market_opportunity_score"] = market_score
    results["growth_score"] = growth_score
    results["innovation_score"] = innovation_score

    # =====================================================
    # STARTUP HEALTH
    # =====================================================

    health_df = pd.DataFrame([{
        "founder_strength_score": founder_score,
        "funding_strength_score": funding_score,
        "market_opportunity_score": market_score,
        "growth_score": growth_score,
        "revenue": data.revenue,
        "customer_count": data.customer_count,
        "retention_rate": data.retention_rate,
        "employee_count": data.employee_count,
        "runway_months": data.runway_months,
        "burn_rate": data.burn_rate
    }])

    health_pred = health_model.predict(
        health_df
    )[0]

    health_label = health_encoder.inverse_transform(
        [health_pred]
    )[0]

    health_score = score_map[health_label]

    results["startup_health"] = health_label
    results["startup_health_score"] = health_score

    # =====================================================
    # INVESTOR READINESS
    # =====================================================

    investor_df = pd.DataFrame([{
        "startup_health_score": health_score,
        "founder_strength_score": founder_score,
        "funding_strength_score": funding_score,
        "growth_score": growth_score,
        "revenue": data.revenue,
        "investor_count": data.investor_count,
        "valuation": data.valuation,
        "retention_rate": data.retention_rate,
        "customer_count": data.customer_count,
        "market_size": data.market_size
    }])

    investor_pred = investor_model.predict(
        investor_df
    )[0]

    investor_label = investor_encoder.inverse_transform(
        [investor_pred]
    )[0]

    investor_score = score_map[investor_label]

    results["investor_readiness"] = investor_label
    results["investor_readiness_score"] = investor_score

    # =====================================================
    # SUCCESS PREDICTION
    # =====================================================

    success_df = pd.DataFrame([{
        "startup_age": data.startup_age,
        "founder_strength_score": founder_score,
        "funding_strength_score": funding_score,
        "market_opportunity_score": market_score,
        "growth_score": growth_score,
        "employee_count": data.employee_count,
        "investor_count": data.investor_count,
        "total_funding": data.total_funding,
        "market_size": data.market_size,
        "revenue": data.revenue,
        "retention_rate": data.retention_rate,
        "customer_count": data.customer_count
    }])

    success_pred = success_model.predict(
        success_df
    )[0]

    success_label = success_encoder.inverse_transform(
        [success_pred]
    )[0]

    success_score = score_map[success_label]

    results["success_prediction"] = success_label
    results["success_prediction_score"] = success_score

    # =====================================================
    # RISK PREDICTION
    # =====================================================

    risk_df = pd.DataFrame([{
        "burn_rate": data.burn_rate,
        "runway_months": data.runway_months,
        "growth_score": growth_score,
        "funding_strength_score": funding_score,
        "retention_rate": data.retention_rate,
        "revenue_growth_rate": data.revenue_growth_rate,
        "customer_growth_rate": data.customer_growth_rate,
        "employee_growth_rate": data.employee_growth_rate,
        "revenue": data.revenue,
        "customer_count": data.customer_count
    }])

    risk_pred = risk_model.predict(
        risk_df
    )[0]

    risk_label = risk_encoder.inverse_transform(
        [risk_pred]
    )[0]

    risk_score = risk_score_map[risk_label]

    results["risk_prediction"] = risk_label
    results["risk_prediction_score"] = risk_score

    # =====================================================
    # COMPETITION ANALYSIS
    # =====================================================

    competition_df = pd.DataFrame([{
        "customer_count": data.customer_count,
        "website_traffic": data.website_traffic,
        "linkedin_followers": data.linkedin_followers,
        "twitter_followers": data.twitter_followers,
        "media_mentions": data.media_mentions,
        "domain_authority": data.domain_authority,
        "market_size": data.market_size,
        "customer_segment_count": data.customer_segment_count
    }])

    competition_pred = competition_model.predict(
        competition_df
    )[0]

    competition_label = competition_encoder.inverse_transform(
        [competition_pred]
    )[0]

    competition_score = score_map[competition_label]

    results["competition"] = competition_label
    results["competition_score"] = competition_score

        # =====================================================
    # WEAKNESS DETECTION
    # =====================================================

    weaknesses = []

    if founder_score <= 60:
        weaknesses.append("Founder Strength")

    if funding_score <= 60:
        weaknesses.append("Funding Strength")

    if market_score <= 60:
        weaknesses.append("Market Opportunity")

    if growth_score <= 60:
        weaknesses.append("Growth Potential")

    results["weaknesses"] = weaknesses

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    recommendations = []

    try:

        for weakness in weaknesses:

            if weakness in recommendation_engine:

                if weakness == "Founder Strength":

                    if founder_score <= 30:
                        recommendations.extend(
                            recommendation_engine[
                                "Founder Strength"
                            ]["0-20"]
                        )

                    elif founder_score <= 60:
                        recommendations.extend(
                            recommendation_engine[
                                "Founder Strength"
                            ]["21-40"]
                        )

                elif weakness == "Funding Strength":

                    if funding_score <= 30:
                        recommendations.extend(
                            recommendation_engine[
                                "Funding Strength"
                            ]["0-20"]
                        )

                    elif funding_score <= 60:
                        recommendations.extend(
                            recommendation_engine[
                                "Funding Strength"
                            ]["21-40"]
                        )

                elif weakness == "Market Opportunity":

                    if market_score <= 30:
                        recommendations.extend(
                            recommendation_engine[
                                "Market Opportunity"
                            ]["0-20"]
                        )

                    elif market_score <= 60:
                        recommendations.extend(
                            recommendation_engine[
                                "Market Opportunity"
                            ]["21-40"]
                        )

                elif weakness == "Growth Potential":

                    if growth_score <= 30:
                        recommendations.extend(
                            recommendation_engine[
                                "Growth"
                            ]["0-20"]
                        )

                    elif growth_score <= 60:
                        recommendations.extend(
                            recommendation_engine[
                                "Growth"
                            ]["21-40"]
                        )

    except Exception as e:

        recommendations = [
            f"Recommendation Engine Error: {e}"
        ]

    results["recommendations"] = recommendations[:10]

        # =====================================================
    # CLUSTERING
    # =====================================================

    cluster_df = pd.DataFrame([{
        "startup_health_score": health_score,
        "founder_strength_score": founder_score,
        "funding_strength_score": funding_score,
        "market_opportunity_score": market_score,
        "growth_score": growth_score,
        "innovation_score": innovation_score,
        "competition_score": competition_score,
        "investor_readiness_score": investor_score
    }])

    scaled_cluster = clustering_scaler.transform(
        cluster_df
    )

    cluster_id = int(
        clustering_engine.predict(
            scaled_cluster
        )[0]
    )

    cluster_names = {
        0: "High Growth",
        1: "Investor Ready",
        2: "Market Leaders",
        3: "Emerging",
        4: "High Risk"
    }

    results["cluster_id"] = cluster_id
    results["cluster_name"] = cluster_names.get(
        cluster_id,
        "Unknown"
    )


    return results