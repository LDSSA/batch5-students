
List of concepts introduced in BLU04
========================================

Part 1 Pandas for Time Series
-------------------------------------

* Definition of Time series
* Time series Indexing : Time stamps
* Time stamps formats : method `to_datetime()`
* Time series selection: methods `loc` and `slice`
* Time series re-sampling : method `resample`
* Input missing data: `fillna(method='ffill')`, `KNNImputer`, `interpolate`
* Time series aggregation : method `cumsum`, `cummax`
* Time series smoothing/averaging : Rolling Windows. Method `rolling`
* Difference between consecutive time periods : method `diff`

Part 2 Multi-indexing
----------------------------

* Selecting in multi indexes : `loc`
* Slicing in multi indexes : `pd.IndexSlice`
* Groupby for different levels of multi-indexed data
* Finding the first occurrence of the min or the max: idxmin() or idxmax()
* Unstacking : method `unstack`
* Using cross sections for plotting : method `xs`

Part 3 Time Series modelling concepts
-------------------------------------

* Time Series decomposition: Trend, Seasonality, Cyclical and Irregular components
* Correlation between time series periods: concept of lag, method `shift`

