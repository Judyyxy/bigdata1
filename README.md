# Basic Analysis
Loaded 10000 violations randomly into ElasticSearch, so analysis is done on this total set.

## Number of violations on time line. 
( Most violations happend on 12/31 and the possible reason for it is that I only load 10k records and the 10k records mainly from this date by accident. There can have other reasons behind it and it needs to an investigation. -> load all the data )

![](img/hit_ts.PNG)

## Most violation reason is "No parking - Street Cleaning": people tend to forget to move his/her cars.

![](img/violation_count.PNG)

## The top 30 plate numbers that have with multiple violations 

![](img/Violation_times.PNG)

## The distribution on different counties 

![](img/County.PNG)
