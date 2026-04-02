# Movie Preference Analysis Task

## Input
Analyze the following CSV containing a user's watched movie history. The CSV includes the columns: `Film Title` and `Rating`.

## Objective
1. **Estimate the user's age range** based on the release years of the watched movies and their ratings.
2. **Calculate genre preferences** as a normalized score (0 to 1) for each of the following genres:
   - Action
   - Adventure
   - Animation
   - Biography
   - Comedy
   - Crime
   - Documentary
   - Drama
   - Family
   - Fantasy
   - History
   - Horror
   - Musical
   - Mystery
   - Romance
   - Sci-Fi (Science Fiction)
   - Sport
   - Thriller
   - War
   - Western

3. **Identify the top 4 most appreciated genres** based on the highest scores.
4. **Output only the JSON** in the following format:

```json
{
  "profile": {
    "age_range": [min_age, max_age],
    "genres": {
      "Action": score,
      "Adventure": score,
      "Animation": score,
      "Biography": score,
      "Comedy": score,
      "Crime": score,
      "Documentary": score,
      "Drama": score,
      "Family": score,
      "Fantasy": score,
      "History": score,
      "Horror": score,
      "Musical": score,
      "Mystery": score,
      "Romance": score,
      "Sci-Fi": score,
      "Sport": score,
      "Thriller": score,
      "War": score,
      "Western": score
    },
    "top_genres": [
      "Genre1",
      "Genre2",
      "Genre3",
      "Genre4"
    ]
  }
}

Here is the CSV :
