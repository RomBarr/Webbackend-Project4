# Helper functions:
import requests

def jsonify_message(message):
    return {"message": message}

# For games:
def compare_guess(guess, secret_word):
    correct_letters = set()
    correct_indices = []
    for sw_idx in range(0, len(secret_word)):
        for g_idx in range(0, len(guess)):
            if sw_idx == g_idx and guess[g_idx] == secret_word[sw_idx]:
                correct_indices.append(g_idx)
            if guess[g_idx] == secret_word[sw_idx]:
                correct_letters.add(guess[g_idx])
    return list(correct_letters), correct_indices


def check_guess(guess, secret_word):
    correct_letters, correct_indices = compare_guess(guess, secret_word)
    if len(secret_word) == len(correct_indices):
        is_correct = True
    else:
        is_correct = False
    return is_correct

def post_to_leaderboard(data):
    try:
        req = requests.post(url='http://127.0.0.1:3000/leaderboard/updateScore', json=data)
        print(r.status_code)
        return True
    except requests.exceptions.HTTPError:
        print('Queueing...')
        return False
