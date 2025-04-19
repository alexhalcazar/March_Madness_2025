# NCAA Data
This dataset contains historical data for the NCAA Men's and Women's Basketball Tournaments, which includes detailed information about team performances, tournament seeds, game results, and scheduling. The data is sourced from multiple CSV files, each containing specific aspects of the tournament history and structure. The primary purpose of this dataset is to build predictive models for tournament outcomes and game scheduling.

#### Dataset Link
<!-- info: Provide a link to the dataset: -->
<!-- width: half -->
[Kaggle](https://www.google.com/url?q=https%3A%2F%2Fwww.kaggle.com%2Fcompetitions%2Fmarch-machine-learning-mania-2025%2Fdata)

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



## Provenance
### Collection
#### Method(s) Used
<!-- scope: telescope -->
<!-- info: Select **all applicable** methods used to collect data: -->
- API
- Artificially Generated
- Crowdsourced - Paid
- Crowdsourced - Volunteer
- Vendor Collection Efforts
- Scraped or Crawled
- Survey, forms, or polls
- Taken from other existing datasets
- Unknown
- To be determined
- Others (please specify)

#### Methodology Detail(s)
<!-- scope: periscope -->
<!-- info: Provide a description of each collection method used.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for collection method
type.) -->
**Collection Type**

**Source:** Describe here. Include links where available.

**Platform:** [Platform Name], Describe platform here. Include links where relevant.

**Is this source considered sensitive or high-risk?** [Yes/No]

**Dates of Collection:** [MMM YYYY - MMM YYYY]

**Primary modality of collection data:**

*Usage Note: Select one for this collection type.*

- Image Data
- Text Data
- Tabular Data
- Audio Data
- Video Data
- Time Series
- Graph Data
- Geospatial Data
- Unknown
- Multimodal (please specify)
- Others (please specify)

**Update Frequency for collected data:**

*Usage Note: Select one for this collection type.*

- Yearly
- Quarterly
- Monthly
- Biweekly
- Weekly
- Daily
- Hourly
- Static
- Others (please specify)

**Additional Links for this collection:**

- [Access Policy]
- [Wipeout Policy]
- [Retention Policy]

**Additional Notes:** Add here

#### Source Description(s)
<!-- scope: microscope -->
<!-- info: Provide a description of each upstream source of data.

Use additional notes to capture any other relevant information or
considerations. -->
- **Source:** Describe here. Include links, data examples, metrics, visualizations where relevant.
- **Source:** Describe here. Include links, data examples, metrics, visualizations where relevant.
- **Source:** Describe here. Include links, data examples, metrics, visualizations where relevant.

**Additional Notes:** Add here

#### Collection Cadence
<!-- scope: telescope -->
<!-- info: Select **all applicable**: -->
**Static:** Data was collected once from single or multiple sources.

**Streamed:** Data is continuously acquired from single or multiple sources.

**Dynamic:** Data is updated regularly from single or multiple sources.

**Others:** Please specify

#### Data Integration
<!-- scope: periscope -->
<!-- info: List all fields collected from different sources, and specify if
they were included or excluded from the dataset.

Use additional notes to
capture any other relevant information or considerations.

(Usage Note: Duplicate and complete the following for each upstream
source.) -->
**Source**

**Included Fields**

Data fields that were collected and are included in the dataset.

Field Name | Description
--- | ---
Field Name | Describe here. Include links, data examples, metrics, visualizations where relevant.
Field Name | Describe here. Include links, data examples, metrics, visualizations where relevant.

**Additional Notes:** Add here

**Excluded Fields**

Data fields that were collected but are excluded from the dataset.

Field Name | Description
--- | ---
Field Name | Describe here. Include links, data examples, metrics, visualizations where relevant.
Field Name | Describe here. Include links, data examples, metrics, visualizations where relevant.

**Additional Notes:** Add here

#### Data Processing
<!-- scope: microscope -->
<!-- info: Summarize how data from different sources or methods aggregated,
processed, or connected.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the following for each source OR
collection method.) -->
**Collection Method or Source**

**Description:** Describe here. Include links where relevant.

**Methods employed:** Describe here. Include links where relevant.

**Tools or libraries:** Describe here. Include links where relevant.

**Additional Notes:** Add here

### Collection Criteria
#### Data Selection
<!-- scope: telescope -->
<!-- info: Summarize the data selection criteria.

Use additional notes to capture any other relevant information or
considerations. -->
- **Collection Method of Source:** Summarize data selection criteria here. Include links where available.
- **Collection Method of Source:** Summarize data selection criteria here. Include links where available.
- **Collection Method of Source:** Summarize data selection criteria here. Include links where available.

**Additional Notes:** Add here

#### Data Inclusion
<!-- scope: periscope -->
<!-- info: Summarize the data inclusion criteria.

Use additional notes to capture any other relevant information or
considerations. -->
- **Collection Method of Source:** Summarize data inclusion criteria here. Include links where available.
- **Collection Method of Source:** Summarize data inclusion criteria here. Include links where available.
- **Collection Method of Source:** Summarize data inclusion criteria here. Include links where available.

**Additional Notes:** Add here

#### Data Exclusion
<!-- scope: microscope -->
<!-- info: Summarize the data exclusion criteria.

Use additional notes to capture any other relevant information or
considerations. -->
- **Collection Method of Source:** Summarize data exclusion criteria here. Include links where available.
- **Collection Method of Source:** Summarize data exclusion criteria here. Include links where available.
- **Collection Method of Source:** Summarize data exclusion criteria here. Include links where available.

**Additional Notes:** Add here

### Relationship to Source
#### Use & Utility(ies)
<!-- scope: telescope -->
<!-- info: Describe how the resulting dataset is aligned with the purposes,
motivations, or intended use of the upstream source(s).

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each source type.) -->
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.

**Additional Notes:** Add here

#### Benefit and Value(s)
<!-- scope: periscope -->
<!-- info: Summarize the benefits of the resulting dataset to its consumers,
compared to the upstream source(s).

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each source type.) -->
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.

**Additional Notes:** Add here

#### Limitation(s) and Trade-Off(s)
<!-- scope: microscope -->
<!-- info: What are the limitations of the resulting dataset to its consumers,
compared to the upstream source(s)?

Break down by source type.<br><br>(Usage Note: Duplicate and complete the
following for each source type.) -->
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.

### Version and Maintenance
<!-- info: Fill this next row if this is not the first version of the dataset,
and there is no data card available for the first version -->
#### First Version
<!-- scope: periscope -->
<!-- info: Provide a **basic description of the first version** of this
dataset. -->
- **Release date:** MM/YYYY
- **Link to dataset:** [Dataset Name + Version]
- **Status:** [Select one: Actively Maintained/Limited Maintenance/Deprecated]
- **Size of Dataset:** 123 MB
- **Number of Instances:** 123456

#### Note(s) and Caveat(s)
<!-- scope: microscope -->
<!-- info: Summarize the caveats or nuances of the first version of this
dataset that may affect the use of the current version.

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include links where available.

**Additional Notes:** Add here

#### Cadence
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Yearly
- Quarterly
- Monthly
- Biweekly
- Weekly
- Daily
- Hourly
- Static
- Others (please specify)

#### Last and Next Update(s)
<!-- scope: periscope -->
<!-- info: Please describe the update schedule: -->
- **Date of last update:** DD/MM/YYYY
- **Total data points affected:** 12345
- **Data points updated:** 12345
- **Data points added:** 12345
- **Data points removed:** 12345
- **Date of next update:** DD/MM/YYYY

#### Changes on Update(s)
<!-- scope: microscope -->
<!-- info: Summarize the changes that occur when the dataset is refreshed.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each source type.) -->
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.
- **Source Type:** Summarize here. Include links where available.

**Additional Notes:** Add here

## Human and Other Sensitive Attributes
#### Sensitive Human Attribute(s)
<!-- scope: telescope -->
<!-- info: Select **all attributes** that are represented (directly or
indirectly) in the dataset. -->
- Gender
- Socio-economic status
- Geography
- Language
- Age
- Culture
- Experience or Seniority
- Others (please specify)

#### Intentionality
<!-- scope: periscope -->
<!-- info: List fields in the dataset that contain human attributes, and
specify if their collection was intentional or unintentional.

Use additional notes to capture any other relevant information or
considerations. -->
**Intentionally Collected Attributes**

Human attributes were labeled or collected as a part of the dataset creation
process.

Field Name | Description
--- | ---
Field Name | Human Attributed Collected
Field Name | Human Attributed Collected

**Additional Notes:** Add here

**Unintentionally Collected Attributes**

Human attributes were not explicitly collected as a part of the dataset
creation process but can be inferred using additional methods.

Field Name | Description
--- | ---
Field Name | Human Attributed Collected
Field Name | Human Attributed Collected

**Additional Notes:** Add here

#### Rationale
<!-- scope: microscope -->
<!-- info: Describe the motivation, rationale, considerations or approaches
that caused this dataset to include the indicated human attributes.

Summarize why or how this might affect the use of the dataset. -->
Summarize here. Include links, table, and media as relevant.

#### Source(s)
<!-- scope: periscope -->
<!-- info: List the sources of the human attributes.

Use additional notes to capture any other relevant information or
considerations. -->
- **Human Attribute:** Sources
- **Human Attribute:** Sources
- **Human Attribute:** Sources

**Additional Notes:** Add here

#### Methodology Detail(s)
<!-- scope: microscope -->
<!-- info: Describe the methods used to collect human attributes in the
dataset.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each human
attribute.) -->

**Human Attribute Method:** Describe the collection method here. Include links where necessary

**Collection task:** Describe the task here. Include links where necessary

**Platforms, tools, or libraries:**

- [Platform, tools, or libraries]: Write description here
- [Platform, tools, or libraries]: Write description here
- [Platform, tools, or libraries]: Write description here

**Additional Notes:** Add here

#### Distribution(s)
<!-- width: full -->
<!-- info: Provide basic descriptive statistics for each human attribute,
noting key takeaways in the caption.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each human
attribute.) -->
Human Attribute | Label or Class | Label or Class | Label or Class | Label or Class
--- | --- | --- | --- | ---
Count | 123456 | 123456 | 123456 | 123456
[Statistic] | 123456 | 123456 | 123456 | 123456
[Statistic] | 123456 | 123456 | 123456 | 123456
[Statistic] | 123456 | 123456 | 123456 | 123456

**Above:** Provide a caption for the above table or visualization.
**Additional Notes:** Add here

#### Known Correlations
<!-- scope: periscope -->
<!-- info: Describe any known correlations with the indicated sensitive
attributes in this dataset.

Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate for each known correlation.) -->
[`field_name`, `field_name`]

**Description:** Summarize here. Include visualizations, metrics, or links
where necessary.

**Impact on dataset use:** Summarize here. Include visualizations, metrics, or
links where necessary.

**Additional Notes:** add here

#### Risk(s) and Mitigation(s)
<!-- scope: microscope -->
<!-- info: Summarize systemic or residual risks, performance expectations,
trade-offs and caveats because of human attributes in this dataset.

Use additional notes to capture any other relevant information or
considerations.

Usage Note: Duplicate and complete the following for each human attribute. -->
**Human Attribute**

Summarize here. Include links and metrics where applicable.

**Risk type:** [Description + Mitigations]

**Risk type:** [Description + Mitigations]

**Risk type:** [Description + Mitigations]

**Trade-offs, caveats, & other considerations:** Summarize here. Include
visualizations, metrics, or links where necessary.

**Additional Notes:** Add here

## Extended Use
### Use with Other Data
#### Safety Level
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Safe to use with other data
- Conditionally safe to use with other data
- Should not be used with other data
- Unknown
- Others (please specify)

#### Known Safe Dataset(s) or Data Type(s)
<!-- scope: periscope -->
<!-- info: List the known datasets or data types and corresponding
transformations that **are safe to join or aggregate** this dataset with. -->
**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

#### Best Practices
<!-- scope: microscope -->
<!-- info: Summarize best practices for using this dataset with other datasets
or data types.

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include visualizations, metrics, demonstrative examples,
or links where necessary.

**Additional Notes:** Add here

#### Known Unsafe Dataset(s) or Data Type(s)
<!-- scope: periscope -->
<!-- info: Fill this out if you selected "Conditionally safe to use with other
datasets" or "Should not be used with other datasets":

List the known datasets or data types and corresponding transformations that
are **unsafe to join or aggregate** with this dataset. -->
**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

**Dataset or Data Type:** Summarize here. Include visualizations, metrics,
or links where necessary.

#### Limitation(s) and Recommendation(s)
<!-- scope: microscope -->
<!-- info: Fill this out if you selected "Conditionally safe to use with
other datasets" or "Should not be used with
other datasets":

Summarize limitations of the dataset that introduce foreseeable risks when the
dataset is conjoined with other datasets.

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include links and metrics where applicable.

**Limitation type:** Dataset or data type, description and recommendation.

**Limitation type:** Dataset or data type, description and recommendation.

**Limitation type:** Dataset or data type, description and recommendation.

**Additional Notes:** Add here

### Forking & Sampling
#### Safety Level
<!-- scope: telescope -->
<!-- info: Select **one**: -->
- Safe to form and/or sample
- Conditionally safe to fork and/or sample
- Should not be forked and/or sampled
- Unknown
- Others (please specify)

#### Acceptable Sampling Method(s)
<!-- scope: periscope -->
<!-- info: Select **all applicable** acceptable methods to sample this
dataset: -->
- Cluster Sampling
- Haphazard Sampling
- Multi-stage sampling
- Random Sampling
- Retrospective Sampling
- Stratified Sampling
- Systematic Sampling
- Weighted Sampling
- Unknown
- Unsampled
- Others (please specify)

#### Best Practice(s)
<!-- scope: microscope -->
<!-- info: Summarize the best practices for forking or sampling this dataset.

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include links, figures, and demonstrative examples where
available.

**Additional Notes:** Add here

#### Risk(s) and Mitigation(s)
<!-- scope: periscope -->
<!-- info: Fill this out if you selected "Conditionally safe to fork and/or
sample" or "Should not be forked and/or sampled":

Summarize known or residual risks associated with forking and sampling methods
when applied to the dataset.

Use additional notes to capture any other
relevant information or considerations. -->
Summarize here. Include links and metrics where applicable.

**Risk Type:** [Description + Mitigations]

**Risk Type:** [Description + Mitigations]

**Risk Type:** [Description + Mitigations]

**Additional Notes:** Add here

#### Limitation(s) and Recommendation(s)
<!-- scope: microscope -->
<!-- info: Fill this out if you selected "Conditionally safe to fork and/or
sample" or "Should not be forked and/or sample":

Summarize the limitations that the dataset introduces when forking
or sampling the dataset and corresponding recommendations.

Use additional notes to capture any other relevant information or
considerations. -->
Summarize here. Include links and metrics where applicable.

**Limitation Type:** [Description + Recommendation]

**Limitation Type:** [Description + Recommendation]

**Limitation Type:** [Description + Recommendation]

**Additional Notes:** Add here

### Use in ML or AI Systems
#### Dataset Use(s)
<!-- scope: telescope -->
<!-- info: Select **all applicable** -->
- Training
- Testing
- Validation
- Development or Production Use
- Fine Tuning
- Others (please specify)

#### Notable Feature(s)
<!-- scope: periscope -->
<!-- info: Describe any notable feature distributions or relationships between
individual instances made explicit.

Include links to servers where readers can explore the data on their own. -->

**Exploration Demo:** [Link to server or demo.]

**Notable Field Name:** Describe here. Include links, data examples, metrics,
visualizations where relevant.

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Usage Guideline(s)
<!-- scope: microscope -->
<!-- info: Summarize usage guidelines or policies that consumers should be
aware of.

Use additional notes to capture any other relevant information or
considerations. -->
**Usage Guidelines:** Summarize here. Include links where necessary.

**Approval Steps:** Summarize here. Include links where necessary.

**Reviewer:** Provide the name of a reviewer for publications referencing
this dataset.

**Additional Notes:** Add here

#### Distribution(s)
<!-- scope: periscope -->
<!-- info: Describe the recommended splits and corresponding criteria.

Use additional notes to capture any other
relevant information or considerations. -->

Set | Number of data points
--- | ---
Train | 62,563
Test | 62,563
Validation | 62,563
Dev | 62,563

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Known Correlation(s)
<!-- scope: microscope -->
<!-- info: Summarize any known correlations with
the indicated features in this dataset.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate for each known
correlation.) -->
`field_name`, `field_name`

**Description:** Summarize here. Include
visualizations, metrics, or links where
necessary.

**Impact on dataset use:** Summarize here.
Include visualizations, metrics, or links
where necessary.

**Risks from correlation:** Summarize here.
Include recommended mitigative steps if
available.

**Additional Notes:** Add here

#### Split Statistics
<!-- scope: periscope -->
<!-- width: full -->
<!-- info: Provide the sizes of each split. As appropriate, provide any
descriptive statistics for features. -->

Statistic | Train | Test | Valid | Dev
--- | --- | --- | --- | ---
Count | 123456 | 123456 | 123456 | 123456
Descriptive Statistic | 123456 | 123456 | 123456 | 123456
Descriptive Statistic | 123456 | 123456 | 123456 | 123456
Descriptive Statistic | 123456 | 123456 | 123456 | 123456

**Above:** Caption for table above.

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
- Structured Validation
- Consistency Validation
- Not Validated
- Others (Please Specify)

#### Breakdown(s)
<!-- scope: periscope -->
<!-- info: Provide a description of the fields and data
points that were validated.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each validator type.) -->
**(Validation Type)**

**Number of Data Points Validated:** 12345

**Fields Validated**
Field | Count (if available)
--- | ---
Field | 123456
Field | 123456
Field | 123456

**Above:** Provide a caption for the above table or visualization.

#### Description(s)
<!-- scope: microscope -->
<!-- info: Provide a description of the methods used to
validate the dataset.

Use additional notes to capture any other
relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each validator type.) -->
**(Validation Type)**

**Method:** Describe the validation method here. Include links where
necessary.

**Platforms, tools, or libraries:**

- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here
- Platform, tool, or library: Write description here

**Validation Results:** Provide results, outcomes, and actions taken because
of the validation. Include visualizations where available.

**Additional Notes:** Add here

### Description of Human Validators
<!-- info: Fill this section if the dataset was validated using human
validators -->
#### Characteristic(s)
<!-- scope: periscope -->
<!-- info: Provide characteristics of the validator
pool(s). Use additional notes to capture any
other relevant information or considerations. -->
**(Validation Type)**
- Unique validators: 12345
- Number of examples per validator: 123456
- Average cost/task/validator: $$$
- Training provided: Y/N
- Expertise required: Y/N

#### Description(s)
<!-- scope: microscope -->
<!-- info: Provide a brief description of the validator
pool(s). Use additional notes to capture any
other relevant information or considerations.

(Usage Note: Duplicate and complete the
following for each validator type.) -->
**(Validation Type)**

**Validator description:** Summarize here. Include links if available.

**Training provided:** Summarize here. Include links if available.

**Validator selection criteria:** Summarize here. Include links if available.

**Training provided:** Summarize here. Include links if available.

**Additional Notes:** Add here

#### Language(s)
<!-- scope: telescope -->
<!-- info: Provide validator distributions.
Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each annotation type.)-->
**(Validation Type)**

- Language [Percentage %]
- Language [Percentage %]
- Language [Percentage %]

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Location(s)
<!-- scope: periscope -->
<!-- info: Provide validator distributions.
Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each annotation type.)-->
**(Validation Type)**

- Location [Percentage %]
- Location [Percentage %]
- Location [Percentage %]

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Gender(s)
<!-- scope: microscope -->
<!-- info: Provide validator distributions.
Use additional notes to capture any other relevant information or
considerations.

(Usage Note: Duplicate and complete the following for each annotation type.)-->
**(Validation Type)**

- Gender [Percentage %]
- Gender [Percentage %]
- Gender [Percentage %]

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

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

## Known Applications & Benchmarks
<!-- info: Fill out the following section if your dataset was primarily
created for use in AI or ML system(s) -->
#### ML Application(s)
<!-- scope: telescope -->
<!-- info: Provide a list of key ML tasks
that the dataset has been
used for.

Usage Note: Use comma-separated keywords. -->
*For example: Classification, Regression, Object Detection*

#### Evaluation Result(s)
<!-- scope: periscope -->
<!-- info: Provide the evaluation results from
models that this dataset has been used
in.

Use additional notes to capture any
other relevant information or
considerations.

(Usage Note: Duplicate and complete the
following for each model.) -->
**(Model Name)**

**Model Card:** [Link to full model card]

Evaluation Results

- Accuracy: 123 (params)
- Precision: 123 (params)
- Recall: 123 (params)
- Performance metric: 123 (params)

**Above:** Provide a caption for the above table or visualization.

**Additional Notes:** Add here

#### Evaluation Process(es)
<!-- scope: microscope -->
<!-- info: Provide a description of the evaluation process for
the model's overall performance or the
determination of how the dataset contributes to
the model's performance.

Use additional notes to capture any other relevant
information or considerations.

(Usage Note: Duplicate and complete the following
for each model and method used.) -->
**(Model Name)**

**[Method used]:** Summarize here. Include links where available.

- **Process:** Summarize here. Include links, diagrams, visualizations, tables as relevant.
- **Factors:** Summarize here. Include links, diagrams, visualizations, tables as relevant.
- **Considerations:** Summarize here. Include links, diagrams, visualizations, tables as relevant.
- **Results:** Summarize here. Include links, diagrams, visualizations, tables as relevant.

**Additional Notes:** Add here

#### Description(s) and Statistic(s)
<!-- scope: periscope -->
<!-- info: Provide a description of the model(s) and
task(s) that this dataset has been used
in.

Use additional notes to capture any
other relevant information or
considerations.

(Usage Note: Duplicate and complete the
following for each model.) -->
**(Model Name)**

**Model Card:** Link to full model card

**Model Description:** Summarize here. Include links where applicable.

- Model Size: 123 (params)
- Model Weights: 123 (params)
- Model Layers 123 (params)
- Latency: 123 (params)

**Additional Notes:** Add here

#### Expected Performance and Known Caveats
<!-- scope: microscope -->
<!-- info: Provide a description of the expected performance
and known caveats of the models for this dataset.

Use additional notes to capture any other relevant
information or considerations.

(Usage Note: Duplicate and complete the following
for each model.) -->
**(Model Name)**

**Expected Performance:** Summarize here. Include links where available.

**Known Caveats:** Summarize here. Include links, diagrams, visualizations, and
tables as relevant.

**Additioanl Notes:** Add here

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


