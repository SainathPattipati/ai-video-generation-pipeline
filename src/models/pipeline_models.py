"""
Pydantic Models for AI Video Pipeline

Data structures for pipeline stages and API responses.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum


class VideoConcept(BaseModel):
    """Video concept input"""
    title: str = Field(..., description="Video title")
    brief: str = Field(..., description="Video brief (300-500 words)")
    target_audience: str = Field(..., description="Target audience")
    duration_seconds: float = Field(60, ge=10, le=600, description="Video duration")
    language: str = Field("English", description="Language for script and voiceover")
    tone: str = Field("professional", description="Video tone")


class GenerationJob(BaseModel):
    """Video generation job status"""
    job_id: str
    status: str  # pending, processing, completed, failed
    progress_percent: float = Field(0.0, ge=0.0, le=100.0)
    current_stage: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None


class ExportFormat(str, Enum):
    """Supported export formats"""
    YOUTUBE_1080 = "youtube_1080"
    YOUTUBE_4K = "youtube_4k"
    INSTAGRAM_REELS = "instagram_reels"
    LINKEDIN = "linkedin"
    TIKTOK = "tiktok"
    STANDARD_MP4 = "standard_mp4"
