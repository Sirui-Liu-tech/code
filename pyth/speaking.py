
import openai
openai.api_key = "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"

m = [
'Someteachers preferstudentstosendquestions about coursework andassignmentsby email. Other teachers prefer students askthese questions in person.Which do you think isbetter? Explain why.'
,'Do you agree or disagree that people will readess in the future.Give examples and details in your answer'
,'Many people think that students study coursematerials more effectively by taking exams, whileothers think that students earn more effectivethrough doing other activities such as writingpaper or completing projects, which do you thinkis more effective for students to learn.'
,'The university you plan to attend has offeredyou a choice of two possible dormitory rooms tolive in next year. One room is in a new dormitorywith many modern conveniences. The other is inan older but historically important building whereformer students who are now famous once livedExplain which you think would be a better choiceand why.Use specific details in your response.'
]

def askChatGPT(question):
    prompt = question
    model_engine = "gpt-3.5-turbo"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)

for i in m:
    askChatGPT(i)
