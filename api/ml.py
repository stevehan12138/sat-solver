
class DummyModel:

    def predict(self, data):
        return {
            "answer": "m1",
            "raw_answer": data["m1"]
        }