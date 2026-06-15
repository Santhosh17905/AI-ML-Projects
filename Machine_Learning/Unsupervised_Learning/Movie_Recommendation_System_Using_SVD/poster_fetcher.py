poster_dict = {
    "Avengers": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg",
    "Batman": "https://i.ebayimg.com/images/g/qtAAAOSw81tkWi6C/s-l1600.jpg",
    "Spider-Man": "http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg",
    "Iron Man": "http://cdn.shopify.com/s/files/1/0037/8008/3782/products/IMG_4737_1-550469_6ad2415d-59de-4f0c-8cb7-a3f1be291340.jpg?v=1656424801",
    "Thor": "https://wallpaperaccess.com/full/645172.jpg",
    "Babe (1995)": "https://upload.wikimedia.org/wikipedia/en/0/0c/Babe_ver1.jpg",
    "Bad Seed, The (1956)": "https://upload.wikimedia.org/wikipedia/en/5/5c/The_Bad_Seed.jpg",
    "Rounders (1998)": "https://upload.wikimedia.org/wikipedia/en/7/7d/RoundersPoster.jpg",
    "Hour of the Pig, The (1993)": "https://upload.wikimedia.org/wikipedia/en/8/8c/The_Advocate.jpg",
    "Firelight (1997)": "https://upload.wikimedia.org/wikipedia/en/2/2d/Firelight1997Poster.jpg",
    # plus your Avengers, Batman, Spider-Man, Iron Man, Thor entries
}

def get_poster(movie):
    # Normalize input (remove year, lowercase, strip spaces)
    normalized = movie.lower().split("(")[0].strip()
    
    for key in poster_dict:
        if key.lower() in normalized:
            return poster_dict[key]
    
    return "https://via.placeholder.com/200x300?text=Movie"