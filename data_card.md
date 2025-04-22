# NCAA Data

This dataset contains historical data for the NCAA Men's and Women's Basketball Tournaments, which includes detailed information about team performances, tournament seeds, game results, and scheduling. The data is sourced from multiple CSV files, each containing specific aspects of the tournament history and structure. The primary purpose of this dataset is to build predictive models for tournament outcomes and game scheduling.

#### Dataset Link

[Kaggle](https://www.kaggle.com/competitions/march-machine-learning-mania-2025/data)

#### Data Card Author(s)

-   **Cesar Ramirez, Group 9:** Contributor
-   **Alma Campos, Group 9:** Contributor
-   **Moheson Alavian, Group 9:** Contributor
-   **Gauri Joshi, Group 9:** Contributor
-   **Rutik Narute, Group 9:** Contributor
-   **Denise Tabilas, Group 9:** Contributor
-   **Rishab Lakhotra, Group 9:** Contributor
-   **Alex Alcazar, Group 9:** Contributor
-   **Moheson Alavian, Group 9:** Contributor
-   **Kris Kajar, Group 9:** Contributor

## Authorship

### Publishers

#### Publishing Organization(s)

Kaggle

#### Industry Type(s)

-   Academic - Tech

#### Contact Detail(s)

-   **Website:** [Kaggle](https://www.kaggle.com/)

### Dataset Owners

#### Team(s)

Kenneth Massey
Sonas Consulting

#### Contact Detail(s)

-   **Dataset Owner(s):** Kenneth Massey, Jeff Sonas, Sonas Consulting
-   **Affiliation:** Massey Ratings, Sonas Consulting
-   **Website:** [Massey Ratings](http://www.masseyratings.com/)

## Dataset Overview

#### Data Subject(s)

-   The Basics
-   Team Box Scores
-   Geography
-   Public Rankings
-   Supplements

#### Dataset Snapshot

| Category            | Data      |
| ------------------- | --------- |
| Size of Dataset     | 182.97 MB |
| Number of Instances | 2636297   |
| Number of Fields    | 282       |
| Labeled Classes     | 32        |

#### Content Description

**The Basics**

-   Team ID's and Team Names
-   Tournament seeds since 1984-85 season
-   Final scores of all regular season, conference tournament, and NCAA® tournament games since 1984-85 season
-   Season-level details including dates and region names

**Team Box Scores**
Game-by-game stats at a team level

-   WFGM - field goals made (by the winning team)
-   WFGA - field goals attempted (by the winning team)
-   WFGM3 - three pointers made (by the winning team)
-   WFGA3 - three pointers attempted (by the winning team)
-   WFTM - free throws made (by the winning team)
-   WFTA - free throws attempted (by the winning team)
-   WOR - offensive rebounds (pulled by the winning team)
-   WDR - defensive rebounds (pulled by the winning team)
-   WAst - assists (by the winning team)
-   WTO - turnovers committed (by the winning team)
-   WStl - steals (accomplished by the winning team)
-   WBlk - blocks (accomplished by the winning team)
-   WPF - personal fouls committed (by the winning team)

**Geography**

-   City locations of all regular season, conference tournament, and NCAA® tournament games since the 2010 season

**Public Rankings**

-   Weekly team rankings (men's teams only) for dozens of top rating systems - Pomeroy, Sagarin, RPI, ESPN, etc., since the 2003 season

**Supplements**

-   Additional supporting information, including coaches, conference affiliations, alternative team name spellings, bracket structure, and game results for NIT and other postseason tournaments.

#### Descriptive Statistics

**Team Statistics**

| Statistic | TeamID      | GamesPlayed | Wins        | Losses     | RegularSeasonGames |
| --------- | ----------- | ----------- | ----------- | ---------- | ------------------ |
| count     | 380.000000  | 380.000000  | 380.000000  | 380.000000 | 380.000000         |
| mean      | 1290.500000 | 1028.673684 | 514.336842  | 514.336842 | 1015.421053        |
| std       | 109.840794  | 338.935823  | 228.058797  | 174.132262 | 330.188419         |
| min       | 1101.000000 | 22.000000   | 3.000000    | 16.000000  | 22.000000          |
| 25%       | 1195.750000 | 1039.000000 | 393.750000  | 458.500000 | 1038.000000        |
| 50%       | 1290.500000 | 1159.500000 | 533.000000  | 559.500000 | 1155.000000        |
| 75%       | 1385.250000 | 1227.250000 | 669.000000  | 634.000000 | 1215.000000        |
| max       | 1480.000000 | 1441.000000 | 1153.000000 | 869.000000 | 1307.000000        |

| Statistic | TournamentGames | HomeGames  | AwayGames  | NeutralGames | WinPercentage |
| --------- | --------------- | ---------- | ---------- | ------------ | ------------- |
| count     | 380.000000      | 380.000000 | 380.000000 | 380.000000   | 380.000000    |
| mean      | 13.252632       | 455.707895 | 455.707895 | 117.257895   | 48.031105     |
| std       | 21.403754       | 170.107048 | 145.575036 | 69.392173    | 11.103786     |
| min       | 0.000000        | 9.000000   | 10.000000  | 0.000000     | 12.500000     |
| 25%       | 1.000000        | 402.500000 | 429.250000 | 71.750000    | 40.560000     |
| 50%       | 5.000000        | 494.000000 | 489.000000 | 110.500000   | 47.980000     |
| 75%       | 14.000000       | 577.000000 | 556.000000 | 156.250000   | 55.422500     |
| max       | 137.000000      | 707.000000 | 668.000000 | 396.000000   | 80.010000     |

| Statistic | TournamentParticipationRate | NumSeasons | AvgGamesPerSeason |
| --------- | --------------------------- | ---------- | ----------------- |
| count     | 380.000000                  | 380.000000 | 380.000000        |
| mean      | 1.062868                    | 35.231579  | 28.994316         |
| std       | 1.575389                    | 11.178761  | 1.803911          |
| min       | 0.000000                    | 1.000000   | 22.000000         |
| 25%       | 0.147500                    | 37.000000  | 27.867500         |
| 50%       | 0.505000                    | 41.000000  | 29.000000         |
| 75%       | 1.152500                    | 41.000000  | 30.070000         |
| max       | 9.510000                    | 41.000000  | 35.150000         |

**Top 10 Teams by Games Played:**

| Team | TeamName       | GamesPlayed | Wins | Losses | WinPercentage |
| ---- | -------------- | ----------- | ---- | ------ | ------------- |
| 80   | Duke           | 1441        | 1153 | 288    | 80.01         |
| 213  | North Carolina | 1436        | 1062 | 374    | 73.96         |
| 141  | Kansas         | 1411        | 1121 | 290    | 79.45         |
| 145  | Kentucky       | 1400        | 1055 | 345    | 75.36         |
| 11   | Arizona        | 1366        | 1022 | 344    | 74.82         |
| 292  | Syracuse       | 1362        | 953  | 409    | 69.97         |
| 176  | Michigan St    | 1350        | 930  | 420    | 68.89         |
| 156  | Louisville     | 1346        | 884  | 462    | 65.68         |
| 62   | Connecticut    | 1344        | 927  | 417    | 68.97         |
| 336  | Villanova      | 1339        | 882  | 457    | 65.87         |

**Top 10 Teams by Win Percentage (min 100 games):**

| Team | TeamName       | GamesPlayed | Wins | Losses | WinPercentage |
| ---- | -------------- | ----------- | ---- | ------ | ------------- |
| 80   | Duke           | 1441        | 1153 | 288    | 80.01         |
| 141  | Kansas         | 1411        | 1121 | 290    | 79.45         |
| 145  | Kentucky       | 1400        | 1055 | 345    | 75.36         |
| 110  | Gonzaga        | 1277        | 960  | 317    | 75.18         |
| 11   | Arizona        | 1366        | 1022 | 344    | 74.82         |
| 213  | North Carolina | 1436        | 1062 | 374    | 73.96         |
| 292  | Syracuse       | 1362        | 953  | 409    | 69.97         |
| 171  | Memphis        | 1326        | 916  | 410    | 69.08         |
| 62   | Connecticut    | 1344        | 927  | 417    | 68.97         |
| 176  | Michigan St    | 1350        | 930  | 420    | 68.89         |

**Conference Statistics Summary:**
Statistic | GamesPlayed | Wins | Losses | IntraConferenceGames
--- | --- | --- | --- | ---
count | 51.000000 | 51.000000 | 51.000000 | 51.000000  
mean | 7664.627451 | 3832.313725 | 3832.313725 | 2350.235294  
std | 5056.436366 | 2702.737460 | 2496.991289 | 1613.305149  
min | 201.000000 | 60.000000 | 104.000000 | 30.000000  
25% | 2584.000000 | 1433.000000 | 1079.000000 | 663.500000  
50% | 8497.000000 | 4131.000000 | 4422.000000 | 2509.000000  
75% | 11776.500000 | 5651.000000 | 6193.500000 | 3776.000000  
max | 15906.000000 | 9373.000000 | 7413.000000 | 4741.000000

| Statistic | InterConferenceGames | TournamentGames | TournamentWins | WinPercentage |
| --------- | -------------------- | --------------- | -------------- | ------------- |
| count     | 51.000000            | 51.000000       | 51.000000      | 51.000000     |
| mean      | 2865.411765          | 98.745098       | 49.372549      | 49.107843     |
| std       | 1834.971806          | 148.593788      | 93.777601      | 7.179466      |
| min       | 85.000000            | 0.000000        | 0.000000       | 29.850000     |
| 25%       | 1135.000000          | 27.000000       | 4.000000       | 45.100000     |
| 50%       | 3618.000000          | 47.000000       | 10.000000      | 48.670000     |
| 75%       | 4233.000000          | 103.000000      | 37.500000      | 54.250000     |
| max       | 5943.000000          | 592.000000      | 389.000000     | 60.800000     |

| Statistic | TournamentWinPercentage | IntraConfPercentage | NumSeasons |
| --------- | ----------------------- | ------------------- | ---------- |
| count     | 48.000000               | 51.000000           | 51.000000  |
| mean      | 34.551875               | 29.316863           | 26.058824  |
| std       | 19.500014               | 4.853258            | 15.532433  |
| min       | 0.000000                | 11.190000           | 1.000000   |
| 25%       | 18.712500               | 29.120000           | 11.500000  |
| 50%       | 33.580000               | 30.730000           | 30.000000  |
| 75%       | 50.950000               | 32.330000           | 41.000000  |
| max       | 66.670000               | 34.620000           | 41.000000  |

| Statistic | AvgGamesPerSeason |
| --------- | ----------------- |
| count     | 51.000000         |
| mean      | 272.038824        |
| std       | 66.332431         |
| min       | 100.500000        |
| 25%       | 226.810000        |
| 50%       | 279.120000        |
| 75%       | 297.565000        |
| max       | 389.230000        |

**Top 10 Conferences by Games Played:**
Conference | Description | GamesPlayed | Wins | Losses
--- | --- | --- | --- | ---
19 | Southeastern Conference | 15906 | 9373 | 6533  
31 | Atlantic 10 Conference | 15392 | 8202 | 7190  
16 | Big East Conference | 15326 | 9152 | 6174  
0 | Big Ten Conference | 15293 | 9080 | 6213  
12 | Atlantic Coast Conference | 14869 | 9040 | 5829  
24 | Mid-American Conference | 13501 | 6698 | 6803  
18 | Sun Belt Conference | 12791 | 6226 | 6565  
14 | Missouri Valley Conference | 12187 | 6350 | 5837  
3 | Mid-Eastern Athletic Conference | 12157 | 4744 | 7413  
25 |Metro Atlantic Athletic Conference | 12051 | 5791 | 6260

| Conference | WinPercentage |
| ---------- | ------------- |
| 19         | 58.93         |
| 31         | 53.29         |
| 16         | 59.72         |
| 0          | 59.37         |
| 12         | 60.80         |
| 24         | 49.61         |
| 18         | 48.67         |
| 14         | 52.10         |
| 3          | 39.02         |
| 25         | 48.05         |

### Dataset Version and Maintenance

#### Maintenance Status

Regularly Updated - New versions of the dataset have been or will continue to be made available.

#### Version Details

**Current Version:** 1.0

**Last Updated:** 03/2025

**Release Date:** 02/2025

#### Maintenance Plan

**Versioning:**

-   Use semantic versioning
-   Store and tag dataset versions using Github

**Updates:**

-   Pre-tournament: load latest regular season and conference tournament games (early March).

**Errors:**

-   Implement validation checks during ingestion:

    -   No missing values in key fields (e.g., team name, points, win/loss).

    -   Score totals make sense (e.g., team points > 0).

-   Maintain an error log for issues found and corrected (manual or automatic).

-   Add a "last_verified" timestamp or flag to records.
-   If errors are found after a model is trained:

    -   Flag the version as faulty (e.g., v1.1.0-buggy).

    -   Retrain model with corrected data and note version linkage in results.

#### Expected Change(s)

**Updates to Data/DataSet:** Updates expected during and towards the end of each college basketball season.

## Example of Data Points

#### Primary Data Modality

-   Image Data
-   Text Data
-   Tabular Data
-   Audio Data
-   Video Data
-   Time Series
-   Graph Data
-   Geospatial Data
-   Multimodel (please specify)
-   Unknown
-   Others (please specify)

#### Sampling of Data Points

-   Tabular Data (majority of data sources)

-   Geospatial Data (city metadata via Cities.csv)

-   Hierarchical Bracket Structure (via MNCAATourneySlots.csv)

#### Data Fields

| Field Name   | Field Value | Description                              |
| ------------ | ----------- | ---------------------------------------- |
| Season       | 2024        | The year the NCAA season was played      |
| DayNum       | 135         | Day of the season                        |
| WTeamID      | 1101        | ID of winning team                       |
| LTeamID      | 1345        | ID of losing team                        |
| TeamName     | Abilene Chr | Name of the team                         |
| WScore       | 91          | Winning Score                            |
| LScore       | 41          | Losing Score                             |
| CityID       | 2154        | Unique ID for city where game was played |
| State        | TX          | State abbreviation                       |
| Ordinal Rank | 4           | Team's ranking in that system            |

#### Typical Data Point

```
{'q_id': '8houtx',
  'title': 'Why does water heated to room temperature feel colder than the air around it?',
  'selftext': '',
  'document': '',
  'subreddit': 'explainlikeimfive',
  'answers': {'a_id': ['dylcnfk', 'dylcj49'],
  'text': ["Water transfers heat more efficiently than air. When something feels cold it's because heat is being transferred from your skin to whatever you're touching. ... Get out of the water and have a breeze blow on you while you're wet, all of the water starts evaporating, pulling even more heat from you."],
  'score': [5, 2]},
  'title_urls': {'url': []},
  'selftext_urls': {'url': []},
  'answers_urls': {'url': []}}
```

#### Atypical Data Point

```
{'q_id': '8houtx',
  'title': 'Why does water heated to room temperature feel colder than the air around it?',
  'selftext': '',
  'document': '',
  'subreddit': 'explainlikeimfive',
  'answers': {'a_id': ['dylcnfk', 'dylcj49'],
  'text': ["Water transfers heat more efficiently than air. When something feels cold it's because heat is being transferred from your skin to whatever you're touching. ... Get out of the water and have a breeze blow on you while you're wet, all of the water starts evaporating, pulling even more heat from you."],
  'score': [5, 2]},
  'title_urls': {'url': []},
  'selftext_urls': {'url': []},
  'answers_urls': {'url': []}}
```

## Motivations & Intentions

### Motivations

#### Purpose(s)

-   Production

#### Domain(s) of Application

#### Motivating Factor(s)

-   Investigate how individual and team-level performance metrics influence outcomes in high-stakes games.
-   Apply machine learning in a real-world sports analytics context.
-   Help improve NCAA bracket selections by offering data-driven insights beyond public rankings.
-   Practice building robust models with noisy data.
-   Create models that help fans guide their picks for the March Madness bracket.

The motivation for the dataset is to build predictive models for tournament outcomes and game scheduling.

### Intended Use

#### Dataset Use(s)

-   Safe for production use

#### Suitable Use Case(s)

**Build a Predictive Model:** Train a machine learning model that predicts the outcome of tournament games using pre-game box score data, geography, public rankings,and supplements.

**Feautre Importance Analysis:** Identify which statistical features are most predictive of winning.

**Simulate the Tournament:** Use the model to simulate entire brackets and compare predicted vs. actual outcomes over multiple years.

**Visualize Insights:** Create dashboards or charts to show trends over time, or how different stats affect win probability.

#### Unsuitable Use Case(s)

**Predicting Individual Player Career Trajectories:** This dataset is not suitable for predicting long-term player development metrics or off-court factors like injuries, training regimens, or scouting reports.

**Determing Player or Team Morale, Motivation, or Chemistry:** Psychological or emotional factors cannot be determined by this dataset.

**Predicting Point Spreads:** This dataset may be unsutiable for predicting point spreads or over/unders for precise betting.

#### Research and Problem Space(s)

This dataset intends to provide better bracket predicatability for March Madness, which is typically a very unpredictable tournament.

#### Citation Guidelines

**BiBTeX:**

```
@misc{march-machine-learning-mania-2025,
  author = {Jeff Sonas and Paul Mooney and Addison Howard and Will Cukierski},
  title = {March Machine Learning Mania 2025},
  year = {2025},
  howpublished = {\url{https://kaggle.com/competitions/march-machine-learning-mania-2025}},
  note = {Kaggle}
}
```

## Access, Rentention, & Wipeout

### Access

#### Access Type

-   External - Open Access

#### Documentation Link(s)

-   [Kaggle Competition Page (2025 NCAA Tournament)](https://www.kaggle.com/competitions/march-machine-learning-mania-2025)
-   [Kaggle Datasets Used](https://www.kaggle.com/competitions/march-machine-learning-mania-2025/data)

#### Prerequisite(s)

No formal prerequisites. Access requires a free Kaggle account and acceptance of the competition’s terms of service.

#### Policy Link(s)

-   [Download Dataset](https://www.kaggle.com/competitions/march-machine-learning-mania-2025/data)
-   [Kaggle Terms of Service](https://www.kaggle.com/terms)

Code to download data:

```
...
```

### Retention

#### Duration

Retain for as long as relevant for the project or competition deadline (e.g., until April 8, 2025), or as required for future academic/research use.

#### Policy Summary

**Retention Plan ID:** N/A

**Summary:** No formal retention policy applies. Dataset can be re-downloaded from Kaggle at any time while the competition is live or archived.

#### Process Guide

**Additional Notes:** Add here

This dataset complies with Kaggle's public data usage and retention policies. Since it is publicly available and does not contain personally identifiable information (PII), there are no strict limitations on how long the dataset can be retained.

**Additional Notes:** Retention may be subject to changes in Kaggle’s hosting or availability policies. Users should ensure they have local copies for long-term access if needed.

#### Exception(s) and Exemption(s)

**Exemption Code:** PUBLIC_DATA

**Summary:** This dataset qualifies as publicly available data with no access restrictions or retention limitations. No additional approvals or exemptions are required to retain or use the dataset for academic purposes.

**Additional Notes:** No personal or sensitive data is included. No special handling or anonymization processes are necessary.

## Human and Other Sensitive Attributes

#### Sensitive Human Attribute(s)

-   Gender: Data sets are divided by gender.
-   Geography: Locations of each team are given.

## Transformations

1. Data Validation & Cleaning
    - Missing vaule handling
    - Duplicate Removal
    - Value Validation
2. Normalization (Min-Max Scaling)
3. Feature Engineering
    - Derived Metrics
4. Bias & Fairness Checks
    - Class Balance Verification
    - Game Distribution Analysis
    - Conference-Level Analysis
5. Visualization (Diagnostic)

### Synopsis

#### Transformation(s) Applied

1. Handling Missing Values and Duplicates
2. Data Validation and Consistency Checks

-   Season Validation
-   Non-Negative Values
-   Team ID Validation
-   Region Validation

3. Class Balance Verification
4. Feature Distribution Analysis
5. Normalization
6. Outlier Removal

#### Field(s) Transformed

| Field Name | Source & Target                      |
| ---------- | ------------------------------------ | -------------------------------------- |
| WScore     | MRegularSeasonCompactResults.csv     | Min-Max Normalized (values scaled 0–1) |
| LScore     | MRegularSeasonCompactResults.csv     | Min-Max Normalized (values scaled 0–1) |
| DayNum     | MRegularSeasonCompactResults.csv     | Min-Max Normalized (values scaled 0–1) |
| NumOT      | MRegularSeasonCompactResults.csv     | Min-Max Normalized (values scaled 0–1) |
| All fields | All CSVs in basics, team_box_scores  | Empty strings/spaces replaced with NaN |
| WTeamID    | All relevant results and seeds files | Validated against master teams list    |

**Transformation Type**

#### Library(ies) and Method(s) Used

<!-- Style Note: Refer to "The Jupyter Notebook used in this project" on first use. Use "the notebook" thereafter. -->

Example Code Snippets from the The Jupyter Notebook used in this Project

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Replace empty strings/spaces with NaN

df = df.replace(r'^\s\*$', np.nan, regex=True)

# Remove duplicates

df = df.drop_duplicates()

# Normalize selected columns

scaler = MinMaxScaler()
df[['WScore', 'LScore', 'DayNum', 'NumOT']] = scaler.fit_transform(df[['WScore', 'LScore', 'DayNum', 'NumOT']])

## Transformation| Library/Method|Dataset/Field(s) Affected|

|Missing Value Handling| pandas replace| All loaded DataFrames
|Duplicate Removal| pandas drop_duplicates| All loaded DataFrames
|Normalization | sklearn MinMaxScaler | WScore, LScore, DayNum, NumOT in regular season results
|Validation Checks |pandas isin, unique | Season, TeamID, Region columns
|Feature Distribution Plot | pandas/matplotlib hist | Score columns in regular season results

**Transformation Type**

**Platforms, tools, or libraries:**
. Programming Language: Python

. Libraries:

1. pandas
2. numpy
3. matplotlib
4. scikit-learn (sklearn)

. Platform: Google Colab

**Transformation Results:**

1. Handling Missing Values and Duplicates
   Outcome: The code identified that there were no missing values or duplicate rows in the datasets.

Action Taken: No specific action was required since no missing or duplicate data was found.

2. Data Validation
   Outcome: The 'Season' column was validated to ensure all years were within the 1985-2025 range.

Columns like 'DayNum', 'WScore', and 'LScore' were confirmed to have no negative numbers.

Team IDs were validated against the master team lists.

Region names were validated.

Action Taken: The validation confirmed that the data met the expected criteria, ensuring data consistency and integrity.

3. Class Balance Check
   Outcome: The total number of wins and losses in both the men's and women's tournament results were equal.

Visualization:

Men's Tournament Results

Women's Tournament Results

Action Taken: The classes (wins and losses) were balanced, which is good for model training.

4. Feature Distributions
   Outcome: The distribution of winning and losing scores was visualized.

Visualization:

Action Taken: The visualization confirmed that winning scores were generally higher than losing scores, as expected.

5. Normalization
   Outcome: The 'WScore', 'LScore', 'DayNum', and 'NumOT' columns in the MRegularSeasonCompactResults.csv file were Min-Max normalized.

Action Taken: Normalization scaled the values of these columns to a range between 0 and 1.

### Breakdown of Transformations

The notebook. does not mention or use transformers in the context of transormer models like NLP instead it focuses on data preparation and processing steps for NCAA basketball data

#### Cleaning Missing Value(s)

In the notebook, the initial data completeness check. revealed no missing vaules in any of the datasets therefore there are no fields with missing vaules to report

#### Method(s) Used

No missing vaules in the datasets

#### Residual & Other Risk(s)

## Transformation | Risk Introduced | Risk Mitigated

Min-Max Normalization |Potential loss of granularity due to data compression. | N/A
Missing Value Handling |NA |Inconsistent data format due to empty strings/spaces, leading to potential misinterpretation or errors.
Data Validation | N/A |Data integrity issues due to invalid season years, negative scores, invalid team IDs, and inconsistent region names.
Class Balance Check | N/A |Model bias due to unequal representation of wins and losses.
Duplicate Removal | N/A |Skewed analysis and model training due to over-representation of duplicate data p

#### Human Oversight Measure(s)

1. Review of Pre-ML Checklist: A review to ensure data completeness, accurate entries, gender representation bias, bias & fairness, privacy consideration and labeling consistency

2. Data Validation: Implementation of specific checks like validate_season, check_non_negative, check_team_ids to confirm the integrity and correctness of the data

3. Manual Inspection of Unique Values: The unique values of region names were printed, implying a manual check for correctness and consistency.

4. Visual Inspection: Visualization of the distribution of winning and losing scores via histograms.

#### Cleaning Mismatched Value(s)

Based on the Notebook, no fields were explicitly corrected for mismatched values. The focus was on validating data integrity by checking for:

Valid season ranges

Non-negative values in score and day number columns

Valid team IDs

Valid region names

If any of these checks had failed (which the output shows they did not), further investigation and correction would have been necessary. However, the code and output do not show any instances where such corrections were applied

#### Method(s) Used

In the NCAA data preparation workflow, the main focus was on identifying and validating possible incorrect or mismatched values rather than directly correcting them
steps to summarize the cleaning process:
Validation Checks:
Action Taken:
Manual Correction (if needed):

Example from Related Basketball Data Cleaning
For example, in a similar basketball dataset, mismatched team names across sources were resolved by mapping different notations (e.g., "UNC" vs. "Carolina") to a standardized team name, often requiring manual review or a mapping table

#### Comparative Summary

Scenario: Invalid Team ID (TeamID = 9999)
Before Cleaning:

# Original data

results_df = pd.DataFrame({
'WTeamID': [1104, 9999], # 9999 is invalid
'LTeamID': [1234, 5678]
})
After Cleaning:

Method Used: Validation check (check_team_ids) flags invalid IDs but does not auto-correct.

Outcome: Row remains unchanged. Requires manual investigation (e.g., cross-referencing historical data to identify the correct team).

#### Residual & Other Risk(s)

## Transformation Risk Introduced Risk Mitigated

Min-Max Normalization | Potential loss of granularity due to data compression. |N/A
Missing Value Handling | N/A |Inconsistent data format due to empty strings/spaces, leading to potential misinterpretation or errors.
Data Validation |N/A |Data integrity issues due to invalid season years, negative scores, invalid team IDs, and inconsistent region names.
Class Balance Check |N/A |Model bias due to unequal representation of wins and losses.
Duplicate Removal |N/A |Skewed analysis and model training due to over-representation of duplicate data points.

#### Human Oversight Measure(s)

Review of Pre-ML Checklist: A review to ensure data completeness, accurate entries, gender representation bias, bias & fairness, privacy consideration and labeling consistency

Data Validation: Implementation of specific checks like validate_season, check_non_negative, check_team_ids to confirm the integrity and correctness of the data

Manual Inspection of Unique Values: The unique values of region names were printed, implying a manual check for correctness and consistency.

Visual Inspection: Visualization of the distribution of winning and losing scores via histograms.

The document does not explicitly mention formal approvals or sign-off procedures.

#### Anomalies

Number of Anomalies/Outliers Detected: According to the "Review of PreML Checklist," the data has a normal distribution with no outliers in points. The code does not implement any specific outlier detection methods.

Handling of Anomalies/Outliers: Since no outliers were detected, no specific outlier handling was performed.

Reasoning: The absence of detected outliers meant that no specific outlier treatment was necessary. The data was considered to be normally distributed, which is acceptable for further analysis without outlier manipulation.

#### Method(s) Used

Review of Pre-ML Checklist: This review stated that the data has a normal distribution with no outliers in points. This suggests a prior assessment, though the specific methods used for this assessment are not detailed in the provided document.

Feature Distributions (Histograms): Histograms of winning and losing scores were plotted to visually inspect the distribution of these features. This could help identify potential outliers, such as unusually high or low scores, but it is primarily a visual assessment.

Validation Checks: The code includes validation checks for:

Valid season ranges: Ensures that the 'Season' column only contains years within the valid range (1985–2025).

Non-negative values: Checks that columns such as 'DayNum', 'WScore', and 'LScore' do not contain negative numbers.

Valid team IDs: Verifies that all team IDs in results and seeds files exist in the master teams list for both men's and women's datasets.

Valid region names: Confirms that region names in the season files are within expected values, listing unique entries for review.

**Platforms, tools, or libraries**
Platforms:

Google Colab

Programming Languages:

Python

Libraries:

pandas: For data loading, manipulation, and descriptive statistics.

numpy: For numerical operations.

matplotlib: For visualizing data distributions (histograms).

scikit-learn (sklearn): MinMaxScaler was used, but there were no functions explicitly used for outlier detection.

#### Comparative Summary

Based on the notbook, no explicit outlier handling measures were taken. The "Review of PreML Checklist" stated, "Data is a normal distribution with no outliers in points." Therefore, there's no "before and after" comparison to present.

#### Residual & Other Risk(s)

## Transformation Risk Introduced Risk Mitigated

Min-Max Normalization |Potential loss of granularity due to data compression. | N/A
Missing Value Handling |N/A |Inconsistent data format due to empty strings/spaces, leading to potential misinterpretation or errors.
Data Validation |N/A |Data integrity issues due to invalid season years, negative scores, invalid team IDs, and inconsistent region names.
Class Balance Check |N/A |Model bias due to unequal representation of wins and losses.
Duplicate Removal |N/A |Skewed analysis and model training due to over-representation of duplicate data points.

#### Human Oversight Measure(s)

Review of Pre-ML Checklist: A review to ensure data completeness, accurate entries, gender representation bias, bias & fairness, privacy consideration and labeling consistency

Data Validation: Implementation of specific checks like validate_season, check_non_negative, check_team_ids to confirm the integrity and correctness of the data

Manual Inspection of Unique Values: The unique values of region names were printed, implying a manual check for correctness and consistency.

Visual Inspection: Visualization of the distribution of winning and losing scores via histograms.

#### Dimensionality Reduction

The Notebook focuses on data completeness, validation, and preprocessing. The number of original features collected and the dimensions reduced are not mentioned. To find this information, review the original dataset documentation on Kaggle, linked in the document.

#### Method(s) Used

The Notebook does not mention the specific methods used to reduce the dimensionality of the data or alternative choices that were considered.

**Platforms, tools, or libraries**
NA

#### Comparative Summary

The Notebook does not discuss why specific dimensionality reduction methods were chosen over others, nor does it include comparative charts showing the before-and-after effects of dimensionality reduction processes.

#### Residual & Other Risks

The Notebook focuses on data completeness, validation, and preprocessing steps such as handling missing values, checking for data inconsistencies (e.g., negative scores or invalid team IDs), and normalization. It does not explicitly discuss risks introduced or mitigated due to specific data transformations

#### Human Oversight Measure(s)

The Notebook does not contain information regarding specific human oversight measures, additional testing, investigations, or approvals taken due to data transformation.

#### Joining Input Sources

The distinct input sources joined in this project are multiple CSV files, each containing specific aspects of the NCAA Men's and Women's Basketball Tournaments history and structure. These files are located in the following directories:

basics_dir_path

team_box_scores_dir_path

geography_dir_path

public_rankings_dir_path

supplements_dir_path

#### Method(s) Used

The shared columns or fields used to join the data sources are not explicitly mentioned in the Notebook .

**Platforms, tools, or libraries**

pandas: For data manipulation and analysis.

os: For interacting with the operating system, such as navigating file paths.

numpy: For numerical computations.

matplotlib.pyplot: For creating visualizations.

sklearn.preprocessing.MinMaxScaler: For normalization.

Kaggle: As the source for downloading the dataset.

Google Colab: As the platform for running the notebook.

#### Comparative Summary

The notebook does not specify additional risks introduced or mitigated.

#### Human Oversight Measure(s)

The notebook does not contain information regarding specific human oversight measures, additional testing, investigations, or approvals taken due to data transformation.

#### Redaction or Anonymization

The notebook indicates "Privacy Consideration: None," suggesting that no features were redacted or anonymized in this dataset.

#### Method(s) Used

The notebook indicates "Privacy Consideration: None," and therefore does not mention any methods used to redact or anonymize data.

**Platforms, tools, or libraries**
Google Colab: Platform for running the notebook.

Kaggle: Source for downloading the dataset.

pandas: For data manipulation and analysis.

numpy: For numerical computations.

os: For interacting with the file system.

matplotlib.pyplot: For data visualization.

sklearn.preprocessing.MinMaxScaler: For feature normalization.

#### Comparative Summary

The Notebook states, "Privacy Consideration: None," meaning no data was redacted or anonymized. Therefore, there were no methods used for this purpose, and no comparative charts exis

#### Residual & Other Risk(s)

Based on the Notebook:

**Risks Introduced:**

-   Normalization\*\*: The document mentions that normalization was applied to the 'WScore', 'LScore', 'DayNum', and 'NumOT' columns using `MinMaxScaler`. It suggests that a potential risk introduced by normalization is altering the original data distribution, which could affect the performance of certain algorithms sensitive to feature scaling.

**Risks Mitigated:**

-   Missing Values\*\*: The initial data completeness check found no missing values, thus mitigating risks associated with imputing or removing missing data.
-   Data Validation\*\*: Validation steps were performed to check for negative scores, invalid team IDs, and season ranges, mitigating the risk of using incorrect or invalid data in the analysis.
-

#### Human Oversight Measure(s)

The Notebook does not include specific details on human oversight measures, additional testing, investigations, or approvals related to data transformations.

#### Additional Considerations

Gender Representation Bias: The data for women's basketball starts from 1988, while the data for men's basketball starts from 1985.

Bias & Fairness: The data is normally distributed with no outliers in points.

Labeling Consistency: Labels remain consistent from men's to women's data and maintain the same labeling for teams across all files.

Class Balance: Ensuring an equal number of wins and losses.

Data Validation: Checking for negative scores, invalid team IDs and valid seasons.

#### Others (Please Specify)

Handling Missing Data: The code checked for missing values in all CSV files within the specified directories using df.isnull().sum(). No missing values were found.

Data Validation: The code validated entries by:

Checking if the 'Season' column contained years between 1985 and 2025 using the validate_season function.

Checking for negative values in 'DayNum', 'WScore', and 'LScore' columns across multiple dataframes using the check_non_negative function.

Verifying 'TeamID' in various dataframes against unique 'TeamID's from 'MTeams' and 'WTeams' dataframes using the check_team_ids function.

Checking unique values in 'RegionW', 'RegionX', 'RegionY', and 'RegionZ' columns for both men's and women's seasons.

Class Balance Check: Verified that wins and losses are balanced in the data.

Normalization: The columns 'WScore', 'LScore', 'DayNum', and 'NumOT' in the MRegularSeasonCompactResults.csv file were normalized using MinMaxScaler from scikit-learn.

The features/fields affected were:

'Season' (validated for year range)

'DayNum', 'WScore', 'LScore' (validated for non-negative values)

'TeamID', 'WTeamID', 'LTeamID' (validated against known team IDs)

'RegionW', 'RegionX', 'RegionY', 'RegionZ' (validated for unique region values)

'WTeamID', 'LTeamID' (used in Class Balance Check)

'WScore', 'LScore', 'DayNum', 'NumOT' (normalized using MinMaxScaler) in the MRegularSeasonCompactResults.csv file.

#### Method(s) Used

Checking for Missing Values: pandas' isnull().sum() was used to find the number of missing values in each column of the dataframes.

Data Validation:

Defined functions to validate data, checking 'Season' columns for values between 1985 and 2025.

Defined functions to check for negative values in specified columns ('DayNum', 'WScore', 'LScore').

Checking 'TeamID' columns against a list of valid team IDs.

Class Balance Check: Counting the number of wins and losses to ensure they are balanced.

Normalization: MinMaxScaler from scikit-learn was used to normalize the 'WScore', 'LScore', 'DayNum', and 'NumOT' columns in the MRegularSeasonCompactResults.csv file.

**Platforms, tools, or libraries**
Platform: Google Colab

Libraries:

pandas

os

numpy

matplotlib.pyplot

sklearn.preprocessing.MinMaxScaler

Data Source: Kaggle

#### Comparative Summary

The Notebook states that MinMaxScaler from scikit-learn was used to normalize the columns 'WScore', 'LScore', 'DayNum', and 'NumOT' in the MRegularSeasonCompactResults.csv file.

Why this method?

The document does not explicitly state why MinMaxScaler was chosen over other scaling methods.

Comparative charts:

The document does not include comparative charts showing the before and after states of the normalization process. However, the code to print the first few rows of the normalized columns is included, which would allow the user to inspect the normalized values directly.

print(df_m_reg[['WScore', 'LScore', 'DayNum', 'NumOT']].head())

#### Residual & Other Risk(s)

Risks Introduced:

Normalization: The document mentions that normalization was applied to the 'WScore', 'LScore', 'DayNum', and 'NumOT' columns using MinMaxScaler. It suggests that a potential risk introduced by normalization is altering the original data distribution, which could affect the performance of certain algorithms sensitive to feature scaling.

Risks Mitigated:

Missing Values: The initial data completeness check found no missing values, thus mitigating risks associated with imputing or removing missing data.

Data Validation: Validation steps were performed to check for negative scores, invalid team IDs, and season ranges, mitigating the risk of using incorrect or invalid data in the analysis.

Class Imbalance: Checking for an equal number of wins and losses ensures no class imbalance, and this mitigates risks associated with biased models.

#### Human Oversight Measure(s)

The Notebook does not contain information regarding specific human oversight measures, additional testing, investigations, or approvals taken due to data transformation.

#### Additional Considerations

Gender Representation Bias: The dataset contains data for women's basketball starting from 1988, whereas men's basketball data starts from 1985.

Bias & Fairness: The data is normally distributed with no outliers in points.

Labeling Consistency: Labels are consistent between men's and women's data and maintain the same labeling for teams across all files.

Class Balance: Ensuring an equal number of wins and losses in the dataset.

Data Validation: Checking for negative scores, invalid team IDs, and valid seasons.

## Validation Types

#### Method(s)

-   Data Type Validation
-   Range and Constraint Validation
-   Code/cross-reference Validation
-   Consistency Validation

#### Breakdown(s)

**Range and Constraint Validation**

**Number of Data Points Validated:** ~100,000+

**Fields Validated**
Field | Count (approx)
--- | ---
Season | 16,000
DayNum | 80,000
WScore | 80,000
LScore | 80,000

**Above:** Checked that seasons were within the range 1985-2025, and that numeric fields like scores and game days were non-negative.

**Code / Cross-reference Validation**

**Number of Data Points Validated:** ~50,000+

**Fields Validated**
Field | Count (approx)
--- | ---
WTeamID | 50,000
LTeamID | 50,000
TeamID | 10,000

**Above:** Verified that team IDs in game and seed datasets matched entries in the MTeams and WTeams lookup files.

**Consistency Validation**

**Number of Data Points Validated:** ~4,000+

**Fields Validated**
Field | Count
--- | ---
RegionW | 2,000
RegionX | 2,000
RegionY | 2,000
RegionZ | 2,000

**Above:** Retrieved unique values for NCAA® tournament regions across seasons. Verified that these are consistent with expected names and historical region naming conventions.

#### Description(s)

**Range and Constraint Validation**

**Method:**

-   Verified that Season values fall within 1985–2025.

-   Checked that fields such as DayNum, WScore, and LScore contain no negative values.

**Platforms, tools, or libraries:**

-   Python
-   Pandas

**Validation Results:**

✅ All Season values are valid.

✅ All numeric game values are non-negative.

**Additional Notes:** This validation step ensures that no out-of-bounds or corrupted data points interfere with model training.

**Code / Cross-reference Validation**

**Method:**

-   Compared team IDs in result and seed datasets to the official team lists using set logic in Python.

-   Checked columns: WTeamID, LTeamID, TeamID.

**Platforms, tools, or libraries:**

-   Python
-   Pandas

**Validation Results:**

✅ All team IDs in both men's and women's datasets match the official team files. No unmatched or orphaned IDs were found.

**Additional Notes:** This validation ensures referential integrity across game result data and team metadata.

**Consistency Validation**

**Method:**

-   Printed unique values of region fields (RegionW, RegionX, RegionY, RegionZ) in MSeasons and WSeasons.

-   Verified consistency with historical naming patterns.

**Platforms, tools, or libraries:**

-   Python
-   Pandas

**Validation Results:**

-   Men's Regions:

    -   RegionW: ['East', 'Atlanta', 'Albuquerque', 'NA1']

    -   RegionX: ['West', 'Midwest', 'Southeast', 'South', 'Phoenix', 'Chicago', 'Oakland', 'NA2']

    -   RegionY: ['Midwest', 'Southeast', 'South', 'EastRutherford', 'Austin', 'Minneapolis', 'NA3']

    -   RegionZ: ['Southeast', 'West', 'South', 'StLouis', 'Syracuse', 'WashingtonDC', 'Southwest', 'NA4']

-   Women's Regions:
    (Includes broader set reflecting more diversity in site locations)

        -  e.g., ['Chattanooga', 'DesMoines', 'Alamo', 'Seattle4', 'RiverWalk', etc.]

**Additional Notes:** The presence of NA1 to NA4 suggests placeholders, which may require downstream handling depending on modeling use cases.

## Sampling Methods

#### Method(s) Used

-   Unknown
-   Unsampled

## Terms of Art

### Concepts and Definitions referenced in this Data Card

#### Term of Art: Brier Score

**Definition**: A metric used to measure the accuracy of probabilistic predictions. It calculates the mean squared difference between predicted probabilities and the actual outcomes.  
**Source**: [Wikipedia - Brier Score](https://en.wikipedia.org/wiki/Brier_score)  
**Interpretation**: In this competition, the Brier Score evaluates how close your predicted win probabilities are to the actual game results. A lower Brier Score indicates better performance.

#### Term of Art: Seed

**Definition**: A number assigned to each team in a tournament to represent its ranking or expected performance. Lower seed numbers indicate higher-ranked teams.  
**Source**: [NCAA - March Madness Seeding](https://www.ncaa.com/news/basketball-men/bracketiq/2025-01-22/what-march-madness-ncaa-tournament-explained)  
**Interpretation**: Seeds are used as a predictive feature in our model, often in the form of "Seed Difference" between two teams in a matchup.

#### Term of Art: Feature Engineering

**Definition**: The process of using domain knowledge to create additional input variables (features) that make machine learning algorithms work better.  
**Source**: [Wikipedia - Feature Engineering](https://en.wikipedia.org/wiki/Feature_engineering)  
**Interpretation**: We created features such as win/loss ratios, scoring margin, and seed differences to improve model accuracy.

#### Term of Art: Matchup

**Definition**: A potential game between two teams in the NCAA tournament bracket.  
**Source**: Common usage in sports analytics.  
**Interpretation**: In this competition, we generate predictions for every possible matchup, whether or not the game actually occurs.

### Team Performance

Games Played: On average, teams play around 28-30 games a season depending how well they do. The top teams by games played, such as Duke, Kansas, and North Carolina, are all consistently strong performers. However their repeated represenation can lead to bias with schools with less extensive data or shorter season.

Win Percentage: The average win percentage across all teams is 48.03%, with top teams (e.g., Duke and Kansas) reaching win percentages over 79% a season, indicating a strong historical performance. Teams with fewer games played tend to show a wider variance in performance. Which we will also need to find a way to account for in our model. (These are the typical underdogs that could lead to big upsets)

Tournament Participation: The mean tournament participation rate is approximately 1.06, suggesting that while some teams regularly make the tournament, others may only participate sporadically. This is also seen in overall games played, the best teams have the highest overall games played since they consistently go to the finals. Seperating themselves from the pack. Teams less involved in the tournaments have little to no uniformity.

### Conference Trends

Games Played: Conferences like the Southeastern Conference (SEC) and Atlantic 10 Conference have the highest number of games played, suggesting strong and competitive leagues. In contrast, conferences like the Mid-Eastern Athletic Conference (MEAC) have lower game totals, reflecting less competition.

Win Percentage: Win percentages across conferences show a lot of variability, with the Atlantic Coast Conference (ACC) performing at a high level (60.80%) and the Mid-Eastern Athletic Conference (MEAC) performing at a much lower level (39.02%). This highlights the difference in strength between conferences.

Tournament Performance: The average tournament win percentage across conferences is 34.55%, with some conferences like the ACC having higher success rates in tournament play, and others facing more challenges.
