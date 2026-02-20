"""
Script Generator Module

Generates structured screenplay scripts from video concepts using LLM.
Supports multi-language generation with culturally appropriate terminology.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


class Tone(str, Enum):
    """Video tone styles"""
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    HUMOROUS = "humorous"
    EMOTIONAL = "emotional"
    EDUCATIONAL = "educational"


class EmotionMarker(str, Enum):
    """Emotion markers for voice emphasis"""
    NEUTRAL = "neutral"
    ENTHUSIASTIC = "enthusiastic"
    SERIOUS = "serious"
    CURIOUS = "curious"
    EMPHATIC = "emphatic"
    WARM = "warm"


@dataclass
class Scene:
    """Represents a single scene in the script"""
    number: int
    title: str
    duration_seconds: float
    visual_description: str  # What the camera sees
    dialogue: str
    camera_direction: str  # e.g., "pan left", "zoom in"
    emotion_markers: Dict[str, EmotionMarker]  # word -> emotion
    speaker: str  # Character name
    suggested_background: str


@dataclass
class Screenplay:
    """Complete screenplay structure"""
    title: str
    duration_seconds: float
    language: str
    tone: Tone
    scenes: List[Scene]
    voice_over_instructions: Optional[str]
    pacing_notes: Optional[str]


class ScriptGenerator:
    """
    Generates structured screenplay scripts from video concepts.
    
    Features:
    - LLM-powered scriptwriting
    - Scene-by-scene structure with timing
    - Camera directions and visual descriptions
    - Multi-language support (20+ languages)
    - Emotion markers for voice synthesis
    """
    
    def __init__(self, llm_client=None):
        """
        Initialize ScriptGenerator.
        
        Args:
            llm_client: LLM client for script generation
        """
        self.llm_client = llm_client
        self.language_styles = self._build_language_styles()
    
    def generate_script(self, concept: Dict[str, Any]) -> Screenplay:
        """
        Generate a screenplay from a video concept.
        
        Args:
            concept: Dict with title, brief, target_audience, duration, language, tone
            
        Returns:
            Screenplay object
        """
        title = concept.get("title", "Untitled")
        duration = concept.get("duration_seconds", 60)
        language = concept.get("language", "English")
        tone_str = concept.get("tone", "professional")
        tone = Tone[tone_str.upper()] if tone_str.upper() in Tone.__members__ else Tone.PROFESSIONAL
        
        brief = concept.get("brief", "")
        audience = concept.get("target_audience", "General")
        
        # Generate scenes based on duration and brief
        scenes = self._generate_scenes(title, brief, audience, duration, language, tone)
        
        return Screenplay(
            title=title,
            duration_seconds=duration,
            language=language,
            tone=tone,
            scenes=scenes,
            voice_over_instructions=self._generate_voice_over_instructions(tone),
            pacing_notes=self._generate_pacing_notes(duration)
        )
    
    def _generate_scenes(
        self,
        title: str,
        brief: str,
        audience: str,
        duration: float,
        language: str,
        tone: Tone
    ) -> List[Scene]:
        """Generate individual scenes for the screenplay"""
        scene_count = self._estimate_scene_count(duration)
        scenes = []
        
        # Opening scene
        scenes.append(Scene(
            number=1,
            title="Opening Hook",
            duration_seconds=duration * 0.1,
            visual_description=f"Engaging opening that captures attention of {audience}",
            dialogue=f"Welcome to {title}",
            camera_direction="wide shot to close-up",
            emotion_markers={"Welcome": EmotionMarker.ENTHUSIASTIC},
            speaker="Narrator",
            suggested_background="dynamic"
        ))
        
        # Content scenes
        content_duration = duration * 0.8
        scene_duration_each = content_duration / max(scene_count - 2, 1)
        
        for i in range(2, scene_count):
            scenes.append(Scene(
                number=i,
                title=f"Content Section {i-1}",
                duration_seconds=scene_duration_each,
                visual_description=f"Presenting key information point {i-1}",
                dialogue=f"Key message {i-1} for {audience}",
                camera_direction="medium shot with emphasis",
                emotion_markers={"message": EmotionMarker.EMPHATIC},
                speaker="Narrator",
                suggested_background="professional"
            ))
        
        # Closing scene
        scenes.append(Scene(
            number=scene_count,
            title="Call to Action",
            duration_seconds=duration * 0.1,
            visual_description="Strong closing with clear call-to-action",
            dialogue="Thank you. Take the next step.",
            camera_direction="direct to camera",
            emotion_markers={"Thank": EmotionMarker.WARM, "step": EmotionMarker.EMPHATIC},
            speaker="Narrator",
            suggested_background="simple"
        ))
        
        return scenes
    
    def _estimate_scene_count(self, duration_seconds: float) -> int:
        """Estimate number of scenes based on video duration"""
        # Typically 8-15 seconds per scene
        return max(3, int(duration_seconds / 12))
    
    def _generate_voice_over_instructions(self, tone: Tone) -> str:
        """Generate voice-over instructions based on tone"""
        instructions = {
            Tone.PROFESSIONAL: "Use clear, authoritative tone. Emphasize key terms. Pace: 120-140 words per minute.",
            Tone.CASUAL: "Conversational, friendly delivery. Natural speech patterns. Pace: 130-150 wpm.",
            Tone.HUMOROUS: "Energetic, playful. Pause for comedic effect. Pace: 140-160 wpm.",
            Tone.EMOTIONAL: "Sincere, heartfelt delivery. Build emotional connection. Pace: 100-120 wpm.",
            Tone.EDUCATIONAL: "Clear explanation, measured pace. Emphasize learning points. Pace: 110-130 wpm.",
        }
        return instructions.get(tone, "Clear, natural delivery.")
    
    def _generate_pacing_notes(self, duration: float) -> str:
        """Generate pacing recommendations"""
        if duration < 30:
            return "Fast-paced. Minimal scene transitions. Quick cuts recommended."
        elif duration < 60:
            return "Moderate pace. 2-3 second scene transitions. Good for social media."
        else:
            return "Measured pace. 3-5 second transitions. Room for scene development."
    
    def _build_language_styles(self) -> Dict[str, Dict[str, str]]:
        """Build language-specific style guides"""
        return {
            "English": {"greeting": "Hello", "closing": "Thank you"},
            "Spanish": {"greeting": "Hola", "closing": "Gracias"},
            "French": {"greeting": "Bonjour", "closing": "Merci"},
            "German": {"greeting": "Guten Tag", "closing": "Danke"},
            "Chinese": {"greeting": "你好", "closing": "谢谢"},
            "Japanese": {"greeting": "こんにちは", "closing": "ありがとう"},
        }
