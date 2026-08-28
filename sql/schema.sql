DROP TABLE IF EXISTS linkedin_posts;
DROP TABLE IF EXISTS linkedin_profiles;

CREATE TABLE linkedin_leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    job_title TEXT,
    company VARCHAR(255),
    industry VARCHAR(255),
    location VARCHAR(255),
    agent VARCHAR(255),
    sdr_status VARCHAR(100),
    comment_status VARCHAR(100),
    hot_score NUMERIC,
    source VARCHAR(100),
    prioritized VARCHAR(50),
    linkedin_url TEXT UNIQUE,
    added_on TIMESTAMP,
    last_contacted TIMESTAMP,
    invite_sent_at TIMESTAMP,
    connected_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);