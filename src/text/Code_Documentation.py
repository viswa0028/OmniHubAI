import google.generativeai as genai
class Gemini:
    def __init__(self):
        genai.configure(api_key="AIzaSyAL_T-aOIbZXaBtZuheDmPJ2_MKrpeBAV0")  
    def CodeDocumentation(self,function):
        genrative_config = {"temperature": 0.9, "top_p": 1, "top_k": 1} 
        model = genai.GenerativeModel("gemini-pro", generation_config=genrative_config)
        try:
            question = model.generate_content(f'First give me the uses of the function, Then give me the uses of the parameters and give me what the function returns in the text form in the form of individual comments and do not give me a code in it and the code is {function} and also the complete thing should be in """""')
            response = question.text
            return response
        except Exception as e:
            return f"Error in generating Response: {e}"