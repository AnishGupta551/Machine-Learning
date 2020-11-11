# -*- coding: utf-8 -*-
"""2020-11-02_Anish_Lesson22

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ULhZCDgAqq6klEmgZyamNbzZVQOGo8mx

# Lesson 22: Meteorite Landings - DataFrame Slicing

### Teacher-Student Activities

In the previous class, we learnt how to create a boxplot. In this class, we will continue from there. Today, we will learn how to slice a Pandas DataFrame to retrieve a specific set of rows and columns. This process is called slicing. In general, the term slicing means retrieving a specific portion of a dataset.

Let's rush through the activities that we did in the previous class and begin this class from the **Activities 1: Slicing A DataFrame** section.

---

#### The Data

The dataset contains the following variables:

1. `name`: the name of the place where a meteorite was found or observed.

2. `id`: a unique identifier for a meteorite.

3. `nametype`: one of the following:
    
    - `valid`: a typical meteorite.
    
    - `relict`: a meteorite that has been highly degraded by the weather on Earth.

4. `recclass`: the class of the meteorite; one of a large number of classes based on physical, chemical, and other characteristics. 

5. `mass:` the mass of the meteorite, in grams

6. `fall`: whether the meteorite was seen falling, or was discovered after its impact; one of the following:

    - `Fell`: the meteorite's fall was observed.
    
    - `Found`: the meteorite's fall was not observed.

7. `year`: the year the meteorite fell, or the year it was found (depending on the value of fell).

8. `reclat`: the latitude of the meteorite's landing.

9. `reclong`: the longitude of the meteorite's landing.

10. `GeoLocation`: a parentheses-enclose, comma-separated tuple that combines reclat and reclong.

---

#### Notes On Missing Or Incorrect Data Points

1. The column names such as `recclass`, `reclat`, `reclong` begin with the `rec` (denotes 'recommended') keyword. They are the recommended values of the classes, latitudes and longitudes variables for the meteorites according to the Meteoritical Society. 

2. Remove any year less than `860` or greater than `2016` from the dataset. 

3. Remove the `0N/0E` latitude and longitude entries.

---

#### Loading The Dataset

Dataset Link (don't click on it):

https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv
"""

# Import the necessary libraries for this class and create a DataFrame.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

met_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv')
met_df.head()

"""---

#### Tuples
"""

# Number of rows in the 'met_df' DataFrame.
print("Number of rows =", met_df.shape[0])

# Number of columns in the 'met_df' DataFrame.
print("Number of columns =", met_df.shape[1])

"""---

#### The `describe()` Function
"""

# Descriptive statistics for the 'year' values in the 'met_df' DataFrame. 
met_df['year'].describe()

"""---

#### The Boxplot

<img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/boxplot_description.png' width='800'>
"""

# Boxplot for the 'pd_series'.
import seaborn as sns # 'sns' is an alias for 'seaborn'.

plt.figure(figsize=(20, 1))
sns.boxplot(met_df['year'])
plt.show()

"""---

#### Activity 1: Slicing A DataFrame

Our next task is to remove all the rows having the year values less than `2016` and greater than `2016`. To do this exercise, we will write a condition inside the square brackets after writing the variable containing the DataFrame.

**Syntax:** `data_frame[some_condition]`

To learn this concept, let's retrieve all the rows containing the `year` values less than or equal to `2016`.
"""

# Teacher Action: Retrieve all the rows from the 'met_df' DataFrame containing the year values less than or equal to 2016.
met_df[met_df['year'] <= 2016]

"""Because of the condition `met_df['year'] <= 2016`, the `met_df` DataFrame will return only those rows in which the year values are less than or equal to `2016`.

At the bottom of the DataFrame, you can see that there are 45,426 rows having the `year` values less than or equal to `2016`. Now, you try to retrieve all the rows having the `year` value greater than or equal to `860` using the same process.
"""

# Student Action: Retrieve all the rows having the year values greater than or equal to 860.
met_df[met_df["year"] >= 860]

"""Because of the condition `met_df['year'] >= 860`, the `met_df` DataFrame will return only those rows in which the year values are greater than or equal to `860`.


So, there are also 45,426 rows having the `year` values greater than or equal to `2016`.

---

#### Activity 2: The Ampersand (`&`) Logical Operator^^

Now, let's retrieve all the rows having the `year` values greater than or equal to `860` and less than or equal to `2016` (i.e., 
$ 860 \le \text{year} \le 2016$
). We will use the **ampersand** logical operator (denoted by the **&** symbol) to combine the above two conditions.
"""

# Teacher Action: Retrieve the rows containing the year values less than 860 and greater than 2016 at the same time.
corrected_year_df=met_df[(met_df['year'] >= 860) & (met_df['year'] <= 2016)]
corrected_year_df.head()

"""Because of the condition `(met_df['year'] >= 860) & (met_df['year'] <= 2016)`, the `met_df` DataFrame will return only those rows in which the year values are greater than or equal to `860` and less than or equal to `2016` .


So in this way, we can slice a DataFrame to get some specific rows by providing a condition in the square brackets. Now, let's find out how many rows are there in the `met_df` DataFrame having the `year` values either less than `860` or greater than `2016`.
"""

# Student Action: Compute the number of rows having the year values either less than 860 or greater than 2016 in the 'met_df' DataFrame.
met_df.shape[0]-corrected_year_df.shape[0]

"""So, there are 292 rows having the `year` values either less than `860` or greater than `2016` in the `met_df` DataFrame. Hence, we have obtained the DataFrame with the correct `year` values.

Let's calculate the percentage of values we have retained in the `correct_years_df` DataFrame as compared to the `met_df` DataFrame.
"""

# Student Action: Calculate the percent of values retained.
print((corrected_year_df.shape[0]/met_df.shape[0])*100)

"""---

#### Activity 3: The `round()` Function

The percentage value that we obtained has many digits after the decimal point. We can use the `round()` function to set the maximum number of digits to be displayed after the decimal point. It takes two inputs.

1. The floating-point value that needs to be rounded off.

2. The maximum number of digits to be displayed after the decimal point.

Here's the syntax of the `round()` function.

**Syntax:** `round(value_to_be_rounded_off, number_of_digits_to_be_displayed_after_decimal_point)`
"""

# Student Action: Calculate the percent of values retained that is rounded off to two digits after the decimal point.
print(round((corrected_year_df.shape[0]/met_df.shape[0])*100, 2))

"""So, after filtering out the rows for the years before `860` and after `2016`, we still have retained 99% of the data-points. Let's also look at the descriptive statistics for the `year` column in the `correct_years_df`."""

# Student Action: Get the descriptive statistics for the 'year' column in the 'correct_years_df'
corrected_year_df["year"].describe()

"""As you can see, the minimum value of the `year` is `860` and the maximum value is `2013`. This also confirms the filtering of the `year` values was a successful exercise.

Let's also make a boxplot for the `year` values in the `correct_years_df` DataFrame to see the effect of the removal of the unwanted `year` values.
"""

# Student Action: Make a boxplot for the 'year' column in the 'correct_years_df' DataFrame.
plt.figure(figsize=(20, 2))

sns.boxplot(corrected_year_df["year"])
plt.show()

"""The box representing the interquartile range appears expanded compared to the box in the previous boxplot. It also shows the median value is close to the third quartile value. Also, there are too many lower outliers as shown by the black dots.

---

#### Activity 4: Removing The Invalid `reclong` Values^

The longitude values go from 
$-180^{\circ}$ to $180^{\circ}$ 
where positive values represent the eastward direction and the negative values represent the westward direction. The 
$0^{\circ}$ 
longitude is called the prime meridian. Refer to the image below for more details.

<img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/britannica_longitudes.jpg' width='800'>

*Image Credits: https://cdn.britannica.com/06/64906-050-675D6688/meridians-Facts-Lines-of-Longitude-angles-halves.jpg*

Now, let's remove the rows containing the `reclong` values greater than 
$180^{\circ} $
and less than 
$-180^{\circ}$
. But first, let's retrieve all the rows containing the `reclong` values less than or equal to 
$ 180^{\circ} $
"""

# Student Action: Retrieve all the rows from the 'correct_years_df' DataFrame having the 'reclong' values less than or equal to 180 degrees.
corrected_year_df[corrected_year_df["reclong"] <= 180]

"""So, there are 38,221 rows which have the `reclong` values less than or equal to 
$180^{\circ}$
. Now, let's retrieve all the rows which have the `reclong` values greater than or equal to 
$-180^{\circ}$
"""

# Student Action: Retrieve all the rows from the 'correct_years_df' DataFrame having the 'reclong' values greater than or equal to -180 degrees.
corrected_year_df[corrected_year_df["reclong"] >= -180]

"""So, there are 38,222 rows which have the `reclong` values greater than or equal to 
$180^{\circ}$
. Now, let's combine both the conditions using the Ampersand (`&`) logical operator to combine the above two conditions.
"""

# Student Action: Retrieve all the rows having the 'reclong' values greater than or equal to -180 degrees and less than or equal to 180 degrees.
corrected_reclong_df = corrected_year_df[(corrected_year_df["reclong"]<= 180) & (corrected_year_df["reclong"]>= -180)]
corrected_reclong_df

"""So, there are 38,221 rows having the correct `reclong` values.

---

#### Activity 5: Removing The Rows Containing `0 N, 0 E` Values Using The Tilde (`~`) Operator^^^

There are also some rows which contain the `0 reclat` and `0 reclong` values. *It is also the point of intersection of the prime meridian and the Equator*. We need to remove such rows because this pair of coordinates represent the portion of the Atlantic Ocean near the west coast of Africa (refer to the image below) from where it is difficult to recover the fallen meteorites.

<img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/zero_north_zero_east.png' width='500'>

Let's retrieve all the rows having the `0 reclat` and `0 reclong` values.
"""

# Student Action: Retrieve the rows containing the '0 reclat' and '0 reclong' values from the 'correct_long_df' DataFrame.
corrected_reclong_df[(corrected_reclong_df["reclong"]==0) & (corrected_reclong_df["reclat"]==0)]

"""So, there are 6,185 rows containing the `0 reclat` and `0 reclong` values in the `correct_long_df`. Let's remove them using the tilde (`~`) operator.

The tilde operator denotes the negation of a condition. In other words, it converts the `True` value to `False` value and vice-versa.
"""

# Teacher Action: Get only the rows having the 'reclat' value equal to 0.
corrected_reclong_df[corrected_reclong_df['reclat']==0]

"""So, there are 6,409 rows having the `reclat` value equal to `0` in the `correct_long_df`. Now, let's get only the rows **NOT** having the `reclat` value equal to 0 using the tilde (or negation) operator."""

# Teacher Action: Get only the rows NOT having the 'reclat' value equal to 0. Use the tilde operator for this operation.
corrected_reclong_df[~(corrected_reclong_df['reclat']==0)]

"""So, there are 31,812 rows in the `correct_long_df` **NOT** having the `reclat` value equal to `0`. Now, let's get the rows **neither** having the `reclat` value equal to 0 **nor** having the `reclong` value equal to `0` using the tilde (or negation) operator. Store the new DataFrame in the `correct_lat_long_df` variable.

We already know that there are 6,185 rows having both the `reclat` and `reclong` values equal to `0` in the `correct_long_df`. So, after removing these rows, we should have a total of (38,221 - 6,185 = 32,036) rows in the new DataFrame.
"""

# Teacher Action: Remove the rows containing the 0 'reclat' and 0 'reclong' values from the 'correct_long_df'.
corrected_latlong_df=corrected_reclong_df[~((corrected_reclong_df["reclong"]==0) & (corrected_reclong_df["reclat"]==0))]
corrected_latlong_df

"""As you can see, after the removal of the rows containing the unwanted `reclat` and `reclong` values, we have a new DataFrame containing 32,036 rows.

Let's check the percentage of values we have retained so far.
"""

# Student Action: Calculate the percentage of values retained in the new DataFrame from the 'met_df' DataFrame.
# Also, round-off the value to two digits after the decimal point.
round((corrected_latlong_df.shape[0]/met_df.shape[0])*100, 2)

"""So far we have retained the approx 70% of the values which is still quite a big dataset.

In the next class, we will learn about logical operations more so that you get comfortable with this concept because a large part of the data cleaning process involves applying the relevant logical operations. Afterwards, we will continue with data cleaning exercises.

---
"""