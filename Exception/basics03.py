val = [
    {"Like" : 21, "Comment" : 2},
    {"Like" : 13, "Comment" : 2, "Shares" : 1},
    {"Like" : 33, "Comment" : 8, "Shares" : 3},
    {"Comment" : 4, "Shares" : 2},
    {"Comment" : 1, "Shares" : 1},
    {"Like" : 19, "Comment" : 3}
]

facebook_posts = val

total_likes = 0

for post in facebook_posts:
    try:
        like_count = post['Like']
    except KeyError:
        print("Key 'Like' is not present in this post")
        continue
    else:
        total_likes += like_count

print(total_likes)