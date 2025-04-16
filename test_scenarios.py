import requests
import json
from typing import Dict, Any

def test_scenario(speech: str, caller: str = "+34123456789", confidence: float = 0.9) -> Dict[str, Any]:
    """Test a specific conversation scenario"""
    payload = {
        "caller": caller,
        "call_sid": "test123",
        "speech_result": speech,
        "confidence": confidence
    }
    
    # For local testing
    response = requests.post(
        "http://127.0.0.1:5000/api/analyze",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    return response.json()

def print_analysis(result: Dict[str, Any]) -> None:
    """Print the analysis in a readable format"""
    analysis = result["analysis"]
    print("\nAnalysis Results:")
    print("-" * 50)
    print(f"Business Type: {analysis['caller_info']['business_type']}")
    print(f"Intent: {analysis['conversation']['intent']}")
    print(f"Interest Level: {analysis['conversation']['interest_level']}")
    print(f"Key Points: {', '.join(analysis['conversation']['key_points_discussed'])}")
    print(f"Schedule Callback: {analysis['next_actions']['schedule_callback']}")
    print(f"Send Info: {analysis['next_actions']['send_info']}")
    print("-" * 50)

# Test scenarios
scenarios = [
    "Me gustaría saber el precio de implementar IA en mi empresa",
    "Necesito una demo para ver cómo funciona con mi negocio",
    "Quiero implementar inteligencia artificial urgentemente",
    "Solo estoy buscando información general sobre sus servicios",
    "Mi empresa de tecnología necesita mejorar la eficiencia"
]

if __name__ == "__main__":
    print("Testing VIBATO AI Voice Agent Scenarios")
    print("=" * 50)
    
    for scenario in scenarios:
        print(f"\nTesting scenario: '{scenario}'")
        try:
            result = test_scenario(scenario)
            print_analysis(result)
        except Exception as e:
            print(f"Error testing scenario: {e}") 