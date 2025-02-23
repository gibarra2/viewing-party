# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

# janes_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }

# MOVIE_TITLE_1 = "It Came from the Stack Trace"

# print(watch_movie(janes_data, MOVIE_TITLE_1))

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

print("\n-----Wave 03 user_data-----")
pp.pprint(clean_wave_3_data())

print(get_unique_watched(clean_wave_3_data()))

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())
# get_available_recs(clean_wave_4_data())


# # Wave 05 user data
# print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())

# # get_new_rec_by_genre(clean_wave_5_data())
# get_rec_from_favorites(clean_wave_5_data())
