import requests

SUGGESTIONS_TOTAL = 100
SUGGESTION_IDS = range(1, SUGGESTIONS_TOTAL + 1)

##We need the API site below where it says 'api site url'
def get_suggestion(suggestion_id):
    return requests.get(f"api site url{suggestion_id}")

def get_random_suggestion_list():
    random_suggestion_ids = random.sample(SUGGESTION_IDS, k=1)
    return [get_suggestion(suggestion_id) for suggestion_id in random_suggestion_ids]


