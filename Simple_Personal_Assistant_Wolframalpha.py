import wolframalpha

# App id obtained by the above steps
app_id = 'Your app_id'

while True:
    # Taking input from user
    question = input('Question: ')

    if question == 'exit':
        break

    try:
        # Instance of wolfram alpha client class
        client = wolframalpha.Client(app_id)

        # Stores the response from wolfram alpha
        res = client.query(question)

        # Includes only text from the response
        answer = next(res.results).text

        print(answer)

    except StopIteration:
        print("No result found for the question: ", question)
    except Exception as e:
        print("Error: ", e)

