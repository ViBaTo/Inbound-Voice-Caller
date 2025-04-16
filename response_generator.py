from twilio.twiml.voice_response import VoiceResponse, Gather
from typing import Dict, Any

class ResponseGenerator:
    def __init__(self):
        self.responses = {
            'greeting': "¡Hola! Soy el asistente virtual de VIBATO AI. ¿En qué puedo ayudarte hoy?",
            'introduction': "En VIBATO AI, creamos soluciones de inteligencia artificial personalizadas para optimizar los procesos de tu negocio, mejorar la atención al cliente y aumentar la eficiencia operativa.",
            'information': {
                'low': "Me encantaría contarte más sobre cómo VIBATO AI puede transformar tu negocio. ¿Podrías decirme en qué sector te encuentras?",
                'medium': "VIBATO AI ofrece soluciones personalizadas que pueden revolucionar tu negocio. ¿Te gustaría saber más sobre cómo podemos ayudarte específicamente?",
                'high': "¡Excelente! VIBATO AI está diseñado para optimizar procesos y mejorar resultados. ¿Podrías compartir más detalles sobre tu negocio?"
            },
            'pricing': {
                'low': "Nuestras soluciones se adaptan a cada negocio. ¿Te gustaría que te explique nuestros diferentes planes y cómo pueden beneficiar a tu empresa?",
                'medium': "Ofrecemos planes flexibles que se ajustan a las necesidades de tu negocio. ¿Podrías decirme qué aspectos te interesan más?",
                'high': "Trabajamos con planes personalizados según las necesidades de cada cliente. ¿Te gustaría que te explique nuestras opciones?"
            },
            'demo': {
                'low': "Podemos programar una demostración personalizada para mostrar cómo VIBATO AI puede beneficiar a tu negocio. ¿Te interesa?",
                'medium': "Una demostración es la mejor manera de ver cómo VIBATO AI puede transformar tu negocio. ¿Cuándo te vendría bien?",
                'high': "¡Perfecto! Podemos organizar una demostración personalizada. ¿Qué día y hora te viene mejor?"
            },
            'implementation': {
                'low': "La implementación de VIBATO AI es sencilla y guiada. ¿Te gustaría saber más sobre el proceso?",
                'medium': "Nuestro equipo te acompañará en cada paso de la implementación. ¿Cuándo te gustaría comenzar?",
                'high': "Podemos comenzar la implementación inmediatamente. ¿Te gustaría que te explique el proceso?"
            },
            'specific_use': {
                'low': "VIBATO AI se adapta a múltiples sectores. ¿Podrías contarme más sobre tu negocio para poder ofrecerte la mejor solución?",
                'medium': "Nuestras soluciones son personalizables para cada sector. ¿Qué aspectos específicos te interesan?",
                'high': "Podemos crear una solución específica para tus necesidades. ¿Qué desafíos te gustaría resolver con IA?"
            },
            'follow_up': "¿Te gustaría programar una llamada de seguimiento con uno de nuestros especialistas para profundizar en cómo VIBATO AI puede ayudar a tu negocio?",
            'goodbye': "Gracias por tu interés en VIBATO AI. ¡Esperamos poder ayudarte a transformar tu negocio con inteligencia artificial!"
        }

    def generate_response(self, analysis: Dict[str, Any]) -> VoiceResponse:
        """
        Generate appropriate TwiML response based on call analysis
        """
        response = VoiceResponse()
        intent = analysis['conversation']['intent']
        interest_level = analysis['conversation']['interest_level']
        
        # Add greeting and introduction
        response.say(self.responses['greeting'])
        response.say(self.responses['introduction'])
        
        # Add specific response based on intent and interest level
        response.say(self.responses[intent][interest_level])
        
        # Add gather for further input
        gather = Gather(
            input='speech',
            action='/analyze',
            method='POST',
            timeout=5,
            speech_timeout='auto'
        )
        
        # If high interest or specific intent, suggest follow-up
        if interest_level in ['high', 'medium'] or intent in ['demo', 'implementation']:
            gather.say(self.responses['follow_up'])
        else:
            gather.say("¿Hay algo más en lo que pueda ayudarte?")
            
        response.append(gather)
        
        # Add fallback message
        response.say("No he recibido respuesta. Por favor, intenta de nuevo.")
        response.redirect('/analyze')

        return response 