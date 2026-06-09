from pydantic import BaseModel


class StartupInput(BaseModel):

    founder_count: int
    max_founder_experience: float
    female_founder_count: int

    iit_founder: int
    iim_founder: int
    foreign_university_founder: int

    patent_count: int
    trademark_count: int

    dpiit_registered: int
    gst_registered: int

    total_funding: float
    latest_funding: float

    funding_round_count: int

    investor_count: int
    top_tier_investor_count: int

    average_round_size: float

    valuation: float

    burn_rate: float
    runway_months: float

    market_size: float
    market_growth_rate: float

    tam: float
    sam: float
    som: float

    customer_segment_count: int

    international_market_access: int

    industry_growth_rate: float

    employee_growth_rate: float
    customer_growth_rate: float
    revenue_growth_rate: float

    monthly_active_users: int

    retention_rate: float

    customer_count: int

    revenue: float

    employee_count: int

    technology_score: float

    api_available: int
    mobile_app_available: int
    web_platform_available: int

    startup_age: int

    website_traffic: int
    linkedin_followers: int
    twitter_followers: int

    media_mentions: int

    domain_authority: float