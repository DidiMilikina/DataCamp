'''
Using pytest
doctest is a great tool, but it's not nearly as powerful as pytest. In this exercise, you'll write tests for your SocialMedia class using the pytest framework.

Instructions 2/2
50 XP
2
import the SocialMedia class.
Complete the name of the test function so it is run by pytest.
Use the appropriate keyword
'''
SOLUTION

2
from collections import Counter
from text_analyzer import SocialMedia

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts
