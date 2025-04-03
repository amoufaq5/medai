# dialogue/dialogue_system.py
import logging

logger = logging.getLogger(__name__)

class DialogueSystem:
    def __init__(self, model_path="./trained_model.h5"):
        # Load the trained TensorFlow model for diagnosis.
        try:
            import tensorflow as tf
            self.model = tf.keras.models.load_model(model_path)
            logger.info("Diagnosis model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading diagnosis model: {e}")
            self.model = None

    def parse_input(self, user_input):
        # Parse input based on ASMETHOD, ENCORE, and SIT DOWN SIR frameworks.
        # For demonstration, we simply map the raw input into one field.
        parsed_data = {
            "age_appearance": None,
            "self_or_other": None,
            "medication": None,
            "extra_medicines": None,
            "time_persisting": None,
            "history": None,
            "other_symptoms": None,
            "danger_symptoms": None,
            "explore": None,
            "no_medication": None,
            "care": None,
            "observe": None,
            "refer": None,
            "explain": None,
            "site": None,
            "intensity": None,
            "type": None,
            "duration": None,
            "onset": None,
            "with_other": None,
            "annoyed": None,
            "spread": None,
            "frequency": None,
            "relieved": None
        }
        parsed_data["other_symptoms"] = user_input
        return parsed_data

    def diagnose(self, parsed_data):
        # Decision engine: if danger symptoms are present (e.g., keyword “severe”), then refer to doctor.
        if "severe" in parsed_data["other_symptoms"].lower():
            diagnosis = "Severe condition detected. Please consult a doctor immediately."
        else:
            diagnosis = "Mild symptoms detected. OTC medications may be appropriate."
        return diagnosis

    def generate_response(self, user_input):
        parsed_data = self.parse_input(user_input)
        diagnosis = self.diagnose(parsed_data)
        response = (f"Diagnosis: {diagnosis}\n"
                    f"Based on information collected using ASMETHOD, ENCORE, and SIT DOWN SIR frameworks.")
        return response

if __name__ == "__main__":
    ds = DialogueSystem()
    sample_input = "I have a mild headache and fever."
    response = ds.generate_response(sample_input)
    print(response)
