from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

    # Too High: should return 'Go LOWER!'
    assert "LOWER" in message.upper()
    
def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"

    # Too Low: should return 'Go HIGHER!'
    assert "HIGHER" in message.upper()

def test_update_score_win_first_attempt():
    # Winning on the first attempt should give 100 points
    assert update_score(0, "Win", 0) == 100

def test_update_score_win_later_attempt():
    # Winning on the 3rd attempt should give 80 points (100 - 10*2)
    assert update_score(0, "Win", 2) == 80

def test_update_score_too_high_penalty():
    # Too High should subtract 5 points
    assert update_score(50, "Too High", 1) == 45

def test_update_score_too_low_penalty():
    # Too Low should subtract 5 points
    assert update_score(50, "Too Low", 1) == 45

def test_update_score_minimum_points():
    # Winning after many attempts should give at least 10 points
    assert update_score(0, "Win", 20) == 10