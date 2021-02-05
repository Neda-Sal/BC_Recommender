# Contraception Recommender

## More details to come soon.

### Current Progress:

**Data Collection:** 60,000 reviews of 113 different contraception methods including IUDs, pills, implants, rings, patches, and emergency contraception.

**Data Processing:** Made all reviews lowercase, removed symbols, removed stop words including drug names.

**Topic Modeling:** 

*Current iteration:*   
NMF with TF-IDF Vectorizer to identify side effect clusters. Have so far identified six side effect clusters including acne, weight gain, mood swings, anxiety/depression, decreased sex drive.

**Recommendation Model:** 

*First iteration:*   
Takes user input for hormonal vs non-hormonal, method (IUD, pill, etc.), and returns highest rated contraception among those. User inputs the number of reviews they want to see for their recommendation.

*Current iteration:*   
Takes user input for hormonal vs non-hormonal, method (IUD, pill, etc.), any side effects they've struggled with, and returns highest rated contraception that has the lowest similarity scores between selecte side effects and average topic score per drug. User inputs the number of reviews they want to see for their recommendation.



