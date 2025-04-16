import json
from typing import Dict, Any

class CallAnalyzer:
    def __init__(self):
        self.intent_keywords = {
            'information': ['información', 'saber', 'conocer', 'qué es', 'cómo funciona'],
            'pricing': ['precio', 'coste', 'cuánto cuesta', 'tarifas', 'planes'],
            'demo': ['demostración', 'demo', 'probar', 'prueba', 'muestra'],
            'implementation': ['implementar', 'instalar', 'comenzar', 'empezar', 'iniciar'],
            'specific_use': ['puede hacer', 'funciona para', 'servicio', 'solución para']
        }
        
        self.interest_keywords = {
            'high': ['me interesa', 'quiero', 'necesito', 'urgente', 'inmediato'],
            'medium': ['podría', 'tal vez', 'quizás', 'considerar', 'evaluar'],
            'low': ['solo información', 'curiosidad', 'más adelante', 'después']
        }
        
        self.business_types = {
            'retail': ['tienda', 'comercio', 'retail', 'venta'],
            'service': ['servicio', 'consultoría', 'asesoría'],
            'manufacturing': ['fabricación', 'producción', 'manufactura'],
            'technology': ['tech', 'tecnología', 'software', 'desarrollo'],
            'healthcare': ['salud', 'médico', 'hospital', 'clínica']
        }

    def analyze(self, call_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze call data and return structured analysis
        """
        # Extract speech result and convert to lowercase for analysis
        speech = call_data.get('speech_result', '').lower()
        confidence = float(call_data.get('confidence', 0))
        
        # Determine intent
        intent = self._determine_intent(speech)
        
        # Determine interest level
        interest_level = self._determine_interest(speech)
        
        # Extract business type if mentioned
        business_type = self._extract_business_type(speech)
        
        # Determine next actions
        next_actions = self._determine_next_actions(intent, interest_level)
        
        # Extract key points discussed
        key_points = self._extract_key_points(speech)
        
        return {
            "caller_info": {
                "phone": call_data.get('caller', ''),
                "business_type": business_type
            },
            "conversation": {
                "intent": intent,
                "interest_level": interest_level,
                "key_points_discussed": key_points
            },
            "next_actions": next_actions,
            "confidence": confidence
        }

    def _determine_intent(self, speech: str) -> str:
        """
        Determine the caller's intent based on keywords in their speech
        """
        for intent, keywords in self.intent_keywords.items():
            if any(keyword in speech for keyword in keywords):
                return intent
        return 'general'

    def _determine_interest(self, speech: str) -> str:
        """
        Determine the interest level based on keywords
        """
        for level, keywords in self.interest_keywords.items():
            if any(keyword in speech for keyword in keywords):
                return level
        return 'medium'

    def _extract_business_type(self, speech: str) -> str:
        """
        Extract business type if mentioned in the conversation
        """
        for business_type, keywords in self.business_types.items():
            if any(keyword in speech for keyword in keywords):
                return business_type
        return ''

    def _determine_next_actions(self, intent: str, interest_level: str) -> Dict[str, Any]:
        """
        Determine next actions based on intent and interest level
        """
        schedule_callback = interest_level in ['high', 'medium'] or intent in ['demo', 'implementation']
        send_info = interest_level != 'low'
        
        return {
            "schedule_callback": schedule_callback,
            "send_info": send_info,
            "notes": f"Intent: {intent}, Interest: {interest_level}"
        }

    def _extract_key_points(self, speech: str) -> list:
        """
        Extract key points discussed in the conversation
        """
        points = []
        for intent, keywords in self.intent_keywords.items():
            if any(keyword in speech for keyword in keywords):
                points.append(f"Discussed {intent}")
        return points 