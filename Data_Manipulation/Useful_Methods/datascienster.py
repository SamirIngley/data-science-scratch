# Datascienster social network platform

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# friendship data
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# FINDING KEY CONNECTORS in the networks

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# Loop over friendship pairs to populate it
for i, j in friendship_pairs:
    friendships[i].append(j)    # j as friend of i
    friendships[j].append(i)    # i as friend of j

def number_of_friends(user):
    ''' How many friends does _user_ have?'''
    user_id = 
    friends_ids = friendships[user_id]
    return len(friend_ids)


if __name__ == "__main__":
    
    number_of_friends(0)