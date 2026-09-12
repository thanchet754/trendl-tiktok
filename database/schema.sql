-- ==============================================================================
-- TIKTOK TRENDS & RADAR INTELLIGENCE - SUPABASE DATABASE SCHEMA
-- Chạy đoạn mã này trong: Supabase Dashboard -> SQL Editor -> New Query -> Run
-- ==============================================================================

-- 1. BẢNG SẢN PHẨM XU HƯỚNG (TIKTOK TRENDS)
CREATE TABLE IF NOT EXISTS public.tiktok_trends (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT,
    sub_niche TEXT,
    price NUMERIC(10, 2) DEFAULT 0,
    gmv_24h NUMERIC(15, 2) DEFAULT 0,
    sales_count_24h INTEGER DEFAULT 0,
    classification TEXT DEFAULT 'VIRAL_SPIKE_24H',
    velocity_score NUMERIC(5, 2) DEFAULT 0,
    image_url TEXT,
    shop_url TEXT,
    query_1688 TEXT,
    query_alibaba TEXT,
    verification_24h JSONB DEFAULT '{}'::jsonb,
    strategy JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index tối ưu tìm kiếm và lọc phân trang
CREATE INDEX IF NOT EXISTS idx_tiktok_trends_category ON public.tiktok_trends(category);
CREATE INDEX IF NOT EXISTS idx_tiktok_trends_classification ON public.tiktok_trends(classification);
CREATE INDEX IF NOT EXISTS idx_tiktok_trends_gmv ON public.tiktok_trends(gmv_24h DESC);
CREATE INDEX IF NOT EXISTS idx_tiktok_trends_updated ON public.tiktok_trends(updated_at DESC);

-- 2. BẢNG TOP CREATORS / KOCs (TIKTOK CREATORS)
CREATE TABLE IF NOT EXISTS public.tiktok_creators (
    id TEXT PRIMARY KEY,
    handle TEXT NOT NULL,
    nickname TEXT,
    avatar_url TEXT,
    follower_count BIGINT DEFAULT 0,
    gmv_24h NUMERIC(15, 2) DEFAULT 0,
    items_sold_24h INTEGER DEFAULT 0,
    category TEXT,
    sub_niche TEXT,
    top_product_title TEXT,
    top_product_image TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_tiktok_creators_gmv ON public.tiktok_creators(gmv_24h DESC);
CREATE INDEX IF NOT EXISTS idx_tiktok_creators_category ON public.tiktok_creators(category);

-- 3. BẢNG TOP VIDEOS VIRAL (TIKTOK VIDEOS)
CREATE TABLE IF NOT EXISTS public.tiktok_videos (
    id TEXT PRIMARY KEY,
    video_id TEXT NOT NULL,
    author_handle TEXT,
    title TEXT,
    cover_url TEXT,
    views_24h BIGINT DEFAULT 0,
    est_items_sold INTEGER DEFAULT 0,
    est_gmv_24h NUMERIC(15, 2) DEFAULT 0,
    sound_title TEXT,
    category TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_tiktok_videos_views ON public.tiktok_videos(views_24h DESC);
CREATE INDEX IF NOT EXISTS idx_tiktok_videos_gmv ON public.tiktok_videos(est_gmv_24h DESC);

-- 4. BẢNG ĐỒNG BỘ ĐÃ LƯU CỦA TEAM (TIKTOK TEAM SAVED)
CREATE TABLE IF NOT EXISTS public.tiktok_team_saved (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    user_name TEXT NOT NULL,
    trend_id TEXT NOT NULL,
    trend_title TEXT,
    trend_category TEXT,
    trend_image TEXT,
    saved_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_user_trend UNIQUE(user_id, trend_id)
);

CREATE INDEX IF NOT EXISTS idx_team_saved_user ON public.tiktok_team_saved(user_id);
CREATE INDEX IF NOT EXISTS idx_team_saved_trend ON public.tiktok_team_saved(trend_id);

-- ==============================================================================
-- CẤU HÌNH BẢO MẬT & PHÂN QUYỀN TRUY CẬP (ROW LEVEL SECURITY - RLS)
-- Cho phép khóa anon_key đọc và ghi an toàn
-- ==============================================================================

ALTER TABLE public.tiktok_trends ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tiktok_creators ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tiktok_videos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tiktok_team_saved ENABLE ROW LEVEL SECURITY;

-- Tạo chính sách cho phép đọc và ghi công khai cho bảng trends
DROP POLICY IF EXISTS "Allow anon read/write trends" ON public.tiktok_trends;
CREATE POLICY "Allow anon read/write trends" ON public.tiktok_trends
    FOR ALL TO anon, authenticated
    USING (true)
    WITH CHECK (true);

-- Tạo chính sách cho phép đọc và ghi cho bảng creators
DROP POLICY IF EXISTS "Allow anon read/write creators" ON public.tiktok_creators;
CREATE POLICY "Allow anon read/write creators" ON public.tiktok_creators
    FOR ALL TO anon, authenticated
    USING (true)
    WITH CHECK (true);

-- Tạo chính sách cho phép đọc và ghi cho bảng videos
DROP POLICY IF EXISTS "Allow anon read/write videos" ON public.tiktok_videos;
CREATE POLICY "Allow anon read/write videos" ON public.tiktok_videos
    FOR ALL TO anon, authenticated
    USING (true)
    WITH CHECK (true);

-- Tạo chính sách cho phép đọc và ghi cho bảng team saved
DROP POLICY IF EXISTS "Allow anon read/write team saved" ON public.tiktok_team_saved;
CREATE POLICY "Allow anon read/write team saved" ON public.tiktok_team_saved
    FOR ALL TO anon, authenticated
    USING (true)
    WITH CHECK (true);
