# Intent Determination Model
Intent data refers to information about a customer's goal or desired outcome, often revealed through their online behavior. This data is crucial for businesses to understand as it can inform their marketing and sales strategies. Machine learning algorithms are increasingly being used to analyze and make predictions from intent data. These algorithms use statistical models to identify patterns and relationships within the data, which can then be used to make predictions about customer behaviour.
## Objective
Various B2B (Business to Business) companies selling software wish to target their sales campaigns to specific companies, firms, institutions and bodies, those that have recently shown an interest in their product. The data that these companies use is a combination of standard computer-logged data such as click-rate, timestamp and occurrences, as well as other substantial data such as seniority level of the person in the targeted company who searched for the aforementioned company’s product. This data, though abundant, has yet to be utilized thoroughly and work on it is nascent. There is a need for developing a model which will harness the insights gained from this vast data and predict the buying intent of a particular customer. The objective of this project is to fill this gap and develop the said
model, which will aid B2B companies in their complete sales pipeline.
## Methodology
Considering the proposed stages, the algorithm on the initial stage was based on the
below formula:
Score = ({Trigger}{Domain})/(Total Company Size)
Where, Score will be High (0.75 and above), Medium - (0.35 to 0.75) and low - (0.35 and below). Furthermore, the rolling 90 days data will be merged with current daily data and the algorithm will become advanced.
## Solution
Stage 1: Simple count. Count how many engagements there are for each account, by campaign. Every engagement (competitive, keyword, hiring) all count as one. Add scaling to compensate for large companies.

Stage 2: Weighted Scaled Scoring. This is significantly more complex but easily implementable. We use a rolling 90 day historical data of engagements + engagement types, company sizes, role and seniority of the engagers to come up with the score.

Stage 3: Weighted, moving ADX. The scoring system is closest to a stock market here, with its own signal weights. The baseline aka trend, is recalculated every day for the first 14 days and then only once a month to look at the last 5 days worth of non-zero data. This is a bit more involved and we’re still working on tweaking and scaling it. This takes care of a lot of underlying issues with the other scoring system we had and is our most data driven
approach.
## Flowchart
<img width="742" alt="Screenshot 2024-09-05 at 4 44 16 PM" src="https://github.com/user-attachments/assets/63d2a8bc-2e6c-47d7-9efb-2f86b52c7dd9">
