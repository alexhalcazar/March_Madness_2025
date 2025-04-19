# NCAA Data
This dataset contains historical data for the NCAA Men's and Women's Basketball Tournaments, which includes detailed information about team performances, tournament seeds, game results, and scheduling. The data is sourced from multiple CSV files, each containing specific aspects of the tournament history and structure. The primary purpose of this dataset is to build predictive models for tournament outcomes and game scheduling.

#### Dataset Link
<!-- info: Provide a link to the dataset: -->
<!-- width: half -->
[Kaggle](https://www.kaggle.com/competitions/march-machine-learning-mania-2025/data)

#### Data Card Author(s)
<!-- info: Select **one role per** Data Card Author:

(Usage Note: Select the most appropriate choice to describe the author's role
in creating the Data Card.) -->
<!-- width: half -->
- **Cesar Ramirez, Group 9:** Contributor
- **Alma Campos, Group 9:** Contributor
- **Moheson Alavian, Group 9:** Contributor
- **Gauri Joshi, Group 9:** Contributor
- **Rutik Narute, Group 9:** Contributor
- **Denise Tabilas, Group 9:** Contributor
- **Rishab Lakhotra, Group 9:** Contributor
- **Alex Alcazar, Group 9:** Contributor
- **Moheson Alavian, Group 9:** Contributor
- **Kris Kajar, Group 9:** Contributor

## Authorship
### Publishers
#### Publishing Organization(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the institution or organization responsible
for publishing the dataset: -->
Kaggle

#### Industry Type(s)
<!-- scope: periscope -->
<!-- info: Select **all applicable** industry types to which the publishing
organizations belong: -->
- Academic - Tech

#### Contact Detail(s)
<!-- scope: microscope -->
<!-- info: Provide publisher contact details: -->
- **Website:** [Kaggle](https://www.kaggle.com/)

### Dataset Owners
#### Team(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the groups or team(s) that own the dataset: -->
Kenneth Massey
Sonas Consulting

#### Contact Detail(s)
<!-- scope: periscope -->
<!-- info: Provide pathways to contact dataset owners: -->
- **Dataset Owner(s):** Kenneth Massey, Jeff Sonas, Sonas Consulting
- **Affiliation:** Massey Ratings, Sonas Consulting
- **Website:** [Massey Ratings](http://www.masseyratings.com/)


## Dataset Overview
#### Data Subject(s)
<!-- scope: telescope -->
<!-- info: Select ***all applicable**** subjects contained the dataset: -->
- The Basics
- Team Box Scores
- Geography
- Public Rankings
- Supplements

#### Dataset Snapshot
<!-- scope: periscope -->
<!-- info: Provide a snapshot of the dataset:<br><br>(Use the additional notes
to include relevant information, considerations, and links to table(s) with
more detailed breakdowns.) -->
Category | Data
--- | ---
Size of Dataset | 182.97 MB
Number of Instances | 2636297
Number of Fields | 282
Labeled Classes | 32

#### Content Description
<!-- scope: microscope -->
<!-- info: Provide a short description of the content in a data point: -->
**The Basics**
- Team ID's and Team Names
- Tournament seeds since 1984-85 season
- Final scores of all regular season, conference tournament, and NCAA® tournament games since 1984-85 season
- Season-level details including dates and region names

**Team Box Scores**
Game-by-game stats at a team level
- WFGM - field goals made (by the winning team)
- WFGA - field goals attempted (by the winning team)
- WFGM3 - three pointers made (by the winning team)
- WFGA3 - three pointers attempted (by the winning team)
- WFTM - free throws made (by the winning team)
- WFTA - free throws attempted (by the winning team)
- WOR - offensive rebounds (pulled by the winning team)
- WDR - defensive rebounds (pulled by the winning team)
- WAst - assists (by the winning team)
- WTO - turnovers committed (by the winning team)
- WStl - steals (accomplished by the winning team)
- WBlk - blocks (accomplished by the winning team)
- WPF - personal fouls committed (by the winning team)

**Geography** 
- City locations of all regular season, conference tournament, and NCAA® tournament games since the 2010 season

**Public Rankings**
- Weekly team rankings (men's teams only) for dozens of top rating systems - Pomeroy, Sagarin, RPI, ESPN, etc., since the 2003 season

**Supplements**
- Additional supporting information, including coaches, conference affiliations, alternative team name spellings, bracket structure, and game results for NIT and other postseason tournaments.

#### Descriptive Statistics
<!-- width: full -->
<!-- info: Provide basic descriptive statistics for each field.

Use additional notes to capture any other relevant information or
considerations.

Usage Note: Some statistics will be relevant for numeric data, for not for
strings. -->
**Team Statistics**

Statistic | TeamID | GamesPlayed | Wins | Losses | RegularSeasonGames 
--- | --- | --- | --- | --- | --- 
count | 380.000000 | 380.000000 | 380.000000 | 380.000000  |   380.000000 
mean |1290.500000 | 1028.673684  | 514.336842 | 514.336842   |   1015.421053
std |109.840794 |  338.935823 |  228.058797 | 174.132262  |   330.188419
min |1101.000000  |  22.000000  |   3.000000  | 16.000000    |   22.000000
25% |1195.750000 | 1039.000000 |  393.750000 | 458.500000    |   1038.000000
50% | 1290.500000 | 1159.500000 |  533.000000 | 559.500000    |   1155.000000
75% |  1385.250000 | 1227.250000  | 669.000000 | 634.000000   |    1215.000000
max | 1480.000000 | 1441.000000 | 1153.000000 | 869.000000    |     1307.000000 
        
Statistic | TournamentGames | HomeGames | AwayGames | NeutralGames | WinPercentage 
--- | --- | --- | --- | --- | --- 
count | 380.000000 | 380.000000 | 380.000000   | 380.000000  |   380.000000
mean | 13.252632 | 455.707895 | 455.707895  | 117.257895   |   48.031105
std | 21.403754 | 170.107048 | 145.575036  |   69.392173   |   11.103786 
min | 0.000000  |  9.000000  | 10.000000   |   0.000000    |  12.500000  
25% | 1.000000 | 402.500000 | 429.250000  |   71.750000   |   40.560000
50%  |      5.000000 | 494.000000 | 489.000000  |  110.500000     | 47.980000   
75%   |       14.000000 | 577.000000 | 556.000000 |   156.250000    |  55.422500   
max    |     137.000000  |707.000000 | 668.000000  |  396.000000   |   80.010000   

Statistic |    TournamentParticipationRate | NumSeasons |  AvgGamesPerSeason  
--- | --- | --- | ---  
count   |                380.000000 | 380.000000     |    380.000000  
mean     |                 1.062868  | 35.231579    |      28.994316  
std       |                1.575389   |11.178761    |       1.803911  
min        |               0.000000    |1.000000    |      22.000000  
25%         |              0.147500   |37.000000    |      27.867500  
50%          |             0.505000   |41.000000    |      29.000000  
75%           |            1.152500   |41.000000    |      30.070000  
max            |           9.510000   |41.000000    |      35.150000  
      
**Top 10 Teams by Games Played:**

Team | TeamName | GamesPlayed | Wins | Losses | WinPercentage 
--- | --- | --- | --- | --- | --- 
80  |           Duke    |     1441 | 1153   |  288     |     80.01
213  |  North Carolina    |     1436 | 1062   |  374     |     73.96
141   |       Kansas    |     1411 | 1121   |  290     |     79.45
145   |     Kentucky    |     1400 | 1055   |  345     |     75.36
11    |      Arizona    |     1366 | 1022   |  344     |     74.82
292   |     Syracuse    |     1362 |  953   |  409     |     69.97
176   |  Michigan St    |     1350 |  930   |  420     |     68.89
156   |   Louisville    |     1346 |  884   |  462     |     65.68
62    |  Connecticut    |     1344 |  927   |  417     |     68.97
336   |    Villanova    |     1339 |  882   |  457     |     65.87

**Top 10 Teams by Win Percentage (min 100 games):**

Team | TeamName | GamesPlayed | Wins | Losses | WinPercentage 
--- | --- | --- | --- | --- | --- 
80    |         Duke     |    1441 | 1153   |  288     |     80.01
141   |       Kansas     |    1411 | 1121   |  290     |     79.45
145   |     Kentucky     |    1400 | 1055   |  345     |     75.36
110   |      Gonzaga     |    1277 |  960   |  317      |    75.18
11    |      Arizona     |    1366 | 1022   |  344     |     74.82
213  | North Carolina    |     1436 | 1062  |   374    |      73.96
292    |    Syracuse     |    1362  | 953   |  409     |     69.97
171    |     Memphis     |    1326  | 916   |  410     |     69.08
62     | Connecticut     |    1344  | 927   |  417     |     68.97
176    | Michigan St     |    1350  | 930   |  420     |     68.89

**Conference Statistics Summary:**
Statistic  | GamesPlayed     |    Wins   |    Losses  | IntraConferenceGames
--- | --- | --- | --- | --- 
count |    51.000000 |   51.000000 |   51.000000     |        51.000000   
mean  |  7664.627451 | 3832.313725 | 3832.313725     |      2350.235294   
std   |  5056.436366 | 2702.737460 | 2496.991289     |      1613.305149   
min   |   201.000000 |   60.000000 |  104.000000     |        30.000000   
25%   |  2584.000000 | 1433.000000 | 1079.000000     |       663.500000   
50%   |  8497.000000 | 4131.000000 | 4422.000000     |      2509.000000   
75%   | 11776.500000 | 5651.000000 | 6193.500000     |      3776.000000   
max   | 15906.000000 | 9373.000000 | 7413.000000     |      4741.000000   

Statistic| InterConferenceGames | TournamentGames | TournamentWins | WinPercentage 
--- | --- | --- | --- | --- 
count |            51.000000    |    51.000000    |   51.000000   |   51.000000   
mean  |          2865.411765    |    98.745098    |   49.372549   |   49.107843   
std   |          1834.971806    |   148.593788    |   93.777601   |    7.179466   
min   |            85.000000    |     0.000000    |    0.000000   |   29.850000   
25%   |          1135.000000    |    27.000000    |    4.000000   |   45.100000   
50%   |          3618.000000    |    47.000000    |   10.000000   |   48.670000   
75%   |          4233.000000    |   103.000000    |   37.500000   |   54.250000   
max   |          5943.000000    |   592.000000    |  389.000000   |   60.800000   

Statistic |  TournamentWinPercentage | IntraConfPercentage | NumSeasons
--- | --- | --- | ---
count   |             48.000000      |      51.000000  | 51.000000   
mean    |             34.551875      |      29.316863  | 26.058824   
std     |             19.500014      |       4.853258  | 15.532433   
min     |              0.000000      |      11.190000  |  1.000000   
25%     |             18.712500      |      29.120000  | 11.500000   
50%     |             33.580000      |      30.730000  | 30.000000   
75%     |             50.950000      |      32.330000  | 41.000000   
max     |             66.670000      |      34.620000  | 41.000000   

Statistic  |     AvgGamesPerSeason 
--- | --- 
count     |     51.000000  
mean      |    272.038824  
std       |     66.332431  
min       |   100.500000  
25%       |   226.810000  
50%       |    279.120000  
75%       |    297.565000  
max       |    389.230000  

**Top 10 Conferences by Games Played:**
Conference   |  Description | GamesPlayed | Wins | Losses
--- | --- | --- | --- | --- 
19  |           Southeastern Conference    |    15906 | 9373  |  6533   
31  |            Atlantic 10 Conference    |    15392 | 8202  |  7190   
16  |               Big East Conference    |    15326 | 9152  |  6174   
0   |                Big Ten Conference    |    15293 | 9080  |  6213   
12  |         Atlantic Coast Conference    |    14869 | 9040  |  5829   
24  |           Mid-American Conference    |    13501 | 6698  |  6803   
18  |               Sun Belt Conference    |    12791 | 6226  |  6565   
14  |        Missouri Valley Conference    |    12187 | 6350  |  5837   
3   |   Mid-Eastern Athletic Conference    |    12157 | 4744  |  7413   
25  |Metro Atlantic Athletic Conference    |    12051 | 5791  |  6260   

Conference |    WinPercentage 
--- | ---
19     |     58.93  
31     |     53.29  
16     |     59.72  
0      |     59.37  
12     |     60.80  
24     |     49.61  
18     |     48.67  
14     |     52.10  
3      |     39.02  
25     |     48.05  

### Dataset Version and Maintenance
#### Maintenance Status
<!-- scope: telescope -->
<!-- info: Select **one:** -->

Regularly Updated - New versions of the dataset have been or will continue to be made available.


#### Version Details
<!-- scope: periscope -->
<!-- info: Provide details about **this** version of the dataset: -->
**Current Version:** 1.0

**Last Updated:** 03/2025

**Release Date:** 02/2025

#### Maintenance Plan
<!-- scope: microscope -->
<!-- info: Summarize the maintenance plan for the dataset:

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include links and metrics where applicable.

**Versioning:** 
- Use semantic versioning
- Store and tag dataset versions using Github

**Updates:** 
- Pre-tournament: load latest regular season and conference tournament games (early March).

**Errors:** 
- Implement validation checks during ingestion:

    - No missing values in key fields (e.g., team name, points, win/loss).

    - Score totals make sense (e.g., team points > 0).

- Maintain an error log for issues found and corrected (manual or automatic).

- Add a "last_verified" timestamp or flag to records.
  
- If errors are found after a model is trained:

    - Flag the version as faulty (e.g., v1.1.0-buggy).

    - Retrain model with corrected data and note version linkage in results.



#### Expected Change(s)
<!-- scope: microscope -->
<!-- info: Summarize the updates to the dataset and/or data that are expected
on the next update.

Use additional notes to capture any other relevant information or
considerations. -->
**Updates to Data/DataSet:** Updates expected during and towards the end of each college basketball season.


## Example of Data Points
#### Primary Data Modality
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Image Data
- Text Data
- Tabular Data
- Audio Data
- Video Data
- Time Series
- Graph Data
- Geospatial Data
- Multimodel (please specify)
- Unknown
- Others (please specify)

#### Sampling of Data Points
<!-- scope: periscope -->
<!-- info: Provide link(s) to data points or exploratory demos: -->
- Demo Link
- Typical Data Point Link
- Outlier Data Point Link
- Other Data Point Link
- Other Data Point Link

#### Data Fields
<!-- scope: microscope -->
<!-- info: List the fields in data points and their descriptions.

(Usage Note: Describe each field in a data point. Optionally use this to show
the example.) -->

Field Name | Field Value | Description
--- | --- | ---
Field Name | Field Value | Description
Field Name | Field Value | Description
Field Name | Field Value | Description

**Above:** Provide a caption for the above table or visualization if used.

**Additional Notes:** Add here

#### Typical Data Point
<!-- width: half -->
<!-- info: Provide an example of a typical data point and describe what makes
it typical.

**Use additional notes to capture any other relevant information or
considerations.** -->
Summarize here. Include any criteria for typicality of data point.

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

**Additional Notes:** Add here

#### Atypical Data Point
<!-- width: half -->
<!-- info: Provide an example of an outlier data point and describe what makes
it atypical.

**Use additional notes to capture any other relevant information or
considerations.** -->
Summarize here. Include any criteria for atypicality of data point.

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

**Additional Notes:** Add here

## Motivations & Intentions
### Motivations
#### Purpose(s)
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Production

#### Domain(s) of Application
<!-- scope: periscope -->
<!-- info: Provide a list of key domains of application that the dataset has
been designed for:<br><br>(Usage Note: Use comma-separated keywords.) -->
For example: `Machine Learning`, `Computer Vision`, `Object Detection`.

`keyword`, `keyword`, `keyword`

#### Motivating Factor(s)
<!-- scope: microscope -->
<!-- info: List the primary motivations for creating or curating this dataset:

(Usage Note: use this to describe the problem space and corresponding
motivations for the dataset.) -->
- Investigate how individual and team-level performance metrics influence outcomes in high-stakes games.
- Apply machine learning in a real-world sports analytics context.
- Help improve NCAA bracket selections by offering data-driven insights beyond public rankings.
- Practice building robust models with noisy data.
- Create models that help fans guide their picks for the March Madness bracket.

The motivation for the dataset is to build predictive models for tournament outcomes and game scheduling. 

### Intended Use
#### Dataset Use(s)
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Safe for production use

#### Suitable Use Case(s)
<!-- scope: periscope -->
<!-- info: Summarize known suitable and intended use cases of this dataset.

Use additional notes to capture any specific patterns that readers should
look out for, or other relevant information or considerations. -->
**Build a Predictive Model:** Train a machine learning model that predicts the outcome of tournament games using pre-game box score data, geography, public rankings,and supplements.

**Feautre Importance Analysis:** Identify which statistical features are most predictive of winning.

**Simulate the Tournament:** Use the model to simulate entire brackets and compare predicted vs. actual outcomes over multiple years.

**Visualize Insights:** Create dashboards or charts to show trends over time, or how different stats affect win probability.

#### Unsuitable Use Case(s)
<!-- scope: microscope -->
<!-- info: Summarize known unsuitable and unintended use cases of this dataset.

Use additional notes to capture any specific patterns that readers should look
out for, or other relevant information or considerations. -->
**Predicting Individual Player Career Trajectories:** This dataset is not suitable for predicting long-term player development metrics or off-court factors like injuries, training regimens, or scouting reports.

**Determing Player or Team Morale, Motivation,  or Chemistry:** Psychological or emotional factors cannot be determined by this dataset.

**Predicting Point Spreads:** This dataset may be unsutiable for predicting point spreads or over/unders for precise betting.

#### Research and Problem Space(s)
<!-- scope: periscope -->
<!-- info: Provide a description of the specific problem space that this
dataset intends to address. -->
This dataset intends to provide better bracket predicatability for March Madness, which is typically a very unpredictable tournament. 

#### Citation Guidelines
<!-- scope: microscope -->
<!-- info: Provide guidelines and steps for citing this dataset in research
and/or production.

Use additional notes to capture any specific patterns that readers should look
out for, or other relevant information or considerations. -->

**BiBTeX:**

@misc{march-machine-learning-mania-2025,
    author = {Jeff Sonas and Paul Mooney and Addison Howard and Will Cukierski},
    title = {March Machine Learning Mania 2025},
    year = {2025},
    howpublished = {\url{https://kaggle.com/competitions/march-machine-learning-mania-2025}},
    note = {Kaggle}
}
```
@article{kuznetsova2020open,
  title={The open images dataset v4},
  author={Kuznetsova, Alina and Rom, Hassan and Alldrin, and others},
  journal={International Journal of Computer Vision},
  volume={128},
  number={7},
  pages={1956--1981},
  year={2020},
  publisher={Springer}
}
```


## Access, Rentention, & Wipeout
### Access
#### Access Type
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Internal - Unrestricted
- Internal - Restricted
- External - Open Access
- Others (please specify)

#### Documentation Link(s)
<!-- scope: periscope -->
<!-- info: Provide links that describe documentation to access this
dataset: -->
- Dataset Website URL
- GitHub URL

#### Prerequisite(s)
<!-- scope: microscope -->
<!-- info: Please describe any required training or prerequisites to access
this dataset. -->
For example:

This dataset requires membership in [specific] database groups:

- Complete the [Mandatory Training]
- Read [Data Usage Policy]
- Initiate a Data Requesting by filing

#### Policy Link(s)
<!-- scope: periscope -->
<!-- info: Provide a link to the access policy: -->
- Direct download URL
- Other repository URL

Code to download data:
```
...
```

#### Access Control List(s)
<!-- scope: microscope -->
<!-- info: List and summarize any access control lists associated with this
dataset. Include links where necessary.

Use additional notes to capture any other information relevant to accessing
the dataset. -->
**Access Control List:** Write summary and notes here.

**Access Control List:** Write summary and notes here.

**Access Control List:** Write summary and notes here.

**Additional Notes:** Add here

### Retention
#### Duration
<!-- scope: periscope -->
<!-- info: Specify the duration for which this dataset can be retained: -->
Specify duration in days, months, or years.

#### Policy Summary
<!-- scope: microscope -->
<!-- info: Summarize the retention policy for this dataset. -->
**Retention Plan ID:** Write here

**Summary:** Write summary and notes here

#### Process Guide
<!-- scope: periscope -->
<!-- info: Summarize any requirements and related steps to retain the dataset.

Use additional notes to capture any other relevant information or
considerations. -->
For example:

This dataset compiles with [standard policy guidelines].

**Additional Notes:** Add here

#### Exception(s) and Exemption(s)
<!-- scope: microscope -->
<!-- info: Summarize any exceptions and related steps to retain the dataset.
Include links where necessary.

Use additional notes to capture any other relevant information or
considerations. -->
**Exemption Code:** `ANONYMOUS_DATA` /
`EMPLOYEE_DATA` / `PUBLIC_DATA` /
`INTERNAL_BUSINESS_DATA` /
`SIMULATED_TEST_DATA`

**Summary:** Write summary and notes here.

**Additional Notes:** Add here




## Human and Other Sensitive Attributes
#### Sensitive Human Attribute(s)
<!-- scope: telescope -->
<!-- info: Select **all attributes** that are represented (directly or
indirectly) in the dataset. -->

- Gender: Data sets are divided by gender. 
- Geography: Locations of each team are given.


## Transformations
<!-- info: Fill this section if any transformations were applied in the
creation of your dataset. -->
### Synopsis
#### Transformation(s) Applied
<!-- scope: telescope -->
<!-- info: Select **all applicable** transformations
that were applied to the dataset. -->
- Anomaly Detection
- Cleaning Mismatched Values
- Cleaning Missing Values
- Converting Data Types
- Data Aggregation
- Dimensionality Reduction
- Joining Input Sources
- Redaction or Anonymization
- Others (Please specify)

#### Field(s) Transformed
<!-- scope: periscope -->
<!-- info: Provide the fields in the dataset that
were transformed.

Use additional notes to capture any
other relevant information or
considerations.

(Usage Note: Duplicate and complete
the following for each transformation
type applied. Include the data types to
which fields were transformed.) -->
**Transformation Type**

Field Name | Source & Target
--- | ---
Field Name | Source Field: Target Field
Field Name | Source Field: Target Field
... | ...

**Additional Notes:** Add here

#### Library(ies) and Method(s) Used
<!-- scope: microscope -->
<!-- info: Provide a description of the methods
used to transform or process the
dataset.

Use additional notes to capture any
other relevant information or
considerations.

(Usage Note: Duplicate and complete
the following for each transformation
type applied.) -->
**Transformation Type**

**Method:** Describe the transformation
method here. Include links where
necessary.

**Platforms, tools, or libraries:**
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

**Transformation Results:** Provide
results, outcomes, and actions taken
because of the transformations. Include
visualizations where available.

**Additional Notes:** Add here

### Breakdown of Transformations
<!-- info: Fill out relevant rows. -->
#### Cleaning Missing Value(s)
<!-- scope: telescope -->
<!-- info: Which fields in the data were missing
values? How many? -->
Summarize here. Include links where available.

**Field Name:** Count or description

**Field Name:** Count or description

**Field Name:** Count or description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: How were missing values cleaned?
What other choices were considered? -->
Summarize here. Include links where necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why were missing values cleaned using
this method (over others)? Provide
comparative charts showing before
and after missing values were cleaned. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

- **Risk Type:** Description + Mitigations
- **Risk Type:** Description + Mitigations
- **Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were
made? -->
Summarize here. Include links where available.

#### Cleaning Mismatched Value(s)
<!-- scope: telescope -->
<!-- info: Which fields in the data were corrected
for mismatched values? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: How were incorrect or mismatched
values cleaned? What other choices
were considered? -->
Summarize here. Include links where available.

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why were incorrect or mismatched
values cleaned using this method (over
others)? Provide a comparative
analysis demonstrating before and
after values were cleaned. -->
Summarize here. Include links where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were made? -->
Summarize here. Include links where available.

#### Anomalies
<!-- scope: telescope -->
<!-- info: How many anomalies or outliers were
detected?
If at all, how were detected anomalies
or outliers handled?
Why or why not? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: What methods were used to detect
anomalies or outliers? -->
Summarize here. Include links where necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Provide a comparative analysis
demonstrating before and after
anomaly handling measures. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were made? -->
Summarize here. Include links where available.

#### Dimensionality Reduction
<!-- scope: telescope -->
<!-- info: How many original features were
collected and how many dimensions
were reduced? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: What methods were used to reduce the
dimensionality of the data? What other
choices were considered? -->
Summarize here. Include links where
necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why were features reduced using this
method (over others)? Provide
comparative charts showing before
and after dimensionality reduction
processes. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risks
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were made? -->
Summarize here. Include links where available.

#### Joining Input Sources
<!-- scope: telescope -->
<!-- info: What were the distinct input sources that were joined? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: What are the shared columns of fields used to join these
sources? -->
Summarize here. Include links where necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why were features joined using this
method over others?

Provide comparative charts showing
before and after dimensionality
reduction processes. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where
available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were
made? -->
Summarize here. Include links where
available.

#### Redaction or Anonymization
<!-- scope: telescope -->
<!-- info: Which features were redacted or
anonymized? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: What methods were used to redact or
anonymize data? -->
Summarize here. Include links where necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why was data redacted or anonymized
using this method over others? Provide
comparative charts showing before
and after redaction or anonymization
process. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

**Risk Type:** Description + Mitigations

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were
made? -->
Summarize here. Include links where available.

#### Others (Please Specify)
<!-- scope: telescope -->
<!-- info: What was done? Which features or
fields were affected? -->
Summarize here. Include links where available.

**Field Name:** Count or Description

**Field Name:** Count or Description

**Field Name:** Count or Description

#### Method(s) Used
<!-- scope: periscope -->
<!-- info: What method were used? -->
Summarize here. Include links where necessary.

**Platforms, tools, or libraries**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

#### Comparative Summary
<!-- scope: microscope -->
<!-- info: Why was this method used over
others? Provide comparative charts
showing before and after this
transformation. -->
Summarize here. Include links, tables, visualizations where available.

**Field Name** | **Diff**
--- | ---
Field Name | Before: After
Field Name | Before: After
... | ...

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Residual & Other Risk(s)
<!-- scope: telescope -->
<!-- info: What risks were introduced because of
this transformation? Which risks were
mitigated? -->
Summarize here. Include links and metrics where applicable.

**Risk type:** [Description + Mitigations]

**Risk type:** [Description + Mitigations]

**Risk type:** [Description + Mitigations]

#### Human Oversight Measure(s)
<!-- scope: periscope -->
<!-- info: What human oversight measures,
including additional testing,
investigations and approvals were
taken due to this transformation? -->
Summarize here. Include links where available.

#### Additional Considerations
<!-- scope: microscope -->
<!-- info: What additional considerations were made? -->
Summarize here. Include links where available.


## Validation Types
<!-- info: Fill this section if the data in the dataset was validated during
or after the creation of your dataset. -->
#### Method(s)
<!-- scope: telescope -->
<!-- info: Select **all applicable**: -->
- Data Type Validation
- Range and Constraint Validation
- Code/cross-reference Validation
- Consistency Validation

#### Breakdown(s)
<!-- scope: periscope -->
<!-- info: Provide a description of the fields and data
points that were validated.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each validator type.) -->
**Range and Constraint Validation**

**Number of Data Points Validated:** ~100,000+

**Fields Validated**
Field | Count (approx)
--- | ---
Season | 16,000
DayNum | 80,000
WScore | 80,000
LScore | 80,000

**Above:** Checked that seasons were within the range 1985-2025, and that numeric fields like scores and game days were non-negative


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
<!-- scope: microscope -->
<!-- info: Provide a description of the methods used to
validate the dataset.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each validator type.) -->
**Range and Constraint Validation**

**Method:** 

- Verified that Season values fall within 1985–2025.

- Checked that fields such as DayNum, WScore, and LScore contain no negative values.

**Platforms, tools, or libraries:**

- Python
- Pandas

**Validation Results:** 

✅ All Season values are valid. 

✅ All numeric game values are non-negative.

**Additional Notes:** This validation step ensures that no out-of-bounds or corrupted data points interfere with model training.

**Code / Cross-reference Validation**

**Method:** 

- Compared team IDs in result and seed datasets to the official team lists using set logic in Python.

- Checked columns: WTeamID, LTeamID, TeamID.

**Platforms, tools, or libraries:**

- Python
- Pandas

**Validation Results:** 

✅ All team IDs in both men's and women's datasets match the official team files. No unmatched or orphaned IDs were found.

**Additional Notes:** This validation ensures referential integrity across game result data and team metadata.

**Consistency Validation**

**Method:** 

- Printed unique values of region fields (RegionW, RegionX, RegionY, RegionZ) in MSeasons and WSeasons.

- Verified consistency with historical naming patterns.

**Platforms, tools, or libraries:**

- Python
- Pandas

**Validation Results:** 
- Men's Regions:

    - RegionW: ['East', 'Atlanta', 'Albuquerque', 'NA1']

    - RegionX: ['West', 'Midwest', 'Southeast', 'South', 'Phoenix', 'Chicago', 'Oakland', 'NA2']

    - RegionY: ['Midwest', 'Southeast', 'South', 'EastRutherford', 'Austin', 'Minneapolis', 'NA3']

    - RegionZ: ['Southeast', 'West', 'South', 'StLouis', 'Syracuse', 'WashingtonDC', 'Southwest', 'NA4']

- Women's Regions:
(Includes broader set reflecting more diversity in site locations)

    -  e.g., ['Chattanooga', 'DesMoines', 'Alamo', 'Seattle4', 'RiverWalk', etc.]

**Additional Notes:** The presence of NA1 to NA4 suggests placeholders, which may require downstream handling depending on modeling use cases.

### Description of Human Validators
<!-- info: Fill this section if the dataset was validated using human
validators -->
No human validators were used; all validations were performed via automated scripts.
## Sampling Methods
<!-- info: Fill out the following block if your dataset employs any sampling
methods. -->
#### Method(s) Used
<!-- scope: telescope -->
<!-- info: Select **all applicable** methods used in the creation of this
dataset: -->
- Cluster Sampling
- Haphazard Sampling
- Multi-stage Sampling
- Random Sampling
- Retrospective Sampling
- Stratified Sampling
- Systematic Sampling
- Weighted Sampling
- Unknown
- Unsampled
- Others (Please specify)

#### Characteristic(s)
<!-- scope: periscope -->
<!-- info: Provide characteristics of each sampling
method used.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each sampling method
used.) -->
**(Sampling Type)** | **Number**
--- | ---
Upstream Source | Write here
Total data sampled | 123m
Sample size | 123
Threshold applied | 123k units at property
Sampling rate | 123
Sample mean | 123
Sample std. dev | 123
Sampling distribution | 123
Sampling variation | 123
Sample statistic | 123

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Sampling Criteria
<!-- scope: microscope -->
<!-- info: Describe the criteria used to sample data from
upstream sources.

Use additional notes to capture any other
relevant information or considerations. -->
- **Sampling method:** Summarize here. Include links where applicable.
- **Sampling method:** Summarize here. Include links where applicable.
- **Sampling method:** Summarize here. Include links where applicable.


## Terms of Art
### Concepts and Definitions referenced in this Data Card
<!-- info: Use this space to include the expansions and definitions of any
acronyms, concepts, or terms of art used across the Data Card.
Use standard definitions where possible. Include the source of the definition
where indicated. If you are using an interpretation,
adaptation, or modification of the standard definition for the purposes of your
Data Card or dataset, include your interpretation as well. -->
#### Term of Art
Definition: Write here

Source: Write here and share link

Interpretation: Write here

#### Term of Art
Definition: Write here

Source: Write here and share link

Interpretation: Write here



## Reflections on Data
<!-- info: Use this space to include any additional information about the
dataset that has not been captured by the Data Card. For example,
does the dataset contain data that might be offensive, insulting, threatening,
or might otherwise cause anxiety? If so, please contact the appropriate parties
to mitigate any risks. -->
### Team Performance
Games Played: On average, teams play around 28-30 games a season depending how well they do. The top teams by games played, such as Duke, Kansas, and North Carolina, are all consistently strong performers. However their repeated represenation can lead to bias with schools with less extensive data or shorter season.

Win Percentage: The average win percentage across all teams is 48.03%, with top teams (e.g., Duke and Kansas) reaching win percentages over 79% a season, indicating a strong historical performance. Teams with fewer games played tend to show a wider variance in performance. Which we will also need to find a way to account for in our model. (These are the typical underdogs that could lead to big upsets)

Tournament Participation: The mean tournament participation rate is approximately 1.06, suggesting that while some teams regularly make the tournament, others may only participate sporadically. This is also seen in overall games played, the best teams have the highest overall games played since they consistently go to the finals. Seperating themselves from the pack. Teams less involved in the tournaments have little to no uniformity.

### Conference Trends
Games Played: Conferences like the Southeastern Conference (SEC) and Atlantic 10 Conference have the highest number of games played, suggesting strong and competitive leagues. In contrast, conferences like the Mid-Eastern Athletic Conference (MEAC) have lower game totals, reflecting less competition.

Win Percentage: Win percentages across conferences show a lot of variability, with the Atlantic Coast Conference (ACC) performing at a high level (60.80%) and the Mid-Eastern Athletic Conference (MEAC) performing at a much lower level (39.02%). This highlights the difference in strength between conferences.

Tournament Performance: The average tournament win percentage across conferences is 34.55%, with some conferences like the ACC having higher success rates in tournament play, and others facing more challenges.


