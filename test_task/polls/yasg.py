from drf_yasg import openapi

report_params = [
    openapi.Parameter(
        'customer',
        openapi.IN_QUERY,
        description="customer id",
        type=openapi.TYPE_INTEGER
    )
]

report_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'quiz': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(
                type=openapi.TYPE_OBJECT,
                properties={
                    'question': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='question_text'
                    ),
                    'answer_text': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='text'
                    ),
                    'choice': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='text'
                    ),
                },
            ),
            description='quiz_name'
        ),
    }
)

report_response = {
    "200": openapi.Response(
        description="Return dict of quizzes with customer answers",
        schema=report_response_schema,
        examples={
            "application/json": {
                "TestQuiz3": [
                    {
                        "question": "TestQuestion",
                        "answer_text": "",
                        "choice": "Choice1"
                    },
                ],
            }
        }
    )
}

answer_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'customer': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='customer ID'
        ),
        'answers': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='Question_id',
                        ),
                        'answer_text': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='text'
                        ),
                        'choices': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_INTEGER
                            ),
                            description='list of choice_id'
                        )
                    },
                    required=['id']
            ),
            description='list of questions with answers'
        ),
    },
    required=['customer', 'answers']
)
