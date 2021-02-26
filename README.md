# Contraception Recommender

## Try the live app [here](https://contraception-recommender.herokuapp.com/)!

### Current Progress:

**Data Collection:** 60,000 reviews of 113 different contraception methods including IUDs, pills, implants, rings, patches, and emergency contraception.

**Data Processing:** Made all reviews lowercase, removed symbols, removed stop words including drug names.

**Topic Modeling:** 

*Current iteration:*   
NMF with TF-IDF Vectorizer to identify side effect clusters. Have so far identified six side effect clusters including acne, weight gain, mood swings, anxiety/depression, decreased sex drive.

**Recommendation Model:** 

*First iteration:*   
Takes user input for hormonal vs non-hormonal, method (IUD, pill, etc.), and returns highest rated contraception among those. User inputs the number of reviews they want to see for their recommendation.

*Second iteration:*   
Takes user input for hormonal vs non-hormonal, method (IUD, pill, etc.), any side effects they've struggled with, and returns highest rated contraception that has the lowest similarity scores between selected side effects and average topic score per drug. User inputs the number of reviews they want to see for their recommendation.

*Current iteration (deployed):*
The current live version takes user input for hormonal and non-hormonal preferences, method (IUD, pill, etc.), any methods they've tried and don't want to see in their recommendations, and any side effects they've struggled with. The algorithm returns the method with the lowest cosine similarity between selected side effects and average topic score per drug. Links to the drugs.com page and the recommendation page are supplied with the recommendation.

*Next Steps:*
Adding a dropdown for medical history to help with the recommendation.   
Labeling pill types between progesterone only vs combination to include in the recommendation.   
Another round of topic modeling.  
  

