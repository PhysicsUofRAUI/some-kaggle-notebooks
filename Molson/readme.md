# Purpose
To hold all of the work I have done compiling a list of beers brewed by companies owned by either Molson Coors or Miller Coors.

# Mistakes in the list
Give the complex web of ownerships in the beer world I am quite sure that I missed a few beers. On the flip side I may have included breweries that do not belong in this list, but I think that is unlikely.

# Description of the Data Collection
I first went to Molson Coors' website and navigated to the brands page at https://www.molsoncoors.com/brands/our-brands and then I used the Python program located at brands.py to scrape some information about the brands. All the information collected was placed into the brands.csv file.

Each brand in the brands.csv file was investigated to figure out what brewery owned it and verify that Molson Coors or Miller Coors owned that brewery. I then located the Beer Advocate (https://www.beeradvocate.com/) page for each brewery.

I then collected the data for every beer for that brewery and placed it in its own .csv file.

I now plan to put all the beers together in one large .csv file with the brewery listed in a separate column. For this I will use a jupyter notebook

# Credits of the Data
AC_Golden_Brewing_Company.csv: https://www.beeradvocate.com/beer/profile/17948/
Apatinska_Pivara_A.D..csv: https://www.beeradvocate.com/beer/profile/12226/
Bergenbier_SA.csv: https://www.beeradvocate.com/beer/profile/1704/
Borsodi_Brewery.csv: https://www.beeradvocate.com/beer/profile/2209/
Cobra_Beer_Partnership_Limited.csv: https://www.beeradvocate.com/beer/profile/10174/
Coors_Brewing_Company_(Molson-Coors).csv: https://www.beeradvocate.com/beer/profile/306/
Creemore_Springs_Brewery_Limited.csv: https://www.beeradvocate.com/beer/profile/455/
Franciscan_Well_Micro_Brewery.csv: https://www.beeradvocate.com/beer/profile/2294/
Granville_Island_Brewery.csv: https://www.beeradvocate.com/beer/profile/780/
Hamms_Brewing_Co..csv: https://www.beeradvocate.com/beer/profile/320/
Hop_Valley.csv: https://www.beeradvocate.com/beer/profile/19378/
Kamenitza_AD.csv: https://www.beeradvocate.com/beer/profile/2181/
Molson_Coors_Canada.csv: https://www.beeradvocate.com/beer/profile/433/
Pivovary_Staropramen.csv: https://www.beeradvocate.com/beer/profile/437/
Saint_Archer_Brewing_Co..csv: https://www.beeradvocate.com/beer/profile/31407/
Terrapin_Beer_Company.csv: https://www.beeradvocate.com/beer/profile/2372/
Thomas_Caffrey_Brewing_Co..csv: https://www.beeradvocate.com/beer/profile/297/
Trebjesa_Brewery.csv: https://www.beeradvocate.com/beer/profile/1943/
Zagrebaèka_Pivovara_D.d..csv: https://www.beeradvocate.com/beer/profile/1720/

# Next Steps
1. Look for outliers in the breweries, and styles. It should be easy with the 'describe' function of pandas. It may also be interesting to do similar analysis of the beer within the styles.
2. Get data from other sources and compare it to the data from Beer Advocate. In particular it would be nice to get data from those who do not like craft beers, and usually stick to the more "normal beers".

# Limitations
1. Those who rated the beer in most cases would have choose to drink it. That means that they will probably be biased towards the style or brand that they are drinking, and perhaps their rating is not objective.
2. The ratings are from only one website and that website may attract a certain type of users that like certain types of beer and not others.
3. It is likely that the person who rated the beer beforehand knew what style and what brewery made the beer and they may not be objective (similar to 1).
