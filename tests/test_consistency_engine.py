"""Tests for character consistency engine"""

import pytest
from src.character.consistency_engine import CharacterConsistencyEngine


class TestCharacterConsistencyEngine:
    """Test CharacterConsistencyEngine class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.engine = CharacterConsistencyEngine()
    
    def test_register_character(self):
        """Test character registration"""
        profile = self.engine.register_character(
            character_id="test_char_001",
            name="Test Character",
            description="Professional woman, 30s",
            reference_images=["ref1.jpg", "ref2.jpg"]
        )
        
        assert profile.character_id == "test_char_001"
        assert profile.name == "Test Character"
        assert len(profile.reference_images) == 2
    
    def test_generate_consistency_prompt(self):
        """Test prompt generation for consistent character"""
        profile = self.engine.register_character(
            character_id="char_001",
            name="Sarah",
            description="Professional woman, warm expression",
            reference_images=["ref.jpg"]
        )
        
        prompt = self.engine.generate_consistency_prompt(
            "char_001",
            "Speaking about product benefits"
        )
        
        assert "Sarah" in prompt
        assert "consistency" in prompt.lower()
        assert "reference" in prompt.lower()
    
    def test_validate_consistency(self):
        """Test consistency validation"""
        profile = self.engine.register_character(
            character_id="char_001",
            name="John",
            description="Professional man",
            reference_images=["ref.jpg"]
        )
        
        score = self.engine.validate_consistency("char_001", "generated_frame.jpg")
        
        assert 0.0 <= score <= 1.0
        assert score > 0.9  # Should be high consistency


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
