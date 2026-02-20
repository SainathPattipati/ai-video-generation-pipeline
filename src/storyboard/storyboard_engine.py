"""
Storyboard Engine Module

Converts scripts into visual storyboards with scene composition and camera direction.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class CameraAngle(str, Enum):
    """Camera angles for scene composition"""
    WIDE_SHOT = "wide_shot"
    MEDIUM_SHOT = "medium_shot"
    CLOSE_UP = "close_up"
    EXTREME_CLOSE_UP = "extreme_close_up"
    AERIAL = "aerial"
    LOW_ANGLE = "low_angle"
    HIGH_ANGLE = "high_angle"
    DUTCH_ANGLE = "dutch_angle"


class CameraMovement(str, Enum):
    """Camera movement types"""
    STATIC = "static"
    PAN = "pan"
    TILT = "tilt"
    ZOOM = "zoom"
    DOLLY = "dolly"
    CRANE = "crane"
    TRACKING = "tracking"


@dataclass
class VisualElement:
    """Visual element in a scene"""
    element_type: str  # character, object, background, text
    position: tuple  # x, y coordinates
    size: float  # relative to scene
    description: str
    duration_seconds: Optional[float] = None


@dataclass
class StoryboardScene:
    """Visual storyboard for a single scene"""
    scene_number: int
    title: str
    duration_seconds: float
    camera_angle: CameraAngle
    camera_movement: CameraMovement
    movement_direction: str  # left, right, up, down, in, out
    visual_elements: List[VisualElement]
    composition_notes: str
    lighting_description: str
    color_palette: List[str]  # hex colors


class StoryboardEngine:
    """
    Converts scripts into visual storyboards.
    
    Responsibilities:
    - Scene composition planning
    - Character placement rules
    - Camera angle selection
    - Visual consistency guidelines
    """
    
    def __init__(self):
        """Initialize StoryboardEngine"""
        self.composition_rules = self._build_composition_rules()
    
    def generate_storyboard(self, scenes: List[Any]) -> List[StoryboardScene]:
        """
        Generate visual storyboard from screenplay scenes.
        
        Args:
            scenes: List of Scene objects from screenplay
            
        Returns:
            List of StoryboardScene objects
        """
        storyboard_scenes = []
        
        for scene in scenes:
            storyboard_scene = self._create_storyboard_scene(scene)
            storyboard_scenes.append(storyboard_scene)
        
        return storyboard_scenes
    
    def _create_storyboard_scene(self, scene: Any) -> StoryboardScene:
        """Create visual storyboard for a single scene"""
        # Determine camera angle based on scene type and duration
        camera_angle = self._select_camera_angle(scene.title)
        camera_movement = self._select_camera_movement(scene.camera_direction)
        movement_dir = self._extract_movement_direction(scene.camera_direction)
        
        # Create visual elements
        visual_elements = self._create_visual_elements(scene)
        
        # Generate composition notes
        composition = self._generate_composition_notes(scene)
        
        # Select lighting and colors based on tone
        lighting = "Bright professional lighting with subtle shadows"
        colors = ["#FFFFFF", "#1F77B4", "#2CA02C", "#FF7F0E"]
        
        return StoryboardScene(
            scene_number=scene.number,
            title=scene.title,
            duration_seconds=scene.duration_seconds,
            camera_angle=camera_angle,
            camera_movement=camera_movement,
            movement_direction=movement_dir,
            visual_elements=visual_elements,
            composition_notes=composition,
            lighting_description=lighting,
            color_palette=colors
        )
    
    def _select_camera_angle(self, scene_title: str) -> CameraAngle:
        """Select camera angle based on scene"""
        if "opening" in scene_title.lower():
            return CameraAngle.WIDE_SHOT
        elif "close" in scene_title.lower() or "detail" in scene_title.lower():
            return CameraAngle.CLOSE_UP
        elif "call to action" in scene_title.lower():
            return CameraAngle.MEDIUM_SHOT
        else:
            return CameraAngle.MEDIUM_SHOT
    
    def _select_camera_movement(self, direction: str) -> CameraMovement:
        """Select camera movement type"""
        direction_lower = direction.lower() if direction else ""
        
        if "zoom" in direction_lower:
            return CameraMovement.ZOOM
        elif "pan" in direction_lower:
            return CameraMovement.PAN
        elif "tilt" in direction_lower:
            return CameraMovement.TILT
        elif "tracking" in direction_lower:
            return CameraMovement.TRACKING
        else:
            return CameraMovement.STATIC
    
    def _extract_movement_direction(self, direction: str) -> str:
        """Extract movement direction"""
        direction_lower = direction.lower() if direction else "static"
        
        if "left" in direction_lower:
            return "left"
        elif "right" in direction_lower:
            return "right"
        elif "up" in direction_lower:
            return "up"
        elif "down" in direction_lower:
            return "down"
        elif "in" in direction_lower or "zoom in" in direction_lower:
            return "in"
        elif "out" in direction_lower or "zoom out" in direction_lower:
            return "out"
        else:
            return "static"
    
    def _create_visual_elements(self, scene: Any) -> List[VisualElement]:
        """Create visual elements for scene"""
        elements = []
        
        # Add character
        elements.append(VisualElement(
            element_type="character",
            position=(0.5, 0.6),  # center-right of frame
            size=0.5,
            description=f"Speaker delivering dialogue",
            duration_seconds=scene.duration_seconds
        ))
        
        # Add background
        elements.append(VisualElement(
            element_type="background",
            position=(0.5, 0.5),
            size=1.0,
            description=scene.suggested_background,
            duration_seconds=scene.duration_seconds
        ))
        
        # Add text overlay if needed
        if "key message" in scene.title.lower():
            elements.append(VisualElement(
                element_type="text",
                position=(0.5, 0.1),
                size=0.3,
                description="Key point text overlay",
                duration_seconds=2.0
            ))
        
        return elements
    
    def _generate_composition_notes(self, scene: Any) -> str:
        """Generate composition guidelines"""
        return (
            "Use rule of thirds for character placement. "
            "Ensure adequate headroom. "
            "Leave space for on-screen text. "
            "Maintain consistent background depth."
        )
    
    def _build_composition_rules(self) -> Dict[str, str]:
        """Build scene composition rules"""
        return {
            "character_position": "Center on right third of frame",
            "camera_distance": "Medium shot for dialogue scenes",
            "depth_of_field": "Shallow (background slightly blurred)",
            "frame_rate": "24fps for cinematic look",
            "aspect_ratio": "16:9 for landscape, 9:16 for vertical",
        }
