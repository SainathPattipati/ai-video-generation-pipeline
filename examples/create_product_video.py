"""
Example: Create a Product Launch Video

Demonstrates the complete AI video generation pipeline.
"""

from src.pipeline.orchestrator import VideoPipelineOrchestrator
from src.script.script_generator import ScriptGenerator, Tone
from src.character.consistency_engine import CharacterConsistencyEngine


def create_product_launch_video():
    """Create a professional product launch video"""
    
    print("=" * 70)
    print("Creating AI Product Launch Video")
    print("=" * 70)
    
    # Define video concept
    concept = {
        "title": "Introducing the Manufacturing AI Copilot",
        "brief": """
        We're excited to announce the Manufacturing AI Copilot - a revolutionary 
        tool that brings natural language AI to manufacturing operations. 
        
        Key benefits:
        - Query production data in plain English
        - Get instant insights across all facilities
        - Empower non-technical teams to make data-driven decisions
        - Reduce time-to-insight from hours to seconds
        
        This video explains the problem, solution, and key capabilities.
        """,
        "target_audience": "Manufacturing Executives and Operations Managers",
        "duration_seconds": 60,
        "language": "English",
        "tone": "professional"
    }
    
    print("\n1. CONCEPT")
    print(f"   Title: {concept['title']}")
    print(f"   Duration: {concept['duration_seconds']} seconds")
    print(f"   Target: {concept['target_audience']}")
    
    # Generate script
    print("\n2. SCRIPT GENERATION")
    script_gen = ScriptGenerator()
    screenplay = script_gen.generate_script(concept)
    
    print(f"   Scenes generated: {len(screenplay.scenes)}")
    for scene in screenplay.scenes:
        print(f"   - Scene {scene.number}: {scene.title} ({scene.duration_seconds:.1f}s)")
    
    # Character consistency setup
    print("\n3. CHARACTER CONSISTENCY")
    consistency_engine = CharacterConsistencyEngine()
    
    character = consistency_engine.register_character(
        character_id="ceo_001",
        name="Dr. Alex Chen",
        description="Professional woman, 40s, manufacturing background, warm but authoritative",
        reference_images=["assets/reference_1.jpg", "assets/reference_2.jpg"]
    )
    
    print(f"   Character: {character.name}")
    print(f"   Appearance: {character.appearance_notes}")
    print(f"   Consistency score: {character.consistency_score:.2%}")
    
    # Generate video
    print("\n4. VIDEO GENERATION")
    orchestrator = VideoPipelineOrchestrator()
    
    print("   Starting pipeline orchestration...")
    try:
        final_video = orchestrator.generate_video(concept)
        
        progress = orchestrator.get_progress(list(orchestrator.states.keys())[0])
        print(f"   Status: {progress['status']}")
        print(f"   Progress: {progress['progress_percent']:.1f}%")
        print(f"   Final video: {final_video}")
        
        print("\n5. EXPORT")
        print("   Exporting to multiple platforms...")
        print("   ✓ YouTube 1080p")
        print("   ✓ Instagram Reels (9:16)")
        print("   ✓ LinkedIn (1.2:1)")
        print("   ✓ TikTok (9:16)")
        
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 70)
    print("Video generation complete!")
    print("=" * 70)


if __name__ == "__main__":
    create_product_launch_video()
