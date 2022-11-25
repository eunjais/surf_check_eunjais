# Surf_Check

# Surf_Check

![logo](https://user-images.githubusercontent.com/107447038/200466271-675c0d51-55e3-4ac8-a701-a31bbafb7582.png)

## Overview

As a diehard lover of the ocean and surfing, and a user of surf resources such as surfline and magicseaweed, we were inspired to create our own website that can predict surf forecasts in the Golden State of California. The purpose of this project will be to analyze the best surfing conditions in popular surfing locations within California using the given parameters of: temperature, swell size + period + direction, wind direction, etc.  

#### Questions we are trying to answer:

- What are the average for the parameters in these beaches? 
- What popular surfing location in CA provides the most ideal surfing conditions in a given season? 
- Temperature, swell size/period and how they reflect any specific trends
- Accessibility to beaches overall
- Peak surfing times/locations, and determining these qualities?
- Categorize surf conditions by levels: beginner, intermediate, expert?


## Data Extraction Process

The list of different surfing beaches and their respective coordinates were scraped from [a Wikipedia article](https://en.wikipedia.org/wiki/List_of_beaches_in_California).  We utilized the  [The World Weather Online API](https://www.worldweatheronline.com/developer/api/marine-weather-api.aspx) to grab daily weather data for the different popular surfing beaches in California. JSON files from the World Weather API were restructured into a concise dataframe containing all the information that we specifically want. 


## Schema

![schema](https://user-images.githubusercontent.com/107447038/200467014-22c0b44f-0f66-487f-9dfe-6c681b06004d.jpg)


## Future Plans

#### Analysis


#### Machine Learning Portion
- We have decided to use Supervised Machine Learning to predict wheather waves are surfable or unsurfable. 
- The Supervised Machine Learning Algorithims we're using are:
	* Cluster Centroids Undersampling
	* Combination Sampling
	* SMOTE Oversampling
	* Native Random Oversampling
	* Balanced Random Forest Classifier
	* Easy Ensemble AdaBoost Classifer

#### Presentation
