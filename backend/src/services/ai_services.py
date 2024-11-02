# from transformers import pipeline

# class AIService:
#     def __init__(self):
#         self.diagnostic_model = self.cargar_modelo()

#     def cargar_modelo(self):
#         # Cargar tu modelo de Hugging Face aquí
#         pass

#     def diagnosticar_historia_clinica(self, historia_clinica: str) -> str:
#         # Mejora del prompt
#         prompt = (
#             "Eres un médico que está revisando la siguiente historia clínica. "
#             "Por favor, proporciona un diagnóstico detallado y claro:\n\n"
#             f"{historia_clinica}\n\n"
#             "Diagnóstico:"
#         )
        
#         # Genera la respuesta con ajustes
#         resultado = self.diagnostic_model(
#             prompt,
#             max_length=300,
#             num_return_sequences=1,
#             do_sample=True,
#             temperature=0.7,
#             top_k=50,
#             truncation=True,
#             pad_token_id=self.diagnostic_model.tokenizer.eos_token_id
#         )
        
#         # Extrae el texto generado
#         diagnostico = resultado[0]['generated_text']
        
#         # Extrae solo el diagnóstico relevante
#         return self.extraer_diagnostico(diagnostico)

#     def extraer_diagnostico(self, texto: str) -> str:
#         # Aquí puedes implementar la lógica para extraer el diagnóstico
#         # Por ejemplo, puedes buscar frases específicas en el texto.
#         return texto.strip()  # Retorna el texto tal cual por ahora.


