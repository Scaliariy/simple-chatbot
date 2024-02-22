from openai import OpenAI


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key="api_key")

    def get_response(self, user_input):
        response_ = self.client.chat.completions.create(
            # model="gpt-3.5-turbo-1106",
            model="gpt-4-1106-preview",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        )
        used_tokens = response_.usage
        print(used_tokens)
        return response_.choices[0].message.content, used_tokens


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hi")
    print(response)
